from typing import Literal, Set, cast

SpikeFindingSubjectType1Invoicer = Literal[
    "anthropic",
    "aws",
    "azure",
    "cohere",
    "coreweave",
    "crusoe",
    "cursor",
    "databricks",
    "gcp",
    "github",
    "lambda",
    "microsoft",
    "mistral",
    "nebius",
    "oci",
    "openai",
    "openrouter",
    "slack",
    "snowflake",
    "xai",
    "zoom",
]

SPIKE_FINDING_SUBJECT_TYPE_1_INVOICER_VALUES: Set[SpikeFindingSubjectType1Invoicer] = {
    "anthropic",
    "aws",
    "azure",
    "cohere",
    "coreweave",
    "crusoe",
    "cursor",
    "databricks",
    "gcp",
    "github",
    "lambda",
    "microsoft",
    "mistral",
    "nebius",
    "oci",
    "openai",
    "openrouter",
    "slack",
    "snowflake",
    "xai",
    "zoom",
}


def check_spike_finding_subject_type_1_invoicer(
    value: str,
) -> SpikeFindingSubjectType1Invoicer:
    if value in SPIKE_FINDING_SUBJECT_TYPE_1_INVOICER_VALUES:
        return cast(SpikeFindingSubjectType1Invoicer, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SPIKE_FINDING_SUBJECT_TYPE_1_INVOICER_VALUES!r}"
    )
