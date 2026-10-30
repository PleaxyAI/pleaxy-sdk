from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AiMeterQuantity")


@_attrs_define
class AiMeterQuantity:
    """
    Attributes:
        meter (Union[Unset, str]):
        unit (Union[Unset, str]):
        quantity (Union[Unset, float]):
    """

    meter: Union[Unset, str] = UNSET
    unit: Union[Unset, str] = UNSET
    quantity: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        meter = self.meter

        unit = self.unit

        quantity = self.quantity

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if meter is not UNSET:
            field_dict["meter"] = meter
        if unit is not UNSET:
            field_dict["unit"] = unit
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        meter = d.pop("meter", UNSET)

        unit = d.pop("unit", UNSET)

        quantity = d.pop("quantity", UNSET)

        ai_meter_quantity = cls(
            meter=meter,
            unit=unit,
            quantity=quantity,
        )

        ai_meter_quantity.additional_properties = d
        return ai_meter_quantity

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
