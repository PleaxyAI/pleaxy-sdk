from typing import Literal, Set, cast

BuyerSourcingEventViewStatus = Literal["awarded", "canceled", "closed", "draft", "open"]

BUYER_SOURCING_EVENT_VIEW_STATUS_VALUES: Set[BuyerSourcingEventViewStatus] = {
    "awarded",
    "canceled",
    "closed",
    "draft",
    "open",
}


def check_buyer_sourcing_event_view_status(value: str) -> BuyerSourcingEventViewStatus:
    if value in BUYER_SOURCING_EVENT_VIEW_STATUS_VALUES:
        return cast(BuyerSourcingEventViewStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BUYER_SOURCING_EVENT_VIEW_STATUS_VALUES!r}"
    )
