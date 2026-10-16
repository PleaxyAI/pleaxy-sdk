from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.credit_note_history_entry_action import (
    CreditNoteHistoryEntryAction,
    check_credit_note_history_entry_action,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreditNoteHistoryEntry")


@_attrs_define
class CreditNoteHistoryEntry:
    """
    Attributes:
        action (Union[Unset, CreditNoteHistoryEntryAction]):
        at (Union[Unset, str]):
        by (Union[Unset, str]):
        by_name (Union[Unset, str]):
        invoice_id (Union[Unset, str]):
        amount (Union[Unset, float]):
        export_id (Union[Unset, str]):
    """

    action: Union[Unset, CreditNoteHistoryEntryAction] = UNSET
    at: Union[Unset, str] = UNSET
    by: Union[Unset, str] = UNSET
    by_name: Union[Unset, str] = UNSET
    invoice_id: Union[Unset, str] = UNSET
    amount: Union[Unset, float] = UNSET
    export_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action: Union[Unset, str] = UNSET
        if not isinstance(self.action, Unset):
            action = self.action

        at = self.at

        by = self.by

        by_name = self.by_name

        invoice_id = self.invoice_id

        amount = self.amount

        export_id = self.export_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if at is not UNSET:
            field_dict["at"] = at
        if by is not UNSET:
            field_dict["by"] = by
        if by_name is not UNSET:
            field_dict["byName"] = by_name
        if invoice_id is not UNSET:
            field_dict["invoiceId"] = invoice_id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if export_id is not UNSET:
            field_dict["exportId"] = export_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _action = d.pop("action", UNSET)
        action: Union[Unset, CreditNoteHistoryEntryAction]
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = check_credit_note_history_entry_action(_action)

        at = d.pop("at", UNSET)

        by = d.pop("by", UNSET)

        by_name = d.pop("byName", UNSET)

        invoice_id = d.pop("invoiceId", UNSET)

        amount = d.pop("amount", UNSET)

        export_id = d.pop("exportId", UNSET)

        credit_note_history_entry = cls(
            action=action,
            at=at,
            by=by,
            by_name=by_name,
            invoice_id=invoice_id,
            amount=amount,
            export_id=export_id,
        )

        credit_note_history_entry.additional_properties = d
        return credit_note_history_entry

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
