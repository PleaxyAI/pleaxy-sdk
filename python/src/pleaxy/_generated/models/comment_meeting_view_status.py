from typing import Literal, Set, cast

CommentMeetingViewStatus = Literal[
    "accepted", "cancelled", "declined", "expired", "open"
]

COMMENT_MEETING_VIEW_STATUS_VALUES: Set[CommentMeetingViewStatus] = {
    "accepted",
    "cancelled",
    "declined",
    "expired",
    "open",
}


def check_comment_meeting_view_status(value: str) -> CommentMeetingViewStatus:
    if value in COMMENT_MEETING_VIEW_STATUS_VALUES:
        return cast(CommentMeetingViewStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COMMENT_MEETING_VIEW_STATUS_VALUES!r}"
    )
