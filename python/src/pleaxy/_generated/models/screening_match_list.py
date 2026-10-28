from typing import Literal, Set, cast

ScreeningMatchList = Literal["eu", "jurisdiction", "ofac", "uk", "un"]

SCREENING_MATCH_LIST_VALUES: Set[ScreeningMatchList] = {
    "eu",
    "jurisdiction",
    "ofac",
    "uk",
    "un",
}


def check_screening_match_list(value: str) -> ScreeningMatchList:
    if value in SCREENING_MATCH_LIST_VALUES:
        return cast(ScreeningMatchList, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SCREENING_MATCH_LIST_VALUES!r}"
    )
