from typing import Literal, Set, cast

CreateFocusExportInputInclude = Literal["all", "non_cloud"]

CREATE_FOCUS_EXPORT_INPUT_INCLUDE_VALUES: Set[CreateFocusExportInputInclude] = {
    "all",
    "non_cloud",
}


def check_create_focus_export_input_include(
    value: str,
) -> CreateFocusExportInputInclude:
    if value in CREATE_FOCUS_EXPORT_INPUT_INCLUDE_VALUES:
        return cast(CreateFocusExportInputInclude, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_FOCUS_EXPORT_INPUT_INCLUDE_VALUES!r}"
    )
