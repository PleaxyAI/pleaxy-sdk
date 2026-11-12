from typing import Literal, Set, cast

CommentMeetingViewAttendeeSide = Literal["buyer", "supplier"]

COMMENT_MEETING_VIEW_ATTENDEE_SIDE_VALUES: Set[CommentMeetingViewAttendeeSide] = {
    "buyer",
    "supplier",
}


def check_comment_meeting_view_attendee_side(
    value: str,
) -> CommentMeetingViewAttendeeSide:
    if value in COMMENT_MEETING_VIEW_ATTENDEE_SIDE_VALUES:
        return cast(CommentMeetingViewAttendeeSide, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COMMENT_MEETING_VIEW_ATTENDEE_SIDE_VALUES!r}"
    )
