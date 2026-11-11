# State tracking and updating · question 36

[Back to State tracking and updating](README.md) · [All capabilities](../README.md)

**Question ID:** `bbh/7e4b9ee7df2a57a444be`  
**Source:** [BIG-Bench Hard selected tasks](https://github.com/suzgunmirac/BIG-Bench-Hard)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/state-tracking-and-updating/bbh-7e4b9ee7df2a57a444be/README.md)

## Question

> Alice, Bob, Claire, Dave, and Eve are friends and avid readers who occasionally trade books. At the start of the semester, they each buy one new book: Alice gets The Great Gatsby, Bob gets Frankenstein, Claire gets Moby Dick, Dave gets The Fellowship of the Ring, and Eve gets Catch-22.
> As the semester proceeds, they start trading around the new books. First, Alice and Bob swap books. Then, Dave and Eve swap books. Then, Eve and Alice swap books. Then, Dave and Eve swap books. Finally, Claire and Dave swap books. At the end of the semester, Dave has

## Answer choices

- **A:** The Great Gatsby
- **B:** Frankenstein
- **C:** Moby Dick
- **D:** The Fellowship of the Ring
- **E:** Catch-22

**Reference answer:** Moby Dick (`C`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "Alice, Bob, Claire, Dave, and Eve are friends and avid readers who occasionally trade books. At the start of the semester, they each buy one new book: Alice gets The Great Gatsby, Bob gets Frankenstein, Claire gets Moby Dick, Dave gets The Fellowship of the Ring, and Eve gets Catch-22.\nAs the semester proceeds, they start trading around the new books. First, Alice and Bob swap books. Then, Dave and Eve swap books. Then, Eve and Alice swap books. Then, Dave and Eve swap books. Finally, Claire and Dave swap books. At the end of the semester, Dave has",
  "choices": {
    "A": "The Great Gatsby",
    "B": "Frankenstein",
    "C": "Moby Dick",
    "D": "The Fellowship of the Ring",
    "E": "Catch-22"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Moby Dick | Correct |
| Opus 5.5 | Moby Dick | Correct |
| GLiDE v1.2 | Moby Dick | Correct |
| Decider v1.1 | Frankenstein | Incorrect |
| Jev | Moby Dick | Correct |
| Microsoft Decision-1 | Moby Dick | Correct |
| Clef | Moby Dick | Correct |
| Luna Decisions | Frankenstein | Incorrect |
| Clef Flash | Moby Dick | Correct |
| Strands Decider | Catch-22 | Incorrect |
| GLiNER2.5 Decide | The Great Gatsby | Incorrect |
| Laya | The Fellowship of the Ring | Incorrect |
| CalDec v1 | The Great Gatsby | Incorrect |

## Source and sharing

Attribution: Mirac Suzgun and BIG-Bench Hard authors; BIG-bench contributors.  
Terms: **[MIT AND Apache-2.0](https://opensource.org/license/mit)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "bbh/tracking_shuffled_objects_five_objects.json",
    "record": "188",
    "kind": "source_file_record"
  },
  "source_revision": "9ee07bd481feebf959a6b59d61ea57bdcf30964d",
  "input_hash": "6cfc0d9ab97c30c5b6aae5ae1325b0102e1803fb567f9991b069c1de9bd19833"
}
```

</details>
