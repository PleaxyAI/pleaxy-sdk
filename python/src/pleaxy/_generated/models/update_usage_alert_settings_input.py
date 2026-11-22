from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_usage_alert_settings_input_sensitivity import (
    UpdateUsageAlertSettingsInputSensitivity,
    check_update_usage_alert_settings_input_sensitivity,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateUsageAlertSettingsInput")


@_attrs_define
class UpdateUsageAlertSettingsInput:
    """
    Attributes:
        enabled (Union[Unset, bool]): Whether usage anomaly alerts are sent. Off: nothing is sent; the spend page still
            shows what the rules find.
        sensitivity (Union[Unset, UpdateUsageAlertSettingsInputSensitivity]): high: 25% above the trend, 20% above last
            month, from 100 a month. medium (default): 50%, 30%, from 500. low: 100%, 50%, from 2,000. Amounts in each
            subject's own currency.
    """

    enabled: Union[Unset, bool] = UNSET
    sensitivity: Union[Unset, UpdateUsageAlertSettingsInputSensitivity] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled

        sensitivity: Union[Unset, str] = UNSET
        if not isinstance(self.sensitivity, Unset):
            sensitivity = self.sensitivity

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if sensitivity is not UNSET:
            field_dict["sensitivity"] = sensitivity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        _sensitivity = d.pop("sensitivity", UNSET)
        sensitivity: Union[Unset, UpdateUsageAlertSettingsInputSensitivity]
        if isinstance(_sensitivity, Unset):
            sensitivity = UNSET
        else:
            sensitivity = check_update_usage_alert_settings_input_sensitivity(
                _sensitivity
            )

        update_usage_alert_settings_input = cls(
            enabled=enabled,
            sensitivity=sensitivity,
        )

        update_usage_alert_settings_input.additional_properties = d
        return update_usage_alert_settings_input

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
