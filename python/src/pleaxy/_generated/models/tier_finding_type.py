from typing import Literal, Set, cast

TierFindingType = Literal["contract_tier"]

TIER_FINDING_TYPE_VALUES: Set[TierFindingType] = {
    "contract_tier",
}


def check_tier_finding_type(value: str) -> TierFindingType:
    if value in TIER_FINDING_TYPE_VALUES:
        return cast(TierFindingType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TIER_FINDING_TYPE_VALUES!r}"
    )
