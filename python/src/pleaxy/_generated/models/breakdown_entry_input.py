from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BreakdownEntryInput")


@_attrs_define
class BreakdownEntryInput:
    """
    Attributes:
        description (str): What the entry is, e.g. "IVA" or "Percepción IIBB CABA". 1–200 characters.
        amount (float): 0 or more, in the currency of the object it belongs to.
        rate (Union[Unset, float]): A percentage, 0–100, when the entry has one (IVA 21). Omit for fixed amounts.
    """

    description: str
    amount: float
    rate: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        amount = self.amount

        rate = self.rate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "amount": amount,
            }
        )
        if rate is not UNSET:
            field_dict["rate"] = rate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description")

        amount = d.pop("amount")

        rate = d.pop("rate", UNSET)

        breakdown_entry_input = cls(
            description=description,
            amount=amount,
            rate=rate,
        )

        breakdown_entry_input.additional_properties = d
        return breakdown_entry_input

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
