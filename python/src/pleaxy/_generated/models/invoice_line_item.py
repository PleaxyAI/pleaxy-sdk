from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_line_item_ai import InvoiceLineItemAi


T = TypeVar("T", bound="InvoiceLineItem")


@_attrs_define
class InvoiceLineItem:
    """
    Attributes:
        description (Union[Unset, str]):
        qty (Union[Unset, float]):
        unit_price (Union[Unset, float]):
        amount (Union[Unset, float]):
        discount (Union[Unset, float]):
        charge (Union[Unset, float]):
        ai (Union[Unset, InvoiceLineItemAi]):
    """

    description: Union[Unset, str] = UNSET
    qty: Union[Unset, float] = UNSET
    unit_price: Union[Unset, float] = UNSET
    amount: Union[Unset, float] = UNSET
    discount: Union[Unset, float] = UNSET
    charge: Union[Unset, float] = UNSET
    ai: Union[Unset, "InvoiceLineItemAi"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        qty = self.qty

        unit_price = self.unit_price

        amount = self.amount

        discount = self.discount

        charge = self.charge

        ai: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ai, Unset):
            ai = self.ai.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if qty is not UNSET:
            field_dict["qty"] = qty
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if amount is not UNSET:
            field_dict["amount"] = amount
        if discount is not UNSET:
            field_dict["discount"] = discount
        if charge is not UNSET:
            field_dict["charge"] = charge
        if ai is not UNSET:
            field_dict["ai"] = ai

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_line_item_ai import InvoiceLineItemAi

        d = src_dict.copy()
        description = d.pop("description", UNSET)

        qty = d.pop("qty", UNSET)

        unit_price = d.pop("unitPrice", UNSET)

        amount = d.pop("amount", UNSET)

        discount = d.pop("discount", UNSET)

        charge = d.pop("charge", UNSET)

        _ai = d.pop("ai", UNSET)
        ai: Union[Unset, InvoiceLineItemAi]
        if isinstance(_ai, Unset):
            ai = UNSET
        else:
            ai = InvoiceLineItemAi.from_dict(_ai)

        invoice_line_item = cls(
            description=description,
            qty=qty,
            unit_price=unit_price,
            amount=amount,
            discount=discount,
            charge=charge,
            ai=ai,
        )

        invoice_line_item.additional_properties = d
        return invoice_line_item

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
