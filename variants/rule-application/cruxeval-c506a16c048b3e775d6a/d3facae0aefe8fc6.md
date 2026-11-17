# Paraphrasing · Change the sentence structure variant

[Original question](../../../questions/rule-application/cruxeval-c506a16c048b3e775d6a.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

```text
def f(d):
    keys = []
    for k in d:
        keys.append('%s => %s' % (k, d[k]))
    return keys
```

## Question

> Determine the return value of f({'-4':'4','1':'2','-':'-3'}).

## Answer choices

- **A.** \[&#x27;-4 =&gt; 4&#x27;, &#x27;1 =&gt; 2&#x27;, &#x27;- =&gt; -3&#x27;\]
- **B.** \[&#x27;-4 =&gt; 4&#x27;, &#x27;1 =&gt; 2&#x27;, &#x27;= =&gt; -3&#x27;\]
- **C.** \[&#x27;-4 =&gt; 4&#x27;, &#x27;1 =&gt; 2&#x27;, &#x27;3- =&gt; -&#x27;\]
- **D.** \[&#x27;-4 =&gt; 4&#x27;, &#x27;2 =&gt; 2&#x27;, &#x27;- =&gt; -3&#x27;\]

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "def f(d):\n    keys = []\n    for k in d:\n        keys.append('%s => %s' % (k, d[k]))\n    return keys",
  "question": "Determine the return value of f({'-4':'4','1':'2','-':'-3'}).",
  "choices": {
    "A": "['-4 => 4', '1 => 2', '- => -3']",
    "B": "['-4 => 4', '1 => 2', '= => -3']",
    "C": "['-4 => 4', '1 => 2', '3- => -']",
    "D": "['-4 => 4', '2 => 2', '- => -3']"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — \[&#x27;-4 =&gt; 4&#x27;, &#x27;1 =&gt; 2&#x27;, &#x27;- =&gt; -3&#x27;\] | `A` — \[&#x27;-4 =&gt; 4&#x27;, &#x27;1 =&gt; 2&#x27;, &#x27;- =&gt; -3&#x27;\] | Same answer |
| Decider v1.1 | `A` — \[&#x27;-4 =&gt; 4&#x27;, &#x27;1 =&gt; 2&#x27;, &#x27;- =&gt; -3&#x27;\] | `A` — \[&#x27;-4 =&gt; 4&#x27;, &#x27;1 =&gt; 2&#x27;, &#x27;- =&gt; -3&#x27;\] | Same answer |
| Jev | `A` — \[&#x27;-4 =&gt; 4&#x27;, &#x27;1 =&gt; 2&#x27;, &#x27;- =&gt; -3&#x27;\] | `A` — \[&#x27;-4 =&gt; 4&#x27;, &#x27;1 =&gt; 2&#x27;, &#x27;- =&gt; -3&#x27;\] | Same answer |
| Microsoft Decision-1 | `A` — \[&#x27;-4 =&gt; 4&#x27;, &#x27;1 =&gt; 2&#x27;, &#x27;- =&gt; -3&#x27;\] | `A` — \[&#x27;-4 =&gt; 4&#x27;, &#x27;1 =&gt; 2&#x27;, &#x27;- =&gt; -3&#x27;\] | Same answer |
| Clef | `A` — \[&#x27;-4 =&gt; 4&#x27;, &#x27;1 =&gt; 2&#x27;, &#x27;- =&gt; -3&#x27;\] | `A` — \[&#x27;-4 =&gt; 4&#x27;, &#x27;1 =&gt; 2&#x27;, &#x27;- =&gt; -3&#x27;\] | Same answer |
| Luna Decisions | `A` — \[&#x27;-4 =&gt; 4&#x27;, &#x27;1 =&gt; 2&#x27;, &#x27;- =&gt; -3&#x27;\] | `A` — \[&#x27;-4 =&gt; 4&#x27;, &#x27;1 =&gt; 2&#x27;, &#x27;- =&gt; -3&#x27;\] | Same answer |
| Clef Flash | `A` — \[&#x27;-4 =&gt; 4&#x27;, &#x27;1 =&gt; 2&#x27;, &#x27;- =&gt; -3&#x27;\] | `A` — \[&#x27;-4 =&gt; 4&#x27;, &#x27;1 =&gt; 2&#x27;, &#x27;- =&gt; -3&#x27;\] | Same answer |
| Strands Decider | `A` — \[&#x27;-4 =&gt; 4&#x27;, &#x27;1 =&gt; 2&#x27;, &#x27;- =&gt; -3&#x27;\] | `A` — \[&#x27;-4 =&gt; 4&#x27;, &#x27;1 =&gt; 2&#x27;, &#x27;- =&gt; -3&#x27;\] | Same answer |
| GLiNER2.5 Decide | `D` — \[&#x27;-4 =&gt; 4&#x27;, &#x27;2 =&gt; 2&#x27;, &#x27;- =&gt; -3&#x27;\] | `D` — \[&#x27;-4 =&gt; 4&#x27;, &#x27;2 =&gt; 2&#x27;, &#x27;- =&gt; -3&#x27;\] | Same answer |
| Laya | `A` — \[&#x27;-4 =&gt; 4&#x27;, &#x27;1 =&gt; 2&#x27;, &#x27;- =&gt; -3&#x27;\] | `C` — \[&#x27;-4 =&gt; 4&#x27;, &#x27;1 =&gt; 2&#x27;, &#x27;3- =&gt; -&#x27;\] | Different answer |
| CalDec v1 | `A` — \[&#x27;-4 =&gt; 4&#x27;, &#x27;1 =&gt; 2&#x27;, &#x27;- =&gt; -3&#x27;\] | `A` — \[&#x27;-4 =&gt; 4&#x27;, &#x27;1 =&gt; 2&#x27;, &#x27;- =&gt; -3&#x27;\] | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cruxeval/c506a16c048b3e775d6a/paraphrasing/structural`

**Input fingerprint:** `83d2b56cc5fe9428a98fdb577d6c501fe4dfba501f77756ffb5bcdd882ae04b8`

| Change | Recorded version |
| --- | --- |
| Paraphrasing | Change the sentence structure |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/rule-application/cruxeval-c506a16c048b3e775d6a.md).
