# Unrelated examples · Add examples unrelated to the question variant

[Original question](../../../questions/information-seeking/questbench-6afaef1c63ed1ae6119f.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Millie decides to open a lemonade stand. She spends $18 to buy enough supplies to make 3 pitchers of lemonade. Each pitcher holds 12 cups of lemonade. She sells each cup of lemonade for $1. If Millie sells all of the lemonade, how much profit will she make per hour that she spends running the lemonade stand?
>
> Uppercase: comet → COMET.

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **A.** Number of cups Millie sells per hour
- **X1.** Amount of a glass of lemonade in ml

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Millie decides to open a lemonade stand. She spends $18 to buy enough supplies to make 3 pitchers of lemonade. Each pitcher holds 12 cups of lemonade. She sells each cup of lemonade for $1. If Millie sells all of the lemonade, how much profit will she make per hour that she spends running the lemonade stand?\n\nUppercase: comet → COMET.",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "A": "Number of cups Millie sells per hour",
    "X1": "Amount of a glass of lemonade in ml"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — Number of cups Millie sells per hour | `A` — Number of cups Millie sells per hour | Same answer |
| Decider v1.1 | `A` — Number of cups Millie sells per hour | `A` — Number of cups Millie sells per hour | Same answer |
| Jev | `A` — Number of cups Millie sells per hour | `A` — Number of cups Millie sells per hour | Same answer |
| Microsoft Decision-1 | `A` — Number of cups Millie sells per hour | `A` — Number of cups Millie sells per hour | Same answer |
| Clef | `A` — Number of cups Millie sells per hour | `A` — Number of cups Millie sells per hour | Same answer |
| Luna Decisions | `A` — Number of cups Millie sells per hour | `A` — Number of cups Millie sells per hour | Same answer |
| Clef Flash | `A` — Number of cups Millie sells per hour | `A` — Number of cups Millie sells per hour | Same answer |
| Strands Decider | `A` — Number of cups Millie sells per hour | `A` — Number of cups Millie sells per hour | Same answer |
| GLiNER2.5 Decide | `A` — Number of cups Millie sells per hour | `A` — Number of cups Millie sells per hour | Same answer |
| Laya | `A` — Number of cups Millie sells per hour | `X1` — Amount of a glass of lemonade in ml | Different answer |
| CalDec v1 | `A` — Number of cups Millie sells per hour | `A` — Number of cups Millie sells per hour | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `questbench/6afaef1c63ed1ae6119f/examples/irrelevant/clean-source_first_quest_literary_contexts_full_0078`

**Input fingerprint:** `57bca221ff42d3b821e6996c25298d988241fd732b58cedc8b4c6b3e551dddcb`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | Add examples unrelated to the question |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/information-seeking/questbench-6afaef1c63ed1ae6119f.md).
