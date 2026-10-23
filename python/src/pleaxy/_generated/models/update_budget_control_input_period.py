from typing import Literal, Set, cast

UpdateBudgetControlInputPeriod = Literal["month", "quarter", "year"]

UPDATE_BUDGET_CONTROL_INPUT_PERIOD_VALUES: Set[UpdateBudgetControlInputPeriod] = {
    "month",
    "quarter",
    "year",
}


def check_update_budget_control_input_period(
    value: str,
) -> UpdateBudgetControlInputPeriod:
    if value in UPDATE_BUDGET_CONTROL_INPUT_PERIOD_VALUES:
        return cast(UpdateBudgetControlInputPeriod, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_BUDGET_CONTROL_INPUT_PERIOD_VALUES!r}"
    )
