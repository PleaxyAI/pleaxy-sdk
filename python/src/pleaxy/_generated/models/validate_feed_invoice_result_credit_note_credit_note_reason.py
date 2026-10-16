from typing import Literal, Set, cast

ValidateFeedInvoiceResultCreditNoteCreditNoteReason = Literal[
    "other", "price_adjustment", "rebate", "returned_goods", "service_credit"
]

VALIDATE_FEED_INVOICE_RESULT_CREDIT_NOTE_CREDIT_NOTE_REASON_VALUES: Set[
    ValidateFeedInvoiceResultCreditNoteCreditNoteReason
] = {
    "other",
    "price_adjustment",
    "rebate",
    "returned_goods",
    "service_credit",
}


def check_validate_feed_invoice_result_credit_note_credit_note_reason(
    value: str,
) -> ValidateFeedInvoiceResultCreditNoteCreditNoteReason:
    if value in VALIDATE_FEED_INVOICE_RESULT_CREDIT_NOTE_CREDIT_NOTE_REASON_VALUES:
        return cast(ValidateFeedInvoiceResultCreditNoteCreditNoteReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {VALIDATE_FEED_INVOICE_RESULT_CREDIT_NOTE_CREDIT_NOTE_REASON_VALUES!r}"
    )
