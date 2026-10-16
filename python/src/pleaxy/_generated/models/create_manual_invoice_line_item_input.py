from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateManualInvoiceLineItemInput")


@_attrs_define
class CreateManualInvoiceLineItemInput:
    """
    Attributes:
        description (str):
        qty (float): Greater than 0, at most 1,000,000
        unit_price (float): 0 or more, at most 1,000,000,000. A reduction is a discount, never a negative price.
        discount (Union[Unset, float]): Total discount on this line, with no more decimal places than the buyer's
            currency allows (at most 2). It can't be more than qty × unitPrice + charge. The line amount is qty × unitPrice
            + charge − discount.
        charge (Union[Unset, float]): Total charges on this line (freight, handling…), with no more decimal places than
            the buyer's currency allows (at most 2).
    """

    description: str
    qty: float
    unit_price: float
    discount: Union[Unset, float] = UNSET
    charge: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        qty = self.qty

        unit_price = self.unit_price

        discount = self.discount

        charge = self.charge

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "qty": qty,
                "unitPrice": unit_price,
            }
        )
        if discount is not UNSET:
            field_dict["discount"] = discount
        if charge is not UNSET:
            field_dict["charge"] = charge

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description")

        qty = d.pop("qty")

        unit_price = d.pop("unitPrice")

        discount = d.pop("discount", UNSET)

        charge = d.pop("charge", UNSET)

        create_manual_invoice_line_item_input = cls(
            description=description,
            qty=qty,
            unit_price=unit_price,
            discount=discount,
            charge=charge,
        )

        create_manual_invoice_line_item_input.additional_properties = d
        return create_manual_invoice_line_item_input

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
