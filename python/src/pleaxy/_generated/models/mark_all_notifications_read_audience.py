from typing import Literal, Set, cast

MarkAllNotificationsReadAudience = Literal["buyer", "supplier"]

MARK_ALL_NOTIFICATIONS_READ_AUDIENCE_VALUES: Set[MarkAllNotificationsReadAudience] = {
    "buyer",
    "supplier",
}


def check_mark_all_notifications_read_audience(
    value: str,
) -> MarkAllNotificationsReadAudience:
    if value in MARK_ALL_NOTIFICATIONS_READ_AUDIENCE_VALUES:
        return cast(MarkAllNotificationsReadAudience, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MARK_ALL_NOTIFICATIONS_READ_AUDIENCE_VALUES!r}"
    )
