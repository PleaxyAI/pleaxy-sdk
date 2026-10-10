from typing import Literal, Set, cast

StripePaymentStatusQuoteCurrency = Literal["USD"]

STRIPE_PAYMENT_STATUS_QUOTE_CURRENCY_VALUES: Set[StripePaymentStatusQuoteCurrency] = {
    "USD",
}


def check_stripe_payment_status_quote_currency(
    value: str,
) -> StripePaymentStatusQuoteCurrency:
    if value in STRIPE_PAYMENT_STATUS_QUOTE_CURRENCY_VALUES:
        return cast(StripePaymentStatusQuoteCurrency, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STRIPE_PAYMENT_STATUS_QUOTE_CURRENCY_VALUES!r}"
    )
