# Retrieval · question 2

[Back to Retrieval](README.md) · [All capabilities](../README.md)

**Question ID:** `boolq/9fe14fdda69face5bd96`  
**Source:** [BoolQ](https://huggingface.co/datasets/google/boolq)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/retrieval/boolq-9fe14fdda69face5bd96/README.md)

## Context

> Mowgli is an upcoming adventure fantasy film directed by Andy Serkis and written by Callie Kloves, based on The Jungle Book by Rudyard Kipling. The film stars Rohan Chand, Matthew Rhys and Freida Pinto, along with voice and motion capture performances from Christian Bale, Cate Blanchett, Benedict Cumberbatch, Naomie Harris and Serkis.

## Question

> is there a new jungle book movie coming out

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** Yes (`yes`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Mowgli is an upcoming adventure fantasy film directed by Andy Serkis and written by Callie Kloves, based on The Jungle Book by Rudyard Kipling. The film stars Rohan Chand, Matthew Rhys and Freida Pinto, along with voice and motion capture performances from Christian Bale, Cate Blanchett, Benedict Cumberbatch, Naomie Harris and Serkis.",
  "question": "is there a new jungle book movie coming out",
  "choices": {
    "yes": "Yes",
    "no": "No"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | Yes | Correct |
| Opus 5.5 | Yes | Correct |
| GLiDE v1.2 | Yes | Correct |
| Decider v1.1 | Yes | Correct |
| Jev | Yes | Correct |
| Microsoft Decision-1 | Yes | Correct |
| Clef | Yes | Correct |
| Luna Decisions | Yes | Correct |
| Clef Flash | Yes | Correct |
| Strands Decider | Yes | Correct |
| GLiNER2.5 Decide | Yes | Correct |
| Laya | Yes | Correct |
| CalDec v1 | Yes | Correct |

## Source and sharing

Original Wikipedia passage: [Mowgli (film)](https://en.wikipedia.org/wiki/Mowgli_%28film%29); [contributor history](https://en.wikipedia.org/w/index.php?title=Mowgli_%28film%29&action=history). The BoolQ excerpt is unchanged. This question material retains CC BY-SA 3.0.

Attribution: Wikipedia contributors; Christopher Clark, Kenton Lee, Ming-Wei Chang, Tom Kwiatkowski, Michael Collins, Kristina Toutanova (BoolQ).  
Terms: **[CC-BY-SA-3.0](https://creativecommons.org/licenses/by-sa/3.0/)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "data/train-00000-of-00001.parquet",
    "record": "5116",
    "kind": "source_file_record"
  },
  "source_revision": "35b264d03638db9f4ce671b711558bf7ff0f80d5",
  "input_hash": "7c200ab2f6a02381db02a098b9c2ba97b55f0730e88f418918e5f02c817d8c45"
}
```

</details>
