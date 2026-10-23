from typing import Literal, Set, cast

CreateInvoiceResultBuyerInvoiceReceiptCheckSkippedReason = Literal["small_invoice"]

CREATE_INVOICE_RESULT_BUYER_INVOICE_RECEIPT_CHECK_SKIPPED_REASON_VALUES: Set[
    CreateInvoiceResultBuyerInvoiceReceiptCheckSkippedReason
] = {
    "small_invoice",
}


def check_create_invoice_result_buyer_invoice_receipt_check_skipped_reason(
    value: str,
) -> CreateInvoiceResultBuyerInvoiceReceiptCheckSkippedReason:
    if value in CREATE_INVOICE_RESULT_BUYER_INVOICE_RECEIPT_CHECK_SKIPPED_REASON_VALUES:
        return cast(CreateInvoiceResultBuyerInvoiceReceiptCheckSkippedReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_BUYER_INVOICE_RECEIPT_CHECK_SKIPPED_REASON_VALUES!r}"
    )
