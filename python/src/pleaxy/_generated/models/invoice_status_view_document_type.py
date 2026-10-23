from typing import Literal, Set, cast

InvoiceStatusViewDocumentType = Literal["debit_note", "invoice"]

INVOICE_STATUS_VIEW_DOCUMENT_TYPE_VALUES: Set[InvoiceStatusViewDocumentType] = {
    "debit_note",
    "invoice",
}


def check_invoice_status_view_document_type(
    value: str,
) -> InvoiceStatusViewDocumentType:
    if value in INVOICE_STATUS_VIEW_DOCUMENT_TYPE_VALUES:
        return cast(InvoiceStatusViewDocumentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_STATUS_VIEW_DOCUMENT_TYPE_VALUES!r}"
    )
