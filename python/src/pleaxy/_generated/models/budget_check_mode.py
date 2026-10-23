from typing import Literal, Set, cast

BudgetCheckMode = Literal["block", "off", "warn"]

BUDGET_CHECK_MODE_VALUES: Set[BudgetCheckMode] = {
    "block",
    "off",
    "warn",
}


def check_budget_check_mode(value: str) -> BudgetCheckMode:
    if value in BUDGET_CHECK_MODE_VALUES:
        return cast(BudgetCheckMode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BUDGET_CHECK_MODE_VALUES!r}"
    )
