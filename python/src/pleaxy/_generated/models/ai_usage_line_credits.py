from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ai_usage_line_credits_unit import (
    AiUsageLineCreditsUnit,
    check_ai_usage_line_credits_unit,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AiUsageLineCredits")


@_attrs_define
class AiUsageLineCredits:
    """
    Attributes:
        quantity (Union[Unset, float]):
        unit (Union[Unset, AiUsageLineCreditsUnit]):
        unit_price (Union[Unset, float]):
    """

    quantity: Union[Unset, float] = UNSET
    unit: Union[Unset, AiUsageLineCreditsUnit] = UNSET
    unit_price: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        quantity = self.quantity

        unit: Union[Unset, str] = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit

        unit_price = self.unit_price

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if unit is not UNSET:
            field_dict["unit"] = unit
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        quantity = d.pop("quantity", UNSET)

        _unit = d.pop("unit", UNSET)
        unit: Union[Unset, AiUsageLineCreditsUnit]
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = check_ai_usage_line_credits_unit(_unit)

        unit_price = d.pop("unitPrice", UNSET)

        ai_usage_line_credits = cls(
            quantity=quantity,
            unit=unit,
            unit_price=unit_price,
        )

        ai_usage_line_credits.additional_properties = d
        return ai_usage_line_credits

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
