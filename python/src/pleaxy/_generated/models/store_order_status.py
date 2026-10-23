from typing import Literal, Set, cast

StoreOrderStatus = Literal[
    "cancelled",
    "confirmed",
    "expired",
    "failed",
    "manual",
    "partial",
    "queued",
    "refused",
    "retrying",
    "sending",
    "sent",
]

STORE_ORDER_STATUS_VALUES: Set[StoreOrderStatus] = {
    "cancelled",
    "confirmed",
    "expired",
    "failed",
    "manual",
    "partial",
    "queued",
    "refused",
    "retrying",
    "sending",
    "sent",
}


def check_store_order_status(value: str) -> StoreOrderStatus:
    if value in STORE_ORDER_STATUS_VALUES:
        return cast(StoreOrderStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STORE_ORDER_STATUS_VALUES!r}"
    )
