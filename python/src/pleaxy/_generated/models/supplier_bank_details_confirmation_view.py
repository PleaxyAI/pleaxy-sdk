from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.supplier_bank_details_confirmation_view_changed_fields_item import (
    SupplierBankDetailsConfirmationViewChangedFieldsItem,
    check_supplier_bank_details_confirmation_view_changed_fields_item,
)
from ..models.supplier_bank_details_confirmation_view_confirmed_via import (
    SupplierBankDetailsConfirmationViewConfirmedVia,
    check_supplier_bank_details_confirmation_view_confirmed_via,
)
from ..models.supplier_bank_details_confirmation_view_status import (
    SupplierBankDetailsConfirmationViewStatus,
    check_supplier_bank_details_confirmation_view_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.supplier_bank_details_confirmation_view_dispute import (
        SupplierBankDetailsConfirmationViewDispute,
    )


T = TypeVar("T", bound="SupplierBankDetailsConfirmationView")


@_attrs_define
class SupplierBankDetailsConfirmationView:
    """
    Attributes:
        status (Union[Unset, SupplierBankDetailsConfirmationViewStatus]):
        requested_at (Union[Unset, str]):
        supplier_can_confirm (Union[Unset, bool]):
        confirmed_via (Union[Unset, SupplierBankDetailsConfirmationViewConfirmedVia]):
        confirmed_at (Union[Unset, str]):
        confirmed_by_name (Union[Unset, str]):
        dispute (Union[Unset, SupplierBankDetailsConfirmationViewDispute]):
        changed_fields (Union[Unset, List[SupplierBankDetailsConfirmationViewChangedFieldsItem]]):
    """

    status: Union[Unset, SupplierBankDetailsConfirmationViewStatus] = UNSET
    requested_at: Union[Unset, str] = UNSET
    supplier_can_confirm: Union[Unset, bool] = UNSET
    confirmed_via: Union[Unset, SupplierBankDetailsConfirmationViewConfirmedVia] = UNSET
    confirmed_at: Union[Unset, str] = UNSET
    confirmed_by_name: Union[Unset, str] = UNSET
    dispute: Union[Unset, "SupplierBankDetailsConfirmationViewDispute"] = UNSET
    changed_fields: Union[
        Unset, List[SupplierBankDetailsConfirmationViewChangedFieldsItem]
    ] = UNSET
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

        confirmed_by_name = self.confirmed_by_name

        dispute: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dispute, Unset):
            dispute = self.dispute.to_dict()

        changed_fields: Union[Unset, List[str]] = UNSET
        if not isinstance(self.changed_fields, Unset):
            changed_fields = []
            for changed_fields_item_data in self.changed_fields:
                changed_fields_item: str = changed_fields_item_data
                changed_fields.append(changed_fields_item)

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
        if confirmed_by_name is not UNSET:
            field_dict["confirmedByName"] = confirmed_by_name
        if dispute is not UNSET:
            field_dict["dispute"] = dispute
        if changed_fields is not UNSET:
            field_dict["changedFields"] = changed_fields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.supplier_bank_details_confirmation_view_dispute import (
            SupplierBankDetailsConfirmationViewDispute,
        )

        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, SupplierBankDetailsConfirmationViewStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_supplier_bank_details_confirmation_view_status(_status)

        requested_at = d.pop("requestedAt", UNSET)

        supplier_can_confirm = d.pop("supplierCanConfirm", UNSET)

        _confirmed_via = d.pop("confirmedVia", UNSET)
        confirmed_via: Union[Unset, SupplierBankDetailsConfirmationViewConfirmedVia]
        if isinstance(_confirmed_via, Unset):
            confirmed_via = UNSET
        else:
            confirmed_via = check_supplier_bank_details_confirmation_view_confirmed_via(
                _confirmed_via
            )

        confirmed_at = d.pop("confirmedAt", UNSET)

        confirmed_by_name = d.pop("confirmedByName", UNSET)

        _dispute = d.pop("dispute", UNSET)
        dispute: Union[Unset, SupplierBankDetailsConfirmationViewDispute]
        if isinstance(_dispute, Unset):
            dispute = UNSET
        else:
            dispute = SupplierBankDetailsConfirmationViewDispute.from_dict(_dispute)

        changed_fields = []
        _changed_fields = d.pop("changedFields", UNSET)
        for changed_fields_item_data in _changed_fields or []:
            changed_fields_item = (
                check_supplier_bank_details_confirmation_view_changed_fields_item(
                    changed_fields_item_data
                )
            )

            changed_fields.append(changed_fields_item)

        supplier_bank_details_confirmation_view = cls(
            status=status,
            requested_at=requested_at,
            supplier_can_confirm=supplier_can_confirm,
            confirmed_via=confirmed_via,
            confirmed_at=confirmed_at,
            confirmed_by_name=confirmed_by_name,
            dispute=dispute,
            changed_fields=changed_fields,
        )

        supplier_bank_details_confirmation_view.additional_properties = d
        return supplier_bank_details_confirmation_view

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
