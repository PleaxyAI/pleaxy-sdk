from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bank_details_confirmation_confirmed_via import (
    BankDetailsConfirmationConfirmedVia,
    check_bank_details_confirmation_confirmed_via,
)
from ..models.bank_details_confirmation_status import (
    BankDetailsConfirmationStatus,
    check_bank_details_confirmation_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bank_details_confirmation_confirmed_by import (
        BankDetailsConfirmationConfirmedBy,
    )
    from ..models.bank_details_confirmation_dispute import (
        BankDetailsConfirmationDispute,
    )
    from ..models.bank_details_confirmation_phone import BankDetailsConfirmationPhone


T = TypeVar("T", bound="BankDetailsConfirmation")


@_attrs_define
class BankDetailsConfirmation:
    """
    Attributes:
        status (Union[Unset, BankDetailsConfirmationStatus]):
        requested_at (Union[Unset, str]):
        supplier_can_confirm (Union[Unset, bool]):
        confirmed_via (Union[Unset, BankDetailsConfirmationConfirmedVia]):
        confirmed_at (Union[Unset, str]):
        confirmed_by (Union[Unset, BankDetailsConfirmationConfirmedBy]):
        phone (Union[Unset, BankDetailsConfirmationPhone]):
        dispute (Union[Unset, BankDetailsConfirmationDispute]):
    """

    status: Union[Unset, BankDetailsConfirmationStatus] = UNSET
    requested_at: Union[Unset, str] = UNSET
    supplier_can_confirm: Union[Unset, bool] = UNSET
    confirmed_via: Union[Unset, BankDetailsConfirmationConfirmedVia] = UNSET
    confirmed_at: Union[Unset, str] = UNSET
    confirmed_by: Union[Unset, "BankDetailsConfirmationConfirmedBy"] = UNSET
    phone: Union[Unset, "BankDetailsConfirmationPhone"] = UNSET
    dispute: Union[Unset, "BankDetailsConfirmationDispute"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        requested_at = self.requested_at

        supplier_can_confirm = self.supplier_can_confirm

        confirmed_via: Union[Unset, str] = UNSET
        if not isinstance(self.confirmed_via, Unset):
            confirmed_via = self.confirmed_via

        confirmed_at = self.confirmed_at

        confirmed_by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.confirmed_by, Unset):
            confirmed_by = self.confirmed_by.to_dict()

        phone: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.phone, Unset):
            phone = self.phone.to_dict()

        dispute: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dispute, Unset):
            dispute = self.dispute.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if requested_at is not UNSET:
            field_dict["requestedAt"] = requested_at
        if supplier_can_confirm is not UNSET:
            field_dict["supplierCanConfirm"] = supplier_can_confirm
        if confirmed_via is not UNSET:
            field_dict["confirmedVia"] = confirmed_via
        if confirmed_at is not UNSET:
            field_dict["confirmedAt"] = confirmed_at
        if confirmed_by is not UNSET:
            field_dict["confirmedBy"] = confirmed_by
        if phone is not UNSET:
            field_dict["phone"] = phone
        if dispute is not UNSET:
            field_dict["dispute"] = dispute

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bank_details_confirmation_confirmed_by import (
            BankDetailsConfirmationConfirmedBy,
        )
        from ..models.bank_details_confirmation_dispute import (
            BankDetailsConfirmationDispute,
        )
        from ..models.bank_details_confirmation_phone import (
            BankDetailsConfirmationPhone,
        )

        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, BankDetailsConfirmationStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_bank_details_confirmation_status(_status)

        requested_at = d.pop("requestedAt", UNSET)

        supplier_can_confirm = d.pop("supplierCanConfirm", UNSET)

        _confirmed_via = d.pop("confirmedVia", UNSET)
        confirmed_via: Union[Unset, BankDetailsConfirmationConfirmedVia]
        if isinstance(_confirmed_via, Unset):
            confirmed_via = UNSET
        else:
            confirmed_via = check_bank_details_confirmation_confirmed_via(
                _confirmed_via
            )

        confirmed_at = d.pop("confirmedAt", UNSET)

        _confirmed_by = d.pop("confirmedBy", UNSET)
        confirmed_by: Union[Unset, BankDetailsConfirmationConfirmedBy]
        if isinstance(_confirmed_by, Unset):
            confirmed_by = UNSET
        else:
            confirmed_by = BankDetailsConfirmationConfirmedBy.from_dict(_confirmed_by)

        _phone = d.pop("phone", UNSET)
        phone: Union[Unset, BankDetailsConfirmationPhone]
        if isinstance(_phone, Unset):
            phone = UNSET
        else:
            phone = BankDetailsConfirmationPhone.from_dict(_phone)

        _dispute = d.pop("dispute", UNSET)
        dispute: Union[Unset, BankDetailsConfirmationDispute]
        if isinstance(_dispute, Unset):
            dispute = UNSET
        else:
            dispute = BankDetailsConfirmationDispute.from_dict(_dispute)

        bank_details_confirmation = cls(
            status=status,
            requested_at=requested_at,
            supplier_can_confirm=supplier_can_confirm,
            confirmed_via=confirmed_via,
            confirmed_at=confirmed_at,
            confirmed_by=confirmed_by,
            phone=phone,
            dispute=dispute,
        )

        bank_details_confirmation.additional_properties = d
        return bank_details_confirmation

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
