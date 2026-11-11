# Social cognition · question 35

[Back to Social cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `bigtom/8a1eb59f5a9db383284a`  
**Source:** [BigToM](https://github.com/cicl-stanford/procedural-evals-tom)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/social-cognition/bigtom-8a1eb59f5a9db383284a/README.md)

## Context

> Alejandro is a professional baker in a small Mexican town. He plans to make a large batch of bread for the local market today. He observes that the yeast he has appears to be fresh and active. Alejandro believes that the yeast is in perfect condition for baking. However, a sudden rise in temperature causes the yeast to become too active and over-ferment. Alejandro notices the change in the yeast's condition.

## Question

> Does Alejandro believe the yeast is in perfect condition or over-fermented?

## Answer choices

- **A:** Alejandro believes the yeast is over-fermented.
- **B:** Alejandro believes the yeast is in perfect condition for baking.

**Reference answer:** Alejandro believes the yeast is over-fermented. (`A`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Alejandro is a professional baker in a small Mexican town. He plans to make a large batch of bread for the local market today. He observes that the yeast he has appears to be fresh and active. Alejandro believes that the yeast is in perfect condition for baking. However, a sudden rise in temperature causes the yeast to become too active and over-ferment. Alejandro notices the change in the yeast's condition.",
  "question": "Does Alejandro believe the yeast is in perfect condition or over-fermented?",
  "choices": {
    "A": "Alejandro believes the yeast is over-fermented.",
    "B": "Alejandro believes the yeast is in perfect condition for baking."
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Alejandro believes the yeast is over-fermented. | Correct |
| Opus 5.5 | Alejandro believes the yeast is over-fermented. | Correct |
| GLiDE v1.2 | Alejandro believes the yeast is over-fermented. | Correct |
| Decider v1.1 | Alejandro believes the yeast is over-fermented. | Correct |
| Jev | Alejandro believes the yeast is in perfect condition for baking. | Incorrect |
| Microsoft Decision-1 | Alejandro believes the yeast is in perfect condition for baking. | Incorrect |
| Clef | Alejandro believes the yeast is in perfect condition for baking. | Incorrect |
| Luna Decisions | Alejandro believes the yeast is in perfect condition for baking. | Incorrect |
| Clef Flash | Alejandro believes the yeast is over-fermented. | Correct |
| Strands Decider | Alejandro believes the yeast is over-fermented. | Correct |
| GLiNER2.5 Decide | Alejandro believes the yeast is in perfect condition for baking. | Incorrect |
| Laya | Alejandro believes the yeast is in perfect condition for baking. | Incorrect |
| CalDec v1 | Alejandro believes the yeast is over-fermented. | Correct |

## Source and sharing

Attribution: Kanishk Gandhi, Jan-Philipp Fränken, Tobias Gerstenberg, Noah D. Goodman.  
Terms: **[MIT](https://opensource.org/license/mit)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "data/bigtom/bigtom.csv",
    "record": "174/forward-belief/true",
    "kind": "source_file_record"
  },
  "source_revision": "fe647d680bddb69f738519313bed625f9e93b549",
  "input_hash": "50498b64e0d9995954616f038289946fbd93c934ed09e0f0bfd0a44f3d3f15bf"
}
```

</details>
