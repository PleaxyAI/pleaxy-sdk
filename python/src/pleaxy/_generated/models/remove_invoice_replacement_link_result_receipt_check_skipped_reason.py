from typing import Literal, Set, cast

RemoveInvoiceReplacementLinkResultReceiptCheckSkippedReason = Literal["small_invoice"]

REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_RECEIPT_CHECK_SKIPPED_REASON_VALUES: Set[
    RemoveInvoiceReplacementLinkResultReceiptCheckSkippedReason
] = {
    "small_invoice",
}


def check_remove_invoice_replacement_link_result_receipt_check_skipped_reason(
    value: str,
) -> RemoveInvoiceReplacementLinkResultReceiptCheckSkippedReason:
    if (
        value
        in REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_RECEIPT_CHECK_SKIPPED_REASON_VALUES
    ):
        return cast(RemoveInvoiceReplacementLinkResultReceiptCheckSkippedReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_RECEIPT_CHECK_SKIPPED_REASON_VALUES!r}"
    )
