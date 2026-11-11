# Physical cognition · question 2

[Back to Physical cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `mmlu/5ddb76b7cce9ea608869`  
**Source:** [MMLU](https://huggingface.co/datasets/cais/mmlu)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/physical-cognition/mmlu-5ddb76b7cce9ea608869/README.md)

## Question

> A guitar string creates a sound wave of known frequency. Which of the following describes a correct and practical method of measuring the wavelength of the sound wave with a meterstick?

## Answer choices

- **A:** Lightly touch the guitar string in the middle such that a single node is created. Measure the length of the string; this is the wavelength.
- **B:** Measure the length of the guitar string; this is half the wavelength.
- **C:** Adjust the length of a pipe placed near the string so that resonances are heard. Measure the difference between the pipe lengths for consecutive resonances; this is half the wavelength.
- **D:** Measure the peak-to-peak distance of the wave as it passes; this is the wavelength.

**Reference answer:** Adjust the length of a pipe placed near the string so that resonances are heard. Measure the difference between the pipe lengths for consecutive resonances; this is half the wavelength. (`C`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "A guitar string creates a sound wave of known frequency. Which of the following describes a correct and practical method of measuring the wavelength of the sound wave with a meterstick?",
  "choices": {
    "A": "Lightly touch the guitar string in the middle such that a single node is created. Measure the length of the string; this is the wavelength.",
    "B": "Measure the length of the guitar string; this is half the wavelength.",
    "C": "Adjust the length of a pipe placed near the string so that resonances are heard. Measure the difference between the pipe lengths for consecutive resonances; this is half the wavelength.",
    "D": "Measure the peak-to-peak distance of the wave as it passes; this is the wavelength."
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Adjust the length of a pipe placed near the string so that resonances are heard. Measure the difference between the pipe lengths for consecutive resonances; this is half the wavelength. | Correct |
| Opus 5.5 | Adjust the length of a pipe placed near the string so that resonances are heard. Measure the difference between the pipe lengths for consecutive resonances; this is half the wavelength. | Correct |
| GLiDE v1.2 | Adjust the length of a pipe placed near the string so that resonances are heard. Measure the difference between the pipe lengths for consecutive resonances; this is half the wavelength. | Correct |
| Decider v1.1 | Adjust the length of a pipe placed near the string so that resonances are heard. Measure the difference between the pipe lengths for consecutive resonances; this is half the wavelength. | Correct |
| Jev | Adjust the length of a pipe placed near the string so that resonances are heard. Measure the difference between the pipe lengths for consecutive resonances; this is half the wavelength. | Correct |
| Microsoft Decision-1 | Adjust the length of a pipe placed near the string so that resonances are heard. Measure the difference between the pipe lengths for consecutive resonances; this is half the wavelength. | Correct |
| Clef | Adjust the length of a pipe placed near the string so that resonances are heard. Measure the difference between the pipe lengths for consecutive resonances; this is half the wavelength. | Correct |
| Luna Decisions | Adjust the length of a pipe placed near the string so that resonances are heard. Measure the difference between the pipe lengths for consecutive resonances; this is half the wavelength. | Correct |
| Clef Flash | Adjust the length of a pipe placed near the string so that resonances are heard. Measure the difference between the pipe lengths for consecutive resonances; this is half the wavelength. | Correct |
| Strands Decider | Lightly touch the guitar string in the middle such that a single node is created. Measure the length of the string; this is the wavelength. | Incorrect |
| GLiNER2.5 Decide | Measure the peak-to-peak distance of the wave as it passes; this is the wavelength. | Incorrect |
| Laya | Adjust the length of a pipe placed near the string so that resonances are heard. Measure the difference between the pipe lengths for consecutive resonances; this is half the wavelength. | Correct |
| CalDec v1 | Adjust the length of a pipe placed near the string so that resonances are heard. Measure the difference between the pipe lengths for consecutive resonances; this is half the wavelength. | Correct |

## Source and sharing

Attribution: Dan Hendrycks et al.; MMLU authors.  
Terms: **[MIT](https://opensource.org/license/mit)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "all/test-00000-of-00001.parquet",
    "record": "4776",
    "kind": "source_file_record"
  },
  "source_revision": "c30699e8356da336a370243923dbaf21066bb9fe",
  "input_hash": "a0f94ee3da7ec39975f97a71b5f9863a12c513d3a05f8b7d4503792abdba3200"
}
```

</details>
