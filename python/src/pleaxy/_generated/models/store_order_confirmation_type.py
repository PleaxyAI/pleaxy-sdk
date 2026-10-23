from typing import Literal, Set, cast

StoreOrderConfirmationType = Literal["accepted", "partial", "rejected"]

STORE_ORDER_CONFIRMATION_TYPE_VALUES: Set[StoreOrderConfirmationType] = {
    "accepted",
    "partial",
    "rejected",
}


def check_store_order_confirmation_type(value: str) -> StoreOrderConfirmationType:
    if value in STORE_ORDER_CONFIRMATION_TYPE_VALUES:
        return cast(StoreOrderConfirmationType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STORE_ORDER_CONFIRMATION_TYPE_VALUES!r}"
    )
