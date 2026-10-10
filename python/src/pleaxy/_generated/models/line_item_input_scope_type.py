from typing import Literal, Set, cast

LineItemInputScopeType = Literal["account", "custom", "service", "sku"]

LINE_ITEM_INPUT_SCOPE_TYPE_VALUES: Set[LineItemInputScopeType] = {
    "account",
    "custom",
    "service",
    "sku",
}


def check_line_item_input_scope_type(value: str) -> LineItemInputScopeType:
    if value in LINE_ITEM_INPUT_SCOPE_TYPE_VALUES:
        return cast(LineItemInputScopeType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LINE_ITEM_INPUT_SCOPE_TYPE_VALUES!r}"
    )
