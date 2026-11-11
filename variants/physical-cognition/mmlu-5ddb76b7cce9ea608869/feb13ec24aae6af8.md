# Option order · Reverse the answer choices variant

[Original question](../../../questions/physical-cognition/mmlu-5ddb76b7cce9ea608869.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Question

> A guitar string creates a sound wave of known frequency. Which of the following describes a correct and practical method of measuring the wavelength of the sound wave with a meterstick?

## Answer choices

- **D.** Measure the peak-to-peak distance of the wave as it passes; this is the wavelength.
- **C.** Adjust the length of a pipe placed near the string so that resonances are heard. Measure the difference between the pipe lengths for consecutive resonances; this is half the wavelength.
- **B.** Measure the length of the guitar string; this is half the wavelength.
- **A.** Lightly touch the guitar string in the middle such that a single node is created. Measure the length of the string; this is the wavelength.

**Reference answer:** `C`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "A guitar string creates a sound wave of known frequency. Which of the following describes a correct and practical method of measuring the wavelength of the sound wave with a meterstick?",
  "choices": {
    "D": "Measure the peak-to-peak distance of the wave as it passes; this is the wavelength.",
    "C": "Adjust the length of a pipe placed near the string so that resonances are heard. Measure the difference between the pipe lengths for consecutive resonances; this is half the wavelength.",
    "B": "Measure the length of the guitar string; this is half the wavelength.",
    "A": "Lightly touch the guitar string in the middle such that a single node is created. Measure the length of the string; this is the wavelength."
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `C` — Adjust the length of a pipe placed near the string so that resonances are heard. Measure the difference between the pipe lengths for consecutive resonances; this is half the wavelength. | `C` — Adjust the length of a pipe placed near the string so that resonances are heard. Measure the difference between the pipe lengths for consecutive resonances; this is half the wavelength. | Same answer |
| Decider v1.1 | `C` — Adjust the length of a pipe placed near the string so that resonances are heard. Measure the difference between the pipe lengths for consecutive resonances; this is half the wavelength. | `C` — Adjust the length of a pipe placed near the string so that resonances are heard. Measure the difference between the pipe lengths for consecutive resonances; this is half the wavelength. | Same answer |
| Jev | `C` — Adjust the length of a pipe placed near the string so that resonances are heard. Measure the difference between the pipe lengths for consecutive resonances; this is half the wavelength. | `C` — Adjust the length of a pipe placed near the string so that resonances are heard. Measure the difference between the pipe lengths for consecutive resonances; this is half the wavelength. | Same answer |
| Microsoft Decision-1 | `C` — Adjust the length of a pipe placed near the string so that resonances are heard. Measure the difference between the pipe lengths for consecutive resonances; this is half the wavelength. | `C` — Adjust the length of a pipe placed near the string so that resonances are heard. Measure the difference between the pipe lengths for consecutive resonances; this is half the wavelength. | Same answer |
| Clef | `C` — Adjust the length of a pipe placed near the string so that resonances are heard. Measure the difference between the pipe lengths for consecutive resonances; this is half the wavelength. | `C` — Adjust the length of a pipe placed near the string so that resonances are heard. Measure the difference between the pipe lengths for consecutive resonances; this is half the wavelength. | Same answer |
| Luna Decisions | `C` — Adjust the length of a pipe placed near the string so that resonances are heard. Measure the difference between the pipe lengths for consecutive resonances; this is half the wavelength. | `C` — Adjust the length of a pipe placed near the string so that resonances are heard. Measure the difference between the pipe lengths for consecutive resonances; this is half the wavelength. | Same answer |
| Clef Flash | `C` — Adjust the length of a pipe placed near the string so that resonances are heard. Measure the difference between the pipe lengths for consecutive resonances; this is half the wavelength. | `C` — Adjust the length of a pipe placed near the string so that resonances are heard. Measure the difference between the pipe lengths for consecutive resonances; this is half the wavelength. | Same answer |
| Strands Decider | `A` — Lightly touch the guitar string in the middle such that a single node is created. Measure the length of the string; this is the wavelength. | `C` — Adjust the length of a pipe placed near the string so that resonances are heard. Measure the difference between the pipe lengths for consecutive resonances; this is half the wavelength. | Different answer |
| GLiNER2.5 Decide | `D` — Measure the peak-to-peak distance of the wave as it passes; this is the wavelength. | `D` — Measure the peak-to-peak distance of the wave as it passes; this is the wavelength. | Same answer |
| Laya | `C` — Adjust the length of a pipe placed near the string so that resonances are heard. Measure the difference between the pipe lengths for consecutive resonances; this is half the wavelength. | `C` — Adjust the length of a pipe placed near the string so that resonances are heard. Measure the difference between the pipe lengths for consecutive resonances; this is half the wavelength. | Same answer |
| CalDec v1 | `C` — Adjust the length of a pipe placed near the string so that resonances are heard. Measure the difference between the pipe lengths for consecutive resonances; this is half the wavelength. | `C` — Adjust the length of a pipe placed near the string so that resonances are heard. Measure the difference between the pipe lengths for consecutive resonances; this is half the wavelength. | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `mmlu/5ddb76b7cce9ea608869/option_order/reverse`

**Input fingerprint:** `f223915c06ab8f24fc17522d8ce7628dcccef05a6ab1a9dbec30a4bade9283fd`

| Change | Recorded version |
| --- | --- |
| Option order | Reverse the answer choices |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/physical-cognition/mmlu-5ddb76b7cce9ea608869.md).
