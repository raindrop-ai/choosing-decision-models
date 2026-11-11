# Communication · question 17

[Back to Communication](README.md) · [All capabilities](../README.md)

**Question ID:** `tombench/26b2923c5f0c29f0d0ec`  
**Source:** [ToMBench](https://github.com/zhchen18/ToMBench)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/communication/tombench-26b2923c5f0c29f0d0ec/README.md)

## Context

> In the self-study class, Mingming suddenly gives a hearty laugh. Shuhua, who sits at the same table, looks over and smiles at him, saying, "Mingming, your laughter really has a unique character."

## Question

> What does Shuhua really want to say when she says this?

## Answer choices

- **A:** Shuhua really likes Mingming&#x27;s laughter and thinks it is very special.
- **B:** Shuhua hints that Mingming&#x27;s laughter is too loud and he should be quieter.
- **C:** Shuhua praises Mingming, thinking his laughter has a unique attraction.
- **D:** Shuhua finds Mingming&#x27;s laughter interesting, it makes her happy.

**Reference answer:** Shuhua hints that Mingming&#x27;s laughter is too loud and he should be quieter. (`B`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "In the self-study class, Mingming suddenly gives a hearty laugh. Shuhua, who sits at the same table, looks over and smiles at him, saying, \"Mingming, your laughter really has a unique character.\"",
  "question": "What does Shuhua really want to say when she says this?",
  "choices": {
    "A": "Shuhua really likes Mingming's laughter and thinks it is very special.",
    "B": "Shuhua hints that Mingming's laughter is too loud and he should be quieter.",
    "C": "Shuhua praises Mingming, thinking his laughter has a unique attraction.",
    "D": "Shuhua finds Mingming's laughter interesting, it makes her happy."
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Shuhua hints that Mingming&#x27;s laughter is too loud and he should be quieter. | Correct |
| Opus 5.5 | Shuhua hints that Mingming&#x27;s laughter is too loud and he should be quieter. | Correct |
| GLiDE v1.2 | Shuhua hints that Mingming&#x27;s laughter is too loud and he should be quieter. | Correct |
| Decider v1.1 | Shuhua hints that Mingming&#x27;s laughter is too loud and he should be quieter. | Correct |
| Jev | Shuhua hints that Mingming&#x27;s laughter is too loud and he should be quieter. | Correct |
| Microsoft Decision-1 | Shuhua hints that Mingming&#x27;s laughter is too loud and he should be quieter. | Correct |
| Clef | Shuhua hints that Mingming&#x27;s laughter is too loud and he should be quieter. | Correct |
| Luna Decisions | Shuhua hints that Mingming&#x27;s laughter is too loud and he should be quieter. | Correct |
| Clef Flash | Shuhua hints that Mingming&#x27;s laughter is too loud and he should be quieter. | Correct |
| Strands Decider | Shuhua praises Mingming, thinking his laughter has a unique attraction. | Incorrect |
| GLiNER2.5 Decide | Shuhua praises Mingming, thinking his laughter has a unique attraction. | Incorrect |
| Laya | Shuhua praises Mingming, thinking his laughter has a unique attraction. | Incorrect |
| CalDec v1 | Shuhua praises Mingming, thinking his laughter has a unique attraction. | Incorrect |

## Source and sharing

Attribution: Zhuang Chen et al.; ToMBench authors.  
Terms: **[MIT](https://opensource.org/license/mit)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "data/Hinting Task Test.jsonl",
    "record": "69",
    "kind": "source_file_record"
  },
  "source_revision": "4f491f0784ed31ef93a8837615fbc48f885cf78d",
  "input_hash": "99a46ccfb392bede85a69869d01e49fee2650ce6e4a7b3581b99f1e15f90f822"
}
```

</details>
