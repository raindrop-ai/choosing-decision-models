# Retrieval · question 39

[Back to Retrieval](README.md) · [All capabilities](../README.md)

**Question ID:** `contractnli/8b3111a82affbd22b1c1`  
**Source:** [ContractNLI](https://github.com/stanfordnlp/contract-nli)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/retrieval/contractnli-8b3111a82affbd22b1c1/README.md)

## Context

<details>
<summary>Read the full context</summary>

> NON DISCLOSURE AGREEMENT (page 1 of 3)
> THIS AGREEMENT is made between the parties named at the end of this document.
> WHEREAS, both parties may provide certain confidential and proprietary information to each other in connection with the business purposes described in Exhibit A attached hereto ("the Business Purpose") and each desires that any such information provided shall be kept confidential by the other party; and
> WHEREAS, in consideration of the disclosure of such information each party is willing to keep the other party's information confidential in accordance with the terms and conditions set forth in this Agreement.
> NOW IT IS HEREBY AGREED AS FOLLOWS:
> 1. Confidentiality
> Each party may use the information received from the other party hereunder and may provide such information to its parent corporation or any other subsidiaries thereof and their respective employees as applicable for their use only in connection with the Business Purpose.
> Each party agrees that, for a period of 5 years from receipt of information from the other party hereunder, such party shall use the same means it uses to protect its own confidential and proprietary information to prevent the disclosure and to protect the confidentiality of both:
> i) written information received from the other party which is marked or identified as "confidential"; and
> ii) oral or visual information identified as confidential at the time of disclosure which is reduced to written form and provided to the other in such written form promptly after such oral or visual disclosure,
> hereinafter collectively referred to as "the Information".
> The foregoing shall not prevent either party from disclosing Information which is:
> i) already known by the recipient party prior to the disclosure thereof with no obligation of confidentiality; or
> ii) publicly known or becomes publicly known not due to any unauthorised act of the recipient party; or
> iii) rightfully received from a third party; or
> iv) independently developed by the recipient party without use of the other party's Information; or
> v) disclosed without similar restrictions by the party owning the Information to any third party; or
> vi) approved by the other party for disclosure; or
> vii) required to be disclosed pursuant to a governmental or legal requirement provided that the disclosing party gives to the other party written notice of such requirement prior to any such disclosure.
> viii) publicly known or becomes publicly known not due to any unauthorised act of the recipient party; or
> ix) rightfully received from a third party; or
> x) independently developed by the recipient party without use of the other party's Information; or
> xi) disclosed without similar restrictions by the party owning the Information to any third party; or
> xii) approved by the other party for disclosure; or
> xiii) required to be disclosed pursuant to a governmental or legal requirement provided that the disclosing party gives to the other party written notice of such requirement prior to any such disclosure.
> 2. Return of Information
> Upon completion of the Business Purpose and/or upon written request of the party providing the Information, the other party shall within 14 days return all copies of the Information to the providing party or certify in writing that all copies of the Information have been destroyed. Nothing in this clause shall affect the right of either party voluntarily to return the Information, or any part thereof, to the other party at any time.
> 3. No Warranty/Liability
> Neither party makes any warranty, express or implied, with respect to the Information. Neither party shall be liable to the other or to any other person hereunder for amounts representing loss of profits or loss of business or indirect, consequential or punitive damages of the other or of such other person in connection with the provision or use of the Information hereunder.
> 4. No Further Rights
> Nothing contained in this Agreement shall be construed as granting or conferring any rights by licence or otherwise in the Information except as provided herein.
> 5. Business Purpose
> The parties expressly agree that the provision of Information hereunder and any discussions held in connection with the Business Purpose shall not prevent either party from pursuing similar discussions with third parties provided that no breach of this Agreement is so occasioned or oblige that party to take, continue or forego any action relating to the Business Purpose. Any forecasts or similar material provided by either party to the other shall not constitute any commitments.
> 6. Injunctive Rights
> Each party acknowledges and agrees that the Information is the confidential and/or proprietary and/or trade secret information of the other and the unauthorised use or disclosure of the Information could cause irreparable harm and significant injury to the other party for which that other party would have no adequate remedy at law. Therefore, each party shall have the right, in addition to any other rights it may have at law or in equity, to seek and obtain immediate injunctive relief in respect of any breach or potential breach of this Agreement by the other.
> 7. Media Releases
> No media releases, public announcements or public disclosure by either party relating to this Agreement, its subject matter or the Information, including but not limited to promotional or marketing, shall be made without the prior written consent of the other party.
> 8. General
> 8.1 Notices
> Any notices required under this Agreement shall be in writing and posted by registered mail return receipt requested to the applicable address indicated in Exhibit A.
> 8.2 Entire Agreement
> This Agreement and any attachments hereto:
> i) are the complete and exclusive statement between the parties with respect to the protection of the confidentiality of the Information; and
> ii) supersede all related discussions and other communications between the parties; and
> iii) may only be modified in writing by authorised representatives of the parties.
> 8.3 Governing Law
> This Agreement shall be governed by and interpreted in accordance with the law of England and shall be subject to the exclusive jurisdiction of the courts of England.
> AS WITNESS WHEREOF the parties named below have caused this Agreement to be signed and delivered by its duly authorised representative on this date: …………………………………………………..
> For and on behalf of For and on behalf of
> iTagg Limited …………………………………………………………
> (herein known as “Party 1”) (herein known as “Party 2”)
> Address Address
> 3rd Floor
> 12 Gough Square
> London
> EC4A 3DW
> England
> Company number 4344060 Company number..............................
> Signed Signed................................................
> Name Steve Procter Name..................................................
> Title Director Title....................................................
> EXHIBIT A
> 1. Business Purpose:
> All business related support services, as well as affiliate, reseller and introducer deals and all commercial and business opportunities. For the purpose of clarity, all information and discussions related to service and product prices, costs, commissions, fees and other monetary matters are also covered under this agreement and to be kept confidential. This includes any prices, costs, commissions, fees or other monetary information offered by one party to the other even if not accepted, as well as any prices, costs, commissions, fees or other monetary information that are accepted by both parties and drawn into a subsequent contract between the parties.
> 2. Addresses for Notices:
> a) Party 1: As above
> b) Party 2: As above (insert alternative address and contact name below if necessary)

