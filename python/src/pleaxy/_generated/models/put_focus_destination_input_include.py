from typing import Literal, Set, cast

PutFocusDestinationInputInclude = Literal["all", "non_cloud"]

PUT_FOCUS_DESTINATION_INPUT_INCLUDE_VALUES: Set[PutFocusDestinationInputInclude] = {
    "all",
    "non_cloud",
}


def check_put_focus_destination_input_include(
    value: str,
) -> PutFocusDestinationInputInclude:
    if value in PUT_FOCUS_DESTINATION_INPUT_INCLUDE_VALUES:
        return cast(PutFocusDestinationInputInclude, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUT_FOCUS_DESTINATION_INPUT_INCLUDE_VALUES!r}"
    )
