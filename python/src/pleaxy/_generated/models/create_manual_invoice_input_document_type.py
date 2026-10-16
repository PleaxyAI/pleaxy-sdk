from typing import Literal, Set, cast

CreateManualInvoiceInputDocumentType = Literal["debit_note", "invoice"]

CREATE_MANUAL_INVOICE_INPUT_DOCUMENT_TYPE_VALUES: Set[
    CreateManualInvoiceInputDocumentType
] = {
    "debit_note",
    "invoice",
}


def check_create_manual_invoice_input_document_type(
    value: str,
) -> CreateManualInvoiceInputDocumentType:
    if value in CREATE_MANUAL_INVOICE_INPUT_DOCUMENT_TYPE_VALUES:
        return cast(CreateManualInvoiceInputDocumentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_MANUAL_INVOICE_INPUT_DOCUMENT_TYPE_VALUES!r}"
    )
