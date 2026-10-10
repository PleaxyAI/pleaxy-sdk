from typing import Literal, Set, cast

LineItemScopeType = Literal["account", "custom", "service", "sku"]

LINE_ITEM_SCOPE_TYPE_VALUES: Set[LineItemScopeType] = {
    "account",
    "custom",
    "service",
    "sku",
}


def check_line_item_scope_type(value: str) -> LineItemScopeType:
    if value in LINE_ITEM_SCOPE_TYPE_VALUES:
        return cast(LineItemScopeType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LINE_ITEM_SCOPE_TYPE_VALUES!r}"
    )
