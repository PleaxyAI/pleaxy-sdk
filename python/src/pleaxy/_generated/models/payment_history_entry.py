from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.payment_history_entry_action import (
    PaymentHistoryEntryAction,
    check_payment_history_entry_action,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.payment_history_entry_record import PaymentHistoryEntryRecord
    from ..models.sole_payer_waiver_record import SolePayerWaiverRecord


T = TypeVar("T", bound="PaymentHistoryEntry")


@_attrs_define
class PaymentHistoryEntry:
    """
    Attributes:
        action (Union[Unset, PaymentHistoryEntryAction]):
        at (Union[Unset, str]):
        by (Union[Unset, str]):
        by_name (Union[Unset, str]):
        remittance_id (Union[Unset, str]):
        credit_note_id (Union[Unset, str]):
        amount (Union[Unset, float]):
        sole_payer (Union[Unset, SolePayerWaiverRecord]):
        record (Union[Unset, PaymentHistoryEntryRecord]):
    """

    action: Union[Unset, PaymentHistoryEntryAction] = UNSET
    at: Union[Unset, str] = UNSET
    by: Union[Unset, str] = UNSET
    by_name: Union[Unset, str] = UNSET
    remittance_id: Union[Unset, str] = UNSET
    credit_note_id: Union[Unset, str] = UNSET
    amount: Union[Unset, float] = UNSET
    sole_payer: Union[Unset, "SolePayerWaiverRecord"] = UNSET
    record: Union[Unset, "PaymentHistoryEntryRecord"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action: Union[Unset, str] = UNSET
        if not isinstance(self.action, Unset):
            action = self.action

        at = self.at

        by = self.by

        by_name = self.by_name

        remittance_id = self.remittance_id

        credit_note_id = self.credit_note_id

        amount = self.amount

        sole_payer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sole_payer, Unset):
            sole_payer = self.sole_payer.to_dict()

        record: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.record, Unset):
            record = self.record.to_dict()

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
        if remittance_id is not UNSET:
            field_dict["remittanceId"] = remittance_id
        if credit_note_id is not UNSET:
            field_dict["creditNoteId"] = credit_note_id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if sole_payer is not UNSET:
            field_dict["solePayer"] = sole_payer
        if record is not UNSET:
            field_dict["record"] = record

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.payment_history_entry_record import PaymentHistoryEntryRecord
        from ..models.sole_payer_waiver_record import SolePayerWaiverRecord

        d = src_dict.copy()
        _action = d.pop("action", UNSET)
        action: Union[Unset, PaymentHistoryEntryAction]
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = check_payment_history_entry_action(_action)

        at = d.pop("at", UNSET)

        by = d.pop("by", UNSET)

        by_name = d.pop("byName", UNSET)

        remittance_id = d.pop("remittanceId", UNSET)

        credit_note_id = d.pop("creditNoteId", UNSET)

        amount = d.pop("amount", UNSET)

        _sole_payer = d.pop("solePayer", UNSET)
        sole_payer: Union[Unset, SolePayerWaiverRecord]
        if isinstance(_sole_payer, Unset):
            sole_payer = UNSET
        else:
            sole_payer = SolePayerWaiverRecord.from_dict(_sole_payer)

        _record = d.pop("record", UNSET)
        record: Union[Unset, PaymentHistoryEntryRecord]
        if isinstance(_record, Unset):
            record = UNSET
        else:
            record = PaymentHistoryEntryRecord.from_dict(_record)

        payment_history_entry = cls(
            action=action,
            at=at,
            by=by,
            by_name=by_name,
            remittance_id=remittance_id,
            credit_note_id=credit_note_id,
            amount=amount,
            sole_payer=sole_payer,
            record=record,
        )

        payment_history_entry.additional_properties = d
        return payment_history_entry

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
