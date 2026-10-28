from typing import Literal, Set, cast

ScreeningMatchEntryKind = Literal["entity", "individual", "other"]

SCREENING_MATCH_ENTRY_KIND_VALUES: Set[ScreeningMatchEntryKind] = {
    "entity",
    "individual",
    "other",
}


def check_screening_match_entry_kind(value: str) -> ScreeningMatchEntryKind:
    if value in SCREENING_MATCH_ENTRY_KIND_VALUES:
        return cast(ScreeningMatchEntryKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SCREENING_MATCH_ENTRY_KIND_VALUES!r}"
    )
