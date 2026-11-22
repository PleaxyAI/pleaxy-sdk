from typing import Literal, Set, cast

TierFindingExcess = Literal[0]

TIER_FINDING_EXCESS_VALUES: Set[TierFindingExcess] = {
    0,
}


def check_tier_finding_excess(value: int) -> TierFindingExcess:
    if value in TIER_FINDING_EXCESS_VALUES:
        return cast(TierFindingExcess, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TIER_FINDING_EXCESS_VALUES!r}"
    )
