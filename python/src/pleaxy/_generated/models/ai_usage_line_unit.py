from typing import Literal, Set, cast

AiUsageLineUnit = Literal[
    "1M_tokens",
    "gpu_hours",
    "images",
    "model_unit_hours",
    "ptu_hours",
    "requests",
    "seconds",
    "tokens",
    "units",
]

AI_USAGE_LINE_UNIT_VALUES: Set[AiUsageLineUnit] = {
    "1M_tokens",
    "gpu_hours",
    "images",
    "model_unit_hours",
    "ptu_hours",
    "requests",
    "seconds",
    "tokens",
    "units",
}


def check_ai_usage_line_unit(value: str) -> AiUsageLineUnit:
    if value in AI_USAGE_LINE_UNIT_VALUES:
        return cast(AiUsageLineUnit, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_USAGE_LINE_UNIT_VALUES!r}"
    )
