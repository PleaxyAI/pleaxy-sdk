from typing import Literal, Set, cast

CommentMeetingInputDurationMinutes = Literal[15, 30, 45]

COMMENT_MEETING_INPUT_DURATION_MINUTES_VALUES: Set[
    CommentMeetingInputDurationMinutes
] = {
    15,
    30,
    45,
}


def check_comment_meeting_input_duration_minutes(
    value: int,
) -> CommentMeetingInputDurationMinutes:
    if value in COMMENT_MEETING_INPUT_DURATION_MINUTES_VALUES:
        return cast(CommentMeetingInputDurationMinutes, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COMMENT_MEETING_INPUT_DURATION_MINUTES_VALUES!r}"
    )
