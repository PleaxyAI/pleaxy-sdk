from typing import Literal, Set, cast

InvoiceBuyerViewReceiptCheckSkippedReason = Literal["small_invoice"]

INVOICE_BUYER_VIEW_RECEIPT_CHECK_SKIPPED_REASON_VALUES: Set[
    InvoiceBuyerViewReceiptCheckSkippedReason
] = {
    "small_invoice",
}


def check_invoice_buyer_view_receipt_check_skipped_reason(
    value: str,
) -> InvoiceBuyerViewReceiptCheckSkippedReason:
    if value in INVOICE_BUYER_VIEW_RECEIPT_CHECK_SKIPPED_REASON_VALUES:
        return cast(InvoiceBuyerViewReceiptCheckSkippedReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_BUYER_VIEW_RECEIPT_CHECK_SKIPPED_REASON_VALUES!r}"
    )
