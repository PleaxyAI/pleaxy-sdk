from typing import Literal, Set, cast

AiUsageLineSource = Literal[
    "billing_export",
    "cost_explorer",
    "cost_management",
    "cost_report",
    "usage_api",
    "usage_report",
]

AI_USAGE_LINE_SOURCE_VALUES: Set[AiUsageLineSource] = {
    "billing_export",
    "cost_explorer",
    "cost_management",
    "cost_report",
    "usage_api",
    "usage_report",
}


def check_ai_usage_line_source(value: str) -> AiUsageLineSource:
    if value in AI_USAGE_LINE_SOURCE_VALUES:
        return cast(AiUsageLineSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_USAGE_LINE_SOURCE_VALUES!r}"
    )
