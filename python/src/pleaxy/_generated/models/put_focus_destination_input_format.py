from typing import Literal, Set, cast

PutFocusDestinationInputFormat = Literal["csv", "parquet"]

PUT_FOCUS_DESTINATION_INPUT_FORMAT_VALUES: Set[PutFocusDestinationInputFormat] = {
    "csv",
    "parquet",
}


def check_put_focus_destination_input_format(
    value: str,
) -> PutFocusDestinationInputFormat:
    if value in PUT_FOCUS_DESTINATION_INPUT_FORMAT_VALUES:
        return cast(PutFocusDestinationInputFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUT_FOCUS_DESTINATION_INPUT_FORMAT_VALUES!r}"
    )
