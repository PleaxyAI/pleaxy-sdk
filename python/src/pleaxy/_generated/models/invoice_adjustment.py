from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_adjustment_type import (
    InvoiceAdjustmentType,
    check_invoice_adjustment_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceAdjustment")


@_attrs_define
class InvoiceAdjustment:
    """
    Attributes:
        type (Union[Unset, InvoiceAdjustmentType]):
        description (Union[Unset, str]):
        amount (Union[Unset, float]):
    """

    type: Union[Unset, InvoiceAdjustmentType] = UNSET
    description: Union[Unset, str] = UNSET
    amount: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type

        description = self.description

        amount = self.amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if description is not UNSET:
            field_dict["description"] = description
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, InvoiceAdjustmentType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = check_invoice_adjustment_type(_type)

        description = d.pop("description", UNSET)

        amount = d.pop("amount", UNSET)

        invoice_adjustment = cls(
            type=type,
            description=description,
            amount=amount,
        )

        invoice_adjustment.additional_properties = d
        return invoice_adjustment

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
