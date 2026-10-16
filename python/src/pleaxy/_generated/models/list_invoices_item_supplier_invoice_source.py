from typing import Literal, Set, cast

ListInvoicesItemSupplierInvoiceSource = Literal["direct", "feed", "manual", "po-flip"]

LIST_INVOICES_ITEM_SUPPLIER_INVOICE_SOURCE_VALUES: Set[
    ListInvoicesItemSupplierInvoiceSource
] = {
    "direct",
    "feed",
    "manual",
    "po-flip",
}


def check_list_invoices_item_supplier_invoice_source(
    value: str,
) -> ListInvoicesItemSupplierInvoiceSource:
    if value in LIST_INVOICES_ITEM_SUPPLIER_INVOICE_SOURCE_VALUES:
        return cast(ListInvoicesItemSupplierInvoiceSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_SUPPLIER_INVOICE_SOURCE_VALUES!r}"
    )
