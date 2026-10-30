from typing import Literal, Set, cast

AiSeatCountSource = Literal[
    "entra", "google_workspace", "jumpcloud", "manual", "okta", "provider_console"
]

AI_SEAT_COUNT_SOURCE_VALUES: Set[AiSeatCountSource] = {
    "entra",
    "google_workspace",
    "jumpcloud",
    "manual",
    "okta",
    "provider_console",
}


def check_ai_seat_count_source(value: str) -> AiSeatCountSource:
    if value in AI_SEAT_COUNT_SOURCE_VALUES:
        return cast(AiSeatCountSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_SEAT_COUNT_SOURCE_VALUES!r}"
    )
