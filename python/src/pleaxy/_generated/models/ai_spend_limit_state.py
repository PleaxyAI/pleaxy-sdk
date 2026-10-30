from typing import Literal, Set, cast

AiSpendLimitState = Literal["failed", "removed", "set"]

AI_SPEND_LIMIT_STATE_VALUES: Set[AiSpendLimitState] = {
    "failed",
    "removed",
    "set",
}


def check_ai_spend_limit_state(value: str) -> AiSpendLimitState:
    if value in AI_SPEND_LIMIT_STATE_VALUES:
        return cast(AiSpendLimitState, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_SPEND_LIMIT_STATE_VALUES!r}"
    )
