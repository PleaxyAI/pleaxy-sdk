from typing import Literal, Set, cast

UsageAlertSettingsSensitivity = Literal["high", "low", "medium"]

USAGE_ALERT_SETTINGS_SENSITIVITY_VALUES: Set[UsageAlertSettingsSensitivity] = {
    "high",
    "low",
    "medium",
}


def check_usage_alert_settings_sensitivity(value: str) -> UsageAlertSettingsSensitivity:
    if value in USAGE_ALERT_SETTINGS_SENSITIVITY_VALUES:
        return cast(UsageAlertSettingsSensitivity, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {USAGE_ALERT_SETTINGS_SENSITIVITY_VALUES!r}"
    )
