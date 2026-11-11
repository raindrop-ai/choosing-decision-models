# Irrelevant details · Add a small amount of irrelevant detail variant

[Original question](../../../questions/information-seeking/questbench-968ef04a9e1c3604b599.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Last night Rick killed ten wolves and 15 cougars while hunting. Today Rick killed three times as many wolves as cougars. How many animals did Rick kill?
>
>
>
> The poem is untitled.

## Question

> Which missing variable should be asked about to solve this problem?

## Answer choices

- **F1.** Number of fewer cougars killed today compared to yesterday
- **J.** Number of juvenile animals killed

**Reference answer:** `F1`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Last night Rick killed ten wolves and 15 cougars while hunting. Today Rick killed three times as many wolves as cougars. How many animals did Rick kill?\n\n\n\nThe poem is untitled.",
  "question": "Which missing variable should be asked about to solve this problem?",
  "choices": {
    "F1": "Number of fewer cougars killed today compared to yesterday",
    "J": "Number of juvenile animals killed"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `F1` — Number of fewer cougars killed today compared to yesterday | `F1` — Number of fewer cougars killed today compared to yesterday | Same answer |
| Decider v1.1 | `F1` — Number of fewer cougars killed today compared to yesterday | `F1` — Number of fewer cougars killed today compared to yesterday | Same answer |
| Jev | `F1` — Number of fewer cougars killed today compared to yesterday | `F1` — Number of fewer cougars killed today compared to yesterday | Same answer |
| Microsoft Decision-1 | `F1` — Number of fewer cougars killed today compared to yesterday | `F1` — Number of fewer cougars killed today compared to yesterday | Same answer |
| Clef | `F1` — Number of fewer cougars killed today compared to yesterday | `F1` — Number of fewer cougars killed today compared to yesterday | Same answer |
| Luna Decisions | `F1` — Number of fewer cougars killed today compared to yesterday | `F1` — Number of fewer cougars killed today compared to yesterday | Same answer |
| Clef Flash | `F1` — Number of fewer cougars killed today compared to yesterday | `F1` — Number of fewer cougars killed today compared to yesterday | Same answer |
| Strands Decider | `F1` — Number of fewer cougars killed today compared to yesterday | `F1` — Number of fewer cougars killed today compared to yesterday | Same answer |
| GLiNER2.5 Decide | `F1` — Number of fewer cougars killed today compared to yesterday | `F1` — Number of fewer cougars killed today compared to yesterday | Same answer |
| Laya | `F1` — Number of fewer cougars killed today compared to yesterday | `F1` — Number of fewer cougars killed today compared to yesterday | Same answer |
| CalDec v1 | `J` — Number of juvenile animals killed | `J` — Number of juvenile animals killed | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `questbench/968ef04a9e1c3604b599/irrelevant_details/low/clean-source_first_quest_literary_contexts_full_0079`

**Input fingerprint:** `a9fda197a2941b5d182cbcf35bcdee96b670290445cfec7e56e512fbf7c16de9`

| Change | Recorded version |
| --- | --- |
| Irrelevant details | Add a small amount of irrelevant detail |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/information-seeking/questbench-968ef04a9e1c3604b599.md).
