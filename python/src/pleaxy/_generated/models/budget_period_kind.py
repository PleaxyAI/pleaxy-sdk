from typing import Literal, Set, cast

BudgetPeriodKind = Literal["month", "quarter", "year"]

BUDGET_PERIOD_KIND_VALUES: Set[BudgetPeriodKind] = {
    "month",
    "quarter",
    "year",
}


def check_budget_period_kind(value: str) -> BudgetPeriodKind:
    if value in BUDGET_PERIOD_KIND_VALUES:
        return cast(BudgetPeriodKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BUDGET_PERIOD_KIND_VALUES!r}"
    )
