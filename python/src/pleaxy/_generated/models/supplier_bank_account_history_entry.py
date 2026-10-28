from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.supplier_bank_account_history_entry_check import (
    SupplierBankAccountHistoryEntryCheck,
    check_supplier_bank_account_history_entry_check,
)
from ..models.supplier_bank_account_history_entry_event import (
    SupplierBankAccountHistoryEntryEvent,
    check_supplier_bank_account_history_entry_event,
)
from ..models.supplier_bank_account_history_entry_verification import (
    SupplierBankAccountHistoryEntryVerification,
    check_supplier_bank_account_history_entry_verification,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SupplierBankAccountHistoryEntry")


@_attrs_define
class SupplierBankAccountHistoryEntry:
    """
    Attributes:
        at (Union[Unset, str]):
        event (Union[Unset, SupplierBankAccountHistoryEntryEvent]):
        masked (Union[Unset, str]):
        invoice_id (Union[Unset, str]):
        by (Union[Unset, str]):
        verification (Union[Unset, SupplierBankAccountHistoryEntryVerification]):
        check (Union[Unset, SupplierBankAccountHistoryEntryCheck]):
    """

    at: Union[Unset, str] = UNSET
    event: Union[Unset, SupplierBankAccountHistoryEntryEvent] = UNSET
    masked: Union[Unset, str] = UNSET
    invoice_id: Union[Unset, str] = UNSET
    by: Union[Unset, str] = UNSET
    verification: Union[Unset, SupplierBankAccountHistoryEntryVerification] = UNSET
    check: Union[Unset, SupplierBankAccountHistoryEntryCheck] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        at = self.at

        event: Union[Unset, str] = UNSET
        if not isinstance(self.event, Unset):
            event = self.event

        masked = self.masked

        invoice_id = self.invoice_id

        by = self.by

        verification: Union[Unset, str] = UNSET
        if not isinstance(self.verification, Unset):
            verification = self.verification

        check: Union[Unset, str] = UNSET
        if not isinstance(self.check, Unset):
            check = self.check

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if event is not UNSET:
            field_dict["event"] = event
        if masked is not UNSET:
            field_dict["masked"] = masked
        if invoice_id is not UNSET:
            field_dict["invoiceId"] = invoice_id
        if by is not UNSET:
            field_dict["by"] = by
        if verification is not UNSET:
            field_dict["verification"] = verification
        if check is not UNSET:
            field_dict["check"] = check

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        at = d.pop("at", UNSET)

        _event = d.pop("event", UNSET)
        event: Union[Unset, SupplierBankAccountHistoryEntryEvent]
        if isinstance(_event, Unset):
            event = UNSET
        else:
            event = check_supplier_bank_account_history_entry_event(_event)

        masked = d.pop("masked", UNSET)

        invoice_id = d.pop("invoiceId", UNSET)

        by = d.pop("by", UNSET)

        _verification = d.pop("verification", UNSET)
        verification: Union[Unset, SupplierBankAccountHistoryEntryVerification]
        if isinstance(_verification, Unset):
            verification = UNSET
        else:
            verification = check_supplier_bank_account_history_entry_verification(
                _verification
            )

        _check = d.pop("check", UNSET)
        check: Union[Unset, SupplierBankAccountHistoryEntryCheck]
        if isinstance(_check, Unset):
            check = UNSET
        else:
            check = check_supplier_bank_account_history_entry_check(_check)

        supplier_bank_account_history_entry = cls(
            at=at,
            event=event,
            masked=masked,
            invoice_id=invoice_id,
            by=by,
            verification=verification,
            check=check,
        )

        supplier_bank_account_history_entry.additional_properties = d
        return supplier_bank_account_history_entry

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
