from typing import Literal, Set, cast

OrderConfirmationOperation = Literal["new", "update"]

ORDER_CONFIRMATION_OPERATION_VALUES: Set[OrderConfirmationOperation] = {
    "new",
    "update",
}


def check_order_confirmation_operation(value: str) -> OrderConfirmationOperation:
    if value in ORDER_CONFIRMATION_OPERATION_VALUES:
        return cast(OrderConfirmationOperation, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ORDER_CONFIRMATION_OPERATION_VALUES!r}"
    )
