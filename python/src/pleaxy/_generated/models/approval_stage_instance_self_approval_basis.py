from typing import Literal, Set, cast

ApprovalStageInstanceSelfApprovalBasis = Literal["sole_eligible_approver"]

APPROVAL_STAGE_INSTANCE_SELF_APPROVAL_BASIS_VALUES: Set[
    ApprovalStageInstanceSelfApprovalBasis
] = {
    "sole_eligible_approver",
}


def check_approval_stage_instance_self_approval_basis(
    value: str,
) -> ApprovalStageInstanceSelfApprovalBasis:
    if value in APPROVAL_STAGE_INSTANCE_SELF_APPROVAL_BASIS_VALUES:
        return cast(ApprovalStageInstanceSelfApprovalBasis, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {APPROVAL_STAGE_INSTANCE_SELF_APPROVAL_BASIS_VALUES!r}"
    )
