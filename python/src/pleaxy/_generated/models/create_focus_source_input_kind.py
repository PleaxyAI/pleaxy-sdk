from typing import Literal, Set, cast

CreateFocusSourceInputKind = Literal[
    "aws_s3", "azure_blob", "gcp_bigquery", "oci", "s3_compatible"
]

CREATE_FOCUS_SOURCE_INPUT_KIND_VALUES: Set[CreateFocusSourceInputKind] = {
    "aws_s3",
    "azure_blob",
    "gcp_bigquery",
    "oci",
    "s3_compatible",
}


def check_create_focus_source_input_kind(value: str) -> CreateFocusSourceInputKind:
    if value in CREATE_FOCUS_SOURCE_INPUT_KIND_VALUES:
        return cast(CreateFocusSourceInputKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_FOCUS_SOURCE_INPUT_KIND_VALUES!r}"
    )
