# Similar distractors · Add more similar but irrelevant items variant

[Original question](../../../questions/retrieval/boolq-a23fe4476f05d44d34f8.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> A blighted ovum or anembryonic gestation is characterized by a normal-appearing gestational sac, but the absence of an embryo. It likely occurs as a result of early embryonic death with continued development of the trophoblast. When small, the sac cannot be distinguished from the early normal pregnancy, as there may be a yolk sac, though a fetal pole is not seen. For diagnosis, the sac must be of sufficient size that the absence of normal embryonic elements is established. The criteria depends on the type of ultrasound exam performed. A pregnancy is anembryonic if a transvaginal ultrasound reveals a sac with a mean gestational sac diameter (MGD) greater than 25 mm and no yolk sac, or an MGD &gt;25 mm with no embryo. Transabdominal imaging without transvaginal scanning may be sufficient for diagnosing early pregnancy failure when an embryo whose crown--rump length is 15 mm or more has no visible cardiac activity.
>
> «This fictional ultrasound-training phantom has a sac-shaped chamber and a yolk-sac-shaped insert.»
>
> «This fictional teaching diagram shows an empty outer chamber with an embryo-shaped marker placed beside it.»
>
> «This fictional mechanical teaching display has a sac-shaped chamber while a fetal-pole-shaped component is stored in a separate box. It is not a biological specimen.»

## Question

> can a blighted ovum have a yolk sac

## Answer choices

- **yes.** Yes
- **no.** No

**Reference answer:** `yes`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "A blighted ovum or anembryonic gestation is characterized by a normal-appearing gestational sac, but the absence of an embryo. It likely occurs as a result of early embryonic death with continued development of the trophoblast. When small, the sac cannot be distinguished from the early normal pregnancy, as there may be a yolk sac, though a fetal pole is not seen. For diagnosis, the sac must be of sufficient size that the absence of normal embryonic elements is established. The criteria depends on the type of ultrasound exam performed. A pregnancy is anembryonic if a transvaginal ultrasound reveals a sac with a mean gestational sac diameter (MGD) greater than 25 mm and no yolk sac, or an MGD >25 mm with no embryo. Transabdominal imaging without transvaginal scanning may be sufficient for diagnosing early pregnancy failure when an embryo whose crown--rump length is 15 mm or more has no visible cardiac activity.\n\n«This fictional ultrasound-training phantom has a sac-shaped chamber and a yolk-sac-shaped insert.»\n\n«This fictional teaching diagram shows an empty outer chamber with an embryo-shaped marker placed beside it.»\n\n«This fictional mechanical teaching display has a sac-shaped chamber while a fetal-pole-shaped component is stored in a separate box. It is not a biological specimen.»",
  "question": "can a blighted ovum have a yolk sac",
  "choices": {
    "yes": "Yes",
    "no": "No"
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
| GLiNER2.5 Decide | `no` — No | `no` — No | Same answer |
| Laya | `yes` — Yes | `yes` — Yes | Same answer |
| CalDec v1 | `yes` — Yes | `no` — No | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `boolq/a23fe4476f05d44d34f8/similar_distractors/high/clean-source_first_parallel_b_operations_0302`

**Input fingerprint:** `13eafec116ce14cfc192e648e0267260e73c482674f00bcea0bf551a2f6e6951`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add more similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/retrieval/boolq-a23fe4476f05d44d34f8.md).
