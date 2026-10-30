from typing import Literal, Set, cast

AiRateCardEntryMeter = Literal[
    "audio_seconds",
    "batch_input_tokens",
    "batch_output_tokens",
    "cache_write_tokens",
    "cached_input_tokens",
    "cluster_hours",
    "embeddings_tokens",
    "gpu_hours",
    "images",
    "input_tokens",
    "model_units_hours",
    "other",
    "output_tokens",
    "ptu_hours",
    "requests",
]

AI_RATE_CARD_ENTRY_METER_VALUES: Set[AiRateCardEntryMeter] = {
    "audio_seconds",
    "batch_input_tokens",
    "batch_output_tokens",
    "cache_write_tokens",
    "cached_input_tokens",
    "cluster_hours",
    "embeddings_tokens",
    "gpu_hours",
    "images",
    "input_tokens",
    "model_units_hours",
    "other",
    "output_tokens",
    "ptu_hours",
    "requests",
}


def check_ai_rate_card_entry_meter(value: str) -> AiRateCardEntryMeter:
    if value in AI_RATE_CARD_ENTRY_METER_VALUES:
        return cast(AiRateCardEntryMeter, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_RATE_CARD_ENTRY_METER_VALUES!r}"
    )
