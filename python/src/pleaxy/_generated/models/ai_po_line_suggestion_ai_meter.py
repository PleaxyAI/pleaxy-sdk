from typing import Literal, Set, cast

AiPoLineSuggestionAiMeter = Literal[
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

AI_PO_LINE_SUGGESTION_AI_METER_VALUES: Set[AiPoLineSuggestionAiMeter] = {
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


def check_ai_po_line_suggestion_ai_meter(value: str) -> AiPoLineSuggestionAiMeter:
    if value in AI_PO_LINE_SUGGESTION_AI_METER_VALUES:
        return cast(AiPoLineSuggestionAiMeter, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_PO_LINE_SUGGESTION_AI_METER_VALUES!r}"
    )
