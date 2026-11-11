# Unrelated examples · Add examples unrelated to the question variant

[Original question](../../../questions/retrieval/boolq-ec63ada344a152ccf20a.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Capitalize the first letter: harbor → Harbor.
>
> As part of Marvel's Marvel NOW! initiative a new Deadpool ongoing series was launched, written by Brian Posehn and Gerry Duggan and illustrated by Tony Moore. He is also a member of the Thunderbolts. In the 27th issue of his new series, as part of \`\`All-New Marvel NOW!'', Deadpool was married for the third time. Initially a secret, his bride was revealed in the webcomic Deadpool: The Gauntlet to be Shiklah, Queen of the Undead. Deadpool also discovers that he has a daughter by the name of Eleanor from a former flame of Deadpool named Carmelita.

## Question

> does deadpool have a kid in the comics

## Answer choices

- **yes.** Yes
- **no.** No

**Reference answer:** `yes`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Capitalize the first letter: harbor → Harbor.\n\nAs part of Marvel's Marvel NOW! initiative a new Deadpool ongoing series was launched, written by Brian Posehn and Gerry Duggan and illustrated by Tony Moore. He is also a member of the Thunderbolts. In the 27th issue of his new series, as part of ``All-New Marvel NOW!'', Deadpool was married for the third time. Initially a secret, his bride was revealed in the webcomic Deadpool: The Gauntlet to be Shiklah, Queen of the Undead. Deadpool also discovers that he has a daughter by the name of Eleanor from a former flame of Deadpool named Carmelita.",
  "question": "does deadpool have a kid in the comics",
  "choices": {
    "yes": "Yes",
    "no": "No"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `yes` — Yes | `yes` — Yes | Same answer |
| Decider v1.1 | `yes` — Yes | `yes` — Yes | Same answer |
| Jev | `yes` — Yes | `yes` — Yes | Same answer |
| Microsoft Decision-1 | `yes` — Yes | `yes` — Yes | Same answer |
| Clef | `yes` — Yes | `yes` — Yes | Same answer |
| Luna Decisions | `yes` — Yes | `yes` — Yes | Same answer |
| Clef Flash | `yes` — Yes | `yes` — Yes | Same answer |
| Strands Decider | `yes` — Yes | `yes` — Yes | Same answer |
| GLiNER2.5 Decide | `yes` — Yes | `yes` — Yes | Same answer |
| Laya | `yes` — Yes | `yes` — Yes | Same answer |
| CalDec v1 | `yes` — Yes | `yes` — Yes | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `boolq/ec63ada344a152ccf20a/examples/irrelevant/clean-source_first_boolq_music_contexts_full_0164`

**Input fingerprint:** `897b0b7d31283b1aee59946bbd2cf4e65b28cad17af58272575d6c0385821504`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | Add examples unrelated to the question |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/retrieval/boolq-ec63ada344a152ccf20a.md).
