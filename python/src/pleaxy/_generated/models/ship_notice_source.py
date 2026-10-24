from typing import Literal, Set, cast

ShipNoticeSource = Literal["api", "cxml", "email", "portal"]

SHIP_NOTICE_SOURCE_VALUES: Set[ShipNoticeSource] = {
    "api",
    "cxml",
    "email",
    "portal",
}


def check_ship_notice_source(value: str) -> ShipNoticeSource:
    if value in SHIP_NOTICE_SOURCE_VALUES:
        return cast(ShipNoticeSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SHIP_NOTICE_SOURCE_VALUES!r}"
    )
