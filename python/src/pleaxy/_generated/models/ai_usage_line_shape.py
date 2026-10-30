from typing import Literal, Set, cast

AiUsageLineShape = Literal["capacity", "credits", "seats", "tokens"]

AI_USAGE_LINE_SHAPE_VALUES: Set[AiUsageLineShape] = {
    "capacity",
    "credits",
    "seats",
    "tokens",
}


def check_ai_usage_line_shape(value: str) -> AiUsageLineShape:
    if value in AI_USAGE_LINE_SHAPE_VALUES:
        return cast(AiUsageLineShape, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_USAGE_LINE_SHAPE_VALUES!r}"
    )
