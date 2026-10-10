from typing import Literal, Set, cast

FeedValidationResultInvoicePaymentType0Status = Literal["recorded"]

FEED_VALIDATION_RESULT_INVOICE_PAYMENT_TYPE_0_STATUS_VALUES: Set[
    FeedValidationResultInvoicePaymentType0Status
] = {
    "recorded",
}


def check_feed_validation_result_invoice_payment_type_0_status(
    value: str,
) -> FeedValidationResultInvoicePaymentType0Status:
    if value in FEED_VALIDATION_RESULT_INVOICE_PAYMENT_TYPE_0_STATUS_VALUES:
        return cast(FeedValidationResultInvoicePaymentType0Status, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FEED_VALIDATION_RESULT_INVOICE_PAYMENT_TYPE_0_STATUS_VALUES!r}"
    )
