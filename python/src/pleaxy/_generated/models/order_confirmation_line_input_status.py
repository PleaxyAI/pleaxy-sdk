from typing import Literal, Set, cast

OrderConfirmationLineInputStatus = Literal["accept", "backordered", "change", "reject"]

ORDER_CONFIRMATION_LINE_INPUT_STATUS_VALUES: Set[OrderConfirmationLineInputStatus] = {
    "accept",
    "backordered",
    "change",
    "reject",
}


def check_order_confirmation_line_input_status(
    value: str,
) -> OrderConfirmationLineInputStatus:
    if value in ORDER_CONFIRMATION_LINE_INPUT_STATUS_VALUES:
        return cast(OrderConfirmationLineInputStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ORDER_CONFIRMATION_LINE_INPUT_STATUS_VALUES!r}"
    )
