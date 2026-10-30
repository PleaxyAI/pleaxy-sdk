from typing import Literal, Set, cast

AiCommitmentViewKind = Literal["capacity", "prepaid_credit", "seats", "spend"]

AI_COMMITMENT_VIEW_KIND_VALUES: Set[AiCommitmentViewKind] = {
    "capacity",
    "prepaid_credit",
    "seats",
    "spend",
}


def check_ai_commitment_view_kind(value: str) -> AiCommitmentViewKind:
    if value in AI_COMMITMENT_VIEW_KIND_VALUES:
        return cast(AiCommitmentViewKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_COMMITMENT_VIEW_KIND_VALUES!r}"
    )
