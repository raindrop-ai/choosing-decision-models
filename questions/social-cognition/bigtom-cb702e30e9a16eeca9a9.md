# Social cognition · question 59

[Back to Social cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `bigtom/cb702e30e9a16eeca9a9`  
**Source:** [BigToM](https://github.com/cicl-stanford/procedural-evals-tom)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/social-cognition/bigtom-cb702e30e9a16eeca9a9/README.md)

## Context

> Amara, a skilled Nigerian weaver, is preparing to create a traditional textile for an upcoming cultural exhibition. Amara wants to use a unique combination of colorful threads that represents her heritage. Amara carefully chooses a set of vibrant, high-quality threads for her project. She believes the threads she has chosen are strong and perfect for her textile. A curious toddler in her home finds the threads and tangles them, making them difficult to use in the weaving process. Amara notices the tangled threads.

## Question

> Does Amara believe the threads are strong and perfect for her textile or tangled and difficult to use?

## Answer choices

- **A:** Amara believes the threads are tangled and difficult to use.
- **B:** Amara believes the threads are strong and perfect for her textile.

**Reference answer:** Amara believes the threads are tangled and difficult to use. (`A`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Amara, a skilled Nigerian weaver, is preparing to create a traditional textile for an upcoming cultural exhibition. Amara wants to use a unique combination of colorful threads that represents her heritage. Amara carefully chooses a set of vibrant, high-quality threads for her project. She believes the threads she has chosen are strong and perfect for her textile. A curious toddler in her home finds the threads and tangles them, making them difficult to use in the weaving process. Amara notices the tangled threads.",
  "question": "Does Amara believe the threads are strong and perfect for her textile or tangled and difficult to use?",
  "choices": {
    "A": "Amara believes the threads are tangled and difficult to use.",
    "B": "Amara believes the threads are strong and perfect for her textile."
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Amara believes the threads are tangled and difficult to use. | Correct |
| Opus 5.5 | Amara believes the threads are tangled and difficult to use. | Correct |
| GLiDE v1.2 | Amara believes the threads are tangled and difficult to use. | Correct |
| Decider v1.1 | Amara believes the threads are tangled and difficult to use. | Correct |
| Jev | Amara believes the threads are strong and perfect for her textile. | Incorrect |
| Microsoft Decision-1 | Amara believes the threads are strong and perfect for her textile. | Incorrect |
| Clef | Amara believes the threads are strong and perfect for her textile. | Incorrect |
| Luna Decisions | Amara believes the threads are strong and perfect for her textile. | Incorrect |
| Clef Flash | Amara believes the threads are strong and perfect for her textile. | Incorrect |
| Strands Decider | Amara believes the threads are strong and perfect for her textile. | Incorrect |
| GLiNER2.5 Decide | Amara believes the threads are strong and perfect for her textile. | Incorrect |
| Laya | Amara believes the threads are tangled and difficult to use. | Correct |
| CalDec v1 | Amara believes the threads are tangled and difficult to use. | Correct |

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
    "record": "68/forward-belief/true",
    "kind": "source_file_record"
  },
  "source_revision": "fe647d680bddb69f738519313bed625f9e93b549",
  "input_hash": "790586986cf4b7411d975fe57b98f5bc3b16102d72025e79406a6dcdaad3d4ba"
}
```

</details>
