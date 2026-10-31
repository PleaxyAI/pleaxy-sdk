from typing import Literal, Set, cast

DraftAiOrdersInputScope = Literal["account", "ai"]

DRAFT_AI_ORDERS_INPUT_SCOPE_VALUES: Set[DraftAiOrdersInputScope] = {
    "account",
    "ai",
}


def check_draft_ai_orders_input_scope(value: str) -> DraftAiOrdersInputScope:
    if value in DRAFT_AI_ORDERS_INPUT_SCOPE_VALUES:
        return cast(DraftAiOrdersInputScope, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DRAFT_AI_ORDERS_INPUT_SCOPE_VALUES!r}"
    )
