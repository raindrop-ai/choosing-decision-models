# Extra events · Add 2 unrelated events variant

[Original question](../../../questions/numerical-cognition/mmlu-b94c0a08436343bbf655.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.
> Nolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue.

## Question

> Two computers communicate with each other by sending data packets across a local area network. The size of these packets is 1,000 bytes. The network has the capacity to carry 1,000 packets per second. The CPU time required to execute the network protocol to send one packet is 10 milliseconds. The maximum rate at which one computer can send data to another is approximately

## Answer choices

- **A.** 10,000 bytes/second
- **B.** 25,000 bytes/ second
- **C.** 100,000 bytes/ second
- **D.** 500,000 bytes/ second

**Reference answer:** `C`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.\nNolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue.",
  "question": "Two computers communicate with each other by sending data packets across a local area network. The size of these packets is 1,000 bytes. The network has the capacity to carry 1,000 packets per second. The CPU time required to execute the network protocol to send one packet is 10 milliseconds. The maximum rate at which one computer can send data to another is approximately",
  "choices": {
    "A": "10,000 bytes/second",
    "B": "25,000 bytes/ second",
    "C": "100,000 bytes/ second",
    "D": "500,000 bytes/ second"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `D` — 500,000 bytes/ second | `C` — 100,000 bytes/ second | Different answer |
| Decider v1.1 | `C` — 100,000 bytes/ second | `C` — 100,000 bytes/ second | Same answer |
| Jev | `C` — 100,000 bytes/ second | `C` — 100,000 bytes/ second | Same answer |
| Microsoft Decision-1 | `A` — 10,000 bytes/second | `A` — 10,000 bytes/second | Same answer |
| Clef | `C` — 100,000 bytes/ second | `C` — 100,000 bytes/ second | Same answer |
| Luna Decisions | `C` — 100,000 bytes/ second | `C` — 100,000 bytes/ second | Same answer |
| Clef Flash | `C` — 100,000 bytes/ second | `C` — 100,000 bytes/ second | Same answer |
| Strands Decider | `C` — 100,000 bytes/ second | `C` — 100,000 bytes/ second | Same answer |
| GLiNER2.5 Decide | `A` — 10,000 bytes/second | `A` — 10,000 bytes/second | Same answer |
| Laya | `A` — 10,000 bytes/second | `A` — 10,000 bytes/second | Same answer |
| CalDec v1 | `A` — 10,000 bytes/second | `A` — 10,000 bytes/second | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `mmlu/b94c0a08436343bbf655/event_count/2/clean-source_first_mmlu_quantitative_contexts_full_0098`

**Input fingerprint:** `6eca26ce2b5a13654477cbf3bfe206ee6a2fcd550eef133e71bbf0de3a21bc78`

| Change | Recorded version |
| --- | --- |
| Extra events | Add 2 unrelated events |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/numerical-cognition/mmlu-b94c0a08436343bbf655.md).
