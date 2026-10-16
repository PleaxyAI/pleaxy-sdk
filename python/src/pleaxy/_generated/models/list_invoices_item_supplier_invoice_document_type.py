from typing import Literal, Set, cast

ListInvoicesItemSupplierInvoiceDocumentType = Literal["debit_note"]

LIST_INVOICES_ITEM_SUPPLIER_INVOICE_DOCUMENT_TYPE_VALUES: Set[
    ListInvoicesItemSupplierInvoiceDocumentType
] = {
    "debit_note",
}


def check_list_invoices_item_supplier_invoice_document_type(
    value: str,
) -> ListInvoicesItemSupplierInvoiceDocumentType:
    if value in LIST_INVOICES_ITEM_SUPPLIER_INVOICE_DOCUMENT_TYPE_VALUES:
        return cast(ListInvoicesItemSupplierInvoiceDocumentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_SUPPLIER_INVOICE_DOCUMENT_TYPE_VALUES!r}"
    )
