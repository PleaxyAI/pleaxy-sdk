from typing import Literal, Set, cast

FeedValidationResultInvoicePaymentType1Status = Literal["stripe"]

FEED_VALIDATION_RESULT_INVOICE_PAYMENT_TYPE_1_STATUS_VALUES: Set[
    FeedValidationResultInvoicePaymentType1Status
] = {
    "stripe",
}


def check_feed_validation_result_invoice_payment_type_1_status(
    value: str,
) -> FeedValidationResultInvoicePaymentType1Status:
    if value in FEED_VALIDATION_RESULT_INVOICE_PAYMENT_TYPE_1_STATUS_VALUES:
        return cast(FeedValidationResultInvoicePaymentType1Status, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FEED_VALIDATION_RESULT_INVOICE_PAYMENT_TYPE_1_STATUS_VALUES!r}"
    )
