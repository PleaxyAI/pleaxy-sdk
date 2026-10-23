from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PurchaseRequestLine")


@_attrs_define
class PurchaseRequestLine:
    """
    Attributes:
        name (Union[Unset, str]):
        qty (Union[Unset, float]):
        unit (Union[Unset, str]):
        unit_price (Union[Unset, float]):
    """

    name: Union[Unset, str] = UNSET
    qty: Union[Unset, float] = UNSET
    unit: Union[Unset, str] = UNSET
    unit_price: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        qty = self.qty

        unit = self.unit

        unit_price = self.unit_price

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if qty is not UNSET:
            field_dict["qty"] = qty
        if unit is not UNSET:
            field_dict["unit"] = unit
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        qty = d.pop("qty", UNSET)

        unit = d.pop("unit", UNSET)

        unit_price = d.pop("unitPrice", UNSET)

        purchase_request_line = cls(
            name=name,
            qty=qty,
            unit=unit,
            unit_price=unit_price,
        )

        purchase_request_line.additional_properties = d
        return purchase_request_line

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
