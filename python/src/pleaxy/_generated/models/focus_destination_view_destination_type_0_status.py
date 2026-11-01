from typing import Literal, Set, cast

FocusDestinationViewDestinationType0Status = Literal[
    "active", "awaiting_role", "failing"
]

FOCUS_DESTINATION_VIEW_DESTINATION_TYPE_0_STATUS_VALUES: Set[
    FocusDestinationViewDestinationType0Status
] = {
    "active",
    "awaiting_role",
    "failing",
}


def check_focus_destination_view_destination_type_0_status(
    value: str,
) -> FocusDestinationViewDestinationType0Status:
    if value in FOCUS_DESTINATION_VIEW_DESTINATION_TYPE_0_STATUS_VALUES:
        return cast(FocusDestinationViewDestinationType0Status, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FOCUS_DESTINATION_VIEW_DESTINATION_TYPE_0_STATUS_VALUES!r}"
    )
