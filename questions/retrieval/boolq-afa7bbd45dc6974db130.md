# Retrieval · question 22

[Back to Retrieval](README.md) · [All capabilities](../README.md)

**Question ID:** `boolq/afa7bbd45dc6974db130`  
**Source:** [BoolQ](https://huggingface.co/datasets/google/boolq)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/retrieval/boolq-afa7bbd45dc6974db130/README.md)

## Context

> Aside from tidal flooding along rivers, the storm's effects were primarily concentrated along the coast. A buoy off the coast of Nova Scotia reported a wave height of 100.7 feet (30.7 m), the highest ever recorded in the province's offshore waters. In the middle of the storm, the fishing vessel Andrea Gail sank, killing her crew of six and inspiring the book, and later movie, The Perfect Storm. Off the shore of New York's Long Island, an Air National Guard helicopter ran out of fuel and crashed; four members of its crew were rescued and one was killed. Two people died after their boat sank off Staten Island. High waves swept two people to their deaths, one in Rhode Island and one in Puerto Rico, and another person was blown off a bridge to his death. The tropical cyclone that formed late in the storm's duration caused little impact, limited to power outages and slick roads; one person was killed in Newfoundland from a traffic accident related to the storm.

## Question

> did a helicopter crash in the perfect storm

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** Yes (`yes`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Aside from tidal flooding along rivers, the storm's effects were primarily concentrated along the coast. A buoy off the coast of Nova Scotia reported a wave height of 100.7 feet (30.7 m), the highest ever recorded in the province's offshore waters. In the middle of the storm, the fishing vessel Andrea Gail sank, killing her crew of six and inspiring the book, and later movie, The Perfect Storm. Off the shore of New York's Long Island, an Air National Guard helicopter ran out of fuel and crashed; four members of its crew were rescued and one was killed. Two people died after their boat sank off Staten Island. High waves swept two people to their deaths, one in Rhode Island and one in Puerto Rico, and another person was blown off a bridge to his death. The tropical cyclone that formed late in the storm's duration caused little impact, limited to power outages and slick roads; one person was killed in Newfoundland from a traffic accident related to the storm.",
  "question": "did a helicopter crash in the perfect storm",
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

Original Wikipedia passage: [1991 Perfect Storm](https://en.wikipedia.org/wiki/1991_Perfect_Storm); [contributor history](https://en.wikipedia.org/w/index.php?title=1991_Perfect_Storm&action=history). The BoolQ excerpt is unchanged. This question material retains CC BY-SA 3.0.

Attribution: Wikipedia contributors; Christopher Clark, Kenton Lee, Ming-Wei Chang, Tom Kwiatkowski, Michael Collins, Kristina Toutanova (BoolQ).  
Terms: **[CC-BY-SA-3.0](https://creativecommons.org/licenses/by-sa/3.0/)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "data/validation-00000-of-00001.parquet",
    "record": "2148",
    "kind": "source_file_record"
  },
  "source_revision": "35b264d03638db9f4ce671b711558bf7ff0f80d5",
  "input_hash": "f997980b1fcac6640535a69066969197209ec44f2a6a6affb3c15bbed07ea9c5"
}
```

</details>
