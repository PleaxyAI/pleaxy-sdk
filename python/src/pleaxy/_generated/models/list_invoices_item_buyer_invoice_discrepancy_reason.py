from typing import Literal, Set, cast

ListInvoicesItemBuyerInvoiceDiscrepancyReason = Literal[
    "amount", "controls", "currency", "no_po_variance"
]

LIST_INVOICES_ITEM_BUYER_INVOICE_DISCREPANCY_REASON_VALUES: Set[
    ListInvoicesItemBuyerInvoiceDiscrepancyReason
] = {
    "amount",
    "controls",
    "currency",
    "no_po_variance",
}


def check_list_invoices_item_buyer_invoice_discrepancy_reason(
    value: str,
) -> ListInvoicesItemBuyerInvoiceDiscrepancyReason:
    if value in LIST_INVOICES_ITEM_BUYER_INVOICE_DISCREPANCY_REASON_VALUES:
        return cast(ListInvoicesItemBuyerInvoiceDiscrepancyReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_BUYER_INVOICE_DISCREPANCY_REASON_VALUES!r}"
    )
