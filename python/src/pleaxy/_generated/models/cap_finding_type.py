from typing import Literal, Set, cast

CapFindingType = Literal["contract_cap"]

CAP_FINDING_TYPE_VALUES: Set[CapFindingType] = {
    "contract_cap",
}


def check_cap_finding_type(value: str) -> CapFindingType:
    if value in CAP_FINDING_TYPE_VALUES:
        return cast(CapFindingType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CAP_FINDING_TYPE_VALUES!r}"
    )
