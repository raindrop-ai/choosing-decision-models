# Retrieval · question 19

[Back to Retrieval](README.md) · [All capabilities](../README.md)

**Question ID:** `contractnli/093e9f5ebd61d4b163c8`  
**Source:** [ContractNLI](https://github.com/stanfordnlp/contract-nli)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/retrieval/contractnli-093e9f5ebd61d4b163c8/README.md)

## Context

<details>
<summary>Read the full context</summary>

> Annex III – Non Disclosure Agreement
> This agreement is made between PricewaterhouseCoopers LLP, a limited liability partnership incorporated in England (number OC303525) whose registered office is at 1 Embankment Place, London WC2N 6RH ("PwC"); and whose registered office is at (“you”).
> Background
> In connection with our discussions relating to ‘\[Insert project name\]’ (the “purpose”) certain confidential information may be disclosed between us.
> 1 Definitions
> In this agreement the following words have the meanings given to them below:
> “confidential information” means any information disclosed by one party to the other party in connection with the purpose, which is of a confidential nature irrespective of whether it is marked as such.
> “disclosing party” means the party to this agreement disclosing the confidential information. “PwC firm” means any entity or partnership within the worldwide network of PricewaterhouseCoopers firms and entities.
> “receiving party” means the party to this agreement to whom the confidential information is disclosed.
> 2 Confidentiality
> 2.1 The receiving party agrees:
> (a) to keep the disclosing party’s confidential information, confidential;
> (b) not to use the disclosing party’s confidential information except in connection with the purpose; and
> (c) not to disclose the disclosing party’s confidential information to anyone else.
> 2.2 Each party agrees that it will keep the purpose and the existence of this agreement confidential.
> 2.3 This agreement will not apply to information which:
> (a) is publicly available; or
> (b) has been received from someone else who owes no duty of confidence in relation to it; or
> (c) was already known by the receiving party.
> 2.4 Nothing in this agreement will prevent the receiving party from disclosing confidential information:
> (a) if the disclosing party has given its prior written consent; or
> (b) to its lawyers; or
> (c) if the disclosure is required by law, regulation or professional requirements; or
> (d) in the case of PwC, to other PwC firms or relevant subcontractors.
> 2.5 The receiving party will ensure that anyone who receives confidential information under clause 2.4 (b) is bound by confidentiality obligations before the confidential information is disclosed.
> 2.6 Nothing in this agreement will restrict your ability to disclose PwC’s advice concerning the tax (including social security) treatment or tax structure of any transaction regardless of any confidentiality markings on any communications.
> 3 Term
> 3.1 This agreement will come into effect on the date of signature by both parties and will continue indefinitely, subject to any subsequent agreement entered into between the parties in relation to the purpose which includes obligations relating to the protection of confidential information. The subsequent agreement will then replace this agreement with effect from the commencement of our services.
> 3.2 Following a written request from the disclosing party, the receiving party will, as soon as practicable, either destroy or return all confidential information to the disclosing party or, in the case of electronic copies of confidential information, delete them or make them reasonably inaccessible. However, PwC may retain a copy of the confidential information for our internal purposes.
> 4 General
> This agreement forms the entire agreement between the parties relating to confidential information disclosed in connection with the purpose. It replaces any earlier agreements, representations or discussions. Neither party excludes liability for any fraud.
> 5 Governing law and jurisdiction
> This agreement and any dispute arising from it, whether contractual or non-contractual, will be governed by English law and be subject to the exclusive jurisdiction of the English courts.
> SIGNED for and on behalf of PricewaterhouseCoopers LLP
> By ………………………………………………………..
> Position………………………………………………………
> Date ………………………………………………………
> SIGNED for and on behalf of \[ \]
> By …………………………………………………………
> Position……………………..…………………………….

</details>

## Question

> Classify the following statement using only the supplied contract: Agreement shall not grant Receiving Party any right to Confidential Information.

## Answer choices

- **Entailment:** The contract supports the statement.
- **NotMentioned:** The contract does not establish whether it is true.
- **Contradiction:** The contract contradicts the statement.

**Reference answer:** The contract does not establish whether it is true. (`NotMentioned`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Annex III – Non Disclosure Agreement\nThis agreement is made between PricewaterhouseCoopers LLP, a limited liability partnership incorporated in England (number OC303525) whose registered office is at 1 Embankment Place, London WC2N 6RH (\"PwC\"); and whose registered office is at (“you”).\nBackground\nIn connection with our discussions relating to ‘[Insert project name]’ (the “purpose”) certain confidential information may be disclosed between us.\n1 Definitions\nIn this agreement the following words have the meanings given to them below:\n“confidential information” means any information disclosed by one party to the other party in connection with the purpose, which is of a confidential nature irrespective of whether it is marked as such.\n“disclosing party” means the party to this agreement disclosing the confidential information. “PwC firm” means any entity or partnership within the worldwide network of PricewaterhouseCoopers firms and entities.\n“receiving party” means the party to this agreement to whom the confidential information is disclosed.\n2 Confidentiality\n2.1 The receiving party agrees:\n(a) to keep the disclosing party’s confidential information, confidential;\n(b) not to use the disclosing party’s confidential information except in connection with the purpose; and\n(c) not to disclose the disclosing party’s confidential information to anyone else.\n2.2 Each party agrees that it will keep the purpose and the existence of this agreement confidential.\n2.3 This agreement will not apply to information which:\n(a) is publicly available; or\n(b) has been received from someone else who owes no duty of confidence in relation to it; or\n(c) was already known by the receiving party.\n2.4 Nothing in this agreement will prevent the receiving party from disclosing confidential information:\n(a) if the disclosing party has given its prior written consent; or\n(b) to its lawyers; or\n(c) if the disclosure is required by law, regulation or professional requirements; or\n(d) in the case of PwC, to other PwC firms or relevant subcontractors.\n2.5 The receiving party will ensure that anyone who receives confidential information under clause 2.4 (b) is bound by confidentiality obligations before the confidential information is disclosed.\n2.6 Nothing in this agreement will restrict your ability to disclose PwC’s advice concerning the tax (including social security) treatment or tax structure of any transaction regardless of any confidentiality markings on any communications.\n3 Term\n3.1 This agreement will come into effect on the date of signature by both parties and will continue indefinitely, subject to any subsequent agreement entered into between the parties in relation to the purpose which includes obligations relating to the protection of confidential information. The subsequent agreement will then replace this agreement with effect from the commencement of our services.\n3.2 Following a written request from the disclosing party, the receiving party will, as soon as practicable, either destroy or return all confidential information to the disclosing party or, in the case of electronic copies of confidential information, delete them or make them reasonably inaccessible. However, PwC may retain a copy of the confidential information for our internal purposes.\n4 General\nThis agreement forms the entire agreement between the parties relating to confidential information disclosed in connection with the purpose. It replaces any earlier agreements, representations or discussions. Neither party excludes liability for any fraud.\n5 Governing law and jurisdiction\nThis agreement and any dispute arising from it, whether contractual or non-contractual, will be governed by English law and be subject to the exclusive jurisdiction of the English courts.\nSIGNED for and on behalf of PricewaterhouseCoopers LLP\nBy ………………………………………………………..\nPosition………………………………………………………\nDate ………………………………………………………\nSIGNED for and on behalf of [ ]\nBy …………………………………………………………\nPosition……………………..…………………………….\n",
  "question": "Classify the following statement using only the supplied contract: Agreement shall not grant Receiving Party any right to Confidential Information.",
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
| Astra | The contract does not establish whether it is true. | Correct |
| Opus 5.5 | The contract does not establish whether it is true. | Correct |
| GLiDE v1.2 | The contract does not establish whether it is true. | Correct |
| Decider v1.1 | The contract does not establish whether it is true. | Correct |
| Jev | The contract contradicts the statement. | Incorrect |
| Microsoft Decision-1 | The contract does not establish whether it is true. | Correct |
| Clef | The contract does not establish whether it is true. | Correct |
| Luna Decisions | The contract supports the statement. | Incorrect |
| Clef Flash | The contract does not establish whether it is true. | Correct |
| Strands Decider | The contract does not establish whether it is true. | Correct |
| GLiNER2.5 Decide | The contract supports the statement. | Incorrect |
| Laya | The contract does not establish whether it is true. | Correct |
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
    "record": "1566",
    "kind": "prepared_normalizer_record",
    "native_id": "contractnli/test.json/57/nda-15/baseline"
  },
  "source_revision": "eced6528dd3c1d14d73f9a87df8f7bdbc03126f9",
  "input_hash": "3f97ba27061aaf3a6192b852171cdfc55fd21142cc733c7b2c4cb234db522e3e"
}
```

</details>
