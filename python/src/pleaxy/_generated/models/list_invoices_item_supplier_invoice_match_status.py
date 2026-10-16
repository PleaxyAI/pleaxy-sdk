from typing import Literal, Set, cast

ListInvoicesItemSupplierInvoiceMatchStatus = Literal[
    "discrepancy", "matched", "pending", "unverified"
]

LIST_INVOICES_ITEM_SUPPLIER_INVOICE_MATCH_STATUS_VALUES: Set[
    ListInvoicesItemSupplierInvoiceMatchStatus
] = {
    "discrepancy",
    "matched",
    "pending",
    "unverified",
}


def check_list_invoices_item_supplier_invoice_match_status(
    value: str,
) -> ListInvoicesItemSupplierInvoiceMatchStatus:
    if value in LIST_INVOICES_ITEM_SUPPLIER_INVOICE_MATCH_STATUS_VALUES:
        return cast(ListInvoicesItemSupplierInvoiceMatchStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_SUPPLIER_INVOICE_MATCH_STATUS_VALUES!r}"
    )
