from typing import Literal, Set, cast

AiDraftOrdersResultSkippedItemReason = Literal[
    "already_drafted", "no_forecast", "no_supplier", "no_usage"
]

AI_DRAFT_ORDERS_RESULT_SKIPPED_ITEM_REASON_VALUES: Set[
    AiDraftOrdersResultSkippedItemReason
] = {
    "already_drafted",
    "no_forecast",
    "no_supplier",
    "no_usage",
}


def check_ai_draft_orders_result_skipped_item_reason(
    value: str,
) -> AiDraftOrdersResultSkippedItemReason:
    if value in AI_DRAFT_ORDERS_RESULT_SKIPPED_ITEM_REASON_VALUES:
        return cast(AiDraftOrdersResultSkippedItemReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_DRAFT_ORDERS_RESULT_SKIPPED_ITEM_REASON_VALUES!r}"
    )
