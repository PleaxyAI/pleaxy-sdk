from typing import Literal, Set, cast

ListInvoicesItemBuyerInvoiceMatchBasis = Literal["no_po_history", "purchase_order"]

LIST_INVOICES_ITEM_BUYER_INVOICE_MATCH_BASIS_VALUES: Set[
    ListInvoicesItemBuyerInvoiceMatchBasis
] = {
    "no_po_history",
    "purchase_order",
}


def check_list_invoices_item_buyer_invoice_match_basis(
    value: str,
) -> ListInvoicesItemBuyerInvoiceMatchBasis:
    if value in LIST_INVOICES_ITEM_BUYER_INVOICE_MATCH_BASIS_VALUES:
        return cast(ListInvoicesItemBuyerInvoiceMatchBasis, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_BUYER_INVOICE_MATCH_BASIS_VALUES!r}"
    )
