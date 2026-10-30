from typing import Literal, Set, cast

AiSpendLimitEnforcement = Literal["alert", "deny"]

AI_SPEND_LIMIT_ENFORCEMENT_VALUES: Set[AiSpendLimitEnforcement] = {
    "alert",
    "deny",
}


def check_ai_spend_limit_enforcement(value: str) -> AiSpendLimitEnforcement:
    if value in AI_SPEND_LIMIT_ENFORCEMENT_VALUES:
        return cast(AiSpendLimitEnforcement, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_SPEND_LIMIT_ENFORCEMENT_VALUES!r}"
    )
