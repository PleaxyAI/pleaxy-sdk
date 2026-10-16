from typing import Literal, Set, cast

InvoiceBuyerViewDocumentType = Literal["debit_note"]

INVOICE_BUYER_VIEW_DOCUMENT_TYPE_VALUES: Set[InvoiceBuyerViewDocumentType] = {
    "debit_note",
}


def check_invoice_buyer_view_document_type(value: str) -> InvoiceBuyerViewDocumentType:
    if value in INVOICE_BUYER_VIEW_DOCUMENT_TYPE_VALUES:
        return cast(InvoiceBuyerViewDocumentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_BUYER_VIEW_DOCUMENT_TYPE_VALUES!r}"
    )
