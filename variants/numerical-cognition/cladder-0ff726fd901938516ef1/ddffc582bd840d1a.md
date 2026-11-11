# Extra events · Add 12 unrelated events variant

[Original question](../../../questions/numerical-cognition/cladder-0ff726fd901938516ef1.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.
> Nolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue. Nolan classifies Kesil as an elegy. Nolan classifies Nereth as a satire. Nolan classifies Pavrel as a fable. Nolan classifies Sovrin as a ballad. Nolan reclassifies Virel as a monologue. Nolan reclassifies Zorven as a dialogue. Nolan reclassifies Kesil as a ballad. Nolan reclassifies Nereth as a fable. Nolan reclassifies Pavrel as a satire. Nolan reclassifies Sovrin as an elegy.
>
> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Vaccination status has a direct effect on vaccination reaction and getting smallpox. Getting smallpox has a direct effect on smallpox survival. Vaccination reaction has a direct effect on smallpox survival.
> The overall probability of vaccination is 96%. For unvaccinated individuals, the probability of smallpox survival is 36%. For vaccinated individuals, the probability of smallpox survival is 56%.

## Question

> Is smallpox survival less likely than smallpox death overall?

## Answer choices

- **yes.** Yes
- **no.** No

**Reference answer:** `no`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.\nNolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue. Nolan classifies Kesil as an elegy. Nolan classifies Nereth as a satire. Nolan classifies Pavrel as a fable. Nolan classifies Sovrin as a ballad. Nolan reclassifies Virel as a monologue. Nolan reclassifies Zorven as a dialogue. Nolan reclassifies Kesil as a ballad. Nolan reclassifies Nereth as a fable. Nolan reclassifies Pavrel as a satire. Nolan reclassifies Sovrin as an elegy.\n\nImagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Vaccination status has a direct effect on vaccination reaction and getting smallpox. Getting smallpox has a direct effect on smallpox survival. Vaccination reaction has a direct effect on smallpox survival.\nThe overall probability of vaccination is 96%. For unvaccinated individuals, the probability of smallpox survival is 36%. For vaccinated individuals, the probability of smallpox survival is 56%.",
  "question": "Is smallpox survival less likely than smallpox death overall?",
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
| GLiDE v1.2 | `no` — No | `no` — No | Same answer |
| Decider v1.1 | `no` — No | `no` — No | Same answer |
| Jev | `no` — No | `no` — No | Same answer |
| Microsoft Decision-1 | `no` — No | `no` — No | Same answer |
| Clef | `yes` — Yes | `yes` — Yes | Same answer |
| Luna Decisions | `yes` — Yes | `yes` — Yes | Same answer |
| Clef Flash | `yes` — Yes | `yes` — Yes | Same answer |
| Strands Decider | `no` — No | `no` — No | Same answer |
| GLiNER2.5 Decide | `no` — No | `yes` — Yes | Different answer |
| Laya | `yes` — Yes | `yes` — Yes | Same answer |
| CalDec v1 | `yes` — Yes | `yes` — Yes | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cladder/0ff726fd901938516ef1/event_count/12/clean-source_first_cladder_short_contexts_full_0129`

**Input fingerprint:** `e661778b5a79be8dc8c89051b1a29ea7e4a9bf490b3b9180f4c182fc232ecd29`

| Change | Recorded version |
| --- | --- |
| Extra events | Add 12 unrelated events |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/numerical-cognition/cladder-0ff726fd901938516ef1.md).
