# State tracking and updating · question 31

[Back to State tracking and updating](README.md) · [All capabilities](../README.md)

**Question ID:** `bbh/bf962fc80db47dec8186`  
**Source:** [BIG-Bench Hard selected tasks](https://github.com/suzgunmirac/BIG-Bench-Hard)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/state-tracking-and-updating/bbh-bf962fc80db47dec8186/README.md)

## Question

> Alice, Bob, and Claire are dancers at a square dance. At the start of a song, they each have a partner: Alice is dancing with Karl, Bob is dancing with Rodrigo, and Claire is dancing with Helga.
> Throughout the song, the dancers often trade partners. First, Bob and Alice switch partners. Then, Alice and Claire switch partners. Finally, Alice and Bob switch partners. At the end of the dance, Alice is dancing with

## Answer choices

- **A:** Karl
- **B:** Rodrigo
- **C:** Helga

**Reference answer:** Karl (`A`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "Alice, Bob, and Claire are dancers at a square dance. At the start of a song, they each have a partner: Alice is dancing with Karl, Bob is dancing with Rodrigo, and Claire is dancing with Helga.\nThroughout the song, the dancers often trade partners. First, Bob and Alice switch partners. Then, Alice and Claire switch partners. Finally, Alice and Bob switch partners. At the end of the dance, Alice is dancing with",
  "choices": {
    "A": "Karl",
    "B": "Rodrigo",
    "C": "Helga"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Karl | Correct |
| Opus 5.5 | Karl | Correct |
| GLiDE v1.2 | Karl | Correct |
| Decider v1.1 | Rodrigo | Incorrect |
| Jev | Karl | Correct |
| Microsoft Decision-1 | Karl | Correct |
| Clef | Rodrigo | Incorrect |
| Luna Decisions | Rodrigo | Incorrect |
| Clef Flash | Rodrigo | Incorrect |
| Strands Decider | Rodrigo | Incorrect |
| GLiNER2.5 Decide | Helga | Incorrect |
| Laya | Karl | Correct |
| CalDec v1 | Karl | Correct |

## Source and sharing

Attribution: Mirac Suzgun and BIG-Bench Hard authors; BIG-bench contributors.  
Terms: **[MIT AND Apache-2.0](https://opensource.org/license/mit)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "bbh/tracking_shuffled_objects_three_objects.json",
    "record": "11",
    "kind": "source_file_record"
  },
  "source_revision": "9ee07bd481feebf959a6b59d61ea57bdcf30964d",
  "input_hash": "5c23cc7781d34163d6800571771b6edc19ae145cd0013658acb2464bb7f4434a"
}
```

</details>
