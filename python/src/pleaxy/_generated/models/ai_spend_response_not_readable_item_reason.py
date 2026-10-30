from typing import Literal, Set, cast

AiSpendResponseNotReadableItemReason = Literal["needs_current_cost", "not_synced_yet"]

AI_SPEND_RESPONSE_NOT_READABLE_ITEM_REASON_VALUES: Set[
    AiSpendResponseNotReadableItemReason
] = {
    "needs_current_cost",
    "not_synced_yet",
}


def check_ai_spend_response_not_readable_item_reason(
    value: str,
) -> AiSpendResponseNotReadableItemReason:
    if value in AI_SPEND_RESPONSE_NOT_READABLE_ITEM_REASON_VALUES:
        return cast(AiSpendResponseNotReadableItemReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_SPEND_RESPONSE_NOT_READABLE_ITEM_REASON_VALUES!r}"
    )
