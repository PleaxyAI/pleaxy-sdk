from typing import Literal, Set, cast

ApprovalStepConditionInputField = Literal[
    "amount", "answer", "costCenter", "glCode", "requester", "requestType", "supplier"
]

APPROVAL_STEP_CONDITION_INPUT_FIELD_VALUES: Set[ApprovalStepConditionInputField] = {
    "amount",
    "answer",
    "costCenter",
    "glCode",
    "requester",
    "requestType",
    "supplier",
}


def check_approval_step_condition_input_field(
    value: str,
) -> ApprovalStepConditionInputField:
    if value in APPROVAL_STEP_CONDITION_INPUT_FIELD_VALUES:
        return cast(ApprovalStepConditionInputField, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {APPROVAL_STEP_CONDITION_INPUT_FIELD_VALUES!r}"
    )
