from typing import Literal, Set, cast

AiSpendCheckResponseOutcome = Literal["fits", "no_budget", "no_po", "over"]

AI_SPEND_CHECK_RESPONSE_OUTCOME_VALUES: Set[AiSpendCheckResponseOutcome] = {
    "fits",
    "no_budget",
    "no_po",
    "over",
}


def check_ai_spend_check_response_outcome(value: str) -> AiSpendCheckResponseOutcome:
    if value in AI_SPEND_CHECK_RESPONSE_OUTCOME_VALUES:
        return cast(AiSpendCheckResponseOutcome, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_SPEND_CHECK_RESPONSE_OUTCOME_VALUES!r}"
    )
