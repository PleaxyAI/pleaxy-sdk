from typing import Literal, Set, cast

PurchaseOrderStatus = Literal[
    "awaiting_fulfillment",
    "canceled",
    "closed",
    "draft",
    "expired",
    "invoiced",
    "paid",
    "pending_approval",
    "rejected",
]

PURCHASE_ORDER_STATUS_VALUES: Set[PurchaseOrderStatus] = {
    "awaiting_fulfillment",
    "canceled",
    "closed",
    "draft",
    "expired",
    "invoiced",
    "paid",
    "pending_approval",
    "rejected",
}


def check_purchase_order_status(value: str) -> PurchaseOrderStatus:
    if value in PURCHASE_ORDER_STATUS_VALUES:
        return cast(PurchaseOrderStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PURCHASE_ORDER_STATUS_VALUES!r}"
    )
