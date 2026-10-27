from typing import Literal, Set, cast

InvoiceBuyerViewDiscrepancyReason = Literal[
    "amount", "controls", "currency", "no_po_variance"
]

INVOICE_BUYER_VIEW_DISCREPANCY_REASON_VALUES: Set[InvoiceBuyerViewDiscrepancyReason] = {
    "amount",
    "controls",
    "currency",
    "no_po_variance",
}


def check_invoice_buyer_view_discrepancy_reason(
    value: str,
) -> InvoiceBuyerViewDiscrepancyReason:
    if value in INVOICE_BUYER_VIEW_DISCREPANCY_REASON_VALUES:
        return cast(InvoiceBuyerViewDiscrepancyReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_BUYER_VIEW_DISCREPANCY_REASON_VALUES!r}"
    )
