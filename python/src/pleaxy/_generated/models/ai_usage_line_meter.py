from typing import Literal, Set, cast

AiUsageLineMeter = Literal[
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
    "seats",
]

AI_USAGE_LINE_METER_VALUES: Set[AiUsageLineMeter] = {
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
    "seats",
}


def check_ai_usage_line_meter(value: str) -> AiUsageLineMeter:
    if value in AI_USAGE_LINE_METER_VALUES:
        return cast(AiUsageLineMeter, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_USAGE_LINE_METER_VALUES!r}"
    )