</details>

## Question

> Classify the following statement using only the supplied contract: Receiving Party shall notify Disclosing Party in case Receiving Party is required by law, regulation or judicial process to disclose any Confidential Information.

## Answer choices

- **Entailment:** The contract supports the statement.
- **Contradiction:** The contract contradicts the statement.
- **NotMentioned:** The contract does not establish whether it is true.

**Reference answer:** The contract supports the statement. (`Entailment`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "NON DISCLOSURE AGREEMENT (page 1 of 3)\nTHIS AGREEMENT is made between the parties named at the end of this document.\nWHEREAS, both parties may provide certain confidential and proprietary information to each other in connection with the business purposes described in Exhibit A attached hereto (\"the Business Purpose\") and each desires that any such information provided shall be kept confidential by the other party; and\nWHEREAS, in consideration of the disclosure of such information each party is willing to keep the other party's information confidential in accordance with the terms and conditions set forth in this Agreement.\nNOW IT IS HEREBY AGREED AS FOLLOWS:\n1. Confidentiality\nEach party may use the information received from the other party hereunder and may provide such information to its parent corporation or any other subsidiaries thereof and their respective employees as applicable for their use only in connection with the Business Purpose.\nEach party agrees that, for a period of 5 years from receipt of information from the other party hereunder, such party shall use the same means it uses to protect its own confidential and proprietary information to prevent the disclosure and to protect the confidentiality of both:\ni) written information received from the other party which is marked or identified as \"confidential\"; and\nii) oral or visual information identified as confidential at the time of disclosure which is reduced to written form and provided to the other in such written form promptly after such oral or visual disclosure,\nhereinafter collectively referred to as \"the Information\".\nThe foregoing shall not prevent either party from disclosing Information which is:\ni) already known by the recipient party prior to the disclosure thereof with no obligation of confidentiality; or\nii) publicly known or becomes publicly known not due to any unauthorised act of the recipient party; or\niii) rightfully received from a third party; or\niv) independently developed by the recipient party without use of the other party's Information; or\nv) disclosed without similar restrictions by the party owning the Information to any third party; or\nvi) approved by the other party for disclosure; or\nvii) required to be disclosed pursuant to a governmental or legal requirement provided that the disclosing party gives to the other party written notice of such requirement prior to any such disclosure.\nviii) publicly known or becomes publicly known not due to any unauthorised act of the recipient party; or\nix) rightfully received from a third party; or\nx) independently developed by the recipient party without use of the other party's Information; or\nxi) disclosed without similar restrictions by the party owning the Information to any third party; or\nxii) approved by the other party for disclosure; or\nxiii) required to be disclosed pursuant to a governmental or legal requirement provided that the disclosing party gives to the other party written notice of such requirement prior to any such disclosure.\n2. Return of Information\nUpon completion of the Business Purpose and/or upon written request of the party providing the Information, the other party shall within 14 days return all copies of the Information to the providing party or certify in writing that all copies of the Information have been destroyed. Nothing in this clause shall affect the right of either party voluntarily to return the Information, or any part thereof, to the other party at any time.\n3. No Warranty/Liability\nNeither party makes any warranty, express or implied, with respect to the Information. Neither party shall be liable to the other or to any other person hereunder for amounts representing loss of profits or loss of business or indirect, consequential or punitive damages of the other or of such other person in connection with the provision or use of the Information hereunder.\n4. No Further Rights\nNothing contained in this Agreement shall be construed as granting or conferring any rights by licence or otherwise in the Information except as provided herein.\n5. Business Purpose\nThe parties expressly agree that the provision of Information hereunder and any discussions held in connection with the Business Purpose shall not prevent either party from pursuing similar discussions with third parties provided that no breach of this Agreement is so occasioned or oblige that party to take, continue or forego any action relating to the Business Purpose. Any forecasts or similar material provided by either party to the other shall not constitute any commitments.\n6. Injunctive Rights\nEach party acknowledges and agrees that the Information is the confidential and/or proprietary and/or trade secret information of the other and the unauthorised use or disclosure of the Information could cause irreparable harm and significant injury to the other party for which that other party would have no adequate remedy at law. Therefore, each party shall have the right, in addition to any other rights it may have at law or in equity, to seek and obtain immediate injunctive relief in respect of any breach or potential breach of this Agreement by the other.\n7. Media Releases\nNo media releases, public announcements or public disclosure by either party relating to this Agreement, its subject matter or the Information, including but not limited to promotional or marketing, shall be made without the prior written consent of the other party.\n8. General\n8.1 Notices\nAny notices required under this Agreement shall be in writing and posted by registered mail return receipt requested to the applicable address indicated in Exhibit A.\n8.2 Entire Agreement\nThis Agreement and any attachments hereto:\ni) are the complete and exclusive statement between the parties with respect to the protection of the confidentiality of the Information; and\nii) supersede all related discussions and other communications between the parties; and\niii) may only be modified in writing by authorised representatives of the parties.\n8.3 Governing Law\nThis Agreement shall be governed by and interpreted in accordance with the law of England and shall be subject to the exclusive jurisdiction of the courts of England.\nAS WITNESS WHEREOF the parties named below have caused this Agreement to be signed and delivered by its duly authorised representative on this date: …………………………………………………..\nFor and on behalf of For and on behalf of\niTagg Limited …………………………………………………………\n(herein known as “Party 1”) (herein known as “Party 2”)\nAddress Address\n3rd Floor\n12 Gough Square\nLondon\nEC4A 3DW\nEngland\nCompany number 4344060 Company number..............................\nSigned Signed................................................\nName Steve Procter Name..................................................\nTitle Director Title....................................................\nEXHIBIT A\n1. Business Purpose:\nAll business related support services, as well as affiliate, reseller and introducer deals and all commercial and business opportunities. For the purpose of clarity, all information and discussions related to service and product prices, costs, commissions, fees and other monetary matters are also covered under this agreement and to be kept confidential. This includes any prices, costs, commissions, fees or other monetary information offered by one party to the other even if not accepted, as well as any prices, costs, commissions, fees or other monetary information that are accepted by both parties and drawn into a subsequent contract between the parties.\n2. Addresses for Notices:\na) Party 1: As above\nb) Party 2: As above (insert alternative address and contact name below if necessary)\n",
  "question": "Classify the following statement using only the supplied contract: Receiving Party shall notify Disclosing Party in case Receiving Party is required by law, regulation or judicial process to disclose any Confidential Information.",
  "choices": {
    "Entailment": "The contract supports the statement.",
    "Contradiction": "The contract contradicts the statement.",
    "NotMentioned": "The contract does not establish whether it is true."
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
    "record": "2036",
    "kind": "prepared_normalizer_record",
    "native_id": "contractnli/test.json/190/nda-8/baseline"
  },
  "source_revision": "eced6528dd3c1d14d73f9a87df8f7bdbc03126f9",
  "input_hash": "89cf25d32aa5268cfb9f074dc2bc25a4768312a7c6cdae0bfdb9d96dd5fd21a9"
}
```

</details>
