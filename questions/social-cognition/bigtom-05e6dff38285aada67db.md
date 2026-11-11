# Social cognition · question 27

[Back to Social cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `bigtom/05e6dff38285aada67db`  
**Source:** [BigToM](https://github.com/cicl-stanford/procedural-evals-tom)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/social-cognition/bigtom-05e6dff38285aada67db/README.md)

## Context

> Rohit is a renowned painter from India who has been commissioned to create a mural on a city building. Rohit wants to paint an intricate scene depicting the vibrant culture and history of India. Rohit selects a set of high-quality, long-lasting paint colors for the mural. Rohit believes that the paint colors he has chosen are of the highest quality and will last for years. While Rohit is out for lunch, a leak in the ceiling drips water onto the paint colors, diluting them and making them less durable. Rohit does not notice the water-damaged paint colors.

## Question

> Does Rohit believe the paint colors are of high quality and long-lasting or water-damaged and less durable?

## Answer choices

- **A:** Rohit believes the paint colors are water-damaged and less durable.
- **B:** Rohit believes the paint colors are of high quality and long-lasting.

**Reference answer:** Rohit believes the paint colors are of high quality and long-lasting. (`B`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Rohit is a renowned painter from India who has been commissioned to create a mural on a city building. Rohit wants to paint an intricate scene depicting the vibrant culture and history of India. Rohit selects a set of high-quality, long-lasting paint colors for the mural. Rohit believes that the paint colors he has chosen are of the highest quality and will last for years. While Rohit is out for lunch, a leak in the ceiling drips water onto the paint colors, diluting them and making them less durable. Rohit does not notice the water-damaged paint colors.",
  "question": "Does Rohit believe the paint colors are of high quality and long-lasting or water-damaged and less durable?",
  "choices": {
    "A": "Rohit believes the paint colors are water-damaged and less durable.",
    "B": "Rohit believes the paint colors are of high quality and long-lasting."
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Rohit believes the paint colors are of high quality and long-lasting. | Correct |
| Opus 5.5 | Rohit believes the paint colors are of high quality and long-lasting. | Correct |
| GLiDE v1.2 | Rohit believes the paint colors are of high quality and long-lasting. | Correct |
| Decider v1.1 | Rohit believes the paint colors are of high quality and long-lasting. | Correct |
| Jev | Rohit believes the paint colors are of high quality and long-lasting. | Correct |
| Microsoft Decision-1 | Rohit believes the paint colors are of high quality and long-lasting. | Correct |
| Clef | Rohit believes the paint colors are of high quality and long-lasting. | Correct |
| Luna Decisions | Rohit believes the paint colors are of high quality and long-lasting. | Correct |
| Clef Flash | Rohit believes the paint colors are of high quality and long-lasting. | Correct |
| Strands Decider | Rohit believes the paint colors are of high quality and long-lasting. | Correct |
| GLiNER2.5 Decide | Rohit believes the paint colors are of high quality and long-lasting. | Correct |
| Laya | Rohit believes the paint colors are water-damaged and less durable. | Incorrect |
| CalDec v1 | Rohit believes the paint colors are water-damaged and less durable. | Incorrect |

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
    "record": "63/forward-belief/false",
    "kind": "source_file_record"
  },
  "source_revision": "fe647d680bddb69f738519313bed625f9e93b549",
  "input_hash": "cdac3366ca8cd4fcaa493d82f9902e047ff018a4d251b76ac0bfdc0c52430790"
}
```

</details>
