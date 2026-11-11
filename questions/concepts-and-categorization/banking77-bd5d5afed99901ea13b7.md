# Concepts and categorization · question 56

[Back to Concepts and categorization](README.md) · [All capabilities](../README.md)

**Question ID:** `banking77/bd5d5afed99901ea13b7`  
**Source:** [Banking77](https://huggingface.co/datasets/PolyAI/banking77)  
**Input format:** native choices

[Explore this question’s altered versions](../../variants/concepts-and-categorization/banking77-bd5d5afed99901ea13b7/README.md)

## Context

> Why do we need to verify a top-up card?

## Question

> Which banking intent does this request express?

## Answer choices

- **0:** activate\_my\_card
- **1:** age\_limit
- **2:** apple\_pay\_or\_google\_pay
- **3:** atm\_support
- **4:** automatic\_top\_up
- **5:** balance\_not\_updated\_after\_bank\_transfer
- **6:** balance\_not\_updated\_after\_cheque\_or\_cash\_deposit
- **7:** beneficiary\_not\_allowed
- **8:** cancel\_transfer
- **9:** card\_about\_to\_expire
- **10:** card\_acceptance
- **11:** card\_arrival
- **12:** card\_delivery\_estimate
- **13:** card\_linking
- **14:** card\_not\_working
- **15:** card\_payment\_fee\_charged
- **16:** card\_payment\_not\_recognised
- **17:** card\_payment\_wrong\_exchange\_rate
- **18:** card\_swallowed
- **19:** cash\_withdrawal\_charge
- **20:** cash\_withdrawal\_not\_recognised
- **21:** change\_pin
- **22:** compromised\_card
- **23:** contactless\_not\_working
- **24:** country\_support
- **25:** declined\_card\_payment
- **26:** declined\_cash\_withdrawal
- **27:** declined\_transfer
- **28:** direct\_debit\_payment\_not\_recognised
- **29:** disposable\_card\_limits
- **30:** edit\_personal\_details
- **31:** exchange\_charge
- **32:** exchange\_rate
- **33:** exchange\_via\_app
- **34:** extra\_charge\_on\_statement
- **35:** failed\_transfer
- **36:** fiat\_currency\_support
- **37:** get\_disposable\_virtual\_card
- **38:** get\_physical\_card
- **39:** getting\_spare\_card
- **40:** getting\_virtual\_card
- **41:** lost\_or\_stolen\_card
- **42:** lost\_or\_stolen\_phone
- **43:** order\_physical\_card
- **44:** passcode\_forgotten
- **45:** pending\_card\_payment
- **46:** pending\_cash\_withdrawal
- **47:** pending\_top\_up
- **48:** pending\_transfer
- **49:** pin\_blocked
- **50:** receiving\_money
- **51:** Refund\_not\_showing\_up
- **52:** request\_refund
- **53:** reverted\_card\_payment?
- **54:** supported\_cards\_and\_currencies
- **55:** terminate\_account
- **56:** top\_up\_by\_bank\_transfer\_charge
- **57:** top\_up\_by\_card\_charge
- **58:** top\_up\_by\_cash\_or\_cheque
- **59:** top\_up\_failed
- **60:** top\_up\_limits
- **61:** top\_up\_reverted
- **62:** topping\_up\_by\_card
- **63:** transaction\_charged\_twice
- **64:** transfer\_fee\_charged
- **65:** transfer\_into\_account
- **66:** transfer\_not\_received\_by\_recipient
- **67:** transfer\_timing
- **68:** unable\_to\_verify\_identity
- **69:** verify\_my\_identity
- **70:** verify\_source\_of\_funds
- **71:** verify\_top\_up
- **72:** virtual\_card\_not\_working
- **73:** visa\_or\_mastercard
- **74:** why\_verify\_identity
- **75:** wrong\_amount\_of\_cash\_received
- **76:** wrong\_exchange\_rate\_for\_cash\_withdrawal

**Reference answer:** verify\_top\_up (`71`)

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Why do we need to verify a top-up card?",
  "question": "Which banking intent does this request express?",
  "choices": {
    "0": "activate_my_card",
    "1": "age_limit",
    "2": "apple_pay_or_google_pay",
    "3": "atm_support",
    "4": "automatic_top_up",
    "5": "balance_not_updated_after_bank_transfer",
    "6": "balance_not_updated_after_cheque_or_cash_deposit",
    "7": "beneficiary_not_allowed",
    "8": "cancel_transfer",
    "9": "card_about_to_expire",
    "10": "card_acceptance",
    "11": "card_arrival",
    "12": "card_delivery_estimate",
    "13": "card_linking",
    "14": "card_not_working",
    "15": "card_payment_fee_charged",
    "16": "card_payment_not_recognised",
    "17": "card_payment_wrong_exchange_rate",
    "18": "card_swallowed",
    "19": "cash_withdrawal_charge",
    "20": "cash_withdrawal_not_recognised",
    "21": "change_pin",
    "22": "compromised_card",
    "23": "contactless_not_working",
    "24": "country_support",
    "25": "declined_card_payment",
    "26": "declined_cash_withdrawal",
    "27": "declined_transfer",
    "28": "direct_debit_payment_not_recognised",
    "29": "disposable_card_limits",
    "30": "edit_personal_details",
    "31": "exchange_charge",
    "32": "exchange_rate",
    "33": "exchange_via_app",
    "34": "extra_charge_on_statement",
    "35": "failed_transfer",
    "36": "fiat_currency_support",
    "37": "get_disposable_virtual_card",
    "38": "get_physical_card",
    "39": "getting_spare_card",
    "40": "getting_virtual_card",
    "41": "lost_or_stolen_card",
    "42": "lost_or_stolen_phone",
    "43": "order_physical_card",
    "44": "passcode_forgotten",
    "45": "pending_card_payment",
    "46": "pending_cash_withdrawal",
    "47": "pending_top_up",
    "48": "pending_transfer",
    "49": "pin_blocked",
    "50": "receiving_money",
    "51": "Refund_not_showing_up",
    "52": "request_refund",
    "53": "reverted_card_payment?",
    "54": "supported_cards_and_currencies",
    "55": "terminate_account",
    "56": "top_up_by_bank_transfer_charge",
    "57": "top_up_by_card_charge",
    "58": "top_up_by_cash_or_cheque",
    "59": "top_up_failed",
    "60": "top_up_limits",
    "61": "top_up_reverted",
    "62": "topping_up_by_card",
    "63": "transaction_charged_twice",
    "64": "transfer_fee_charged",
    "65": "transfer_into_account",
    "66": "transfer_not_received_by_recipient",
    "67": "transfer_timing",
    "68": "unable_to_verify_identity",
    "69": "verify_my_identity",
    "70": "verify_source_of_funds",
    "71": "verify_top_up",
    "72": "virtual_card_not_working",
    "73": "visa_or_mastercard",
    "74": "why_verify_identity",
    "75": "wrong_amount_of_cash_received",
    "76": "wrong_exchange_rate_for_cash_withdrawal"
  }
}
```

</details>

## Recorded model answers

| Model | Answer | Outcome |
| --- | --- | --- |
| Astra | verify\_top\_up | Correct |
| Opus 5.5 | verify\_top\_up | Correct |
| GLiDE v1.2 | verify\_top\_up | Correct |
| Decider v1.1 | verify\_top\_up | Correct |
| Jev | verify\_top\_up | Correct |
| Microsoft Decision-1 | verify\_top\_up | Correct |
| Clef | verify\_top\_up | Correct |
| Luna Decisions | verify\_top\_up | Correct |
| Clef Flash | verify\_top\_up | Correct |
| Strands Decider | verify\_top\_up | Correct |
| GLiNER2.5 Decide | verify\_top\_up | Correct |
| Laya | verify\_top\_up | Correct |
| CalDec v1 | verify\_top\_up | Correct |

## Source and sharing

Attribution: PolyAI; Iñigo Casanueva et al..  
Terms: **[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)**. [Source sharing decision](../../docs/data-sharing.md).  
The capability assignment and choice-format normalization are part of this experiment. Source data retain their own terms.

<details>
<summary>Exact source locator and input fingerprint</summary>

```json
{
  "source_locator": {
    "path": "data/train-00000-of-00001.parquet",
    "record": "7712",
    "kind": "source_file_record"
  },
  "source_revision": "1846984189f2bc0ac51c6fc3a600fa9e1714e0c6",
  "input_hash": "96e971da23c857101a36c8b8d2c3a8e8215e206ac248be2cdebc2a3168201444"
}
```

</details>
