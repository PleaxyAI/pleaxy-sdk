from typing import Literal, Set, cast

BudgetControlSettingsPeriod = Literal["month", "quarter", "year"]

BUDGET_CONTROL_SETTINGS_PERIOD_VALUES: Set[BudgetControlSettingsPeriod] = {
    "month",
    "quarter",
    "year",
}


def check_budget_control_settings_period(value: str) -> BudgetControlSettingsPeriod:
    if value in BUDGET_CONTROL_SETTINGS_PERIOD_VALUES:
        return cast(BudgetControlSettingsPeriod, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BUDGET_CONTROL_SETTINGS_PERIOD_VALUES!r}"
    )
