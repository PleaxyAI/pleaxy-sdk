from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateUsageAlertSettingsInputMinimums")


@_attrs_define
class UpdateUsageAlertSettingsInputMinimums:
    """The least a finding must add (or miss by) over a month, per currency the workspace is billed in (ISO 4217): used as
    set, whatever the sensitivity. Merged into what is stored; null for a currency goes back to its default.

        Example:
            {'USD': 1000, 'JPY': 100000}

    """

    additional_properties: Dict[str, Union[None, float]] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        update_usage_alert_settings_input_minimums = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(data: object) -> Union[None, float]:
                if data is None:
                    return data
                return cast(Union[None, float], data)

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        update_usage_alert_settings_input_minimums.additional_properties = (
            additional_properties
        )
        return update_usage_alert_settings_input_minimums

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Union[None, float]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Union[None, float]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
