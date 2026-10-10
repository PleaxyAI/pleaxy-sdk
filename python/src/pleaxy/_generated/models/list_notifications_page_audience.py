from typing import Literal, Set, cast

ListNotificationsPageAudience = Literal["buyer", "supplier"]

LIST_NOTIFICATIONS_PAGE_AUDIENCE_VALUES: Set[ListNotificationsPageAudience] = {
    "buyer",
    "supplier",
}


def check_list_notifications_page_audience(value: str) -> ListNotificationsPageAudience:
    if value in LIST_NOTIFICATIONS_PAGE_AUDIENCE_VALUES:
        return cast(ListNotificationsPageAudience, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_NOTIFICATIONS_PAGE_AUDIENCE_VALUES!r}"
    )
