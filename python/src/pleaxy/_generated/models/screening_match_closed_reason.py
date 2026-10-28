from typing import Literal, Set, cast

ScreeningMatchClosedReason = Literal["entry_removed", "no_longer_matches"]

SCREENING_MATCH_CLOSED_REASON_VALUES: Set[ScreeningMatchClosedReason] = {
    "entry_removed",
    "no_longer_matches",
}


def check_screening_match_closed_reason(value: str) -> ScreeningMatchClosedReason:
    if value in SCREENING_MATCH_CLOSED_REASON_VALUES:
        return cast(ScreeningMatchClosedReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SCREENING_MATCH_CLOSED_REASON_VALUES!r}"
    )
