from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UsageAlertCurrency")


@_attrs_define
class UsageAlertCurrency:
    """
    Attributes:
        currency (Union[Unset, str]):
        minimum (Union[Unset, float]):
        default_minimum (Union[Unset, float]):
        custom (Union[Unset, bool]):
    """

    currency: Union[Unset, str] = UNSET
    minimum: Union[Unset, float] = UNSET
    default_minimum: Union[Unset, float] = UNSET
    custom: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        currency = self.currency

        minimum = self.minimum

        default_minimum = self.default_minimum

        custom = self.custom

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency is not UNSET:
            field_dict["currency"] = currency
        if minimum is not UNSET:
            field_dict["minimum"] = minimum
        if default_minimum is not UNSET:
            field_dict["defaultMinimum"] = default_minimum
        if custom is not UNSET:
            field_dict["custom"] = custom

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        currency = d.pop("currency", UNSET)

        minimum = d.pop("minimum", UNSET)

        default_minimum = d.pop("defaultMinimum", UNSET)

        custom = d.pop("custom", UNSET)

        usage_alert_currency = cls(
            currency=currency,
            minimum=minimum,
            default_minimum=default_minimum,
            custom=custom,
        )

        usage_alert_currency.additional_properties = d
        return usage_alert_currency

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
