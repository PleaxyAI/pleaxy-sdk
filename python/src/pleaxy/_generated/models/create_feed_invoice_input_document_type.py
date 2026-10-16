from typing import Literal, Set, cast

CreateFeedInvoiceInputDocumentType = Literal["debit_note", "invoice"]

CREATE_FEED_INVOICE_INPUT_DOCUMENT_TYPE_VALUES: Set[
    CreateFeedInvoiceInputDocumentType
] = {
    "debit_note",
    "invoice",
}


def check_create_feed_invoice_input_document_type(
    value: str,
) -> CreateFeedInvoiceInputDocumentType:
    if value in CREATE_FEED_INVOICE_INPUT_DOCUMENT_TYPE_VALUES:
        return cast(CreateFeedInvoiceInputDocumentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_FEED_INVOICE_INPUT_DOCUMENT_TYPE_VALUES!r}"
    )
