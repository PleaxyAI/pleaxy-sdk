from typing import Literal, Set, cast

ApprovalStageGroupDefInputMode = Literal["parallel", "sequential"]

APPROVAL_STAGE_GROUP_DEF_INPUT_MODE_VALUES: Set[ApprovalStageGroupDefInputMode] = {
    "parallel",
    "sequential",
}


def check_approval_stage_group_def_input_mode(
    value: str,
) -> ApprovalStageGroupDefInputMode:
    if value in APPROVAL_STAGE_GROUP_DEF_INPUT_MODE_VALUES:
        return cast(ApprovalStageGroupDefInputMode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {APPROVAL_STAGE_GROUP_DEF_INPUT_MODE_VALUES!r}"
    )
