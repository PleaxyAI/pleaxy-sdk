from typing import Literal, Set, cast

ApprovalStepConditionOperator = Literal["gt", "gte", "is", "is_not", "lt", "lte"]

APPROVAL_STEP_CONDITION_OPERATOR_VALUES: Set[ApprovalStepConditionOperator] = {
    "gt",
    "gte",
    "is",
    "is_not",
    "lt",
    "lte",
}


def check_approval_step_condition_operator(value: str) -> ApprovalStepConditionOperator:
    if value in APPROVAL_STEP_CONDITION_OPERATOR_VALUES:
        return cast(ApprovalStepConditionOperator, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {APPROVAL_STEP_CONDITION_OPERATOR_VALUES!r}"
    )
