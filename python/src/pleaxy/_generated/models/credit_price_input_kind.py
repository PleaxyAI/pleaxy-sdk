from typing import Literal, Set, cast

CreditPriceInputKind = Literal["capacity", "commit", "on_demand"]

CREDIT_PRICE_INPUT_KIND_VALUES: Set[CreditPriceInputKind] = {
    "capacity",
    "commit",
    "on_demand",
}


def check_credit_price_input_kind(value: str) -> CreditPriceInputKind:
    if value in CREDIT_PRICE_INPUT_KIND_VALUES:
        return cast(CreditPriceInputKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREDIT_PRICE_INPUT_KIND_VALUES!r}"
    )
