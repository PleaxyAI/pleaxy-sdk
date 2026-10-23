from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bank_details_confirmation_dispute_reason import (
    BankDetailsConfirmationDisputeReason,
    check_bank_details_confirmation_dispute_reason,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bank_details_confirmation_dispute_by import (
        BankDetailsConfirmationDisputeBy,
    )


T = TypeVar("T", bound="BankDetailsConfirmationDispute")


@_attrs_define
class BankDetailsConfirmationDispute:
    """
    Attributes:
        reason (Union[Unset, BankDetailsConfirmationDisputeReason]):
        note (Union[Unset, str]):
        at (Union[Unset, str]):
        by (Union[Unset, BankDetailsConfirmationDisputeBy]):
    """

    reason: Union[Unset, BankDetailsConfirmationDisputeReason] = UNSET
    note: Union[Unset, str] = UNSET
    at: Union[Unset, str] = UNSET
    by: Union[Unset, "BankDetailsConfirmationDisputeBy"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reason: Union[Unset, str] = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason

        note = self.note

        at = self.at

        by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.by, Unset):
            by = self.by.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reason is not UNSET:
            field_dict["reason"] = reason
        if note is not UNSET:
            field_dict["note"] = note
        if at is not UNSET:
            field_dict["at"] = at
        if by is not UNSET:
            field_dict["by"] = by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bank_details_confirmation_dispute_by import (
            BankDetailsConfirmationDisputeBy,
        )

        d = src_dict.copy()
        _reason = d.pop("reason", UNSET)
        reason: Union[Unset, BankDetailsConfirmationDisputeReason]
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = check_bank_details_confirmation_dispute_reason(_reason)

        note = d.pop("note", UNSET)

        at = d.pop("at", UNSET)

        _by = d.pop("by", UNSET)
        by: Union[Unset, BankDetailsConfirmationDisputeBy]
        if isinstance(_by, Unset):
            by = UNSET
        else:
            by = BankDetailsConfirmationDisputeBy.from_dict(_by)

        bank_details_confirmation_dispute = cls(
            reason=reason,
            note=note,
            at=at,
            by=by,
        )

        bank_details_confirmation_dispute.additional_properties = d
        return bank_details_confirmation_dispute

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
