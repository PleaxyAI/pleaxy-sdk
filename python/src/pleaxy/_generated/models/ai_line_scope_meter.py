from typing import Literal, Set, cast

AiLineScopeMeter = Literal[
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
    "prepaid_credit",
    "ptu_hours",
    "requests",
]

AI_LINE_SCOPE_METER_VALUES: Set[AiLineScopeMeter] = {
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
    "prepaid_credit",
    "ptu_hours",
    "requests",
}


def check_ai_line_scope_meter(value: str) -> AiLineScopeMeter:
    if value in AI_LINE_SCOPE_METER_VALUES:
        return cast(AiLineScopeMeter, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_LINE_SCOPE_METER_VALUES!r}"
    )
