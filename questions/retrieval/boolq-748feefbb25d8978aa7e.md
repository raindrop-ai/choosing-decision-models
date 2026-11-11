# Retrieval · question 42

[Back to Retrieval](README.md) · [All capabilities](../README.md)

**Question ID:** `boolq/748feefbb25d8978aa7e`  
**Source:** [BoolQ](https://huggingface.co/datasets/google/boolq)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/retrieval/boolq-748feefbb25d8978aa7e/README.md)

## Context

> Later Liz realizes that she now has a power: to see the future. When she touches Max she has visions that she, Max, Isabel, and Michael are going to die. Michael says that Max, Liz and Isabel should leave Roswell separately because the FBI knows who they are and their life in Roswell has to be over. Maria is upset by this because she doesn't want to be left in Roswell alone without Michael or Liz. Max proposes to Liz, making the choice to be with her even if they have only 12 days. Liz says yes. They all attend their graduation and when they realize this is where they are supposed to die from one of Liz's flashes they all escape into the desert. Now Max, Liz, Michael, Maria, Isabel and Kyle decide to leave together because even though Maria and Kyle were not going to be killed, Kyle wants to be with his own kind when he develops his alien powers from Max's healing and Maria wants to be with Michael. They leave Roswell that night, and go together in a van, deciding to live life using their powers to do good deeds on the road. Liz sends her father her journal, continuing the truth about everything so he can understand why she left and finally know what has been going on in her life. Liz marries Max in a beautiful country church.

## Question

> roswell do max and liz end up together

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** Yes (`yes`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Later Liz realizes that she now has a power: to see the future. When she touches Max she has visions that she, Max, Isabel, and Michael are going to die. Michael says that Max, Liz and Isabel should leave Roswell separately because the FBI knows who they are and their life in Roswell has to be over. Maria is upset by this because she doesn't want to be left in Roswell alone without Michael or Liz. Max proposes to Liz, making the choice to be with her even if they have only 12 days. Liz says yes. They all attend their graduation and when they realize this is where they are supposed to die from one of Liz's flashes they all escape into the desert. Now Max, Liz, Michael, Maria, Isabel and Kyle decide to leave together because even though Maria and Kyle were not going to be killed, Kyle wants to be with his own kind when he develops his alien powers from Max's healing and Maria wants to be with Michael. They leave Roswell that night, and go together in a van, deciding to live life using their powers to do good deeds on the road. Liz sends her father her journal, continuing the truth about everything so he can understand why she left and finally know what has been going on in her life. Liz marries Max in a beautiful country church.",
  "question": "roswell do max and liz end up together",
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

Original Wikipedia passage: [Liz Parker](https://en.wikipedia.org/wiki/Liz_Parker); [contributor history](https://en.wikipedia.org/w/index.php?title=Liz_Parker&action=history). The BoolQ excerpt is unchanged. This question material retains CC BY-SA 3.0.

Attribution: Wikipedia contributors; Christopher Clark, Kenton Lee, Ming-Wei Chang, Tom Kwiatkowski, Michael Collins, Kristina Toutanova (BoolQ).  
Terms: **[CC-BY-SA-3.0](https://creativecommons.org/licenses/by-sa/3.0/)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "data/train-00000-of-00001.parquet",
    "record": "8237",
    "kind": "source_file_record"
  },
  "source_revision": "35b264d03638db9f4ce671b711558bf7ff0f80d5",
  "input_hash": "4b6a39e18639243d343ec52b319c5622f6843251d9d10f1cf6603224233f3ed4"
}
```

</details>
