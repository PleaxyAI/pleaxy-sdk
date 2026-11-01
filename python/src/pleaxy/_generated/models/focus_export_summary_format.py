from typing import Literal, Set, cast

FocusExportSummaryFormat = Literal["csv", "parquet"]

FOCUS_EXPORT_SUMMARY_FORMAT_VALUES: Set[FocusExportSummaryFormat] = {
    "csv",
    "parquet",
}


def check_focus_export_summary_format(value: str) -> FocusExportSummaryFormat:
    if value in FOCUS_EXPORT_SUMMARY_FORMAT_VALUES:
        return cast(FocusExportSummaryFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FOCUS_EXPORT_SUMMARY_FORMAT_VALUES!r}"
    )
