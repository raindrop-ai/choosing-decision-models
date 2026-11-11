"""Standalone Modal entrypoint. No model runtime is imported on the laptop."""
import contextlib
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import shutil
import sys
import time


class ContextLimit(ValueError):
    pass


def complete_choice_head(tok, question, head_max_len=None, option_order=None):
    """Audited recovery layout: native markers and order, without clipping text."""
    if question["t"] != "choice":
        raise ValueError("Recovery only supports native choice questions")
    choices = list(question["crit"].items())
    order = list(range(len(choices))) if option_order is None else option_order
    if sorted(order) != list(range(len(choices))):
        raise ValueError("Invalid option permutation")
    def encode(text):
        return tok.encode(text.replace(tok.mask_token, " "), add_special_tokens=False)
    ids = [tok.cls_token_id] + encode("choice question: " + question["ins"]) + [tok.sep_token_id]
    markers, spans = [], []
    for i in order:
        key, description = choices[i]
        if not isinstance(description, str):
            raise ValueError("Recovery requires frozen string option descriptions")
        rendered = str(key) if description == "" else str(key) + ": " + description
        span = [tok.mask_token_id] + encode(" " + rendered)
        markers.append(len(ids))
        ids.extend(span)
        spans.append(tuple(span))
    ids.append(tok.sep_token_id)
    return ids, markers, {"options": len(spans), "options_distinct": len(set(spans)), "tokens_per_option": None}


def recovery_laya_predict(agent, common, case, maximum):
    """Keep the checkpoint; validate every encoded token before native inference."""
    question = {"type": "choice", "instructions": case["question"], "criteria": case["choices"]}
    internal = agent._to_internal(question)
    head, markers, stats = complete_choice_head(agent.tok, internal)
    state = agent.tok.encode(case["state"].replace(agent.tok.mask_token, " "), add_special_tokens=False)
    expected = head + state + [agent.tok.sep_token_id]
    if len(expected) > maximum or stats["options_distinct"] != len(case["choices"]):
        raise ContextLimit("Complete recovery input does not fit or options collide")
    window = 512 if len(expected) <= 512 else maximum
    old = common.build_head
    common.build_head = complete_choice_head
    try:
        encoded = agent._encode_state(case["state"], ["judgment"], {"judgment": internal},
                                      max_len=window, head_max_len=len(head))
        if encoded[0]["ids"] != expected or encoded[0]["markers"] != markers:
            raise ValueError("Native encoded input differs from the complete audited sequence")
        if encoded[0]["state_stats"]["truncated"]:
            raise ContextLimit("Native encoder unexpectedly truncated recovery input")
        raw = agent.system_one(case["state"], {"judgment": question}, max_len=window, head_max_len=len(head))
    finally:
        common.build_head = old
    if raw.get("usage", {}).get("truncated"):
        raise ContextLimit("Runtime reported unexpected truncation")
    if not str(agent.device).startswith("cuda"):
        raise RuntimeError("Native runtime fell back to CPU")
    info = {"condition": "complete-head-512" if window == 512 else "complete-head-8192",
            "encoded_tokens": len(expected), "head_tokens": len(head), "max_tokens": window,
            "state_tokens_dropped": 0, "options": len(markers), "option_clipping": False}
    return raw["answers"]["judgment"]["probabilities"], info


def strands_native_probabilities(engine, module, request):
    """Capture native softmax values before four-decimal response serialization."""
    original = module._to_answer
    captured = []
    def capture(rq, probs, **kwargs):
        answer = original(rq, probs, **kwargs)
        if rq.kind == "choice":
            values = {label: float(value) for label, value in zip(rq.slot_labels, probs, strict=True)}
            captured.append((values, sum(answer.probabilities.values())))
        return answer
    module._to_answer = capture
    try:
        engine.evaluate(request)
    finally:
        module._to_answer = original
    if len(captured) != 1:
        raise ValueError("Expected one native choice distribution")
    values, serialized_sum = captured[0]
    return values, {"output_precision": "native_float_before_four_decimal_serialization",
                    "native_probability_sum": sum(values.values()), "serialized_probability_sum": serialized_sum}


