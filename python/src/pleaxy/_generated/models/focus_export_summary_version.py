from typing import Literal, Set, cast

FocusExportSummaryVersion = Literal["1.2", "1.4"]

FOCUS_EXPORT_SUMMARY_VERSION_VALUES: Set[FocusExportSummaryVersion] = {
    "1.2",
    "1.4",
}


def check_focus_export_summary_version(value: str) -> FocusExportSummaryVersion:
    if value in FOCUS_EXPORT_SUMMARY_VERSION_VALUES:
        return cast(FocusExportSummaryVersion, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FOCUS_EXPORT_SUMMARY_VERSION_VALUES!r}"
    )
