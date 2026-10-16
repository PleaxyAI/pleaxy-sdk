from typing import Literal, Set, cast

ListInvoicesItemBuyerInvoiceEnteredBy = Literal["buyer", "supplier"]

LIST_INVOICES_ITEM_BUYER_INVOICE_ENTERED_BY_VALUES: Set[
    ListInvoicesItemBuyerInvoiceEnteredBy
] = {
    "buyer",
    "supplier",
}


def check_list_invoices_item_buyer_invoice_entered_by(
    value: str,
) -> ListInvoicesItemBuyerInvoiceEnteredBy:
    if value in LIST_INVOICES_ITEM_BUYER_INVOICE_ENTERED_BY_VALUES:
        return cast(ListInvoicesItemBuyerInvoiceEnteredBy, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_BUYER_INVOICE_ENTERED_BY_VALUES!r}"
    )
