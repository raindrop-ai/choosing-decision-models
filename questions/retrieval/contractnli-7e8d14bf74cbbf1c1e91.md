# Retrieval · question 52

[Back to Retrieval](README.md) · [All capabilities](../README.md)

**Question ID:** `contractnli/7e8d14bf74cbbf1c1e91`  
**Source:** [ContractNLI](https://github.com/stanfordnlp/contract-nli)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/retrieval/contractnli-7e8d14bf74cbbf1c1e91/README.md)

## Context

<details>
<summary>Read the full context</summary>

> CORPORATE NON-DISCLOSURE AGREEMENT
> This Agreement is entered into and made effective as of the date set forth above by and between Intel Corporation (hereinafter "Intel"), and the participant identified below (hereinafter "Participant"). Unless the Participant indicates that this Agreement shall apply only to a specific division or location, this Agreement shall apply to the Participant's entire company.
> THE PARTIES AGREE AS FOLLOWS:
> CONFIDENTIAL INFORMATION TRANSMITTAL FORM. The confidential, proprietary and trade secret information of the disclosing party (hereinafter "Confidential Information") provided hereunder, is that information described in the Confidential Information Transmittal Record (CITR) form executed from time to time hereafter. CITR's are subject to the terms of this Agreement and shall be executed by the parties prior to the disclosure of Confidential Information. All information described in a CITR and marked with a "confidential," "proprietary," or similar legend shall be deemed Confidential Information. All Confidential Information received from the disclosing party shall be in tangible form. The CITR shall set forth the disclosing party, a description of the Confidential Information disclosed, the names of the representatives of the parties and the date when the disclosure covered by the CITR commenced.
> OBLIGATIONS OF RECEIVING PARTY. The receiving party shall not disclose Confidential Information to any third party without the prior written approval of the disclosing party. The receiving party shall maintain the Confidential Information with at least the same degree of care that the receiving party uses to protect its own similar categories of confidential and proprietary information, but no less than a reasonable degree of care under the circumstances. The receiving party shall not make any copies of Confidential Information received from the disclosing party except as necessary for its employees with a need to know. Any copies which are made shall be identified as belonging to the disclosing party and marked "confidential," "proprietary," or with a similar legend.
> PERIOD OF CONFIDENTIALITY. Unless a shorter period is stated in the applicable CITR, the disclosing party will not assert any claims against the receiving party for disclosures of Confidential Information made more than five (5) years from the date of the CITR.
> TERMINATION OF OBLIGATION OF CONFIDENTIALITY. The receiving party shall not be liable for the disclosure of any Confidential Information which is:
> (a) in the public domain other than by a breach of this Agreement on the part of the receiving party; or
> (b) rightfully received from a third party without any obligation of confidentiality; or
> (c) rightfully known to the receiving party without any limitation on use or disclosure prior to its receipt from the disclosing party; or
> (d) independently developed by employees of the receiving party; or (e) generally made available to third parties by the disclosing party
> without restriction on disclosure.
> TITLE. Title or the right to possess Confidential Information as between the parties shall remain in the disclosing party.
> NO OBLIGATION OF DISCLOSURE. Neither party has any obligation to disclose Confidential Information to the other. Either party may, at any time, cease giving Confidential Information to the other party without any liability or request in writing the return of Confidential Information previously disclosed.
> TERMINATION AND DUTY TO RETURN. Either party may terminate this Agreement at any time without cause upon notice to the other party. However, all obligations of confidentiality shall survive the termination of this Agreement. In the event this Agreement is terminated, and the disclosing party so requests, the receiving party shall promptly return or destroy (and certify destruction of) all Confidential Information which it received from the disclosing party along with all copies which it made. GENERAL.
> (a) This Agreement is neither intended to nor shall it be construed as creating a joint venture, partnership or other form of business association between the parties, nor an obligation to buy or sell products using or incorporating the Confidential Information, nor as creating an implied or express license grant from either party to the other.
> (b) The failure of either party to enforce any right resulting from breach of any provision of this Agreement by the other party shall not be deemed a waiver of any right relating to a subsequent breach of such provision or of any other right hereunder.
> (c) This Agreement shall be governed by the laws of the State of California.
> (d) This Agreement, any accompanying CITR and CITRs executed from time to time hereafter which incorporate the terms of this Agreement constitute the entire agreement, written or verbal, between the parties with respect to the disclosure(s) of Confidential Information described in each CITR. This Agreement may not be amended except in writing signed by a duly authorized representative of the respective parties. Any other agreements between the parties, including non-disclosure agreements, shall not be affected by this Agreement.
> &lt;TABLE&gt;
> &lt;S&gt; &lt;C&gt;
> AGREED: PARTICIPANT: XIRCOM
> -------------------------------------------
> INTEL CORPORATION (Company Name, Division/Sub, if applicable)
> 3065 Bowers Avenue
> Santa Clara, CA 95052 26025 Mureau Road
> --------------------------------------------------------
> (Address)
> Calabasas CA 91302
> --------------------------------------------------------
> (City) (State) (Zip)
> /s/ CARL EVERETT /s/ JEROME P. CHERWINSKI
> -------------------------------- --------------------------------------------------------
> Signature Signature
> CARL EVERETT JEROME P. CHERWINSKI
> -------------------------------- --------------------------------------------------------
> Printed Name Printed Name
> VICE PRESIDENT-DIRECTOR OF SALES V.P. ENG. 230-0000-30 (7/90)
> -------------------------------- --------------------------------------------------------
> Title Title
> &lt;/TABLE&gt;
> SEND TO: CORPORATE CONTRACT
> MANAGEMENT, FM 1-03

</details>

## Question

> Classify the following statement using only the supplied contract: Receiving Party shall not disclose the fact that Agreement was agreed or negotiated.

## Answer choices

- **Contradiction:** The contract contradicts the statement.
- **Entailment:** The contract supports the statement.
- **NotMentioned:** The contract does not establish whether it is true.

**Reference answer:** The contract does not establish whether it is true. (`NotMentioned`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "CORPORATE NON-DISCLOSURE AGREEMENT\nThis Agreement is entered into and made effective as of the date set forth above by and between Intel Corporation (hereinafter \"Intel\"), and the participant identified below (hereinafter \"Participant\"). Unless the Participant indicates that this Agreement shall apply only to a specific division or location, this Agreement shall apply to the Participant's entire company.\nTHE PARTIES AGREE AS FOLLOWS:\nCONFIDENTIAL INFORMATION TRANSMITTAL FORM. The confidential, proprietary and trade secret information of the disclosing party (hereinafter \"Confidential Information\") provided hereunder, is that information described in the Confidential Information Transmittal Record (CITR) form executed from time to time hereafter. CITR's are subject to the terms of this Agreement and shall be executed by the parties prior to the disclosure of Confidential Information. All information described in a CITR and marked with a \"confidential,\" \"proprietary,\" or similar legend shall be deemed Confidential Information. All Confidential Information received from the disclosing party shall be in tangible form. The CITR shall set forth the disclosing party, a description of the Confidential Information disclosed, the names of the representatives of the parties and the date when the disclosure covered by the CITR commenced.\nOBLIGATIONS OF RECEIVING PARTY. The receiving party shall not disclose Confidential Information to any third party without the prior written approval of the disclosing party. The receiving party shall maintain the Confidential Information with at least the same degree of care that the receiving party uses to protect its own similar categories of confidential and proprietary information, but no less than a reasonable degree of care under the circumstances. The receiving party shall not make any copies of Confidential Information received from the disclosing party except as necessary for its employees with a need to know. Any copies which are made shall be identified as belonging to the disclosing party and marked \"confidential,\" \"proprietary,\" or with a similar legend.\nPERIOD OF CONFIDENTIALITY. Unless a shorter period is stated in the applicable CITR, the disclosing party will not assert any claims against the receiving party for disclosures of Confidential Information made more than five (5) years from the date of the CITR.\nTERMINATION OF OBLIGATION OF CONFIDENTIALITY. The receiving party shall not be liable for the disclosure of any Confidential Information which is:\n(a) in the public domain other than by a breach of this Agreement on the part of the receiving party; or\n(b) rightfully received from a third party without any obligation of confidentiality; or\n(c) rightfully known to the receiving party without any limitation on use or disclosure prior to its receipt from the disclosing party; or\n(d) independently developed by employees of the receiving party; or (e) generally made available to third parties by the disclosing party\nwithout restriction on disclosure.\nTITLE. Title or the right to possess Confidential Information as between the parties shall remain in the disclosing party.\nNO OBLIGATION OF DISCLOSURE. Neither party has any obligation to disclose Confidential Information to the other. Either party may, at any time, cease giving Confidential Information to the other party without any liability or request in writing the return of Confidential Information previously disclosed.\nTERMINATION AND DUTY TO RETURN. Either party may terminate this Agreement at any time without cause upon notice to the other party. However, all obligations of confidentiality shall survive the termination of this Agreement. In the event this Agreement is terminated, and the disclosing party so requests, the receiving party shall promptly return or destroy (and certify destruction of) all Confidential Information which it received from the disclosing party along with all copies which it made. GENERAL.\n(a) This Agreement is neither intended to nor shall it be construed as creating a joint venture, partnership or other form of business association between the parties, nor an obligation to buy or sell products using or incorporating the Confidential Information, nor as creating an implied or express license grant from either party to the other.\n(b) The failure of either party to enforce any right resulting from breach of any provision of this Agreement by the other party shall not be deemed a waiver of any right relating to a subsequent breach of such provision or of any other right hereunder.\n(c) This Agreement shall be governed by the laws of the State of California.\n(d) This Agreement, any accompanying CITR and CITRs executed from time to time hereafter which incorporate the terms of this Agreement constitute the entire agreement, written or verbal, between the parties with respect to the disclosure(s) of Confidential Information described in each CITR. This Agreement may not be amended except in writing signed by a duly authorized representative of the respective parties. Any other agreements between the parties, including non-disclosure agreements, shall not be affected by this Agreement.\n<TABLE>\n<S> <C>\nAGREED: PARTICIPANT: XIRCOM\n-------------------------------------------\nINTEL CORPORATION (Company Name, Division/Sub, if applicable)\n3065 Bowers Avenue\nSanta Clara, CA 95052 26025 Mureau Road\n--------------------------------------------------------\n(Address)\nCalabasas CA 91302\n--------------------------------------------------------\n(City) (State) (Zip)\n/s/ CARL EVERETT /s/ JEROME P. CHERWINSKI\n-------------------------------- --------------------------------------------------------\nSignature Signature\nCARL EVERETT JEROME P. CHERWINSKI\n-------------------------------- --------------------------------------------------------\nPrinted Name Printed Name\nVICE PRESIDENT-DIRECTOR OF SALES V.P. ENG. 230-0000-30 (7/90)\n-------------------------------- --------------------------------------------------------\nTitle Title\n</TABLE>\nSEND TO: CORPORATE CONTRACT\nMANAGEMENT, FM 1-03\n",
  "question": "Classify the following statement using only the supplied contract: Receiving Party shall not disclose the fact that Agreement was agreed or negotiated.",
  "choices": {
    "Contradiction": "The contract contradicts the statement.",
    "Entailment": "The contract supports the statement.",
    "NotMentioned": "The contract does not establish whether it is true."
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
| Jev | The contract does not establish whether it is true. | Correct |
| Microsoft Decision-1 | The contract does not establish whether it is true. | Correct |
| Clef | The contract does not establish whether it is true. | Correct |
| Luna Decisions | The contract does not establish whether it is true. | Correct |
| Clef Flash | The contract does not establish whether it is true. | Correct |
| Strands Decider | The contract does not establish whether it is true. | Correct |
| GLiNER2.5 Decide | The contract does not establish whether it is true. | Correct |
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
    "record": "2468",
    "kind": "prepared_normalizer_record",
    "native_id": "contractnli/test.json/413/nda-10/baseline"
  },
  "source_revision": "eced6528dd3c1d14d73f9a87df8f7bdbc03126f9",
  "input_hash": "d42c8ad43f88a9b1b2b594482c518a09fbfb5aa4d5254a3dd79e1a20c8660703"
}
```

</details>
