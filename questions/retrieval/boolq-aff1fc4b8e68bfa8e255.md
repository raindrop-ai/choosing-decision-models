# Retrieval · question 45

[Back to Retrieval](README.md) · [All capabilities](../README.md)

**Question ID:** `boolq/aff1fc4b8e68bfa8e255`  
**Source:** [BoolQ](https://huggingface.co/datasets/google/boolq)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/retrieval/boolq-aff1fc4b8e68bfa8e255/README.md)

## Context

> Clark Kent's body is exhumed and placed in the amniotic fluid of the genesis chamber of the Kryptonian ship alongside the Mother Box, which in turn activates and successfully resurrects Superman. However, Superman's memories have not returned, and he attacks the group after Stone accidentally launches a projectile at him. On the verge of being killed by Superman, Batman enacts his contingency plan: Lois Lane. Superman calms down and leaves with Lane to his family home in Smallville, where he reflects and his memories slowly come back. In the turmoil, the last Mother Box is left unguarded and Steppenwolf retrieves it with ease. Without Superman to aid them, the five heroes travel to a village in Russia where Steppenwolf aims to unite the Mother Boxes once again to remake Earth. The team fights their way through the Parademons to reach Steppenwolf, although they are unable to distract him enough for Stone to separate the Mother boxes. Superman arrives and assists Allen in evacuating the city, as well as Stone in separating the Mother Boxes. The team defeats Steppenwolf, who, overcome with fear, is attacked by his own Parademons before they all teleport away.

## Question

> does superman appear in the movie justice league

## Answer choices

- **yes:** Yes
- **no:** No

**Reference answer:** Yes (`yes`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Clark Kent's body is exhumed and placed in the amniotic fluid of the genesis chamber of the Kryptonian ship alongside the Mother Box, which in turn activates and successfully resurrects Superman. However, Superman's memories have not returned, and he attacks the group after Stone accidentally launches a projectile at him. On the verge of being killed by Superman, Batman enacts his contingency plan: Lois Lane. Superman calms down and leaves with Lane to his family home in Smallville, where he reflects and his memories slowly come back. In the turmoil, the last Mother Box is left unguarded and Steppenwolf retrieves it with ease. Without Superman to aid them, the five heroes travel to a village in Russia where Steppenwolf aims to unite the Mother Boxes once again to remake Earth. The team fights their way through the Parademons to reach Steppenwolf, although they are unable to distract him enough for Stone to separate the Mother boxes. Superman arrives and assists Allen in evacuating the city, as well as Stone in separating the Mother Boxes. The team defeats Steppenwolf, who, overcome with fear, is attacked by his own Parademons before they all teleport away.",
  "question": "does superman appear in the movie justice league",
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

Original Wikipedia passage: [Justice League (film)](https://en.wikipedia.org/wiki/Justice_League_%28film%29); [contributor history](https://en.wikipedia.org/w/index.php?title=Justice_League_%28film%29&action=history). The BoolQ excerpt is unchanged. This question material retains CC BY-SA 3.0.

Attribution: Wikipedia contributors; Christopher Clark, Kenton Lee, Ming-Wei Chang, Tom Kwiatkowski, Michael Collins, Kristina Toutanova (BoolQ).  
Terms: **[CC-BY-SA-3.0](https://creativecommons.org/licenses/by-sa/3.0/)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "data/train-00000-of-00001.parquet",
    "record": "4761",
    "kind": "source_file_record"
  },
  "source_revision": "35b264d03638db9f4ce671b711558bf7ff0f80d5",
  "input_hash": "a376e68bef92cfe1c468a2dbca001841ccffe2439e264720939382257a7a56d6"
}
```

</details>
