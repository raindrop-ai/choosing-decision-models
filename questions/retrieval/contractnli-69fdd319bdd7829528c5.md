# Retrieval · question 49

[Back to Retrieval](README.md) · [All capabilities](../README.md)

**Question ID:** `contractnli/69fdd319bdd7829528c5`  
**Source:** [ContractNLI](https://github.com/stanfordnlp/contract-nli)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/retrieval/contractnli-69fdd319bdd7829528c5/README.md)

## Context

<details>
<summary>Read the full context</summary>

> Exhibit (d)(10)
> NON-DISCLOSURE AGREEMENT
> THIS NON-DISCLOSURE AGREEMENT (“Agreement”) between Universal Hospital Services, Inc. (“UHS”) and Emergent Group, Inc. (“Company”), is effective October 26, 2010.
> Whereas, UHS and Company intend to engage in confidential discussions for the purpose of evaluating a potential business transaction between UHS and Company (“Business Transaction”), and as part of the Business Transaction, each party anticipates that it will disclose to the other party certain information that its deems confidential and/or proprietary.
> Now, therefore, to assure the confidentiality of the parties’ confidential information and to prevent the unauthorized use or disclosure of this information, UHS and Company agree as follows:
> 1. Confidential Information Defined. The term “Confidential Information” means all confidential and proprietary information belonging to one party (the “Disclosing Party”) that is revealed to the other party (the “Receiving Party”) during the Disclosure Period, which begins on the effective date and ends April 26, 2011. Confidential Information, regardless of the form in which it appears, may include, without limitation, information about customers, business and marketing plans, financial data, expertise of employees, forecasts and strategies that is related to the business of the Disclosing Party and is of the type of information that would reasonably be deemed to be confidential.
> 2. Use Restriction. The Receiving Party agrees to use the Confidential Information for the sole purpose of evaluating and negotiating the Business Transaction.
> 3. Disclosure Restrictions and Exceptions. The Receiving Party will disclose Confidential Information only to its employees and to its representative whose participation is necessary or helpful to evaluate and advance to the Business Transaction and who have agreed to be bound by the terms of this Agreement. The Receiving Party will limit the unauthorized disclosure of Confidential Information by using the same degree of care, but no less than a reasonable degree of care, as the Receiving Party uses to protect its own confidential information. Notwithstanding anything to the contrary in this Agreement, the Receiving Party is not prohibited from disclosing Confidential Information it is legally compelled to disclose (by deposition, subpoena, civil investigative demand, court order or otherwise), provided that the Receiving Party gives the Disclosing Party prompt written notice of any such required disclosure so that the Disclosing Party may seek a protective order or other appropriate remedy. If such protective order or other remedy is not obtained and the Disclosing Party has not waived compliance with the provisions of this Agreement, the Receiving Party will furnish only that portion of the Confidential Information which the Receiving Party is advised by opinion of counsel it is legally required to furnish and will exercise reasonable efforts to limit the scope and content of such disclosure and obtain confidential treatment of such Confidential Information, Furthermore, the Receiving Party’s obligations under this Agreement do not apply with respect to any Confidential Information that (a) is or becomes generally available to the public other than from the improper action of the Receiving Party, (b) is developed by the Receiving Party without reference to the Confidential Information, (c) was in the Receiving Party’s possession before receipt from the Disclosing Party, or (d) is received by the Receiving Party from a third party who is not subject to an obligation of confidentiality owed to the Disclosing Party.
> 4. Nondisclosure of Possible Business Transaction. Except as permitted by the previous paragraph, neither the Receiving Party nor the Receiving Party’s representatives will disclose to any person the fact that the Confidential information has been made available to the Receiving Party or the Receiving Party’s representatives or that the Receiving Party or the Receiving Party’s representatives have inspected any portion of the Confidential Information.
> 5. Waiver. The failure of a party to insist, in one or more instances, upon performance of any of the provisions or conditions of this Agreement will not be construed as a waiver of any other provision or condition of this Agreement, and no present waiver will be construed as a future waiver of such provision or condition.
> 6. Remedies. Because of the unique and proprietary nature of Confidential Information, it is understood and agreed that remedies at law for a breach by the Receiving Party of its obligations under this Agreement may be inadequate and that in the event of such breach or threatened breach the Disclosing Party will be entitled to seek equitable relief, including without limitation injunctive relief and specific performance. The remedies set forth in this Section are in addition to any other remedies available for any such breach or threatened breach, including the recovery of damages from the breaching party.
> 7. Assignment. This Agreement is not assignable by either party without the prior express written consent of the other, except that UHS may assign this Agreement to an affiliate or to a successor in interest to which the business relates.
> 8. Entire Agreement and Amendment. This Agreement states the entire understanding of the parties regarding the Disclosing Party’s Confidential Information and it cannot be altered or amended without a writing signed by both parties. This Agreement will not be construed to create any obligation on the part of either party to retain the other party’s services or to compensate the other party in any manner.
> 9. Return of Confidential Information. Upon the written request of the Disclosing Party, the Receiving Party will promptly return to the Disclosing Party or destroy all documents or other materials furnished by the Disclosing Party constituting Confidential Information, together with all copies thereof in the possession, custody or control of the Receiving Party, without retaining any copies. Any destruction must be confirmed by the Receiving Party to the Disclosing Party in writing. Notwithstanding anything to the contrary set forth herein, the Receiving Party is not required to return or destroy computer files stored in the ordinary course of its business as a result of automated back-up procedures (subject, however, to the confidentiality restrictions set forth herein).
> 10. Term. The Receiving Party’s obligations imposed pursuant to this Agreement will continue for two years from the date hereof. ACCEPTED AND AGREED TO:
> Universal Hospital Services, Inc. Emergent Group, Inc.
> 7700 France Avenue South, Suite 275 10939 Pendleton Street
> Edina, MN 55435-5228 Sun Valley, CA 91352
> By: /s/ Timothy W. Kuck \[ILLEGIBLE\] By: /s/ Bruce J. Haber
> Timothy W. Kuck Bruce J. Haber
> Its: Executive Vice President Its: Chairman &amp; CEO
> Date: 10/26/10 Date: 10/26/10

</details>

## Question

> Classify the following statement using only the supplied contract: Receiving Party shall notify Disclosing Party in case Receiving Party is required by law, regulation or judicial process to disclose any Confidential Information.

## Answer choices

- **NotMentioned:** The contract does not establish whether it is true.
- **Contradiction:** The contract contradicts the statement.
- **Entailment:** The contract supports the statement.

**Reference answer:** The contract supports the statement. (`Entailment`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Exhibit (d)(10)\nNON-DISCLOSURE AGREEMENT\nTHIS NON-DISCLOSURE AGREEMENT (“Agreement”) between Universal Hospital Services, Inc. (“UHS”) and Emergent Group, Inc. (“Company”), is effective October 26, 2010.\nWhereas, UHS and Company intend to engage in confidential discussions for the purpose of evaluating a potential business transaction between UHS and Company (“Business Transaction”), and as part of the Business Transaction, each party anticipates that it will disclose to the other party certain information that its deems confidential and/or proprietary.\nNow, therefore, to assure the confidentiality of the parties’ confidential information and to prevent the unauthorized use or disclosure of this information, UHS and Company agree as follows:\n1. Confidential Information Defined. The term “Confidential Information” means all confidential and proprietary information belonging to one party (the “Disclosing Party”) that is revealed to the other party (the “Receiving Party”) during the Disclosure Period, which begins on the effective date and ends April 26, 2011. Confidential Information, regardless of the form in which it appears, may include, without limitation, information about customers, business and marketing plans, financial data, expertise of employees, forecasts and strategies that is related to the business of the Disclosing Party and is of the type of information that would reasonably be deemed to be confidential.\n2. Use Restriction. The Receiving Party agrees to use the Confidential Information for the sole purpose of evaluating and negotiating the Business Transaction.\n3. Disclosure Restrictions and Exceptions. The Receiving Party will disclose Confidential Information only to its employees and to its representative whose participation is necessary or helpful to evaluate and advance to the Business Transaction and who have agreed to be bound by the terms of this Agreement. The Receiving Party will limit the unauthorized disclosure of Confidential Information by using the same degree of care, but no less than a reasonable degree of care, as the Receiving Party uses to protect its own confidential information. Notwithstanding anything to the contrary in this Agreement, the Receiving Party is not prohibited from disclosing Confidential Information it is legally compelled to disclose (by deposition, subpoena, civil investigative demand, court order or otherwise), provided that the Receiving Party gives the Disclosing Party prompt written notice of any such required disclosure so that the Disclosing Party may seek a protective order or other appropriate remedy. If such protective order or other remedy is not obtained and the Disclosing Party has not waived compliance with the provisions of this Agreement, the Receiving Party will furnish only that portion of the Confidential Information which the Receiving Party is advised by opinion of counsel it is legally required to furnish and will exercise reasonable efforts to limit the scope and content of such disclosure and obtain confidential treatment of such Confidential Information, Furthermore, the Receiving Party’s obligations under this Agreement do not apply with respect to any Confidential Information that (a) is or becomes generally available to the public other than from the improper action of the Receiving Party, (b) is developed by the Receiving Party without reference to the Confidential Information, (c) was in the Receiving Party’s possession before receipt from the Disclosing Party, or (d) is received by the Receiving Party from a third party who is not subject to an obligation of confidentiality owed to the Disclosing Party.\n4. Nondisclosure of Possible Business Transaction. Except as permitted by the previous paragraph, neither the Receiving Party nor the Receiving Party’s representatives will disclose to any person the fact that the Confidential information has been made available to the Receiving Party or the Receiving Party’s representatives or that the Receiving Party or the Receiving Party’s representatives have inspected any portion of the Confidential Information.\n5. Waiver. The failure of a party to insist, in one or more instances, upon performance of any of the provisions or conditions of this Agreement will not be construed as a waiver of any other provision or condition of this Agreement, and no present waiver will be construed as a future waiver of such provision or condition.\n6. Remedies. Because of the unique and proprietary nature of Confidential Information, it is understood and agreed that remedies at law for a breach by the Receiving Party of its obligations under this Agreement may be inadequate and that in the event of such breach or threatened breach the Disclosing Party will be entitled to seek equitable relief, including without limitation injunctive relief and specific performance. The remedies set forth in this Section are in addition to any other remedies available for any such breach or threatened breach, including the recovery of damages from the breaching party.\n7. Assignment. This Agreement is not assignable by either party without the prior express written consent of the other, except that UHS may assign this Agreement to an affiliate or to a successor in interest to which the business relates.\n8. Entire Agreement and Amendment. This Agreement states the entire understanding of the parties regarding the Disclosing Party’s Confidential Information and it cannot be altered or amended without a writing signed by both parties. This Agreement will not be construed to create any obligation on the part of either party to retain the other party’s services or to compensate the other party in any manner.\n9. Return of Confidential Information. Upon the written request of the Disclosing Party, the Receiving Party will promptly return to the Disclosing Party or destroy all documents or other materials furnished by the Disclosing Party constituting Confidential Information, together with all copies thereof in the possession, custody or control of the Receiving Party, without retaining any copies. Any destruction must be confirmed by the Receiving Party to the Disclosing Party in writing. Notwithstanding anything to the contrary set forth herein, the Receiving Party is not required to return or destroy computer files stored in the ordinary course of its business as a result of automated back-up procedures (subject, however, to the confidentiality restrictions set forth herein).\n10. Term. The Receiving Party’s obligations imposed pursuant to this Agreement will continue for two years from the date hereof. ACCEPTED AND AGREED TO:\nUniversal Hospital Services, Inc. Emergent Group, Inc.\n7700 France Avenue South, Suite 275 10939 Pendleton Street\nEdina, MN 55435-5228 Sun Valley, CA 91352\nBy: /s/ Timothy W. Kuck [ILLEGIBLE] By: /s/ Bruce J. Haber\nTimothy W. Kuck Bruce J. Haber\nIts: Executive Vice President Its: Chairman & CEO\nDate: 10/26/10 Date: 10/26/10\n",
  "question": "Classify the following statement using only the supplied contract: Receiving Party shall notify Disclosing Party in case Receiving Party is required by law, regulation or judicial process to disclose any Confidential Information.",
  "choices": {
    "NotMentioned": "The contract does not establish whether it is true.",
    "Contradiction": "The contract contradicts the statement.",
    "Entailment": "The contract supports the statement."
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | The contract supports the statement. | Correct |
| Opus 5.5 | The contract supports the statement. | Correct |
| GLiDE v1.2 | The contract supports the statement. | Correct |
| Decider v1.1 | The contract supports the statement. | Correct |
| Jev | The contract supports the statement. | Correct |
| Microsoft Decision-1 | The contract supports the statement. | Correct |
| Clef | The contract supports the statement. | Correct |
| Luna Decisions | The contract supports the statement. | Correct |
| Clef Flash | The contract supports the statement. | Correct |
| Strands Decider | The contract supports the statement. | Correct |
| GLiNER2.5 Decide | The contract supports the statement. | Correct |
| Laya | The contract supports the statement. | Correct |
| CalDec v1 | The contract supports the statement. | Correct |

## Source and sharing

Attribution: Yuta Koreeda and Christopher D. Manning; Stanford NLP.  
Terms: **[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "data/prepared/contractnli.jsonl",
    "record": "880",
    "kind": "prepared_normalizer_record",
    "native_id": "contractnli/dev.json/547/nda-8/baseline"
  },
  "source_revision": "eced6528dd3c1d14d73f9a87df8f7bdbc03126f9",
  "input_hash": "4a69a33868f83b19726e6e19e5082fc875f6286804e6c4c8eb4d39c8c3ad6f0b"
}
```

</details>
