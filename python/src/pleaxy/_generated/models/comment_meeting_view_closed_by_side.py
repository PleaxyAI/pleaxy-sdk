from typing import Literal, Set, cast

CommentMeetingViewClosedBySide = Literal["buyer", "supplier"]

COMMENT_MEETING_VIEW_CLOSED_BY_SIDE_VALUES: Set[CommentMeetingViewClosedBySide] = {
    "buyer",
    "supplier",
}


def check_comment_meeting_view_closed_by_side(
    value: str,
) -> CommentMeetingViewClosedBySide:
    if value in COMMENT_MEETING_VIEW_CLOSED_BY_SIDE_VALUES:
        return cast(CommentMeetingViewClosedBySide, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COMMENT_MEETING_VIEW_CLOSED_BY_SIDE_VALUES!r}"
    )
