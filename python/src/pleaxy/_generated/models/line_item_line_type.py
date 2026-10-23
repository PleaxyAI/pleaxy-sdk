from typing import Literal, Set, cast

LineItemLineType = Literal["goods", "service"]

LINE_ITEM_LINE_TYPE_VALUES: Set[LineItemLineType] = {
    "goods",
    "service",
}


def check_line_item_line_type(value: str) -> LineItemLineType:
    if value in LINE_ITEM_LINE_TYPE_VALUES:
        return cast(LineItemLineType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LINE_ITEM_LINE_TYPE_VALUES!r}"
    )
