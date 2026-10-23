from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.supplier_bank_details_confirmation_view_dispute_reason import (
    SupplierBankDetailsConfirmationViewDisputeReason,
    check_supplier_bank_details_confirmation_view_dispute_reason,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SupplierBankDetailsConfirmationViewDispute")


@_attrs_define
class SupplierBankDetailsConfirmationViewDispute:
    """
    Attributes:
        reason (Union[Unset, SupplierBankDetailsConfirmationViewDisputeReason]):
        note (Union[Unset, str]):
        at (Union[Unset, str]):
        by_name (Union[Unset, str]):
    """

    reason: Union[Unset, SupplierBankDetailsConfirmationViewDisputeReason] = UNSET
    note: Union[Unset, str] = UNSET
    at: Union[Unset, str] = UNSET
    by_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reason: Union[Unset, str] = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason

        note = self.note

        at = self.at

        by_name = self.by_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reason is not UNSET:
            field_dict["reason"] = reason
        if note is not UNSET:
            field_dict["note"] = note
        if at is not UNSET:
            field_dict["at"] = at
        if by_name is not UNSET:
            field_dict["byName"] = by_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _reason = d.pop("reason", UNSET)
        reason: Union[Unset, SupplierBankDetailsConfirmationViewDisputeReason]
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = check_supplier_bank_details_confirmation_view_dispute_reason(
                _reason
            )

        note = d.pop("note", UNSET)

        at = d.pop("at", UNSET)

        by_name = d.pop("byName", UNSET)

        supplier_bank_details_confirmation_view_dispute = cls(
            reason=reason,
            note=note,
            at=at,
            by_name=by_name,
        )

        supplier_bank_details_confirmation_view_dispute.additional_properties = d
        return supplier_bank_details_confirmation_view_dispute

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
