from typing import Literal, Set, cast

CommitmentFindingType = Literal["contract_commitment"]

COMMITMENT_FINDING_TYPE_VALUES: Set[CommitmentFindingType] = {
    "contract_commitment",
}


def check_commitment_finding_type(value: str) -> CommitmentFindingType:
    if value in COMMITMENT_FINDING_TYPE_VALUES:
        return cast(CommitmentFindingType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COMMITMENT_FINDING_TYPE_VALUES!r}"
    )
