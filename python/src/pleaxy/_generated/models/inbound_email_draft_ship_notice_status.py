from typing import Literal, Set, cast

InboundEmailDraftShipNoticeStatus = Literal["canceled", "planned", "shipped"]

INBOUND_EMAIL_DRAFT_SHIP_NOTICE_STATUS_VALUES: Set[
    InboundEmailDraftShipNoticeStatus
] = {
    "canceled",
    "planned",
    "shipped",
}


def check_inbound_email_draft_ship_notice_status(
    value: str,
) -> InboundEmailDraftShipNoticeStatus:
    if value in INBOUND_EMAIL_DRAFT_SHIP_NOTICE_STATUS_VALUES:
        return cast(InboundEmailDraftShipNoticeStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INBOUND_EMAIL_DRAFT_SHIP_NOTICE_STATUS_VALUES!r}"
    )
