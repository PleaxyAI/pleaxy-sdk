from typing import Literal, Set, cast

StoreOrderConfirmationLinesItemStatus = Literal[
    "accept", "backordered", "detail", "reject"
]

STORE_ORDER_CONFIRMATION_LINES_ITEM_STATUS_VALUES: Set[
    StoreOrderConfirmationLinesItemStatus
] = {
    "accept",
    "backordered",
    "detail",
    "reject",
}


def check_store_order_confirmation_lines_item_status(
    value: str,
) -> StoreOrderConfirmationLinesItemStatus:
    if value in STORE_ORDER_CONFIRMATION_LINES_ITEM_STATUS_VALUES:
        return cast(StoreOrderConfirmationLinesItemStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STORE_ORDER_CONFIRMATION_LINES_ITEM_STATUS_VALUES!r}"
    )
