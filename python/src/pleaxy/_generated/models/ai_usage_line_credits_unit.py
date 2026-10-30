from typing import Literal, Set, cast

AiUsageLineCreditsUnit = Literal["credits", "dbu"]

AI_USAGE_LINE_CREDITS_UNIT_VALUES: Set[AiUsageLineCreditsUnit] = {
    "credits",
    "dbu",
}


def check_ai_usage_line_credits_unit(value: str) -> AiUsageLineCreditsUnit:
    if value in AI_USAGE_LINE_CREDITS_UNIT_VALUES:
        return cast(AiUsageLineCreditsUnit, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_USAGE_LINE_CREDITS_UNIT_VALUES!r}"
    )
