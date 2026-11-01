from typing import Literal, Set, cast

FocusExportVersion = Literal["1.2", "1.4"]

FOCUS_EXPORT_VERSION_VALUES: Set[FocusExportVersion] = {
    "1.2",
    "1.4",
}


def check_focus_export_version(value: str) -> FocusExportVersion:
    if value in FOCUS_EXPORT_VERSION_VALUES:
        return cast(FocusExportVersion, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FOCUS_EXPORT_VERSION_VALUES!r}"
    )
