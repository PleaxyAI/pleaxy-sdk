from typing import Literal, Set, cast

ApprovalReassignmentDetailByPolicy = Literal["requester_rule"]

APPROVAL_REASSIGNMENT_DETAIL_BY_POLICY_VALUES: Set[
    ApprovalReassignmentDetailByPolicy
] = {
    "requester_rule",
}


def check_approval_reassignment_detail_by_policy(
    value: str,
) -> ApprovalReassignmentDetailByPolicy:
    if value in APPROVAL_REASSIGNMENT_DETAIL_BY_POLICY_VALUES:
        return cast(ApprovalReassignmentDetailByPolicy, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {APPROVAL_REASSIGNMENT_DETAIL_BY_POLICY_VALUES!r}"
    )
