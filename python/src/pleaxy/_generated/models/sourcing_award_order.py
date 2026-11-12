from typing import Literal, Set, cast

SourcingAwardOrder = Literal["draft", "none", "submit"]

SOURCING_AWARD_ORDER_VALUES: Set[SourcingAwardOrder] = {
    "draft",
    "none",
    "submit",
}


def check_sourcing_award_order(value: str) -> SourcingAwardOrder:
    if value in SOURCING_AWARD_ORDER_VALUES:
        return cast(SourcingAwardOrder, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SOURCING_AWARD_ORDER_VALUES!r}"
    )
