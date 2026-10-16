from typing import Literal, Set, cast

ListInvoicesItemSupplierInvoiceEnteredBy = Literal["buyer", "supplier"]

LIST_INVOICES_ITEM_SUPPLIER_INVOICE_ENTERED_BY_VALUES: Set[
    ListInvoicesItemSupplierInvoiceEnteredBy
] = {
    "buyer",
    "supplier",
}


def check_list_invoices_item_supplier_invoice_entered_by(
    value: str,
) -> ListInvoicesItemSupplierInvoiceEnteredBy:
    if value in LIST_INVOICES_ITEM_SUPPLIER_INVOICE_ENTERED_BY_VALUES:
        return cast(ListInvoicesItemSupplierInvoiceEnteredBy, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_SUPPLIER_INVOICE_ENTERED_BY_VALUES!r}"
    )
