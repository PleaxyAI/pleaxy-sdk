from typing import Literal, Set, cast

FocusExportSummaryInclude = Literal["all", "non_cloud"]

FOCUS_EXPORT_SUMMARY_INCLUDE_VALUES: Set[FocusExportSummaryInclude] = {
    "all",
    "non_cloud",
}


def check_focus_export_summary_include(value: str) -> FocusExportSummaryInclude:
    if value in FOCUS_EXPORT_SUMMARY_INCLUDE_VALUES:
        return cast(FocusExportSummaryInclude, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FOCUS_EXPORT_SUMMARY_INCLUDE_VALUES!r}"
    )
