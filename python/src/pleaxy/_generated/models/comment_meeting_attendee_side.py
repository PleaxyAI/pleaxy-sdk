from typing import Literal, Set, cast

CommentMeetingAttendeeSide = Literal["buyer", "supplier"]

COMMENT_MEETING_ATTENDEE_SIDE_VALUES: Set[CommentMeetingAttendeeSide] = {
    "buyer",
    "supplier",
}


def check_comment_meeting_attendee_side(value: str) -> CommentMeetingAttendeeSide:
    if value in COMMENT_MEETING_ATTENDEE_SIDE_VALUES:
        return cast(CommentMeetingAttendeeSide, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COMMENT_MEETING_ATTENDEE_SIDE_VALUES!r}"
    )
