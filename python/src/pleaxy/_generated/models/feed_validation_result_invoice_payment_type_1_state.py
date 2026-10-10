from typing import Literal, Set, cast

FeedValidationResultInvoicePaymentType1State = Literal["processing", "succeeded"]

FEED_VALIDATION_RESULT_INVOICE_PAYMENT_TYPE_1_STATE_VALUES: Set[
    FeedValidationResultInvoicePaymentType1State
] = {
    "processing",
    "succeeded",
}


def check_feed_validation_result_invoice_payment_type_1_state(
    value: str,
) -> FeedValidationResultInvoicePaymentType1State:
    if value in FEED_VALIDATION_RESULT_INVOICE_PAYMENT_TYPE_1_STATE_VALUES:
        return cast(FeedValidationResultInvoicePaymentType1State, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FEED_VALIDATION_RESULT_INVOICE_PAYMENT_TYPE_1_STATE_VALUES!r}"
    )
