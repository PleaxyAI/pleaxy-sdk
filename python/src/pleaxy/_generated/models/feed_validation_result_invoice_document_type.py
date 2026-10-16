from typing import Literal, Set, cast

FeedValidationResultInvoiceDocumentType = Literal["debit_note"]

FEED_VALIDATION_RESULT_INVOICE_DOCUMENT_TYPE_VALUES: Set[
    FeedValidationResultInvoiceDocumentType
] = {
    "debit_note",
}


def check_feed_validation_result_invoice_document_type(
    value: str,
) -> FeedValidationResultInvoiceDocumentType:
    if value in FEED_VALIDATION_RESULT_INVOICE_DOCUMENT_TYPE_VALUES:
        return cast(FeedValidationResultInvoiceDocumentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FEED_VALIDATION_RESULT_INVOICE_DOCUMENT_TYPE_VALUES!r}"
    )
