from typing import Literal, Set, cast

OrderConfirmationSubstituteLineType = Literal["goods", "service"]

ORDER_CONFIRMATION_SUBSTITUTE_LINE_TYPE_VALUES: Set[
    OrderConfirmationSubstituteLineType
] = {
    "goods",
    "service",
}


def check_order_confirmation_substitute_line_type(
    value: str,
) -> OrderConfirmationSubstituteLineType:
    if value in ORDER_CONFIRMATION_SUBSTITUTE_LINE_TYPE_VALUES:
        return cast(OrderConfirmationSubstituteLineType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ORDER_CONFIRMATION_SUBSTITUTE_LINE_TYPE_VALUES!r}"
    )
