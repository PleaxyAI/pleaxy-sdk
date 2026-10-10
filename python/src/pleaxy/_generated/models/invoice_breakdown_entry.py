from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceBreakdownEntry")


@_attrs_define
class InvoiceBreakdownEntry:
    """
    Attributes:
        description (Union[Unset, str]):
        amount (Union[Unset, float]):
        rate (Union[Unset, float]):
    """

    description: Union[Unset, str] = UNSET
    amount: Union[Unset, float] = UNSET
    rate: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        amount = self.amount

        rate = self.rate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if amount is not UNSET:
            field_dict["amount"] = amount
        if rate is not UNSET:
            field_dict["rate"] = rate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        amount = d.pop("amount", UNSET)

        rate = d.pop("rate", UNSET)

        invoice_breakdown_entry = cls(
            description=description,
            amount=amount,
            rate=rate,
        )

        invoice_breakdown_entry.additional_properties = d
        return invoice_breakdown_entry

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
