from typing import Literal, Set, cast

FocusSourceViewProvider = Literal["aws", "azure", "gcp", "oci"]

FOCUS_SOURCE_VIEW_PROVIDER_VALUES: Set[FocusSourceViewProvider] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_focus_source_view_provider(value: str) -> FocusSourceViewProvider:
    if value in FOCUS_SOURCE_VIEW_PROVIDER_VALUES:
        return cast(FocusSourceViewProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FOCUS_SOURCE_VIEW_PROVIDER_VALUES!r}"
    )
