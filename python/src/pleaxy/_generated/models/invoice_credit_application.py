from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceCreditApplication")


@_attrs_define
class InvoiceCreditApplication:
    """
    Attributes:
        id (str):
        credit_note_id (Union[Unset, str]):
        external_credit_note_number (Union[Unset, str]):
        amount (Union[Unset, float]):
        applied_at (Union[Unset, str]):
        applied_by (Union[Unset, str]):
        applied_by_name (Union[Unset, str]):
        auto (Union[Unset, bool]):
    """

    id: str
    credit_note_id: Union[Unset, str] = UNSET
    external_credit_note_number: Union[Unset, str] = UNSET
    amount: Union[Unset, float] = UNSET
    applied_at: Union[Unset, str] = UNSET
    applied_by: Union[Unset, str] = UNSET
    applied_by_name: Union[Unset, str] = UNSET
    auto: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        credit_note_id = self.credit_note_id

        external_credit_note_number = self.external_credit_note_number

        amount = self.amount

        applied_at = self.applied_at

        applied_by = self.applied_by

        applied_by_name = self.applied_by_name

        auto = self.auto

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if credit_note_id is not UNSET:
            field_dict["creditNoteId"] = credit_note_id
        if external_credit_note_number is not UNSET:
            field_dict["externalCreditNoteNumber"] = external_credit_note_number
        if amount is not UNSET:
            field_dict["amount"] = amount
        if applied_at is not UNSET:
            field_dict["appliedAt"] = applied_at
        if applied_by is not UNSET:
            field_dict["appliedBy"] = applied_by
        if applied_by_name is not UNSET:
            field_dict["appliedByName"] = applied_by_name
        if auto is not UNSET:
            field_dict["auto"] = auto

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        credit_note_id = d.pop("creditNoteId", UNSET)

        external_credit_note_number = d.pop("externalCreditNoteNumber", UNSET)

        amount = d.pop("amount", UNSET)

        applied_at = d.pop("appliedAt", UNSET)

        applied_by = d.pop("appliedBy", UNSET)

        applied_by_name = d.pop("appliedByName", UNSET)

        auto = d.pop("auto", UNSET)

        invoice_credit_application = cls(
            id=id,
            credit_note_id=credit_note_id,
            external_credit_note_number=external_credit_note_number,
            amount=amount,
            applied_at=applied_at,
            applied_by=applied_by,
            applied_by_name=applied_by_name,
            auto=auto,
        )

        invoice_credit_application.additional_properties = d
        return invoice_credit_application

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
