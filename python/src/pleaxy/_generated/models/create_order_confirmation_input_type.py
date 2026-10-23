from typing import Literal, Set, cast

CreateOrderConfirmationInputType = Literal["accept", "backordered", "detail", "reject"]

CREATE_ORDER_CONFIRMATION_INPUT_TYPE_VALUES: Set[CreateOrderConfirmationInputType] = {
    "accept",
    "backordered",
    "detail",
    "reject",
}


def check_create_order_confirmation_input_type(
    value: str,
) -> CreateOrderConfirmationInputType:
    if value in CREATE_ORDER_CONFIRMATION_INPUT_TYPE_VALUES:
        return cast(CreateOrderConfirmationInputType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_ORDER_CONFIRMATION_INPUT_TYPE_VALUES!r}"
    )
