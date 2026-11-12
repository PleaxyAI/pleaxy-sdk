from typing import Literal, Set, cast

BuyerSourcingEventSummaryAwardOrder = Literal["draft", "none", "submit"]

BUYER_SOURCING_EVENT_SUMMARY_AWARD_ORDER_VALUES: Set[
    BuyerSourcingEventSummaryAwardOrder
] = {
    "draft",
    "none",
    "submit",
}


def check_buyer_sourcing_event_summary_award_order(
    value: str,
) -> BuyerSourcingEventSummaryAwardOrder:
    if value in BUYER_SOURCING_EVENT_SUMMARY_AWARD_ORDER_VALUES:
        return cast(BuyerSourcingEventSummaryAwardOrder, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BUYER_SOURCING_EVENT_SUMMARY_AWARD_ORDER_VALUES!r}"
    )
