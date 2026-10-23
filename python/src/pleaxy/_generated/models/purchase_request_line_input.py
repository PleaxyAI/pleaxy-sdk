from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PurchaseRequestLineInput")


@_attrs_define
class PurchaseRequestLineInput:
    """
    Attributes:
        name (str): What is needed, e.g. 27-inch monitor.
        qty (float): How many.
        unit_price (float): Roughly what one costs, in the request's currency.
        unit (Union[Unset, str]): e.g. each, hour, month.
    """

    name: str
    qty: float
    unit_price: float
    unit: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        qty = self.qty

        unit_price = self.unit_price

        unit = self.unit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "qty": qty,
                "unitPrice": unit_price,
            }
        )
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        qty = d.pop("qty")

        unit_price = d.pop("unitPrice")

        unit = d.pop("unit", UNSET)

        purchase_request_line_input = cls(
            name=name,
            qty=qty,
            unit_price=unit_price,
            unit=unit,
        )

        purchase_request_line_input.additional_properties = d
        return purchase_request_line_input

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
