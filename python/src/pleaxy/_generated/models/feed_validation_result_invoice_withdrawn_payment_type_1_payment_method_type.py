from typing import Literal, Set, cast

FeedValidationResultInvoiceWithdrawnPaymentType1PaymentMethodType = Literal[
    "card", "us_bank_account"
]

FEED_VALIDATION_RESULT_INVOICE_WITHDRAWN_PAYMENT_TYPE_1_PAYMENT_METHOD_TYPE_VALUES: Set[
    FeedValidationResultInvoiceWithdrawnPaymentType1PaymentMethodType
] = {
    "card",
    "us_bank_account",
}


def check_feed_validation_result_invoice_withdrawn_payment_type_1_payment_method_type(
    value: str,
) -> FeedValidationResultInvoiceWithdrawnPaymentType1PaymentMethodType:
    if (
        value
        in FEED_VALIDATION_RESULT_INVOICE_WITHDRAWN_PAYMENT_TYPE_1_PAYMENT_METHOD_TYPE_VALUES
    ):
        return cast(
            FeedValidationResultInvoiceWithdrawnPaymentType1PaymentMethodType, value
        )
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FEED_VALIDATION_RESULT_INVOICE_WITHDRAWN_PAYMENT_TYPE_1_PAYMENT_METHOD_TYPE_VALUES!r}"
    )
