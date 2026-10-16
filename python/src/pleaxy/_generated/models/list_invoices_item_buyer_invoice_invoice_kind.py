from typing import Literal, Set, cast

ListInvoicesItemBuyerInvoiceInvoiceKind = Literal["prepayment"]

LIST_INVOICES_ITEM_BUYER_INVOICE_INVOICE_KIND_VALUES: Set[
    ListInvoicesItemBuyerInvoiceInvoiceKind
] = {
    "prepayment",
}


def check_list_invoices_item_buyer_invoice_invoice_kind(
    value: str,
) -> ListInvoicesItemBuyerInvoiceInvoiceKind:
    if value in LIST_INVOICES_ITEM_BUYER_INVOICE_INVOICE_KIND_VALUES:
        return cast(ListInvoicesItemBuyerInvoiceInvoiceKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_BUYER_INVOICE_INVOICE_KIND_VALUES!r}"
    )
