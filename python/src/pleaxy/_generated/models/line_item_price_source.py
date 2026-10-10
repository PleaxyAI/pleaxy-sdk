from typing import Literal, Set, cast

LineItemPriceSource = Literal["contract", "list", "manual"]

LINE_ITEM_PRICE_SOURCE_VALUES: Set[LineItemPriceSource] = {
    "contract",
    "list",
    "manual",
}


def check_line_item_price_source(value: str) -> LineItemPriceSource:
    if value in LINE_ITEM_PRICE_SOURCE_VALUES:
        return cast(LineItemPriceSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LINE_ITEM_PRICE_SOURCE_VALUES!r}"
    )
