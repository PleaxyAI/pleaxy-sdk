from typing import Literal, Set, cast

AiUncoveredSpendReason = Literal["no_po", "over_po"]

AI_UNCOVERED_SPEND_REASON_VALUES: Set[AiUncoveredSpendReason] = {
    "no_po",
    "over_po",
}


def check_ai_uncovered_spend_reason(value: str) -> AiUncoveredSpendReason:
    if value in AI_UNCOVERED_SPEND_REASON_VALUES:
        return cast(AiUncoveredSpendReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_UNCOVERED_SPEND_REASON_VALUES!r}"
    )
