from typing import Literal, Set, cast

AiDraftOrdersResultScope = Literal["account", "ai"]

AI_DRAFT_ORDERS_RESULT_SCOPE_VALUES: Set[AiDraftOrdersResultScope] = {
    "account",
    "ai",
}


def check_ai_draft_orders_result_scope(value: str) -> AiDraftOrdersResultScope:
    if value in AI_DRAFT_ORDERS_RESULT_SCOPE_VALUES:
        return cast(AiDraftOrdersResultScope, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_DRAFT_ORDERS_RESULT_SCOPE_VALUES!r}"
    )
