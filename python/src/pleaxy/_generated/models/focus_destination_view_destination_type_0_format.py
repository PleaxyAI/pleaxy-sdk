from typing import Literal, Set, cast

FocusDestinationViewDestinationType0Format = Literal["csv", "parquet"]

FOCUS_DESTINATION_VIEW_DESTINATION_TYPE_0_FORMAT_VALUES: Set[
    FocusDestinationViewDestinationType0Format
] = {
    "csv",
    "parquet",
}


def check_focus_destination_view_destination_type_0_format(
    value: str,
) -> FocusDestinationViewDestinationType0Format:
    if value in FOCUS_DESTINATION_VIEW_DESTINATION_TYPE_0_FORMAT_VALUES:
        return cast(FocusDestinationViewDestinationType0Format, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FOCUS_DESTINATION_VIEW_DESTINATION_TYPE_0_FORMAT_VALUES!r}"
    )
