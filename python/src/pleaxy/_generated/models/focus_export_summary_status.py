from typing import Literal, Set, cast

FocusExportSummaryStatus = Literal["ready"]

FOCUS_EXPORT_SUMMARY_STATUS_VALUES: Set[FocusExportSummaryStatus] = {
    "ready",
}


def check_focus_export_summary_status(value: str) -> FocusExportSummaryStatus:
    if value in FOCUS_EXPORT_SUMMARY_STATUS_VALUES:
        return cast(FocusExportSummaryStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FOCUS_EXPORT_SUMMARY_STATUS_VALUES!r}"
    )
