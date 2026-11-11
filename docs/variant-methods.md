# How the question variants were made

[Browse variants](../variants/README.md) · [Results](variant-results.md) · [Verify or rerun](variant-reproduction.md)

The context-sensitivity study uses **24,563 distinct altered inputs derived from the same 1,005 original questions**, across 12 kinds of change. Each original has multiple versions; the number varies because not every edit applies to every question. Eleven decision models were tested. Astra and Opus are baseline comparators only.

The variants change the context, question wording or instructions, or answer-choice order while retaining the recorded reference answer. The exact evaluated text is saved: reproducing a variant does not require asking another language model to rewrite it.

## The changes

| Change | What the versions vary |
| --- | --- |
| Text length | Added text targeting 512, 2,048 or 8,192 tokens, with additional source-specific length versions. These are input targets, rather than a guarantee of the same token count under every model's tokenizer. |
| Extra events | Two, six or twelve unrelated events alongside the original information. |
| Evidence position | The same decisive information near the beginning, middle or end of a surrounding passage. |
| Evidence order | Reversed or shuffled presentation of the same information. Local rearrangements and edits that also change wording have separate records. |
| Repetition | The same evidence presented twice or three times. |
| Invented names | Replacement familiar names compared with invented names. |
| Irrelevant details | Smaller or larger amounts of information unrelated to the answer. |
| Similar distractors | Fewer or more irrelevant items resembling the information needed to answer. |
| Misleading details | An added reader assessment that suggests either the correct answer or an incorrect answer. These are claims about the answer, rather than changes to the underlying evidence. |
| Unrelated examples | Worked examples unrelated to the target judgment, with separately constructed versions without the examples or with prose in their place. |
| Paraphrasing | Changes to words and phrases, or to sentence structure. |
| Option order | Reversing the choices or moving the first choice to the end. |

Edits are adapted to the original source format. An added passage can appear in the context or in the question instructions. Some versions use shared construction recipes across a source family; others have question-specific edits. The [individual pages](../variants/README.md) show the changed fields, complete text where shareable, recorded condition names and input fingerprint.

A reference answer is the answer key used for scoring, not a model's prediction. Retaining the key records the intended answer-preserving design. It does not establish that every authored rewrite is semantically equivalent; inspect an individual input before drawing conclusions from an unexpected answer.

## Which versions are compared?

An edit's stored label alone is not enough to establish a controlled comparison. For example, a version labelled “reversed” may reverse the complete evidence, move a single phrase, or combine rearrangement with a wording change. The reported ordering comparison uses only the exact questions identified as complete-information permutations.

The explicit lists in [`comparisons.json`](../data/variants/comparisons.json) identify the versions of each original used together. Each family records its original question, the input ID at each level and construction information. These lists were established from the inputs and construction records, rather than from which models answered correctly.

| Comparison | Original questions with all required inputs fitting every model |
| --- | ---: |
| 512- vs 2,048-token targets | 733 |
| 2, 6 and 12 extra events | 1,005 |
| Beginning, middle and end | 944 |
| Original, reversed and shuffled evidence | 335 |
| Evidence repeated twice vs three times | 989 |
| Familiar vs invented names | 103 |
| Low vs high irrelevant detail | 1,004 |
| Low vs high similar distractors | 988 |
| Accurate vs misleading reader assessment | 1,004 |
| Worked examples vs their authored no-example version | 592 |
| Worked examples vs a prose control | 241 |
| Worked examples vs a natural-prose control | 71 |
| Word substitutions vs sentence restructuring | 989 |
| Original, rotated and reversed answer choices | 673 |

Unrelated examples are compared with versions that omit the examples or replace them with ordinary prose. These are separate comparisons, and the versions used for comparison can differ from the unedited original. Additional variants outside the comparisons above remain available on the [individual pages](../variants/README.md).

## Linking each variant to its original answer

Some original responses were reused from earlier runs with matching inputs and model settings. Unchanged questions were not rerun for every model, so individual answer changes may also reflect variation between runs.

Every variant outcome has an `original_result_id` pointing to the exact response in [`original-controls.jsonl`](../results/variants/original-controls.jsonl). The individual variant pages display that response next to the variant answer. Proven identical native model inputs can also share a result; `input_alias`, `source_case_id` and `source_input_hash` preserve that relationship.

## Scoring and coverage

Each comparison shows accuracy and answer changes, including mistakes introduced or corrected. Overall accuracy can stay the same even when individual answers change. Scores use questions with valid responses to every version required for the comparison; counts are shown for each model. Multiple versions of one question are not independent questions.

Clef and Clef Flash sort answer choices before answering. Their option-order results reflect this preprocessing.

## Sharing the text

Full evaluated text is included for **20,961 variants**. The other **3,602** derive from originals whose terms do not clearly support republishing their text here, or impose additional requirements. Download those originals under their source terms and [recover the selected variants locally](variant-reproduction.md#recover-the-remaining-variant-texts). Saved edit recipes combine authored additions with references into your original files, and verify the reconstructed input fingerprint. All IDs, reference keys, model outcomes and comparison lists are included regardless of text availability.
