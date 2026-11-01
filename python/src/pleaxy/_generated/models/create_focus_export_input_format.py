from typing import Literal, Set, cast

CreateFocusExportInputFormat = Literal["csv", "parquet"]

CREATE_FOCUS_EXPORT_INPUT_FORMAT_VALUES: Set[CreateFocusExportInputFormat] = {
    "csv",
    "parquet",
}


def check_create_focus_export_input_format(value: str) -> CreateFocusExportInputFormat:
    if value in CREATE_FOCUS_EXPORT_INPUT_FORMAT_VALUES:
        return cast(CreateFocusExportInputFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_FOCUS_EXPORT_INPUT_FORMAT_VALUES!r}"
    )
