from typing import Literal, Set, cast

OrderConfirmationLineStatus = Literal["accept", "backordered", "change", "reject"]

ORDER_CONFIRMATION_LINE_STATUS_VALUES: Set[OrderConfirmationLineStatus] = {
    "accept",
    "backordered",
    "change",
    "reject",
}


def check_order_confirmation_line_status(value: str) -> OrderConfirmationLineStatus:
    if value in ORDER_CONFIRMATION_LINE_STATUS_VALUES:
        return cast(OrderConfirmationLineStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ORDER_CONFIRMATION_LINE_STATUS_VALUES!r}"
    )
