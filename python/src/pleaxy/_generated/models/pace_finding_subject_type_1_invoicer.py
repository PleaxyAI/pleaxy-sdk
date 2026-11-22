from typing import Literal, Set, cast

PaceFindingSubjectType1Invoicer = Literal[
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

PACE_FINDING_SUBJECT_TYPE_1_INVOICER_VALUES: Set[PaceFindingSubjectType1Invoicer] = {
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


def check_pace_finding_subject_type_1_invoicer(
    value: str,
) -> PaceFindingSubjectType1Invoicer:
    if value in PACE_FINDING_SUBJECT_TYPE_1_INVOICER_VALUES:
        return cast(PaceFindingSubjectType1Invoicer, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PACE_FINDING_SUBJECT_TYPE_1_INVOICER_VALUES!r}"
    )
