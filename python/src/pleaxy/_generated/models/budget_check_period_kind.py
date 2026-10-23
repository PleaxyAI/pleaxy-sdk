from typing import Literal, Set, cast

BudgetCheckPeriodKind = Literal["month", "quarter", "year"]

BUDGET_CHECK_PERIOD_KIND_VALUES: Set[BudgetCheckPeriodKind] = {
    "month",
    "quarter",
    "year",
}


def check_budget_check_period_kind(value: str) -> BudgetCheckPeriodKind:
    if value in BUDGET_CHECK_PERIOD_KIND_VALUES:
        return cast(BudgetCheckPeriodKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BUDGET_CHECK_PERIOD_KIND_VALUES!r}"
    )
