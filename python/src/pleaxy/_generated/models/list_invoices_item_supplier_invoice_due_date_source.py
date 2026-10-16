from typing import Literal, Set, cast

ListInvoicesItemSupplierInvoiceDueDateSource = Literal["default", "stated"]

LIST_INVOICES_ITEM_SUPPLIER_INVOICE_DUE_DATE_SOURCE_VALUES: Set[
    ListInvoicesItemSupplierInvoiceDueDateSource
] = {
    "default",
    "stated",
}


def check_list_invoices_item_supplier_invoice_due_date_source(
    value: str,
) -> ListInvoicesItemSupplierInvoiceDueDateSource:
    if value in LIST_INVOICES_ITEM_SUPPLIER_INVOICE_DUE_DATE_SOURCE_VALUES:
        return cast(ListInvoicesItemSupplierInvoiceDueDateSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_SUPPLIER_INVOICE_DUE_DATE_SOURCE_VALUES!r}"
    )
