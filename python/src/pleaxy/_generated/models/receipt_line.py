from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReceiptLine")


@_attrs_define
class ReceiptLine:
    """
    Attributes:
        line_no (Union[Unset, float]):
        qty (Union[Unset, float]):
        amount (Union[Unset, float]):
    """

    line_no: Union[Unset, float] = UNSET
    qty: Union[Unset, float] = UNSET
    amount: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        line_no = self.line_no

        qty = self.qty

        amount = self.amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if line_no is not UNSET:
            field_dict["lineNo"] = line_no
        if qty is not UNSET:
            field_dict["qty"] = qty
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        line_no = d.pop("lineNo", UNSET)

        qty = d.pop("qty", UNSET)

        amount = d.pop("amount", UNSET)

        receipt_line = cls(
            line_no=line_no,
            qty=qty,
            amount=amount,
        )

        receipt_line.additional_properties = d
        return receipt_line

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
