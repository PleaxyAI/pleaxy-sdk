from typing import Literal, Set, cast

InvoiceLineItemAiMeter = Literal[
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

INVOICE_LINE_ITEM_AI_METER_VALUES: Set[InvoiceLineItemAiMeter] = {
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


def check_invoice_line_item_ai_meter(value: str) -> InvoiceLineItemAiMeter:
    if value in INVOICE_LINE_ITEM_AI_METER_VALUES:
        return cast(InvoiceLineItemAiMeter, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_LINE_ITEM_AI_METER_VALUES!r}"
    )
