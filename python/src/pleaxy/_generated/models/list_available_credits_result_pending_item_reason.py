from typing import Literal, Set, cast

ListAvailableCreditsResultPendingItemReason = Literal[
    "other", "price_adjustment", "rebate", "returned_goods", "service_credit"
]

LIST_AVAILABLE_CREDITS_RESULT_PENDING_ITEM_REASON_VALUES: Set[
    ListAvailableCreditsResultPendingItemReason
] = {
    "other",
    "price_adjustment",
    "rebate",
    "returned_goods",
    "service_credit",
}


def check_list_available_credits_result_pending_item_reason(
    value: str,
) -> ListAvailableCreditsResultPendingItemReason:
    if value in LIST_AVAILABLE_CREDITS_RESULT_PENDING_ITEM_REASON_VALUES:
        return cast(ListAvailableCreditsResultPendingItemReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_AVAILABLE_CREDITS_RESULT_PENDING_ITEM_REASON_VALUES!r}"
    )
