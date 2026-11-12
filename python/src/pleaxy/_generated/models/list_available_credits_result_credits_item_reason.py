from typing import Literal, Set, cast

ListAvailableCreditsResultCreditsItemReason = Literal[
    "other", "price_adjustment", "rebate", "returned_goods", "service_credit"
]

LIST_AVAILABLE_CREDITS_RESULT_CREDITS_ITEM_REASON_VALUES: Set[
    ListAvailableCreditsResultCreditsItemReason
] = {
    "other",
    "price_adjustment",
    "rebate",
    "returned_goods",
    "service_credit",
}


def check_list_available_credits_result_credits_item_reason(
    value: str,
) -> ListAvailableCreditsResultCreditsItemReason:
    if value in LIST_AVAILABLE_CREDITS_RESULT_CREDITS_ITEM_REASON_VALUES:
        return cast(ListAvailableCreditsResultCreditsItemReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_AVAILABLE_CREDITS_RESULT_CREDITS_ITEM_REASON_VALUES!r}"
    )
