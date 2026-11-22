from typing import Literal, Set, cast

PaceFindingType = Literal["pace"]

PACE_FINDING_TYPE_VALUES: Set[PaceFindingType] = {
    "pace",
}


def check_pace_finding_type(value: str) -> PaceFindingType:
    if value in PACE_FINDING_TYPE_VALUES:
        return cast(PaceFindingType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PACE_FINDING_TYPE_VALUES!r}"
    )
