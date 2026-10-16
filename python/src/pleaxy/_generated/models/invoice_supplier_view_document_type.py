from typing import Literal, Set, cast

InvoiceSupplierViewDocumentType = Literal["debit_note"]

INVOICE_SUPPLIER_VIEW_DOCUMENT_TYPE_VALUES: Set[InvoiceSupplierViewDocumentType] = {
    "debit_note",
}


def check_invoice_supplier_view_document_type(
    value: str,
) -> InvoiceSupplierViewDocumentType:
    if value in INVOICE_SUPPLIER_VIEW_DOCUMENT_TYPE_VALUES:
        return cast(InvoiceSupplierViewDocumentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_SUPPLIER_VIEW_DOCUMENT_TYPE_VALUES!r}"
    )
