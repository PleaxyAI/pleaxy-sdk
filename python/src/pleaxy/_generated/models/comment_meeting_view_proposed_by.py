from typing import Literal, Set, cast

CommentMeetingViewProposedBy = Literal["buyer", "supplier"]

COMMENT_MEETING_VIEW_PROPOSED_BY_VALUES: Set[CommentMeetingViewProposedBy] = {
    "buyer",
    "supplier",
}


def check_comment_meeting_view_proposed_by(value: str) -> CommentMeetingViewProposedBy:
    if value in COMMENT_MEETING_VIEW_PROPOSED_BY_VALUES:
        return cast(CommentMeetingViewProposedBy, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COMMENT_MEETING_VIEW_PROPOSED_BY_VALUES!r}"
    )
