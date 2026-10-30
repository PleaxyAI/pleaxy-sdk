from typing import Literal, Set, cast

AiRateCardEntryUnit = Literal[
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

AI_RATE_CARD_ENTRY_UNIT_VALUES: Set[AiRateCardEntryUnit] = {
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


def check_ai_rate_card_entry_unit(value: str) -> AiRateCardEntryUnit:
    if value in AI_RATE_CARD_ENTRY_UNIT_VALUES:
        return cast(AiRateCardEntryUnit, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_RATE_CARD_ENTRY_UNIT_VALUES!r}"
    )
