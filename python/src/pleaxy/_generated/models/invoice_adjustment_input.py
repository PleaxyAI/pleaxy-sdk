from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_adjustment_input_type import (
    InvoiceAdjustmentInputType,
    check_invoice_adjustment_input_type,
)

T = TypeVar("T", bound="InvoiceAdjustmentInput")


@_attrs_define
class InvoiceAdjustmentInput:
    """
    Attributes:
        type (InvoiceAdjustmentInputType):
        description (str): What the discount or charge is for, 1–200 characters
        amount (float): A positive amount, with no more decimal places than the buyer's currency allows (at most 2).
            `type` says whether it reduces or adds to the total.
    """

    type: InvoiceAdjustmentInputType
    description: str
    amount: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: str = self.type

        description = self.description

        amount = self.amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "description": description,
                "amount": amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = check_invoice_adjustment_input_type(d.pop("type"))

        description = d.pop("description")

        amount = d.pop("amount")

        invoice_adjustment_input = cls(
            type=type,
            description=description,
            amount=amount,
        )

        invoice_adjustment_input.additional_properties = d
        return invoice_adjustment_input

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
