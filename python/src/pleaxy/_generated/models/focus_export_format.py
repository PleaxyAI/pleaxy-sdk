from typing import Literal, Set, cast

FocusExportFormat = Literal["csv", "parquet"]

FOCUS_EXPORT_FORMAT_VALUES: Set[FocusExportFormat] = {
    "csv",
    "parquet",
}


def check_focus_export_format(value: str) -> FocusExportFormat:
    if value in FOCUS_EXPORT_FORMAT_VALUES:
        return cast(FocusExportFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FOCUS_EXPORT_FORMAT_VALUES!r}"
    )
