from typing import Literal, Set, cast

OrderConfirmationSource = Literal["api", "cxml", "portal"]

ORDER_CONFIRMATION_SOURCE_VALUES: Set[OrderConfirmationSource] = {
    "api",
    "cxml",
    "portal",
}


def check_order_confirmation_source(value: str) -> OrderConfirmationSource:
    if value in ORDER_CONFIRMATION_SOURCE_VALUES:
        return cast(OrderConfirmationSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ORDER_CONFIRMATION_SOURCE_VALUES!r}"
    )
