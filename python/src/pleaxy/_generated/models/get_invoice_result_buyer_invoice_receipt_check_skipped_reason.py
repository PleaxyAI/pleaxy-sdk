from typing import Literal, Set, cast

GetInvoiceResultBuyerInvoiceReceiptCheckSkippedReason = Literal["small_invoice"]

GET_INVOICE_RESULT_BUYER_INVOICE_RECEIPT_CHECK_SKIPPED_REASON_VALUES: Set[
    GetInvoiceResultBuyerInvoiceReceiptCheckSkippedReason
] = {
    "small_invoice",
}


def check_get_invoice_result_buyer_invoice_receipt_check_skipped_reason(
    value: str,
) -> GetInvoiceResultBuyerInvoiceReceiptCheckSkippedReason:
    if value in GET_INVOICE_RESULT_BUYER_INVOICE_RECEIPT_CHECK_SKIPPED_REASON_VALUES:
        return cast(GetInvoiceResultBuyerInvoiceReceiptCheckSkippedReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_BUYER_INVOICE_RECEIPT_CHECK_SKIPPED_REASON_VALUES!r}"
    )
