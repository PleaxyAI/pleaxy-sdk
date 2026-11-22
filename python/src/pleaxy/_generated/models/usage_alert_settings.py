from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.usage_alert_settings_sensitivity import (
    UsageAlertSettingsSensitivity,
    check_usage_alert_settings_sensitivity,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UsageAlertSettings")


@_attrs_define
class UsageAlertSettings:
    """
    Attributes:
        enabled (Union[Unset, bool]):
        sensitivity (Union[Unset, UsageAlertSettingsSensitivity]):
        updated_at (Union[Unset, str]):
        updated_by (Union[Unset, str]):
    """

    enabled: Union[Unset, bool] = UNSET
    sensitivity: Union[Unset, UsageAlertSettingsSensitivity] = UNSET
    updated_at: Union[Unset, str] = UNSET
    updated_by: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled

        sensitivity: Union[Unset, str] = UNSET
        if not isinstance(self.sensitivity, Unset):
            sensitivity = self.sensitivity

        updated_at = self.updated_at

        updated_by = self.updated_by

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if sensitivity is not UNSET:
            field_dict["sensitivity"] = sensitivity
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if updated_by is not UNSET:
            field_dict["updatedBy"] = updated_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        _sensitivity = d.pop("sensitivity", UNSET)
        sensitivity: Union[Unset, UsageAlertSettingsSensitivity]
        if isinstance(_sensitivity, Unset):
            sensitivity = UNSET
        else:
            sensitivity = check_usage_alert_settings_sensitivity(_sensitivity)

        updated_at = d.pop("updatedAt", UNSET)

        updated_by = d.pop("updatedBy", UNSET)

        usage_alert_settings = cls(
            enabled=enabled,
            sensitivity=sensitivity,
            updated_at=updated_at,
            updated_by=updated_by,
        )

        usage_alert_settings.additional_properties = d
        return usage_alert_settings

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
