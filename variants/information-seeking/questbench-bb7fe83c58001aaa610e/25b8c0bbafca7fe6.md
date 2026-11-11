# Unrelated examples · No worked example (absence-control recipe) variant

[Original question](../../../questions/information-seeking/questbench-bb7fe83c58001aaa610e.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> A simple folding newspaper or tabloid can be made by folding a piece of paper vertically and unfolding it. Then, say, page 1 is printed on the left back, page 2 is printed on the left front, and then, perhaps page 32 is printed on the right back, and page 31 is printed on the right front. How many pieces of paper would be used in a -page tabloid 2 inches long by 3 inches wide?
>
> The poem has a refrain and an anonymous narrator.

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **P.** Total number of pages in the tabloid
- **L.** Length of each piece (in inches)
- **W.** Width of each piece (in inches)

**Reference answer:** `P`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "A simple folding newspaper or tabloid can be made by folding a piece of paper vertically and unfolding it. Then, say, page 1 is printed on the left back, page 2 is printed on the left front, and then, perhaps page 32 is printed on the right back, and page 31 is printed on the right front. How many pieces of paper would be used in a -page tabloid 2 inches long by 3 inches wide?\n\nThe poem has a refrain and an anonymous narrator.",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "P": "Total number of pages in the tabloid",
    "L": "Length of each piece (in inches)",
    "W": "Width of each piece (in inches)"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `P` — Total number of pages in the tabloid | `P` — Total number of pages in the tabloid | Same answer |
| Decider v1.1 | `P` — Total number of pages in the tabloid | `P` — Total number of pages in the tabloid | Same answer |
| Jev | `P` — Total number of pages in the tabloid | `P` — Total number of pages in the tabloid | Same answer |
| Microsoft Decision-1 | `P` — Total number of pages in the tabloid | `P` — Total number of pages in the tabloid | Same answer |
| Clef | `P` — Total number of pages in the tabloid | `P` — Total number of pages in the tabloid | Same answer |
| Luna Decisions | `P` — Total number of pages in the tabloid | `P` — Total number of pages in the tabloid | Same answer |
| Clef Flash | `P` — Total number of pages in the tabloid | `P` — Total number of pages in the tabloid | Same answer |
| Strands Decider | `P` — Total number of pages in the tabloid | `P` — Total number of pages in the tabloid | Same answer |
| GLiNER2.5 Decide | `L` — Length of each piece (in inches) | `L` — Length of each piece (in inches) | Same answer |
| Laya | `L` — Length of each piece (in inches) | `L` — Length of each piece (in inches) | Same answer |
| CalDec v1 | `L` — Length of each piece (in inches) | `L` — Length of each piece (in inches) | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `questbench/bb7fe83c58001aaa610e/examples/absent/clean-source_first_quest_literary_contexts_full_0077`

**Input fingerprint:** `4cd0cbbb0af356dd0ddd3d93a83c01e50bd209e6b83b0e7022d12e850660cb5b`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | No worked example (absence-control recipe) |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/information-seeking/questbench-bb7fe83c58001aaa610e.md).
