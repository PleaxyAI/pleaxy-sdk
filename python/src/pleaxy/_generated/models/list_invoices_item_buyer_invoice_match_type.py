from typing import Literal, Set, cast

ListInvoicesItemBuyerInvoiceMatchType = Literal["three_way", "two_way", "usage"]

LIST_INVOICES_ITEM_BUYER_INVOICE_MATCH_TYPE_VALUES: Set[
    ListInvoicesItemBuyerInvoiceMatchType
] = {
    "three_way",
    "two_way",
    "usage",
}


def check_list_invoices_item_buyer_invoice_match_type(
    value: str,
) -> ListInvoicesItemBuyerInvoiceMatchType:
    if value in LIST_INVOICES_ITEM_BUYER_INVOICE_MATCH_TYPE_VALUES:
        return cast(ListInvoicesItemBuyerInvoiceMatchType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_BUYER_INVOICE_MATCH_TYPE_VALUES!r}"
    )
