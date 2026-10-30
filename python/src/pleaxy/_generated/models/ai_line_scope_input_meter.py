from typing import Literal, Set, cast

AiLineScopeInputMeter = Literal[
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
    "seats",
]

AI_LINE_SCOPE_INPUT_METER_VALUES: Set[AiLineScopeInputMeter] = {
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
    "seats",
}


def check_ai_line_scope_input_meter(value: str) -> AiLineScopeInputMeter:
    if value in AI_LINE_SCOPE_INPUT_METER_VALUES:
        return cast(AiLineScopeInputMeter, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_LINE_SCOPE_INPUT_METER_VALUES!r}"
    )
