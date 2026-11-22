from typing import Literal, Set, cast

AiCommitmentFindingType = Literal["ai_commitment"]

AI_COMMITMENT_FINDING_TYPE_VALUES: Set[AiCommitmentFindingType] = {
    "ai_commitment",
}


def check_ai_commitment_finding_type(value: str) -> AiCommitmentFindingType:
    if value in AI_COMMITMENT_FINDING_TYPE_VALUES:
        return cast(AiCommitmentFindingType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_COMMITMENT_FINDING_TYPE_VALUES!r}"
    )
