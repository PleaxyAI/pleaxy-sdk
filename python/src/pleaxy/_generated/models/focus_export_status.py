from typing import Literal, Set, cast

FocusExportStatus = Literal["ready"]

FOCUS_EXPORT_STATUS_VALUES: Set[FocusExportStatus] = {
    "ready",
}


def check_focus_export_status(value: str) -> FocusExportStatus:
    if value in FOCUS_EXPORT_STATUS_VALUES:
        return cast(FocusExportStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FOCUS_EXPORT_STATUS_VALUES!r}"
    )
