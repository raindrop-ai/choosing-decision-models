# Retrieval · question 67

[Back to Retrieval](README.md) · [All capabilities](../README.md)

**Question ID:** `boolq/1c12c4b9578fa18abcd1`  
**Source:** [BoolQ](https://huggingface.co/datasets/google/boolq)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/retrieval/boolq-1c12c4b9578fa18abcd1/README.md)

## Context

> Batman v Superman: Dawn of Justice premiered at the Auditorio Nacional in Mexico City on March 19, 2016, and was released in the United States on March 25, 2016 in 2D, 3D, IMAX 3D, 4DX, premium large formats, and 70 mm prints by Warner Bros. Pictures. Following a strong debut that set new box office records, the film experienced a historic drop in its second weekend and never recovered. Despite turning a profit, it was deemed a box office disappointment and received generally unfavorable reviews from critics for its tone, screenplay, and pacing, though some praised its visual style and acting performances. An extended cut dubbed the \`\`Ultimate Edition'', which features 31 minutes of additional footage, was released digitally on June 28, 2016, and on Blu-ray on July 19, 2016. A direct sequel, titled Justice League, was released in November 2017.

## Question

> is there a sequel to batman versus superman

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** Yes (`yes`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Batman v Superman: Dawn of Justice premiered at the Auditorio Nacional in Mexico City on March 19, 2016, and was released in the United States on March 25, 2016 in 2D, 3D, IMAX 3D, 4DX, premium large formats, and 70 mm prints by Warner Bros. Pictures. Following a strong debut that set new box office records, the film experienced a historic drop in its second weekend and never recovered. Despite turning a profit, it was deemed a box office disappointment and received generally unfavorable reviews from critics for its tone, screenplay, and pacing, though some praised its visual style and acting performances. An extended cut dubbed the ``Ultimate Edition'', which features 31 minutes of additional footage, was released digitally on June 28, 2016, and on Blu-ray on July 19, 2016. A direct sequel, titled Justice League, was released in November 2017.",
  "question": "is there a sequel to batman versus superman",
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

Original Wikipedia passage: [Batman v Superman: Dawn of Justice](https://en.wikipedia.org/wiki/Batman_v_Superman%3A_Dawn_of_Justice); [contributor history](https://en.wikipedia.org/w/index.php?title=Batman_v_Superman%3A_Dawn_of_Justice&action=history). The BoolQ excerpt is unchanged. This question material retains CC BY-SA 3.0.

Attribution: Wikipedia contributors; Christopher Clark, Kenton Lee, Ming-Wei Chang, Tom Kwiatkowski, Michael Collins, Kristina Toutanova (BoolQ).  
Terms: **[CC-BY-SA-3.0](https://creativecommons.org/licenses/by-sa/3.0/)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "data/train-00000-of-00001.parquet",
    "record": "2351",
    "kind": "source_file_record"
  },
  "source_revision": "35b264d03638db9f4ce671b711558bf7ff0f80d5",
  "input_hash": "90ade01b9c5441f606a9ef554465592fb42836ffe1c0c1fc8017c023125a20ba"
}
```

</details>
