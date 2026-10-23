from typing import Literal, Set, cast

LineItemInputLineType = Literal["goods", "service"]

LINE_ITEM_INPUT_LINE_TYPE_VALUES: Set[LineItemInputLineType] = {
    "goods",
    "service",
}


def check_line_item_input_line_type(value: str) -> LineItemInputLineType:
    if value in LINE_ITEM_INPUT_LINE_TYPE_VALUES:
        return cast(LineItemInputLineType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LINE_ITEM_INPUT_LINE_TYPE_VALUES!r}"
    )
