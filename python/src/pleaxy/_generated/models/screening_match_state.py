from typing import Literal, Set, cast

ScreeningMatchState = Literal["closed", "confirmed", "dismissed", "open"]

SCREENING_MATCH_STATE_VALUES: Set[ScreeningMatchState] = {
    "closed",
    "confirmed",
    "dismissed",
    "open",
}


def check_screening_match_state(value: str) -> ScreeningMatchState:
    if value in SCREENING_MATCH_STATE_VALUES:
        return cast(ScreeningMatchState, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SCREENING_MATCH_STATE_VALUES!r}"
    )
