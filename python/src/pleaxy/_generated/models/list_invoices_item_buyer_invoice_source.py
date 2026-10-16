from typing import Literal, Set, cast

ListInvoicesItemBuyerInvoiceSource = Literal["direct", "feed", "manual", "po-flip"]

LIST_INVOICES_ITEM_BUYER_INVOICE_SOURCE_VALUES: Set[
    ListInvoicesItemBuyerInvoiceSource
] = {
    "direct",
    "feed",
    "manual",
    "po-flip",
}


def check_list_invoices_item_buyer_invoice_source(
    value: str,
) -> ListInvoicesItemBuyerInvoiceSource:
    if value in LIST_INVOICES_ITEM_BUYER_INVOICE_SOURCE_VALUES:
        return cast(ListInvoicesItemBuyerInvoiceSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_BUYER_INVOICE_SOURCE_VALUES!r}"
    )
