from typing import Literal, Set, cast

ApprovalStageGroupInstanceMode = Literal["parallel", "sequential"]

APPROVAL_STAGE_GROUP_INSTANCE_MODE_VALUES: Set[ApprovalStageGroupInstanceMode] = {
    "parallel",
    "sequential",
}


def check_approval_stage_group_instance_mode(
    value: str,
) -> ApprovalStageGroupInstanceMode:
    if value in APPROVAL_STAGE_GROUP_INSTANCE_MODE_VALUES:
        return cast(ApprovalStageGroupInstanceMode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {APPROVAL_STAGE_GROUP_INSTANCE_MODE_VALUES!r}"
    )
