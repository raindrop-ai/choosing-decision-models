# Questions, corrections and contributions

This is the research companion for Raindrop's *A practical guide to choosing decision models*. Use these guidelines to report a reproducible issue or propose a correction.

For questions, corrections or contributions, contact Afika Nyati at [afika@raindrop.ai](mailto:afika@raindrop.ai).

## Report a question or result issue

Include:

- The exact question ID, such as `bbh/639b88b1fe80634a7d66`.
- The model name and the saved answer or score you are discussing.
- The source evidence or reference answer supporting the correction.
- The command, output and relevant Python version for a code issue.

Start by inspecting the saved case:

```bash
python3 baseline.py inspect --case bbh/639b88b1fe80634a7d66
python3 baseline.py verify
```

No model calls are needed to inspect or verify the saved results. See [the source-recovery guide](docs/recovering-inputs.md) if the question text is obtained separately.

## Prepare a change

Run the offline checks from the repository root:

```bash
python3 -B baseline.py verify
python3 -B variants.py verify
python3 -B -m unittest discover -s tests -v
```

Explain which question, code path or documented method changes and why. Keep recorded model outputs intact when proposing a reference-answer or scoring correction, and document the effect on the summary. Save rerun predictions separately from the reference results. [Updating results](docs/updating-results.md) describes the import and validation commands.

For data additions, retain the original-source attribution, version and applicable terms. Recovered question text remains outside the public copy unless its inclusion is supported by the source's terms and the sharing review is updated. Do not commit credentials or private data.

## Source terms

Question materials retain their individual source licenses; see [licenses](licenses/README.md). Preserve source notices and attribution when proposing changes.
