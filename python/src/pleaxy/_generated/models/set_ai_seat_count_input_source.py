from typing import Literal, Set, cast

SetAiSeatCountInputSource = Literal[
    "entra", "google_workspace", "jumpcloud", "manual", "okta", "provider_console"
]

SET_AI_SEAT_COUNT_INPUT_SOURCE_VALUES: Set[SetAiSeatCountInputSource] = {
    "entra",
    "google_workspace",
    "jumpcloud",
    "manual",
    "okta",
    "provider_console",
}


def check_set_ai_seat_count_input_source(value: str) -> SetAiSeatCountInputSource:
    if value in SET_AI_SEAT_COUNT_INPUT_SOURCE_VALUES:
        return cast(SetAiSeatCountInputSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SET_AI_SEAT_COUNT_INPUT_SOURCE_VALUES!r}"
    )
