from typing import Literal, Set, cast

FocusDestinationViewDestinationType0Include = Literal["all", "non_cloud"]

FOCUS_DESTINATION_VIEW_DESTINATION_TYPE_0_INCLUDE_VALUES: Set[
    FocusDestinationViewDestinationType0Include
] = {
    "all",
    "non_cloud",
}


def check_focus_destination_view_destination_type_0_include(
    value: str,
) -> FocusDestinationViewDestinationType0Include:
    if value in FOCUS_DESTINATION_VIEW_DESTINATION_TYPE_0_INCLUDE_VALUES:
        return cast(FocusDestinationViewDestinationType0Include, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FOCUS_DESTINATION_VIEW_DESTINATION_TYPE_0_INCLUDE_VALUES!r}"
    )
