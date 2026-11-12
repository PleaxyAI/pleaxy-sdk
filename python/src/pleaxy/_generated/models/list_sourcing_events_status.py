from typing import Literal, Set, cast

ListSourcingEventsStatus = Literal["awarded", "canceled", "closed", "draft", "open"]

LIST_SOURCING_EVENTS_STATUS_VALUES: Set[ListSourcingEventsStatus] = {
    "awarded",
    "canceled",
    "closed",
    "draft",
    "open",
}


def check_list_sourcing_events_status(value: str) -> ListSourcingEventsStatus:
    if value in LIST_SOURCING_EVENTS_STATUS_VALUES:
        return cast(ListSourcingEventsStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_SOURCING_EVENTS_STATUS_VALUES!r}"
    )
