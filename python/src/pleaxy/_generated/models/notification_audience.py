from typing import Literal, Set, cast

NotificationAudience = Literal["buyer", "supplier"]

NOTIFICATION_AUDIENCE_VALUES: Set[NotificationAudience] = {
    "buyer",
    "supplier",
}


def check_notification_audience(value: str) -> NotificationAudience:
    if value in NOTIFICATION_AUDIENCE_VALUES:
        return cast(NotificationAudience, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NOTIFICATION_AUDIENCE_VALUES!r}"
    )
