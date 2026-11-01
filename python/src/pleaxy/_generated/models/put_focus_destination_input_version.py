from typing import Literal, Set, cast

PutFocusDestinationInputVersion = Literal["1.2", "1.4"]

PUT_FOCUS_DESTINATION_INPUT_VERSION_VALUES: Set[PutFocusDestinationInputVersion] = {
    "1.2",
    "1.4",
}


def check_put_focus_destination_input_version(
    value: str,
) -> PutFocusDestinationInputVersion:
    if value in PUT_FOCUS_DESTINATION_INPUT_VERSION_VALUES:
        return cast(PutFocusDestinationInputVersion, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUT_FOCUS_DESTINATION_INPUT_VERSION_VALUES!r}"
    )
