from typing import Literal, Set, cast

CreateShipNoticeInputStatus = Literal["canceled", "planned", "shipped"]

CREATE_SHIP_NOTICE_INPUT_STATUS_VALUES: Set[CreateShipNoticeInputStatus] = {
    "canceled",
    "planned",
    "shipped",
}


def check_create_ship_notice_input_status(value: str) -> CreateShipNoticeInputStatus:
    if value in CREATE_SHIP_NOTICE_INPUT_STATUS_VALUES:
        return cast(CreateShipNoticeInputStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_SHIP_NOTICE_INPUT_STATUS_VALUES!r}"
    )
