from typing import Literal, Set, cast

FocusDestinationViewDestinationType0Version = Literal["1.2", "1.4"]

FOCUS_DESTINATION_VIEW_DESTINATION_TYPE_0_VERSION_VALUES: Set[
    FocusDestinationViewDestinationType0Version
] = {
    "1.2",
    "1.4",
}


def check_focus_destination_view_destination_type_0_version(
    value: str,
) -> FocusDestinationViewDestinationType0Version:
    if value in FOCUS_DESTINATION_VIEW_DESTINATION_TYPE_0_VERSION_VALUES:
        return cast(FocusDestinationViewDestinationType0Version, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FOCUS_DESTINATION_VIEW_DESTINATION_TYPE_0_VERSION_VALUES!r}"
    )
