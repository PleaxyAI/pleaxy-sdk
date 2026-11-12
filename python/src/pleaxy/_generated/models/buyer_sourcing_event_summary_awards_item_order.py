from typing import Literal, Set, cast

BuyerSourcingEventSummaryAwardsItemOrder = Literal["draft", "none", "submit"]

BUYER_SOURCING_EVENT_SUMMARY_AWARDS_ITEM_ORDER_VALUES: Set[
    BuyerSourcingEventSummaryAwardsItemOrder
] = {
    "draft",
    "none",
    "submit",
}


def check_buyer_sourcing_event_summary_awards_item_order(
    value: str,
) -> BuyerSourcingEventSummaryAwardsItemOrder:
    if value in BUYER_SOURCING_EVENT_SUMMARY_AWARDS_ITEM_ORDER_VALUES:
        return cast(BuyerSourcingEventSummaryAwardsItemOrder, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BUYER_SOURCING_EVENT_SUMMARY_AWARDS_ITEM_ORDER_VALUES!r}"
    )
