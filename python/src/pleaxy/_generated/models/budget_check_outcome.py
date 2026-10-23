from typing import Literal, Set, cast

BudgetCheckOutcome = Literal["no_budget", "no_rate", "off", "over", "within"]

BUDGET_CHECK_OUTCOME_VALUES: Set[BudgetCheckOutcome] = {
    "no_budget",
    "no_rate",
    "off",
    "over",
    "within",
}


def check_budget_check_outcome(value: str) -> BudgetCheckOutcome:
    if value in BUDGET_CHECK_OUTCOME_VALUES:
        return cast(BudgetCheckOutcome, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BUDGET_CHECK_OUTCOME_VALUES!r}"
    )
