from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bank_account_view_pending_change_side import (
    BankAccountViewPendingChangeSide,
    check_bank_account_view_pending_change_side,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.remittance_instructions import RemittanceInstructions


T = TypeVar("T", bound="BankAccountViewPendingChange")


@_attrs_define
class BankAccountViewPendingChange:
    """
    Attributes:
        details (Union[Unset, RemittanceInstructions]):
        invoice_id (Union[Unset, str]):
        side (Union[Unset, BankAccountViewPendingChangeSide]):
        at (Union[Unset, str]):
    """

    details: Union[Unset, "RemittanceInstructions"] = UNSET
    invoice_id: Union[Unset, str] = UNSET
    side: Union[Unset, BankAccountViewPendingChangeSide] = UNSET
    at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        invoice_id = self.invoice_id

        side: Union[Unset, str] = UNSET
        if not isinstance(self.side, Unset):
            side = self.side

        at = self.at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if details is not UNSET:
            field_dict["details"] = details
        if invoice_id is not UNSET:
            field_dict["invoiceId"] = invoice_id
        if side is not UNSET:
            field_dict["side"] = side
        if at is not UNSET:
            field_dict["at"] = at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.remittance_instructions import RemittanceInstructions

        d = src_dict.copy()
        _details = d.pop("details", UNSET)
        details: Union[Unset, RemittanceInstructions]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = RemittanceInstructions.from_dict(_details)

        invoice_id = d.pop("invoiceId", UNSET)

        _side = d.pop("side", UNSET)
        side: Union[Unset, BankAccountViewPendingChangeSide]
        if isinstance(_side, Unset):
            side = UNSET
        else:
            side = check_bank_account_view_pending_change_side(_side)

        at = d.pop("at", UNSET)

        bank_account_view_pending_change = cls(
            details=details,
            invoice_id=invoice_id,
            side=side,
            at=at,
        )

        bank_account_view_pending_change.additional_properties = d
        return bank_account_view_pending_change

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
