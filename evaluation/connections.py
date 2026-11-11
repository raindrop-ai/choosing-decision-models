"""Read a provider connection without loading credentials or making requests."""
import json
from pathlib import Path
import re
from urllib.parse import urlsplit


def load_connection(path):
    value = json.loads(Path(path).read_text(encoding="utf-8"))
    allowed = {"format", "endpoint", "model_id", "auth", "api_key_env", "request_parameters",
               "structured_output", "reported_model_aliases", "comparison_model"}
    if not isinstance(value, dict) or set(value) - allowed:
        raise ValueError("Unknown connection fields; put credentials in an environment variable, not this file")
    for field in ("endpoint", "model_id", "format"):
        if not isinstance(value.get(field), str) or not value[field]:
            raise ValueError("Connection requires " + field)
    url = urlsplit(value["endpoint"])
    if (not url.hostname or url.username or url.password or url.query or url.fragment
            or not (url.scheme == "https" or url.scheme == "http" and url.hostname in {"localhost", "127.0.0.1", "::1"})):
        raise ValueError("Use an HTTPS endpoint, or HTTP on localhost; do not put credentials in the URL")
    formats = {"openai-chat": ("openai_compatible", None),
               "evaluation-v4": ("gateway", "gateway-evaluation-v4"),
               "decisions-v1": ("gateway", "decisions-v1")}
    if value["format"] not in formats:
        raise ValueError("Supported formats: openai-chat, evaluation-v4, decisions-v1")
    auth = value.get("auth", "bearer")
    if auth not in {"bearer", "x-api-key", "none"}:
        raise ValueError("auth must be bearer, x-api-key or none")
    env = value.get("api_key_env", "MODEL_API_KEY")
    if not isinstance(env, str) or not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", env):
        raise ValueError("api_key_env must name an environment variable")
    params = value.get("request_parameters", {})
    if not isinstance(params, dict) or set(params) & {"model", "messages", "stream", "response_format", "api_key", "authorization"}:
        raise ValueError("request_parameters cannot replace the model, question, output schema or authentication")
    if value.get("structured_output", "json_schema") not in {"json_schema", "json_object", "none"}:
        raise ValueError("structured_output must be json_schema, json_object or none")
    aliases = value.get("reported_model_aliases", [])
    if not isinstance(aliases, list) or any(not isinstance(a, str) or not a for a in aliases):
        raise ValueError("reported_model_aliases must be a list of model identifiers")
    backend, api = formats[value["format"]]
    return {**value, "backend": backend, "api": api, "auth": auth, "api_key_env": env,
            "request_parameters": params, "structured_output": value.get("structured_output", "json_schema")}


def auth_headers(cfg, key):
    auth = cfg.get("auth", "bearer")
    if auth == "none":
        return {}
    if not key:
        raise ValueError("An API key is required for this connection")
    return {"Authorization": "Bearer " + key} if auth == "bearer" else {"x-api-key": key}
