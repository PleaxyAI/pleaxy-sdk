from typing import Literal, Set, cast

ApprovalStageInstanceStatus = Literal["approved", "pending", "rejected"]

APPROVAL_STAGE_INSTANCE_STATUS_VALUES: Set[ApprovalStageInstanceStatus] = {
    "approved",
    "pending",
    "rejected",
}


def check_approval_stage_instance_status(value: str) -> ApprovalStageInstanceStatus:
    if value in APPROVAL_STAGE_INSTANCE_STATUS_VALUES:
        return cast(ApprovalStageInstanceStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {APPROVAL_STAGE_INSTANCE_STATUS_VALUES!r}"
    )
