from typing import Literal, Set, cast

PriceAmountInterval = Literal["month", "year"]

PRICE_AMOUNT_INTERVAL_VALUES: Set[PriceAmountInterval] = {
    "month",
    "year",
}


def check_price_amount_interval(value: str) -> PriceAmountInterval:
    if value in PRICE_AMOUNT_INTERVAL_VALUES:
        return cast(PriceAmountInterval, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRICE_AMOUNT_INTERVAL_VALUES!r}"
    )
