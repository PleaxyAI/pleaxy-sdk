from typing import Literal, Set, cast

ApprovalStageGroupInstanceStatus = Literal["approved", "pending", "rejected"]

APPROVAL_STAGE_GROUP_INSTANCE_STATUS_VALUES: Set[ApprovalStageGroupInstanceStatus] = {
    "approved",
    "pending",
    "rejected",
}


def check_approval_stage_group_instance_status(
    value: str,
) -> ApprovalStageGroupInstanceStatus:
    if value in APPROVAL_STAGE_GROUP_INSTANCE_STATUS_VALUES:
        return cast(ApprovalStageGroupInstanceStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {APPROVAL_STAGE_GROUP_INSTANCE_STATUS_VALUES!r}"
    )
