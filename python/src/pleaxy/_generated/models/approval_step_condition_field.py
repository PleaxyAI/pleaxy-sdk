from typing import Literal, Set, cast

ApprovalStepConditionField = Literal["amount", "requester", "supplier"]

APPROVAL_STEP_CONDITION_FIELD_VALUES: Set[ApprovalStepConditionField] = {
    "amount",
    "requester",
    "supplier",
}


def check_approval_step_condition_field(value: str) -> ApprovalStepConditionField:
    if value in APPROVAL_STEP_CONDITION_FIELD_VALUES:
        return cast(ApprovalStepConditionField, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {APPROVAL_STEP_CONDITION_FIELD_VALUES!r}"
    )
