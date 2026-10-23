from typing import Literal, Set, cast

BudgetStatusPeriodKind = Literal["month", "quarter", "year"]

BUDGET_STATUS_PERIOD_KIND_VALUES: Set[BudgetStatusPeriodKind] = {
    "month",
    "quarter",
    "year",
}


def check_budget_status_period_kind(value: str) -> BudgetStatusPeriodKind:
    if value in BUDGET_STATUS_PERIOD_KIND_VALUES:
        return cast(BudgetStatusPeriodKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BUDGET_STATUS_PERIOD_KIND_VALUES!r}"
    )