def install_dependencies():
    """Image build step; the image contains only explicitly copied source files."""
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "--require-hashes", "--only-binary=:all:",
                    "-r", "/requirements.txt"], check=True, timeout=870)


def checksum(path):
    with Path(path).open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def probabilities(values, choices):
    if set(values) != set(choices) or any(isinstance(v, bool) for v in values.values()):
        raise ValueError("Incomplete native choice distribution")
    values = {k: float(v) for k, v in values.items()}
    total = sum(values.values())
    if any(not math.isfinite(v) or v < 0 or v > 1 for v in values.values()) or abs(total - 1) > 0.002:
        raise ValueError("Invalid native choice distribution")
    return {k: v / total for k, v in values.items()}


def safe_child(root, name):
    path = (Path(root) / name).resolve()
    if not path.is_relative_to(Path(root).resolve()):
        raise ValueError("Artifact path escapes its model directory")
    return path


def stage(job, root=Path("/models")):
    from huggingface_hub import snapshot_download
    result = {"models": {}}
    for name, cfg in job["sources"].items():
        target = safe_child(root, name)
        snapshot_download(cfg["repo"], revision=cfg["revision"], local_dir=target,
                          allow_patterns=cfg["allow_patterns"], token=False, max_workers=4)
        for required in cfg["required_files"]:
            if not safe_child(target, required).is_file():
                raise ValueError("Required model artifact was not downloaded")
        if cfg.get("base"):
            base = cfg["base"]
            snapshot_download(base["repo"], revision=base["revision"], local_dir=target / "base",
                              allow_patterns=base["allow_patterns"], token=False, max_workers=4)
        files = {}
        for path in sorted(target.rglob("*")):
            relative = path.relative_to(target)
            if path.is_file() and ".cache" not in relative.parts:
                files[str(relative)] = {"sha256": checksum(path), "bytes": path.stat().st_size}
        if cfg.get("code_sha256") and files["joint_schema_model.py"]["sha256"] != cfg["code_sha256"]:
            raise ValueError("Published model code differs from the reviewed revision")
        for relative, expected in cfg.get("reviewed_files", {}).items():
            if files.get(relative, {}).get("sha256") != expected:
                raise ValueError("Downloaded source/config differs from reviewed artifact")
        result["models"][name] = {"repo": cfg["repo"], "revision": cfg["revision"],
                                  "base": cfg.get("base"), "files": files}
    data = json.dumps(result, sort_keys=True)
    (root / "stage-manifest.json").write_text(data)
    return {"manifest_sha256": hashlib.sha256(data.encode()).hexdigest(),
            "models": {k: {"revision": v["revision"], "bytes": sum(f["bytes"] for f in v["files"].values())}
                       for k, v in result["models"].items()}}


def writable_checkpoint(source, destination):
    """Copy small configs; keep large model files on the read-only volume."""
    destination.mkdir(parents=True, exist_ok=True)
    for path in source.rglob("*"):
        relative = path.relative_to(source)
        if ".cache" in relative.parts or relative.parts[0] == "base":
            continue
        out = destination / relative
        if path.is_dir():
            out.mkdir(parents=True, exist_ok=True)
        elif path.is_file():
            out.parent.mkdir(parents=True, exist_ok=True)
            if path.suffix == ".json":
                shutil.copyfile(path, out)
            else:
                out.symlink_to(path)
    return destination


