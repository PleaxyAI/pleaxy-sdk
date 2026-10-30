from typing import Literal, Set, cast

InvoiceAiLineInputMeter = Literal[
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

INVOICE_AI_LINE_INPUT_METER_VALUES: Set[InvoiceAiLineInputMeter] = {
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


def check_invoice_ai_line_input_meter(value: str) -> InvoiceAiLineInputMeter:
    if value in INVOICE_AI_LINE_INPUT_METER_VALUES:
        return cast(InvoiceAiLineInputMeter, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_AI_LINE_INPUT_METER_VALUES!r}"
    )
