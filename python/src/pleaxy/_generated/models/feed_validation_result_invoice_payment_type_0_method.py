from typing import Literal, Set, cast

FeedValidationResultInvoicePaymentType0Method = Literal[
    "ach", "card", "check", "credit", "other", "wire"
]

FEED_VALIDATION_RESULT_INVOICE_PAYMENT_TYPE_0_METHOD_VALUES: Set[
    FeedValidationResultInvoicePaymentType0Method
] = {
    "ach",
    "card",
    "check",
    "credit",
    "other",
    "wire",
}


def check_feed_validation_result_invoice_payment_type_0_method(
    value: str,
) -> FeedValidationResultInvoicePaymentType0Method:
    if value in FEED_VALIDATION_RESULT_INVOICE_PAYMENT_TYPE_0_METHOD_VALUES:
        return cast(FeedValidationResultInvoicePaymentType0Method, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FEED_VALIDATION_RESULT_INVOICE_PAYMENT_TYPE_0_METHOD_VALUES!r}"
    )
