# Similar distractors · Add fewer similar but irrelevant items variant

[Original question](../../../questions/physical-cognition/mmlu-21b36ade886452018632.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> «A separate optical setup sends a red beam toward a water surface from the surrounding air.»

## Question

> A beam of monochromatic light entering a glass window pane from the air will experience a change in

## Answer choices

- **A.** frequency and wavelength
- **B.** frequency and speed
- **C.** speed and wavelength
- **D.** speed only

**Reference answer:** `C`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "«A separate optical setup sends a red beam toward a water surface from the surrounding air.»",
  "question": "A beam of monochromatic light entering a glass window pane from the air will experience a change in",
  "choices": {
    "A": "frequency and wavelength",
    "B": "frequency and speed",
    "C": "speed and wavelength",
    "D": "speed only"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `C` — speed and wavelength | `C` — speed and wavelength | Same answer |
| Decider v1.1 | `C` — speed and wavelength | `C` — speed and wavelength | Same answer |
| Jev | `C` — speed and wavelength | `C` — speed and wavelength | Same answer |
| Microsoft Decision-1 | `C` — speed and wavelength | `C` — speed and wavelength | Same answer |
| Clef | `C` — speed and wavelength | `C` — speed and wavelength | Same answer |
| Luna Decisions | `C` — speed and wavelength | `C` — speed and wavelength | Same answer |
| Clef Flash | `C` — speed and wavelength | `C` — speed and wavelength | Same answer |
| Strands Decider | `C` — speed and wavelength | `C` — speed and wavelength | Same answer |
| GLiNER2.5 Decide | `B` — frequency and speed | `A` — frequency and wavelength | Different answer |
| Laya | `A` — frequency and wavelength | `A` — frequency and wavelength | Same answer |
| CalDec v1 | `A` — frequency and wavelength | `A` — frequency and wavelength | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `mmlu/21b36ade886452018632/similar_distractors/low/clean-source_first_parallel_b_near_accounts_0301`

**Input fingerprint:** `8c5b81cb82821dc096cadfb4b48adfdafca8426224b6a4841c56b3efd24dd765`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add fewer similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/physical-cognition/mmlu-21b36ade886452018632.md).
