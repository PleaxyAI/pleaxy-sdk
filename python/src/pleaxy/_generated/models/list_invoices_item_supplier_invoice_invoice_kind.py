from typing import Literal, Set, cast

ListInvoicesItemSupplierInvoiceInvoiceKind = Literal["prepayment"]

LIST_INVOICES_ITEM_SUPPLIER_INVOICE_INVOICE_KIND_VALUES: Set[
    ListInvoicesItemSupplierInvoiceInvoiceKind
] = {
    "prepayment",
}


def check_list_invoices_item_supplier_invoice_invoice_kind(
    value: str,
) -> ListInvoicesItemSupplierInvoiceInvoiceKind:
    if value in LIST_INVOICES_ITEM_SUPPLIER_INVOICE_INVOICE_KIND_VALUES:
        return cast(ListInvoicesItemSupplierInvoiceInvoiceKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_SUPPLIER_INVOICE_INVOICE_KIND_VALUES!r}"
    )
