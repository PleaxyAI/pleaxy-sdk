from typing import Literal, Set, cast

FeedValidationResultInvoiceWithdrawnPaymentType1State = Literal[
    "processing", "succeeded"
]

FEED_VALIDATION_RESULT_INVOICE_WITHDRAWN_PAYMENT_TYPE_1_STATE_VALUES: Set[
    FeedValidationResultInvoiceWithdrawnPaymentType1State
] = {
    "processing",
    "succeeded",
}


def check_feed_validation_result_invoice_withdrawn_payment_type_1_state(
    value: str,
) -> FeedValidationResultInvoiceWithdrawnPaymentType1State:
    if value in FEED_VALIDATION_RESULT_INVOICE_WITHDRAWN_PAYMENT_TYPE_1_STATE_VALUES:
        return cast(FeedValidationResultInvoiceWithdrawnPaymentType1State, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FEED_VALIDATION_RESULT_INVOICE_WITHDRAWN_PAYMENT_TYPE_1_STATE_VALUES!r}"
    )
