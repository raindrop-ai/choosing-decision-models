# Analogy · question 59

[Back to Analogy](README.md) · [All capabilities](../README.md)

**Question ID:** `analogical_similarity/f14a8f4304b654d3288b`  
**Source:** [BIG-bench Analogical Similarity](https://github.com/google/BIG-bench)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/analogy/analogical-similarity-f14a8f4304b654d3288b/README.md)

## Context

<details>
<summary>Read the full context</summary>

> The essence of the task: for two given sentence episodes, choose a category that best describes the level of analogical similarity between them.
>   The parent guided the child, compelling the child to follow the parent. &lt;-&gt; The teacher guided the student, compelling the student to follow the teacher. This is an example of literal similarity because the two episodes share all aspects of similarity.
>   The parent guided the child, compelling the child to follow the parent. &lt;-&gt; The student followed the teacher, compelling the teacher to guide the student. This is an example of surface similarity because the two episodes share all aspects of similarity except higher-order structure.
>   The parent guided the child, compelling the child to follow the parent. &lt;-&gt; The student ignored the teacher, compelling the teacher to reprimand the student. This is an example of only objects similarity because the two episodes only share object attribute similarity and higher-order relation similarity.
>   The parent guided the child, compelling the child to follow the parent. &lt;-&gt; The Bible guided the worshippers, compelling the worshippers to follow the Bible. This is an example of an analogy because the two episodes share all aspects of similarity except role-filler binding similarity and object attribute similarity.
>   The parent guided the child, compelling the child to follow the parent. &lt;-&gt; The minor guided the chaperone, compelling the chaperone to follow the minor. This is an example of a cross mapping because the two episodes share all aspects of similarity except role-filler binding similarity.
>   The parent guided the child, compelling the child to follow the parent. &lt;-&gt; The Bible followed the worshippers, compelling the worshippers to guide the Bible. This is an example of a false analogy because the two episodes only share first-order relation similarity, higher-order relation similarity, and object-level isomorphism.
>   The parent guided the child, compelling the child to follow the parent. &lt;-&gt; The cat swiped at the dog, and the dog barked at the cat. This is an example of no similarity because the two episodes share no aspects of similarity.
>   The lion intimidated the zebra, causing the zebra to fear the lion. &lt;-&gt; The coyote intimidated the deer, causing the deer to fear the coyote. This is an example of literal similarity because the two episodes share all aspects of similarity.
>   The lion intimidated the zebra, causing the zebra to fear the lion. &lt;-&gt; The coyote intimidated the deer, and the deer feared the coyote. This is an example of surface similarity because the two episodes share all aspects of similarity except higher-order relation similarity and higher-order structure similarity.
>   The lion intimidated the zebra, causing the zebra to fear the lion. &lt;-&gt; The coyote pounced on the deer, but the deer escaped from the coyote. This is an example of only objects similarity because the two episodes share object attribute similarity.
>   The lion intimidated the zebra, causing the zebra to fear the lion. &lt;-&gt; The mob intimidated the witness, causing the witness to fear the mob. This is an example of an analogy because the two episodes share all aspects of similarity except role-filler binding similarity and object attribute similarity.
>   The lion intimidated the zebra, causing the zebra to fear the lion. &lt;-&gt; The mob feared the witness, causing the mob to intimidate the witness. This is an example of a false analogy because the two episodes only share first-order relation similarity, higher-order relation similarity, and higher-order structure similarity.
>   The lion intimidated the zebra, causing the zebra to fear the lion. &lt;-&gt; The manager relied on the employee, and the employee assisted the manager. This is an example of no similarity because the two episodes share no aspects of similarity.

</details>

## Question

> The mouse sat on the beagle, causing the beagle to shake off the mouse. &lt;-&gt; The golden retriever sniffed the hamster, causing the hamster to squeak at the golden retriever. This is an example of 

## Answer choices

- **A:** literal similarity.
- **B:** an analogy.
- **C:** a cross mapping.
- **D:** surface similarity.
- **E:** a false analogy.
- **F:** only objects similarity.
- **G:** no similarity.

**Reference answer:** only objects similarity. (`F`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The essence of the task: for two given sentence episodes, choose a category that best describes the level of analogical similarity between them.\n  The parent guided the child, compelling the child to follow the parent. <-> The teacher guided the student, compelling the student to follow the teacher. This is an example of literal similarity because the two episodes share all aspects of similarity.\n  The parent guided the child, compelling the child to follow the parent. <-> The student followed the teacher, compelling the teacher to guide the student. This is an example of surface similarity because the two episodes share all aspects of similarity except higher-order structure.\n  The parent guided the child, compelling the child to follow the parent. <-> The student ignored the teacher, compelling the teacher to reprimand the student. This is an example of only objects similarity because the two episodes only share object attribute similarity and higher-order relation similarity.\n  The parent guided the child, compelling the child to follow the parent. <-> The Bible guided the worshippers, compelling the worshippers to follow the Bible. This is an example of an analogy because the two episodes share all aspects of similarity except role-filler binding similarity and object attribute similarity.\n  The parent guided the child, compelling the child to follow the parent. <-> The minor guided the chaperone, compelling the chaperone to follow the minor. This is an example of a cross mapping because the two episodes share all aspects of similarity except role-filler binding similarity.\n  The parent guided the child, compelling the child to follow the parent. <-> The Bible followed the worshippers, compelling the worshippers to guide the Bible. This is an example of a false analogy because the two episodes only share first-order relation similarity, higher-order relation similarity, and object-level isomorphism.\n  The parent guided the child, compelling the child to follow the parent. <-> The cat swiped at the dog, and the dog barked at the cat. This is an example of no similarity because the two episodes share no aspects of similarity.\n  The lion intimidated the zebra, causing the zebra to fear the lion. <-> The coyote intimidated the deer, causing the deer to fear the coyote. This is an example of literal similarity because the two episodes share all aspects of similarity.\n  The lion intimidated the zebra, causing the zebra to fear the lion. <-> The coyote intimidated the deer, and the deer feared the coyote. This is an example of surface similarity because the two episodes share all aspects of similarity except higher-order relation similarity and higher-order structure similarity.\n  The lion intimidated the zebra, causing the zebra to fear the lion. <-> The coyote pounced on the deer, but the deer escaped from the coyote. This is an example of only objects similarity because the two episodes share object attribute similarity.\n  The lion intimidated the zebra, causing the zebra to fear the lion. <-> The mob intimidated the witness, causing the witness to fear the mob. This is an example of an analogy because the two episodes share all aspects of similarity except role-filler binding similarity and object attribute similarity.\n  The lion intimidated the zebra, causing the zebra to fear the lion. <-> The mob feared the witness, causing the mob to intimidate the witness. This is an example of a false analogy because the two episodes only share first-order relation similarity, higher-order relation similarity, and higher-order structure similarity.\n  The lion intimidated the zebra, causing the zebra to fear the lion. <-> The manager relied on the employee, and the employee assisted the manager. This is an example of no similarity because the two episodes share no aspects of similarity.\n",
  "question": "The mouse sat on the beagle, causing the beagle to shake off the mouse. <-> The golden retriever sniffed the hamster, causing the hamster to squeak at the golden retriever. This is an example of ",
  "choices": {
    "A": "literal similarity.",
    "B": "an analogy.",
    "C": "a cross mapping.",
    "D": "surface similarity.",
    "E": "a false analogy.",
    "F": "only objects similarity.",
    "G": "no similarity."
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | only objects similarity. | Correct |
| Opus 5.5 | only objects similarity. | Correct |
| GLiDE v1.2 | only objects similarity. | Correct |
| Decider v1.1 | only objects similarity. | Correct |
| Jev | only objects similarity. | Correct |
| Microsoft Decision-1 | an analogy. | Incorrect |
| Clef | only objects similarity. | Correct |
| Luna Decisions | only objects similarity. | Correct |
| Clef Flash | no similarity. | Incorrect |
| Strands Decider | no similarity. | Incorrect |
| GLiNER2.5 Decide | a false analogy. | Incorrect |
| Laya | literal similarity. | Incorrect |
| CalDec v1 | surface similarity. | Incorrect |

## Source and sharing

Attribution: BIG-bench analogical\_similarity contributors.  
Terms: **[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "bigbench/benchmark_tasks/analogical_similarity/task.json",
    "record": "49",
    "kind": "source_file_record"
  },
  "source_revision": "092b196c1f8f14a54bbc62f24759d43bde46dd3b",
  "input_hash": "b1266cfb7c53c55f6415135a16f799397be4bfb98aae7714b8a50eb97f5cc9ea"
}
```

</details>
