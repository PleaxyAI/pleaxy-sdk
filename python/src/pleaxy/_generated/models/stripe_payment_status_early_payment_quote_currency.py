from typing import Literal, Set, cast

StripePaymentStatusEarlyPaymentQuoteCurrency = Literal["USD"]

STRIPE_PAYMENT_STATUS_EARLY_PAYMENT_QUOTE_CURRENCY_VALUES: Set[
    StripePaymentStatusEarlyPaymentQuoteCurrency
] = {
    "USD",
}


def check_stripe_payment_status_early_payment_quote_currency(
    value: str,
) -> StripePaymentStatusEarlyPaymentQuoteCurrency:
    if value in STRIPE_PAYMENT_STATUS_EARLY_PAYMENT_QUOTE_CURRENCY_VALUES:
        return cast(StripePaymentStatusEarlyPaymentQuoteCurrency, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STRIPE_PAYMENT_STATUS_EARLY_PAYMENT_QUOTE_CURRENCY_VALUES!r}"
    )
