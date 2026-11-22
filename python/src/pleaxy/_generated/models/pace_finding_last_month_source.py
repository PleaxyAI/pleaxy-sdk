from typing import Literal, Set, cast

PaceFindingLastMonthSource = Literal["invoice", "snapshot"]

PACE_FINDING_LAST_MONTH_SOURCE_VALUES: Set[PaceFindingLastMonthSource] = {
    "invoice",
    "snapshot",
}


def check_pace_finding_last_month_source(value: str) -> PaceFindingLastMonthSource:
    if value in PACE_FINDING_LAST_MONTH_SOURCE_VALUES:
        return cast(PaceFindingLastMonthSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PACE_FINDING_LAST_MONTH_SOURCE_VALUES!r}"
    )
