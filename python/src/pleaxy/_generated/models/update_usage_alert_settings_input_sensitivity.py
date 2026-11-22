from typing import Literal, Set, cast

UpdateUsageAlertSettingsInputSensitivity = Literal["high", "low", "medium"]

UPDATE_USAGE_ALERT_SETTINGS_INPUT_SENSITIVITY_VALUES: Set[
    UpdateUsageAlertSettingsInputSensitivity
] = {
    "high",
    "low",
    "medium",
}


def check_update_usage_alert_settings_input_sensitivity(
    value: str,
) -> UpdateUsageAlertSettingsInputSensitivity:
    if value in UPDATE_USAGE_ALERT_SETTINGS_INPUT_SENSITIVITY_VALUES:
        return cast(UpdateUsageAlertSettingsInputSensitivity, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_USAGE_ALERT_SETTINGS_INPUT_SENSITIVITY_VALUES!r}"
    )
