from typing import Literal, Set, cast

CreateFocusExportInputVersion = Literal["1.2", "1.4"]

CREATE_FOCUS_EXPORT_INPUT_VERSION_VALUES: Set[CreateFocusExportInputVersion] = {
    "1.2",
    "1.4",
}


def check_create_focus_export_input_version(
    value: str,
) -> CreateFocusExportInputVersion:
    if value in CREATE_FOCUS_EXPORT_INPUT_VERSION_VALUES:
        return cast(CreateFocusExportInputVersion, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_FOCUS_EXPORT_INPUT_VERSION_VALUES!r}"
    )
