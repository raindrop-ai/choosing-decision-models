# Retrieval · question 55

[Back to Retrieval](README.md) · [All capabilities](../README.md)

**Question ID:** `contractnli/a1b14e24b1b8882089be`  
**Source:** [ContractNLI](https://github.com/stanfordnlp/contract-nli)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/retrieval/contractnli-a1b14e24b1b8882089be/README.md)

## Context

<details>
<summary>Read the full context</summary>

> NON DISCLOSURE AGREEMENT
> (Generic NDA provided by Pitch Deck Fire)
> THIS AGREEMENT is made and entered into as on \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ (“Effective Date”), by and between \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_, (“the Disclosing Party”) and \_\_\_Pitch Deck Fire\_\_\_, (“the Recipient”) (collectively, “the Parties”).
> Purpose for Disclosure (“Business Purpose”): Relevant information will be disclosed by the
> Disclosing Party to the Recipient for the purposes of providing a quote for services and for providing services, generally the completion of a pitch deck or similar materials by the Recipient for Disclosing Party’s use at their discretion. Products of services also fall under this non-disclosure agreement, with the sole exception that the Recipient can use products of services as portfolio examples on the Pitchdeckfire.com website or otherwise, provided that the images are in a non-editable format, and scrubbed clean of branding and specific content (blurred out all logos, company and industry specific content), unless contrary written permission is given by the disclosing party.
> The Parties hereby agree as follows:
> 1. For purposes of this Agreement, "Confidential Information" shall mean any and all non-public information, including, without limitation, technical, developmental, marketing, sales, operating, performance, cost, know-how, business plans, business methods, and process information, disclosed to the Recipient. For convenience, the Disclosing Party may, but is not required to, mark written Confidential Information with the legend "Confidential" or an equivalent designation.
> 2. All Confidential Information disclosed to the Recipient will be used solely for the Business Purpose and for no other purpose whatsoever. The Recipient agrees to keep the Disclosing Party’s Confidential Information confidential and to protect the confidentiality of such Confidential Information with the same degree of care with which it protects the confidentiality of its own confidential information, but in no event with less than a reasonable degree of care. Recipient may disclose Confidential Information only to its employees, agents, consultants and contractors on a need-to-know basis, and only if such employees, agents, consultants and contractors have executed appropriate written agreements with Recipient sufficient to enable Recipient to enforce all the provisions of this Agreement. Recipient shall not make any copies of Disclosing Party’s Confidential Information except as needed for the Business Purpose. At the request of Disclosing Party, Recipient shall return to Disclosing Party all Confidential Information of Disclosing Party (including any copies thereof) or certify the destruction thereof.
> 3. All right title and interest in and to the Confidential Information shall remain with Disclosing Party or its licensors. Nothing in this Agreement is intended to grant any rights to Recipient under any patents, copyrights, trademarks, or trade secrets of Disclosing Party. ALL CONFIDENTIAL INFORMATION IS PROVIDED "AS IS". THE DISCLOSING PARTY MAKES NO WARRANTIES, EXPRESS, IMPLIED OR OTHERWISE, REGARDING NON-INFRINGEMENT OF THIRD PARTY RIGHTS OR ITS ACCURACY, COMPLETENESS OR PERFORMANCE.
> 4. The obligations and limitations set forth herein regarding Confidential Information shall not apply to information which is: (a) at any time in the public domain, other than by a breach on the part of the Recipient; or (b) at any time rightfully received from a third party which had the right to and transmits it to the Recipient without any obligation of confidentiality.
> 5. In the event that the Recipient shall breach this Agreement, or in the event that a breach appears to be imminent, the Disclosing Party shall be entitled to all legal and equitable remedies afforded it by law, and in addition may recover all reasonable costs and attorneys' fees incurred in seeking such remedies. If the Confidential Information is sought by any third party, including by way of subpoena or other court process, the Recipient shall inform the Disclosing Party of the request in sufficient time to permit the Disclosing Party to object to and, if necessary, seek court intervention to prevent the disclosure.
> 6. The validity, construction and enforceability of this Agreement shall be governed in all respects by the law of the state of Colorado. This Agreement may not be amended except in writing signed by a duly authorized representative of the respective Parties. This Agreement shall control in the event of a conflict with any other agreement between the Parties with respect to the subject matter hereof.
> IN WITNESS WHEREOF, the Parties have executed this Agreement as of the date first above written.
> Disclosing Party: The Recipient:
> Company: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Company: \_\_\_\_\_Pitch Deck Fire\_\_\_\_\_\_
> Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Name: \_\_\_\_\_\_\_Stacie Shaw\_\_\_\_\_\_\_\_\_\_
> Role: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Role: \_\_\_\_\_\_\_\_\_Founder\_\_\_\_\_\_\_\_\_\_\_
> Phone Number: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Phone Number: \_\_\_214-770-9216\_\_\_\_
> Signature: Signature:
> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

</details>

## Question

> Classify the following statement using only the supplied contract: All Confidential Information shall be expressly identified by the Disclosing Party.

## Answer choices

- **Entailment:** The contract supports the statement.
- **NotMentioned:** The contract does not establish whether it is true.
- **Contradiction:** The contract contradicts the statement.

**Reference answer:** The contract contradicts the statement. (`Contradiction`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "NON DISCLOSURE AGREEMENT\n(Generic NDA provided by Pitch Deck Fire)\nTHIS AGREEMENT is made and entered into as on _________________ (“Effective Date”), by and between ____________________, (“the Disclosing Party”) and ___Pitch Deck Fire___, (“the Recipient”) (collectively, “the Parties”).\nPurpose for Disclosure (“Business Purpose”): Relevant information will be disclosed by the\nDisclosing Party to the Recipient for the purposes of providing a quote for services and for providing services, generally the completion of a pitch deck or similar materials by the Recipient for Disclosing Party’s use at their discretion. Products of services also fall under this non-disclosure agreement, with the sole exception that the Recipient can use products of services as portfolio examples on the Pitchdeckfire.com website or otherwise, provided that the images are in a non-editable format, and scrubbed clean of branding and specific content (blurred out all logos, company and industry specific content), unless contrary written permission is given by the disclosing party.\nThe Parties hereby agree as follows:\n1. For purposes of this Agreement, \"Confidential Information\" shall mean any and all non-public information, including, without limitation, technical, developmental, marketing, sales, operating, performance, cost, know-how, business plans, business methods, and process information, disclosed to the Recipient. For convenience, the Disclosing Party may, but is not required to, mark written Confidential Information with the legend \"Confidential\" or an equivalent designation.\n2. All Confidential Information disclosed to the Recipient will be used solely for the Business Purpose and for no other purpose whatsoever. The Recipient agrees to keep the Disclosing Party’s Confidential Information confidential and to protect the confidentiality of such Confidential Information with the same degree of care with which it protects the confidentiality of its own confidential information, but in no event with less than a reasonable degree of care. Recipient may disclose Confidential Information only to its employees, agents, consultants and contractors on a need-to-know basis, and only if such employees, agents, consultants and contractors have executed appropriate written agreements with Recipient sufficient to enable Recipient to enforce all the provisions of this Agreement. Recipient shall not make any copies of Disclosing Party’s Confidential Information except as needed for the Business Purpose. At the request of Disclosing Party, Recipient shall return to Disclosing Party all Confidential Information of Disclosing Party (including any copies thereof) or certify the destruction thereof.\n3. All right title and interest in and to the Confidential Information shall remain with Disclosing Party or its licensors. Nothing in this Agreement is intended to grant any rights to Recipient under any patents, copyrights, trademarks, or trade secrets of Disclosing Party. ALL CONFIDENTIAL INFORMATION IS PROVIDED \"AS IS\". THE DISCLOSING PARTY MAKES NO WARRANTIES, EXPRESS, IMPLIED OR OTHERWISE, REGARDING NON-INFRINGEMENT OF THIRD PARTY RIGHTS OR ITS ACCURACY, COMPLETENESS OR PERFORMANCE.\n4. The obligations and limitations set forth herein regarding Confidential Information shall not apply to information which is: (a) at any time in the public domain, other than by a breach on the part of the Recipient; or (b) at any time rightfully received from a third party which had the right to and transmits it to the Recipient without any obligation of confidentiality.\n5. In the event that the Recipient shall breach this Agreement, or in the event that a breach appears to be imminent, the Disclosing Party shall be entitled to all legal and equitable remedies afforded it by law, and in addition may recover all reasonable costs and attorneys' fees incurred in seeking such remedies. If the Confidential Information is sought by any third party, including by way of subpoena or other court process, the Recipient shall inform the Disclosing Party of the request in sufficient time to permit the Disclosing Party to object to and, if necessary, seek court intervention to prevent the disclosure.\n6. The validity, construction and enforceability of this Agreement shall be governed in all respects by the law of the state of Colorado. This Agreement may not be amended except in writing signed by a duly authorized representative of the respective Parties. This Agreement shall control in the event of a conflict with any other agreement between the Parties with respect to the subject matter hereof.\nIN WITNESS WHEREOF, the Parties have executed this Agreement as of the date first above written.\nDisclosing Party: The Recipient:\nCompany: _______________________ Company: _____Pitch Deck Fire______\nName: __________________________ Name: _______Stacie Shaw__________\nRole: ___________________________ Role: _________Founder___________\nPhone Number: __________________ Phone Number: ___214-770-9216____\nSignature: Signature:\n_______________________________ _______________________________\n",
  "question": "Classify the following statement using only the supplied contract: All Confidential Information shall be expressly identified by the Disclosing Party.",
  "choices": {
    "Entailment": "The contract supports the statement.",
    "NotMentioned": "The contract does not establish whether it is true.",
    "Contradiction": "The contract contradicts the statement."
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | The contract contradicts the statement. | Correct |
| Opus 5.5 | The contract contradicts the statement. | Correct |
| GLiDE v1.2 | The contract contradicts the statement. | Correct |
| Decider v1.1 | The contract contradicts the statement. | Correct |
| Jev | The contract contradicts the statement. | Correct |
| Microsoft Decision-1 | The contract contradicts the statement. | Correct |
| Clef | The contract contradicts the statement. | Correct |
| Luna Decisions | The contract contradicts the statement. | Correct |
| Clef Flash | The contract contradicts the statement. | Correct |
| Strands Decider | The contract contradicts the statement. | Correct |
| GLiNER2.5 Decide | The contract supports the statement. | Incorrect |
| Laya | The contract supports the statement. | Incorrect |
| CalDec v1 | The contract supports the statement. | Incorrect |

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
    "record": "1909",
    "kind": "prepared_normalizer_record",
    "native_id": "contractnli/test.json/117/nda-1/baseline"
  },
  "source_revision": "eced6528dd3c1d14d73f9a87df8f7bdbc03126f9",
  "input_hash": "7e6409370d0d23674386b38171bc04f55f193930665ffca7d6c664bb61ab32d1"
}
```

</details>
