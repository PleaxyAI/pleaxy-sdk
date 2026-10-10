from typing import Literal, Set, cast

FeedValidationResultInvoiceWithdrawnPaymentType0Status = Literal["recorded"]

FEED_VALIDATION_RESULT_INVOICE_WITHDRAWN_PAYMENT_TYPE_0_STATUS_VALUES: Set[
    FeedValidationResultInvoiceWithdrawnPaymentType0Status
] = {
    "recorded",
}


def check_feed_validation_result_invoice_withdrawn_payment_type_0_status(
    value: str,
) -> FeedValidationResultInvoiceWithdrawnPaymentType0Status:
    if value in FEED_VALIDATION_RESULT_INVOICE_WITHDRAWN_PAYMENT_TYPE_0_STATUS_VALUES:
        return cast(FeedValidationResultInvoiceWithdrawnPaymentType0Status, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FEED_VALIDATION_RESULT_INVOICE_WITHDRAWN_PAYMENT_TYPE_0_STATUS_VALUES!r}"
    )
