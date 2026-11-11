# Social cognition · question 19

[Back to Social cognition](README.md) · [All capabilities](../README.md)

**Question ID:** `bigtom/c5644ba015c2bdfaeeab`  
**Source:** [BigToM](https://github.com/cicl-stanford/procedural-evals-tom)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/social-cognition/bigtom-c5644ba015c2bdfaeeab/README.md)

## Context

> Olga is a botanist exploring a remote rainforest in search of a rare orchid species. Olga wants to find and document the orchid to contribute to her research on endangered plants. She sees that the map she carries with her indicates that the orchid is located in a specific area of the rainforest. Olga believes that the rare orchid is in the area shown on the map. A sudden landslide alters the rainforest landscape, moving the orchid to a different location. Olga does not notice the aftermath of the landslide.

## Question

> Does Olga believe the rare orchid is in the area shown on the map or in the affected area?

## Answer choices

- **A:** Olga believes the rare orchid is in the affected area.
- **B:** Olga believes the rare orchid is in the area shown on the map.

**Reference answer:** Olga believes the rare orchid is in the area shown on the map. (`B`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Olga is a botanist exploring a remote rainforest in search of a rare orchid species. Olga wants to find and document the orchid to contribute to her research on endangered plants. She sees that the map she carries with her indicates that the orchid is located in a specific area of the rainforest. Olga believes that the rare orchid is in the area shown on the map. A sudden landslide alters the rainforest landscape, moving the orchid to a different location. Olga does not notice the aftermath of the landslide.",
  "question": "Does Olga believe the rare orchid is in the area shown on the map or in the affected area?",
  "choices": {
    "A": "Olga believes the rare orchid is in the affected area.",
    "B": "Olga believes the rare orchid is in the area shown on the map."
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Olga believes the rare orchid is in the area shown on the map. | Correct |
| Opus 5.5 | Olga believes the rare orchid is in the area shown on the map. | Correct |
| GLiDE v1.2 | Olga believes the rare orchid is in the area shown on the map. | Correct |
| Decider v1.1 | Olga believes the rare orchid is in the area shown on the map. | Correct |
| Jev | Olga believes the rare orchid is in the area shown on the map. | Correct |
| Microsoft Decision-1 | Olga believes the rare orchid is in the area shown on the map. | Correct |
| Clef | Olga believes the rare orchid is in the area shown on the map. | Correct |
| Luna Decisions | Olga believes the rare orchid is in the area shown on the map. | Correct |
| Clef Flash | Olga believes the rare orchid is in the area shown on the map. | Correct |
| Strands Decider | Olga believes the rare orchid is in the area shown on the map. | Correct |
| GLiNER2.5 Decide | Olga believes the rare orchid is in the area shown on the map. | Correct |
| Laya | Olga believes the rare orchid is in the area shown on the map. | Correct |
| CalDec v1 | Olga believes the rare orchid is in the area shown on the map. | Correct |

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
    "record": "119/forward-belief/false",
    "kind": "source_file_record"
  },
  "source_revision": "fe647d680bddb69f738519313bed625f9e93b549",
  "input_hash": "ca08d8eb469bf7733ec46811ae2021382c81a8220696148e3f669f42adbe76b3"
}
```

</details>
