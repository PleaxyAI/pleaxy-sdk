from typing import Literal, Set, cast

FeedValidationResultInvoiceWithdrawnPaymentType0Method = Literal[
    "ach", "card", "check", "other", "wire"
]

FEED_VALIDATION_RESULT_INVOICE_WITHDRAWN_PAYMENT_TYPE_0_METHOD_VALUES: Set[
    FeedValidationResultInvoiceWithdrawnPaymentType0Method
] = {
    "ach",
    "card",
    "check",
    "other",
    "wire",
}


def check_feed_validation_result_invoice_withdrawn_payment_type_0_method(
    value: str,
) -> FeedValidationResultInvoiceWithdrawnPaymentType0Method:
    if value in FEED_VALIDATION_RESULT_INVOICE_WITHDRAWN_PAYMENT_TYPE_0_METHOD_VALUES:
        return cast(FeedValidationResultInvoiceWithdrawnPaymentType0Method, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FEED_VALIDATION_RESULT_INVOICE_WITHDRAWN_PAYMENT_TYPE_0_METHOD_VALUES!r}"
    )
