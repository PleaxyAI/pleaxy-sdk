from typing import Literal, Set, cast

EarlyPaymentDiscountTakenSource = Literal["supplier_offer"]

EARLY_PAYMENT_DISCOUNT_TAKEN_SOURCE_VALUES: Set[EarlyPaymentDiscountTakenSource] = {
    "supplier_offer",
}


def check_early_payment_discount_taken_source(
    value: str,
) -> EarlyPaymentDiscountTakenSource:
    if value in EARLY_PAYMENT_DISCOUNT_TAKEN_SOURCE_VALUES:
        return cast(EarlyPaymentDiscountTakenSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {EARLY_PAYMENT_DISCOUNT_TAKEN_SOURCE_VALUES!r}"
    )
