from typing import Literal, Set, cast

BudgetControlSettingsMode = Literal["block", "off", "warn"]

BUDGET_CONTROL_SETTINGS_MODE_VALUES: Set[BudgetControlSettingsMode] = {
    "block",
    "off",
    "warn",
}


def check_budget_control_settings_mode(value: str) -> BudgetControlSettingsMode:
    if value in BUDGET_CONTROL_SETTINGS_MODE_VALUES:
        return cast(BudgetControlSettingsMode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BUDGET_CONTROL_SETTINGS_MODE_VALUES!r}"
    )
