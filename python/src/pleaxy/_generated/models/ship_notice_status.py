from typing import Literal, Set, cast

ShipNoticeStatus = Literal["canceled", "planned", "shipped"]

SHIP_NOTICE_STATUS_VALUES: Set[ShipNoticeStatus] = {
    "canceled",
    "planned",
    "shipped",
}


def check_ship_notice_status(value: str) -> ShipNoticeStatus:
    if value in SHIP_NOTICE_STATUS_VALUES:
        return cast(ShipNoticeStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SHIP_NOTICE_STATUS_VALUES!r}"
    )
