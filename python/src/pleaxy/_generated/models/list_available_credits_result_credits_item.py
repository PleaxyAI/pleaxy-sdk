from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_available_credits_result_credits_item_reason import (
    ListAvailableCreditsResultCreditsItemReason,
    check_list_available_credits_result_credits_item_reason,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListAvailableCreditsResultCreditsItem")


@_attrs_define
class ListAvailableCreditsResultCreditsItem:
    """
    Attributes:
        credit_note_id (Union[Unset, str]):
        external_credit_note_number (Union[Unset, str]):
        reason (Union[Unset, ListAvailableCreditsResultCreditsItemReason]):
        issue_date (Union[Unset, str]):
        amount (Union[Unset, float]):
        remaining (Union[Unset, float]):
        suggested (Union[Unset, float]):
    """

    credit_note_id: Union[Unset, str] = UNSET
    external_credit_note_number: Union[Unset, str] = UNSET
    reason: Union[Unset, ListAvailableCreditsResultCreditsItemReason] = UNSET
    issue_date: Union[Unset, str] = UNSET
    amount: Union[Unset, float] = UNSET
    remaining: Union[Unset, float] = UNSET
    suggested: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        credit_note_id = self.credit_note_id

        external_credit_note_number = self.external_credit_note_number

        reason: Union[Unset, str] = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason

        issue_date = self.issue_date

        amount = self.amount

        remaining = self.remaining

        suggested = self.suggested

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if credit_note_id is not UNSET:
            field_dict["creditNoteId"] = credit_note_id
        if external_credit_note_number is not UNSET:
            field_dict["externalCreditNoteNumber"] = external_credit_note_number
        if reason is not UNSET:
            field_dict["reason"] = reason
        if issue_date is not UNSET:
            field_dict["issueDate"] = issue_date
        if amount is not UNSET:
            field_dict["amount"] = amount
        if remaining is not UNSET:
            field_dict["remaining"] = remaining
        if suggested is not UNSET:
            field_dict["suggested"] = suggested

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        credit_note_id = d.pop("creditNoteId", UNSET)

        external_credit_note_number = d.pop("externalCreditNoteNumber", UNSET)

        _reason = d.pop("reason", UNSET)
        reason: Union[Unset, ListAvailableCreditsResultCreditsItemReason]
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = check_list_available_credits_result_credits_item_reason(_reason)

        issue_date = d.pop("issueDate", UNSET)

        amount = d.pop("amount", UNSET)

        remaining = d.pop("remaining", UNSET)

        suggested = d.pop("suggested", UNSET)

        list_available_credits_result_credits_item = cls(
            credit_note_id=credit_note_id,
            external_credit_note_number=external_credit_note_number,
            reason=reason,
            issue_date=issue_date,
            amount=amount,
            remaining=remaining,
            suggested=suggested,
        )

        list_available_credits_result_credits_item.additional_properties = d
        return list_available_credits_result_credits_item

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
