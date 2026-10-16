from typing import Literal, Set, cast

ValidateFeedInvoiceResultCreditNoteDocumentType = Literal["credit_note"]

VALIDATE_FEED_INVOICE_RESULT_CREDIT_NOTE_DOCUMENT_TYPE_VALUES: Set[
    ValidateFeedInvoiceResultCreditNoteDocumentType
] = {
    "credit_note",
}


def check_validate_feed_invoice_result_credit_note_document_type(
    value: str,
) -> ValidateFeedInvoiceResultCreditNoteDocumentType:
    if value in VALIDATE_FEED_INVOICE_RESULT_CREDIT_NOTE_DOCUMENT_TYPE_VALUES:
        return cast(ValidateFeedInvoiceResultCreditNoteDocumentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {VALIDATE_FEED_INVOICE_RESULT_CREDIT_NOTE_DOCUMENT_TYPE_VALUES!r}"
    )
