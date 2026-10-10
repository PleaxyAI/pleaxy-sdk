from typing import Literal, Set, cast

ApprovalStageGroupDefMode = Literal["parallel", "sequential"]

APPROVAL_STAGE_GROUP_DEF_MODE_VALUES: Set[ApprovalStageGroupDefMode] = {
    "parallel",
    "sequential",
}


def check_approval_stage_group_def_mode(value: str) -> ApprovalStageGroupDefMode:
    if value in APPROVAL_STAGE_GROUP_DEF_MODE_VALUES:
        return cast(ApprovalStageGroupDefMode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {APPROVAL_STAGE_GROUP_DEF_MODE_VALUES!r}"
    )
