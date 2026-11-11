# Option order · Move the first answer choice to the end variant

[Original question](../../../questions/retrieval/boolq-aff1fc4b8e68bfa8e255.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Clark Kent's body is exhumed and placed in the amniotic fluid of the genesis chamber of the Kryptonian ship alongside the Mother Box, which in turn activates and successfully resurrects Superman. However, Superman's memories have not returned, and he attacks the group after Stone accidentally launches a projectile at him. On the verge of being killed by Superman, Batman enacts his contingency plan: Lois Lane. Superman calms down and leaves with Lane to his family home in Smallville, where he reflects and his memories slowly come back. In the turmoil, the last Mother Box is left unguarded and Steppenwolf retrieves it with ease. Without Superman to aid them, the five heroes travel to a village in Russia where Steppenwolf aims to unite the Mother Boxes once again to remake Earth. The team fights their way through the Parademons to reach Steppenwolf, although they are unable to distract him enough for Stone to separate the Mother boxes. Superman arrives and assists Allen in evacuating the city, as well as Stone in separating the Mother Boxes. The team defeats Steppenwolf, who, overcome with fear, is attacked by his own Parademons before they all teleport away.

## Question

> does superman appear in the movie justice league

## Answer choices

- **no.** No
- **yes.** Yes

**Reference answer:** `yes`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Clark Kent's body is exhumed and placed in the amniotic fluid of the genesis chamber of the Kryptonian ship alongside the Mother Box, which in turn activates and successfully resurrects Superman. However, Superman's memories have not returned, and he attacks the group after Stone accidentally launches a projectile at him. On the verge of being killed by Superman, Batman enacts his contingency plan: Lois Lane. Superman calms down and leaves with Lane to his family home in Smallville, where he reflects and his memories slowly come back. In the turmoil, the last Mother Box is left unguarded and Steppenwolf retrieves it with ease. Without Superman to aid them, the five heroes travel to a village in Russia where Steppenwolf aims to unite the Mother Boxes once again to remake Earth. The team fights their way through the Parademons to reach Steppenwolf, although they are unable to distract him enough for Stone to separate the Mother boxes. Superman arrives and assists Allen in evacuating the city, as well as Stone in separating the Mother Boxes. The team defeats Steppenwolf, who, overcome with fear, is attacked by his own Parademons before they all teleport away.",
  "question": "does superman appear in the movie justice league",
  "choices": {
    "no": "No",
    "yes": "Yes"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `yes` — Yes | `yes` — Yes | Same answer |
| Decider v1.1 | `yes` — Yes | `yes` — Yes | Same answer |
| Jev | `yes` — Yes | `yes` — Yes | Same answer |
| Microsoft Decision-1 | `yes` — Yes | `yes` — Yes | Same answer |
| Clef | `yes` — Yes | `yes` — Yes | Same answer |
| Luna Decisions | `yes` — Yes | `yes` — Yes | Same answer |
| Clef Flash | `yes` — Yes | `yes` — Yes | Same answer |
| Strands Decider | `yes` — Yes | `yes` — Yes | Same answer |
| GLiNER2.5 Decide | `yes` — Yes | `yes` — Yes | Same answer |
| Laya | `yes` — Yes | `yes` — Yes | Same answer |
| CalDec v1 | `yes` — Yes | `yes` — Yes | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `boolq/aff1fc4b8e68bfa8e255/option_order/rotate_1`

**Input fingerprint:** `826708e49708af13bd87ef170459e8e1d70c066f32b5e399b4e461a2b62f0482`

| Change | Recorded version |
| --- | --- |
| Option order | Move the first answer choice to the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/retrieval/boolq-aff1fc4b8e68bfa8e255.md).
