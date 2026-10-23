from typing import Literal, Set, cast

UpdateBudgetControlInputMode = Literal["block", "off", "warn"]

UPDATE_BUDGET_CONTROL_INPUT_MODE_VALUES: Set[UpdateBudgetControlInputMode] = {
    "block",
    "off",
    "warn",
}


def check_update_budget_control_input_mode(value: str) -> UpdateBudgetControlInputMode:
    if value in UPDATE_BUDGET_CONTROL_INPUT_MODE_VALUES:
        return cast(UpdateBudgetControlInputMode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_BUDGET_CONTROL_INPUT_MODE_VALUES!r}"
    )
