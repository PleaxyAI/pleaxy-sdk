from typing import Literal, Set, cast

AiSpendLimitHistoryItemAction = Literal["failed", "raise", "remove", "set"]

AI_SPEND_LIMIT_HISTORY_ITEM_ACTION_VALUES: Set[AiSpendLimitHistoryItemAction] = {
    "failed",
    "raise",
    "remove",
    "set",
}


def check_ai_spend_limit_history_item_action(
    value: str,
) -> AiSpendLimitHistoryItemAction:
    if value in AI_SPEND_LIMIT_HISTORY_ITEM_ACTION_VALUES:
        return cast(AiSpendLimitHistoryItemAction, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_SPEND_LIMIT_HISTORY_ITEM_ACTION_VALUES!r}"
    )