def load_predictor(kind, path, cfg):
    import torch
    if not torch.cuda.is_available():
        raise RuntimeError("The requested GPU is unavailable; CPU fallback is disabled")
    if kind in ('decider11', 'glide'):
        from decision_lab.decision27 import question, verify_encoding
        for relative, expected in cfg['reviewed_files'].items():
            if checksum(safe_child(path, relative)) != expected:
                raise ValueError('Pinned native loader artifact changed')
        if kind == 'decider11':
            sys.path.insert(0, str(path / 'source/src'))
            from autojev.model import DecisionModel
            model = DecisionModel(path, device='cuda', cpu_threads=2)
            if model.attention_mode != 'noncausal_full_attention' or model.pooling != 'last':
                raise ValueError('Native checkpoint attention/pooling mismatch')
            def audit(case):
                batch = model.prepare([dict(state=case['state'], question=question(case))])
                ids = batch.inputs['input_ids'][0].tolist()
                verify_encoding(ids, case['input_audit'], cfg['max_input_tokens'])
            def predict(case):
                values = model.predict([dict(state=case['state'], question=question(case))], batch_size=1)[0]
                return dict(zip(case['choices'], values, strict=True))
        else:
            sys.path.insert(0, str(path))
            from glide import Glide
            model = Glide.from_pretrained(str(path), device='cuda', dtype=torch.bfloat16,
                                          vision=False, max_len=cfg['max_input_tokens'])
            if model.config['attention_mode'] != 'noncausal_full_attention' or model.config['pooling'] != 'last':
                raise ValueError('Native checkpoint attention/pooling mismatch')
            def audit(case):
                entries, vis = model._prepare(dict(state=case['state'], questions={'judgment': question(case)}))
                if vis or len(entries) != 1: raise ValueError('Unexpected native input')
                ids = model.tokenizer.encode(entries[0][3], add_special_tokens=False)
                verify_encoding(ids, case['input_audit'], cfg['max_input_tokens'], margin=8)
            def predict(case):
                return model.decide(case['state'], {'judgment': question(case)})['answers']['judgment']['probabilities']
        predict.audit = audit
        return predict
    if kind == "clef":
        module_path = path / "joint_schema_model.py"
        if checksum(module_path) != cfg["code_sha256"]:
            raise ValueError("Model loader code checksum mismatch")
        spec = importlib.util.spec_from_file_location("decision_lab_clef", module_path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        model, processor = module.load_release_model(path, device="cuda", dtype=torch.bfloat16,
                                                      local_files_only=True, attn_implementation="eager")
        def predict(case):
            record = {"state": {"text": case["state"]}, "questions": {"judgment": {
                "type": "choice", "instructions": case["question"], "criteria": case["choices"]}}}
            # Encode without the upstream encoder's silent state truncation, then check.
            encoded = module.encode_record(processor.tokenizer, record, max_length=1_000_000_000, processor=processor)
            if len(encoded.input_ids) > cfg["max_input_tokens"]:
                raise ContextLimit("Complete encoded request exceeds the model context")
            batch = module.collate_records([encoded], processor.tokenizer.pad_token_id, torch.device("cuda"))
            with torch.inference_mode():
                logits = model(batch)[0][0]
            return dict(zip(encoded.questions[0].option_ids, logits.float().softmax(-1).tolist()))
        return predict
    if kind == "laya":
        import laya
        from laya.common import build_head, build_sequence, render_options
        import laya.common as laya_common
        local = writable_checkpoint(path, Path("/tmp/laya-checkpoint"))
        agent = laya.load(str(local), device="cuda", backend="eager")
        def predict(case):
            if cfg.get("input_fit_recovery") == "complete-input-v1":
                values, predict.input_fit = recovery_laya_predict(agent, laya_common, case, cfg["max_input_tokens"])
                return values
            question = {"type": "choice", "instructions": case["question"], "criteria": case["choices"]}
            internal = agent._to_internal(question)
            # Laya also caps individual option descriptions to 48 tokens.
            for option in render_options(internal):
                if len(agent.tok.encode(" " + option, add_special_tokens=False)) > 48:
                    raise ContextLimit("Native option-description budget would shorten an option")
            actual, _, stats = build_head(agent.tok, internal, agent.cfg.get("head_max_len", 192))
            full, _, _ = build_head(agent.tok, internal, 1_000_000_000)
            if actual != full or stats["options_distinct"] != len(case["choices"]):
                raise ContextLimit("Native question-head budget would alter the question")
            maximum = min(cfg["max_input_tokens"], agent.cfg["max_len"])
            _, _, truncation = build_sequence(agent.tok, case["state"], internal, max_len=maximum,
                                              head_max_len=agent.cfg.get("head_max_len", 192),
                                              return_truncation_stats=True)
            if truncation["truncated"]:
                raise ContextLimit("Complete state does not fit the native model window")
            raw = agent.system_one(case["state"], {"judgment": question})
            if raw.get("usage", {}).get("truncated"):
                raise ContextLimit("Runtime reported unexpected truncation")
            if str(agent.device) != "cuda" and not str(agent.device).startswith("cuda:"):
                raise RuntimeError("Native runtime fell back to CPU")
            return raw["answers"]["judgment"]["probabilities"]
        return predict
    if kind == "strands":
        from strands_decider.infer import load_engine
        import strands_decider.infer as strands_infer
        from strands_decider.schema import SystemOneRequest
        local = writable_checkpoint(path, Path("/tmp/strands-checkpoint"))
        file = local / "strands_decider_config.json"
        settings = json.loads(file.read_text())
        settings.update(base_model=str(path / "base"), base_revision=None)
        file.write_text(json.dumps(settings))
        engine = load_engine(str(local), device="cuda", use_prefix_cache=False, attn_implementation="eager")
        engine.cfg.strict_window = True
        if cfg.get("input_fit_recovery") == "complete-input-v1":
            engine.model.config.max_length = cfg["max_input_tokens"]
        else:
            engine.model.config.max_length = min(engine.model.config.max_length, cfg["max_input_tokens"])
        def predict(case):
            request = SystemOneRequest.model_validate({"state": case["state"], "questions": {"judgment": {
                "type": "choice", "instructions": case["question"], "criteria": case["choices"]}}})
            if cfg.get("input_fit_recovery") == "complete-input-v1":
                from strands_decider.prompting import render_state, render_question
                state_ids, question_ids, _ = engine._fit(render_state(request.state),
                    [render_question(request.questions["judgment"]).text])
                predict.input_fit = {"condition": "strict-window-8192", "encoded_tokens": len(state_ids) + len(question_ids[0]),
                                     "max_tokens": cfg["max_input_tokens"], "state_tokens_dropped": 0}
            try:
                if cfg.get("native_probability_precision") is True:
                    values, precision = strands_native_probabilities(engine, strands_infer, request)
                    predict.input_fit = {**getattr(predict, "input_fit", {}), **precision}
                    return values
                raw = engine.evaluate(request).model_dump()
            except ValueError as error:
                if "context window" in str(error):
                    raise ContextLimit("Complete native request exceeds the context window") from None
                raise
            return raw["answers"]["judgment"]["probabilities"]
        return predict
    if kind == "gliner":
        from gliner2 import AutoExtractor
        model = AutoExtractor.from_pretrained(str(path), local_files_only=True).to("cuda").eval()
        captured = {}
        original = model._decode_classification_probabilities
        def capture(results, schema_name, cls_config, probs):
            captured["values"] = dict(zip(cls_config["labels"], probs.detach().float().cpu().tolist()))
            return original(results, schema_name, cls_config, probs)
        model._decode_classification_probabilities = capture
        def predict(case):
            task = {"judgment": {"labels": case["choices"], "prompt": case["question"], "multi_label": False}}
            captured.clear()
            if cfg.get("input_fit_recovery") == "complete-input-v1":
                original_transform = model.processor._transform_record
                inspected = []
                def complete_record(record, max_len=None, **kwargs):
                    encoded = original_transform(record, max_len=None, **kwargs)
                    count = len(encoded.input_ids)
                    if count > cfg["max_input_tokens"]:
                        raise ContextLimit("Complete native classification encoding exceeds context")
                    inspected.append(count)
                    return encoded
                model.processor._transform_record = complete_record
                try:
                    model.classify_text(case["state"], task, max_len=None)
                finally:
                    model.processor._transform_record = original_transform
                if len(inspected) != 1:
                    raise ValueError("Native input was not validated exactly once")
                predict.input_fit = {"condition": "exact-native-encoding", "encoded_tokens": inspected[0],
                                     "max_tokens": cfg["max_input_tokens"], "state_tokens_dropped": 0}
            else:
                tokenizer = model.processor.tokenizer
                bound = len(tokenizer.encode(case["state"])) + len(tokenizer.encode(json.dumps(task))) + 2048
                if bound > cfg["max_input_tokens"]:
                    raise ContextLimit("Conservative complete native input bound exceeds context")
                model.classify_text(case["state"], task, max_len=cfg["max_input_tokens"])
            if "values" not in captured:
                raise RuntimeError("Native complete class probabilities were not exposed")
            return captured["values"]
        return predict
    raise ValueError("Unsupported worker kind")


def infer(job, root=Path("/models")):
    import torch
    manifest_path = root / "stage-manifest.json"
    if checksum(manifest_path) != job["manifest_sha256"]:
        raise ValueError("Staged model manifest differs from the controller's manifest")
    manifest = json.loads(manifest_path.read_text())
    name, cfg = job["model_name"], job["config"]
    if manifest["models"][name]["revision"] != cfg["revision"]:
        raise ValueError("Wrong staged model revision")
    start = time.perf_counter()
    predict = load_predictor(cfg["kind"], safe_child(root, name), cfg)
    if hasattr(predict, 'audit'):
        # Validate every native encoding before the first model forward pass.
        for case in job['cases']:
            predict.audit(case)
    torch.cuda.synchronize()
    loading_ms = (time.perf_counter() - start) * 1000
    rows = []
    failed = False
    for case in job["cases"]:
        row = {"case_id": case["id"], "requested_model": cfg["model_id"], "model_revision": cfg["revision"]}
        if failed:
            rows.append({**row, "status": "not_run", "reason": "earlier_worker_error"})
            continue
        torch.cuda.synchronize()
        start = time.perf_counter()
        try:
            with torch.inference_mode():
                values = probabilities(predict(case), case["choices"])
            row.update(status="ok", prediction=max(values, key=values.get), probabilities=values,
                       probability_source="native_choice_distribution")
            if hasattr(predict, "input_fit"):
                row["input_fit"] = predict.input_fit
        except ContextLimit as error:
            row.update(status="context_limit", reason=str(error))
        except Exception as error:
            row.update(status="error", reason=type(error).__name__, error_detail=str(error)[:500])
            failed = True
        torch.cuda.synchronize()
        row["latency_ms"] = (time.perf_counter() - start) * 1000
        rows.append(row)
    import importlib.metadata
    versions = {p: importlib.metadata.version(p) for p in ("torch", "transformers", "huggingface-hub")}
    if shutil.which('cc'):
        import subprocess
        versions['c_compiler'] = subprocess.check_output(['cc', '-dumpfullversion'], text=True).strip()
    return {"records": rows, "model_load_ms": loading_ms, "gpu": torch.cuda.get_device_name(),
            "runtime_versions": versions}


def main():
    mode, request_file, output_file = sys.argv[1:]
    job = json.loads(Path(request_file).read_text())
    # Third-party progress and warnings must not become protocol output.
    with contextlib.redirect_stdout(sys.stderr):
        result = stage(job) if mode == "stage" else infer(job) if mode == "infer" else None
    if result is None:
        raise ValueError("Unknown worker operation")
    Path(output_file).write_text(json.dumps(result, allow_nan=False))


if __name__ == "__main__":
    main()
