# Social cognition · question 63

[Back to Social cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `bigtom/8c662fdedcb6ce9d6b91`  
**Source:** [BigToM](https://github.com/cicl-stanford/procedural-evals-tom)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/social-cognition/bigtom-8c662fdedcb6ce9d6b91/README.md)

## Context

> Devika is attending a wedding reception at a luxurious hotel. She plans to give the newlyweds a heartfelt speech as a close friend of the couple. She sees that the microphone on the stage is connected and ready to use. Devika believes that the microphone is functioning well. However, just before her turn to speak, a waiter accidentally spills water on the microphone, causing it to malfunction. Devika does not see the waiter spilling water on the microphone.

## Question

> Does Devika believe the microphone is functioning well or malfunctioning due to the water spill?

## Answer choices

- **A:** Devika believes the microphone is malfunctioning due to the water spill.
- **B:** Devika believes the microphone is functioning well.

**Reference answer:** Devika believes the microphone is functioning well. (`B`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Devika is attending a wedding reception at a luxurious hotel. She plans to give the newlyweds a heartfelt speech as a close friend of the couple. She sees that the microphone on the stage is connected and ready to use. Devika believes that the microphone is functioning well. However, just before her turn to speak, a waiter accidentally spills water on the microphone, causing it to malfunction. Devika does not see the waiter spilling water on the microphone.",
  "question": "Does Devika believe the microphone is functioning well or malfunctioning due to the water spill?",
  "choices": {
    "A": "Devika believes the microphone is malfunctioning due to the water spill.",
    "B": "Devika believes the microphone is functioning well."
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Devika believes the microphone is functioning well. | Correct |
| Opus 5.5 | Devika believes the microphone is functioning well. | Correct |
| GLiDE v1.2 | Devika believes the microphone is functioning well. | Correct |
| Decider v1.1 | Devika believes the microphone is functioning well. | Correct |
| Jev | Devika believes the microphone is functioning well. | Correct |
| Microsoft Decision-1 | Devika believes the microphone is functioning well. | Correct |
| Clef | Devika believes the microphone is functioning well. | Correct |
| Luna Decisions | Devika believes the microphone is functioning well. | Correct |
| Clef Flash | Devika believes the microphone is functioning well. | Correct |
| Strands Decider | Devika believes the microphone is functioning well. | Correct |
| GLiNER2.5 Decide | Devika believes the microphone is malfunctioning due to the water spill. | Incorrect |
| Laya | Devika believes the microphone is malfunctioning due to the water spill. | Incorrect |
| CalDec v1 | Devika believes the microphone is malfunctioning due to the water spill. | Incorrect |

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
    "record": "185/forward-belief/false",
    "kind": "source_file_record"
  },
  "source_revision": "fe647d680bddb69f738519313bed625f9e93b549",
  "input_hash": "64d0beaed573cd9e81e9ddbdbf1c2538081fc2fb7e9b9a018a6d6d643d2d7a33"
}
```

</details>
