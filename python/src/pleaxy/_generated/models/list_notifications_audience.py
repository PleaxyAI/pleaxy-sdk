from typing import Literal, Set, cast

ListNotificationsAudience = Literal["buyer", "supplier"]

LIST_NOTIFICATIONS_AUDIENCE_VALUES: Set[ListNotificationsAudience] = {
    "buyer",
    "supplier",
}


def check_list_notifications_audience(value: str) -> ListNotificationsAudience:
    if value in LIST_NOTIFICATIONS_AUDIENCE_VALUES:
        return cast(ListNotificationsAudience, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_NOTIFICATIONS_AUDIENCE_VALUES!r}"
    )
