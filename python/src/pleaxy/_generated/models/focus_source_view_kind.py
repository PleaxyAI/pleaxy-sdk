from typing import Literal, Set, cast

FocusSourceViewKind = Literal[
    "aws_s3", "azure_blob", "gcp_bigquery", "oci", "s3_compatible", "upload"
]

FOCUS_SOURCE_VIEW_KIND_VALUES: Set[FocusSourceViewKind] = {
    "aws_s3",
    "azure_blob",
    "gcp_bigquery",
    "oci",
    "s3_compatible",
    "upload",
}


def check_focus_source_view_kind(value: str) -> FocusSourceViewKind:
    if value in FOCUS_SOURCE_VIEW_KIND_VALUES:
        return cast(FocusSourceViewKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FOCUS_SOURCE_VIEW_KIND_VALUES!r}"
    )
