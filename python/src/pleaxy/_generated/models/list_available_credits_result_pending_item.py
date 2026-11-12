from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_available_credits_result_pending_item_reason import (
    ListAvailableCreditsResultPendingItemReason,
    check_list_available_credits_result_pending_item_reason,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListAvailableCreditsResultPendingItem")


@_attrs_define
class ListAvailableCreditsResultPendingItem:
    """
    Attributes:
        credit_note_id (Union[Unset, str]):
        external_credit_note_number (Union[Unset, str]):
        reason (Union[Unset, ListAvailableCreditsResultPendingItemReason]):
        amount (Union[Unset, float]):
    """

    credit_note_id: Union[Unset, str] = UNSET
    external_credit_note_number: Union[Unset, str] = UNSET
    reason: Union[Unset, ListAvailableCreditsResultPendingItemReason] = UNSET
    amount: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        credit_note_id = self.credit_note_id

        external_credit_note_number = self.external_credit_note_number

        reason: Union[Unset, str] = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason

        amount = self.amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if credit_note_id is not UNSET:
            field_dict["creditNoteId"] = credit_note_id
        if external_credit_note_number is not UNSET:
            field_dict["externalCreditNoteNumber"] = external_credit_note_number
        if reason is not UNSET:
            field_dict["reason"] = reason
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        credit_note_id = d.pop("creditNoteId", UNSET)

        external_credit_note_number = d.pop("externalCreditNoteNumber", UNSET)

        _reason = d.pop("reason", UNSET)
        reason: Union[Unset, ListAvailableCreditsResultPendingItemReason]
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = check_list_available_credits_result_pending_item_reason(_reason)

        amount = d.pop("amount", UNSET)

        list_available_credits_result_pending_item = cls(
            credit_note_id=credit_note_id,
            external_credit_note_number=external_credit_note_number,
            reason=reason,
            amount=amount,
        )

        list_available_credits_result_pending_item.additional_properties = d
        return list_available_credits_result_pending_item

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
