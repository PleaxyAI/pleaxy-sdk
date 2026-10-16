from typing import Literal, Set, cast

ListInvoicesItemBuyerInvoiceMatchStatus = Literal[
    "discrepancy", "matched", "pending", "unverified"
]

LIST_INVOICES_ITEM_BUYER_INVOICE_MATCH_STATUS_VALUES: Set[
    ListInvoicesItemBuyerInvoiceMatchStatus
] = {
    "discrepancy",
    "matched",
    "pending",
    "unverified",
}


def check_list_invoices_item_buyer_invoice_match_status(
    value: str,
) -> ListInvoicesItemBuyerInvoiceMatchStatus:
    if value in LIST_INVOICES_ITEM_BUYER_INVOICE_MATCH_STATUS_VALUES:
        return cast(ListInvoicesItemBuyerInvoiceMatchStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_BUYER_INVOICE_MATCH_STATUS_VALUES!r}"
    )
