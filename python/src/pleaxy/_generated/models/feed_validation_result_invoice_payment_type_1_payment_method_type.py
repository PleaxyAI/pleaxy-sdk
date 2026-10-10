from typing import Literal, Set, cast

FeedValidationResultInvoicePaymentType1PaymentMethodType = Literal[
    "card", "us_bank_account"
]

FEED_VALIDATION_RESULT_INVOICE_PAYMENT_TYPE_1_PAYMENT_METHOD_TYPE_VALUES: Set[
    FeedValidationResultInvoicePaymentType1PaymentMethodType
] = {
    "card",
    "us_bank_account",
}


def check_feed_validation_result_invoice_payment_type_1_payment_method_type(
    value: str,
) -> FeedValidationResultInvoicePaymentType1PaymentMethodType:
    if (
        value
        in FEED_VALIDATION_RESULT_INVOICE_PAYMENT_TYPE_1_PAYMENT_METHOD_TYPE_VALUES
    ):
        return cast(FeedValidationResultInvoicePaymentType1PaymentMethodType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FEED_VALIDATION_RESULT_INVOICE_PAYMENT_TYPE_1_PAYMENT_METHOD_TYPE_VALUES!r}"
    )
