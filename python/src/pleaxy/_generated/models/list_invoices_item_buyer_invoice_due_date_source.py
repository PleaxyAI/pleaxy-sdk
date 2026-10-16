from typing import Literal, Set, cast

ListInvoicesItemBuyerInvoiceDueDateSource = Literal["default", "stated"]

LIST_INVOICES_ITEM_BUYER_INVOICE_DUE_DATE_SOURCE_VALUES: Set[
    ListInvoicesItemBuyerInvoiceDueDateSource
] = {
    "default",
    "stated",
}


def check_list_invoices_item_buyer_invoice_due_date_source(
    value: str,
) -> ListInvoicesItemBuyerInvoiceDueDateSource:
    if value in LIST_INVOICES_ITEM_BUYER_INVOICE_DUE_DATE_SOURCE_VALUES:
        return cast(ListInvoicesItemBuyerInvoiceDueDateSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_BUYER_INVOICE_DUE_DATE_SOURCE_VALUES!r}"
    )
