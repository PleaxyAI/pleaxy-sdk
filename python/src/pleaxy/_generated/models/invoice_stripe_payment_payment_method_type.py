from typing import Literal, Set, cast

InvoiceStripePaymentPaymentMethodType = Literal["card", "us_bank_account"]

INVOICE_STRIPE_PAYMENT_PAYMENT_METHOD_TYPE_VALUES: Set[
    InvoiceStripePaymentPaymentMethodType
] = {
    "card",
    "us_bank_account",
}


def check_invoice_stripe_payment_payment_method_type(
    value: str,
) -> InvoiceStripePaymentPaymentMethodType:
    if value in INVOICE_STRIPE_PAYMENT_PAYMENT_METHOD_TYPE_VALUES:
        return cast(InvoiceStripePaymentPaymentMethodType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_STRIPE_PAYMENT_PAYMENT_METHOD_TYPE_VALUES!r}"
    )
