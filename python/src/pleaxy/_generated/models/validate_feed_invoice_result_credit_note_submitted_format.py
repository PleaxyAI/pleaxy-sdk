from typing import Literal, Set, cast

ValidateFeedInvoiceResultCreditNoteSubmittedFormat = Literal["cxml", "json", "ubl"]

VALIDATE_FEED_INVOICE_RESULT_CREDIT_NOTE_SUBMITTED_FORMAT_VALUES: Set[
    ValidateFeedInvoiceResultCreditNoteSubmittedFormat
] = {
    "cxml",
    "json",
    "ubl",
}


def check_validate_feed_invoice_result_credit_note_submitted_format(
    value: str,
) -> ValidateFeedInvoiceResultCreditNoteSubmittedFormat:
    if value in VALIDATE_FEED_INVOICE_RESULT_CREDIT_NOTE_SUBMITTED_FORMAT_VALUES:
        return cast(ValidateFeedInvoiceResultCreditNoteSubmittedFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {VALIDATE_FEED_INVOICE_RESULT_CREDIT_NOTE_SUBMITTED_FORMAT_VALUES!r}"
    )
