from typing import Literal, Set, cast

AiPoLineSuggestionUnit = Literal[
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

AI_PO_LINE_SUGGESTION_UNIT_VALUES: Set[AiPoLineSuggestionUnit] = {
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


def check_ai_po_line_suggestion_unit(value: str) -> AiPoLineSuggestionUnit:
    if value in AI_PO_LINE_SUGGESTION_UNIT_VALUES:
        return cast(AiPoLineSuggestionUnit, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_PO_LINE_SUGGESTION_UNIT_VALUES!r}"
    )
