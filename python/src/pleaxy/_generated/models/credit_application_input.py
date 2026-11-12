from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreditApplicationInput")


@_attrs_define
class CreditApplicationInput:
    """
    Attributes:
        credit_note_id (str):
        amount (float): More than 0, in the invoice's currency, at most what's left of the credit note.
    """

    credit_note_id: str
    amount: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        credit_note_id = self.credit_note_id

        amount = self.amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "creditNoteId": credit_note_id,
                "amount": amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        credit_note_id = d.pop("creditNoteId")

        amount = d.pop("amount")

        credit_application_input = cls(
            credit_note_id=credit_note_id,
            amount=amount,
        )

        credit_application_input.additional_properties = d
        return credit_application_input

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
