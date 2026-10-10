from typing import Literal, Set, cast

FeedValidationResultInvoiceWithdrawnPaymentType1Status = Literal["stripe"]

FEED_VALIDATION_RESULT_INVOICE_WITHDRAWN_PAYMENT_TYPE_1_STATUS_VALUES: Set[
    FeedValidationResultInvoiceWithdrawnPaymentType1Status
] = {
    "stripe",
}


def check_feed_validation_result_invoice_withdrawn_payment_type_1_status(
    value: str,
) -> FeedValidationResultInvoiceWithdrawnPaymentType1Status:
    if value in FEED_VALIDATION_RESULT_INVOICE_WITHDRAWN_PAYMENT_TYPE_1_STATUS_VALUES:
        return cast(FeedValidationResultInvoiceWithdrawnPaymentType1Status, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FEED_VALIDATION_RESULT_INVOICE_WITHDRAWN_PAYMENT_TYPE_1_STATUS_VALUES!r}"
    )
