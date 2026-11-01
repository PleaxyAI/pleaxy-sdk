from typing import Literal, Set, cast

FocusExportInclude = Literal["all", "non_cloud"]

FOCUS_EXPORT_INCLUDE_VALUES: Set[FocusExportInclude] = {
    "all",
    "non_cloud",
}


def check_focus_export_include(value: str) -> FocusExportInclude:
    if value in FOCUS_EXPORT_INCLUDE_VALUES:
        return cast(FocusExportInclude, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FOCUS_EXPORT_INCLUDE_VALUES!r}"
    )
