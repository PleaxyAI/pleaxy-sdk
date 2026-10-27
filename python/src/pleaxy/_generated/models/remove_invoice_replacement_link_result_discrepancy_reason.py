from typing import Literal, Set, cast

RemoveInvoiceReplacementLinkResultDiscrepancyReason = Literal[
    "amount", "controls", "currency", "no_po_variance"
]

REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_DISCREPANCY_REASON_VALUES: Set[
    RemoveInvoiceReplacementLinkResultDiscrepancyReason
] = {
    "amount",
    "controls",
    "currency",
    "no_po_variance",
}


def check_remove_invoice_replacement_link_result_discrepancy_reason(
    value: str,
) -> RemoveInvoiceReplacementLinkResultDiscrepancyReason:
    if value in REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_DISCREPANCY_REASON_VALUES:
        return cast(RemoveInvoiceReplacementLinkResultDiscrepancyReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_DISCREPANCY_REASON_VALUES!r}"
    )
