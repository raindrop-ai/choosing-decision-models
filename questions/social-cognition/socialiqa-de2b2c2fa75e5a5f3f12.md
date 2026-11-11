# Social cognition · question 56

[Back to Social cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `socialiqa/de2b2c2fa75e5a5f3f12`  
**Source:** [Social IQa](https://storage.googleapis.com/ai2-mosaic/public/socialiqa/socialiqa-train-dev.zip)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/social-cognition/socialiqa-de2b2c2fa75e5a5f3f12/README.md)

## Context

> Kendall ate a hamburger from the local diner and later felt sick to their stomach.

## Question

> What will Kendall want to do next?

## Answer choices

- **A:** eat another hamburger
- **B:** complain to the diner&#x27;s owner
- **C:** order a burger

**Reference answer:** complain to the diner&#x27;s owner (`B`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Kendall ate a hamburger from the local diner and later felt sick to their stomach.",
  "question": "What will Kendall want to do next?",
  "choices": {
    "A": "eat another hamburger",
    "B": "complain to the diner's owner",
    "C": "order a burger"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | complain to the diner&#x27;s owner | Correct |
| Opus 5.5 | complain to the diner&#x27;s owner | Correct |
| GLiDE v1.2 | complain to the diner&#x27;s owner | Correct |
| Decider v1.1 | complain to the diner&#x27;s owner | Correct |
| Jev | complain to the diner&#x27;s owner | Correct |
| Microsoft Decision-1 | complain to the diner&#x27;s owner | Correct |
| Clef | complain to the diner&#x27;s owner | Correct |
| Luna Decisions | complain to the diner&#x27;s owner | Correct |
| Clef Flash | complain to the diner&#x27;s owner | Correct |
| Strands Decider | complain to the diner&#x27;s owner | Correct |
| GLiNER2.5 Decide | complain to the diner&#x27;s owner | Correct |
| Laya | eat another hamburger | Incorrect |
| CalDec v1 | eat another hamburger | Incorrect |

## Source and sharing

Attribution: Maarten Sap, Hannah Rashkin, Derek Chen, Ronan LeBras, Yejin Choi.  
Terms: **[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "extracted/socialiqa.zip/socialiqa-train-dev/train.jsonl",
    "record": "30668",
    "kind": "source_file_record"
  },
  "source_revision": null,
  "input_hash": "43711c481a38f3cb4d13c04fb1e43e9270bb58e5cff681891360b9ba94034e3e"
}
```

</details>
