# Extra events · Add 12 unrelated events variant

[Original question](../../../questions/retrieval/boolq-58a69904d6d6af211123.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Merovan is a fictional musical suite with a refrain. The refrain begins on the tonic. The refrain pauses. The refrain resumes on a dominant tone. The refrain changes to detached articulation. The refrain returns to the tonic. The refrain repeats its final interval. The refrain changes to a minor-mode variant. The refrain adopts sustained articulation. The refrain returns to a dominant tone. The refrain pauses again. The refrain resumes on the tonic. The refrain ends.
>
> The Willis Tower, built as and still commonly referred to as the Sears Tower, is a 110-story, 1,450-foot (442.1 m) skyscraper in Chicago, Illinois. At completion in 1973, it surpassed the World Trade Center towers in New York to become the tallest building in the world, a title it held for nearly 25 years; it remained the tallest building in the Western Hemisphere until the completion of a new building at the rebuilt World Trade Center site in 2014. The building is considered a seminal achievement for its designer Fazlur Rahman Khan. The Willis Tower is the second-tallest building in the United States and the Western hemisphere -- and the 16th-tallest in the world. More than one million people visit its observation deck each year, making it one of Chicago's most-popular tourist destinations. The structure was renamed in 2009 by the Willis Group as part of its lease on a portion of the tower's space.

## Question

> was the sears tower ever the tallest building in the world

## Answer choices

- **yes.** Yes
- **no.** No

**Reference answer:** `yes`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Merovan is a fictional musical suite with a refrain. The refrain begins on the tonic. The refrain pauses. The refrain resumes on a dominant tone. The refrain changes to detached articulation. The refrain returns to the tonic. The refrain repeats its final interval. The refrain changes to a minor-mode variant. The refrain adopts sustained articulation. The refrain returns to a dominant tone. The refrain pauses again. The refrain resumes on the tonic. The refrain ends.\n\nThe Willis Tower, built as and still commonly referred to as the Sears Tower, is a 110-story, 1,450-foot (442.1 m) skyscraper in Chicago, Illinois. At completion in 1973, it surpassed the World Trade Center towers in New York to become the tallest building in the world, a title it held for nearly 25 years; it remained the tallest building in the Western Hemisphere until the completion of a new building at the rebuilt World Trade Center site in 2014. The building is considered a seminal achievement for its designer Fazlur Rahman Khan. The Willis Tower is the second-tallest building in the United States and the Western hemisphere -- and the 16th-tallest in the world. More than one million people visit its observation deck each year, making it one of Chicago's most-popular tourist destinations. The structure was renamed in 2009 by the Willis Group as part of its lease on a portion of the tower's space.",
  "question": "was the sears tower ever the tallest building in the world",
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

**Variant ID:** `boolq/58a69904d6d6af211123/event_count/12/clean-source_first_boolq_music_contexts_full_0164`

**Input fingerprint:** `d43a227096ffbfdcf8765768f6245afd7c44eecf100b289f6bdd0c35416923d5`

| Change | Recorded version |
| --- | --- |
| Extra events | Add 12 unrelated events |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/retrieval/boolq-58a69904d6d6af211123.md).
