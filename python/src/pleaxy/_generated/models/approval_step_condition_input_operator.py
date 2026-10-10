from typing import Literal, Set, cast

ApprovalStepConditionInputOperator = Literal["gt", "gte", "is", "is_not", "lt", "lte"]

APPROVAL_STEP_CONDITION_INPUT_OPERATOR_VALUES: Set[
    ApprovalStepConditionInputOperator
] = {
    "gt",
    "gte",
    "is",
    "is_not",
    "lt",
    "lte",
}


def check_approval_step_condition_input_operator(
    value: str,
) -> ApprovalStepConditionInputOperator:
    if value in APPROVAL_STEP_CONDITION_INPUT_OPERATOR_VALUES:
        return cast(ApprovalStepConditionInputOperator, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {APPROVAL_STEP_CONDITION_INPUT_OPERATOR_VALUES!r}"
    )
