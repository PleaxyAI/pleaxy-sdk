from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetAiRenewalRuleInput")


@_attrs_define
class SetAiRenewalRuleInput:
    """
    Attributes:
        enabled (bool): Whether next month's AI orders are drafted from the forecast.
        day_of_month (Union[Unset, float]): The day of the month (1-28) from which the drafts are raised. Default 25.
    """

    enabled: bool
    day_of_month: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled

        day_of_month = self.day_of_month

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
            }
        )
        if day_of_month is not UNSET:
            field_dict["dayOfMonth"] = day_of_month

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled")

        day_of_month = d.pop("dayOfMonth", UNSET)

        set_ai_renewal_rule_input = cls(
            enabled=enabled,
            day_of_month=day_of_month,
        )

        set_ai_renewal_rule_input.additional_properties = d
        return set_ai_renewal_rule_input

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
