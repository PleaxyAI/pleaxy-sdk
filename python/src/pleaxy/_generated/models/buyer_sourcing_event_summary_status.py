from typing import Literal, Set, cast

BuyerSourcingEventSummaryStatus = Literal[
    "awarded", "canceled", "closed", "draft", "open"
]

BUYER_SOURCING_EVENT_SUMMARY_STATUS_VALUES: Set[BuyerSourcingEventSummaryStatus] = {
    "awarded",
    "canceled",
    "closed",
    "draft",
    "open",
}


def check_buyer_sourcing_event_summary_status(
    value: str,
) -> BuyerSourcingEventSummaryStatus:
    if value in BUYER_SOURCING_EVENT_SUMMARY_STATUS_VALUES:
        return cast(BuyerSourcingEventSummaryStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BUYER_SOURCING_EVENT_SUMMARY_STATUS_VALUES!r}"
    )
