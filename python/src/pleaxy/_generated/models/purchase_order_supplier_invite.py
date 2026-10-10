from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.purchase_order_supplier_invite_status import (
    PurchaseOrderSupplierInviteStatus,
    check_purchase_order_supplier_invite_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PurchaseOrderSupplierInvite")


@_attrs_define
class PurchaseOrderSupplierInvite:
    """
    Attributes:
        status (Union[Unset, PurchaseOrderSupplierInviteStatus]):
        connection_id (Union[Unset, str]):
        at (Union[Unset, str]):
    """

    status: Union[Unset, PurchaseOrderSupplierInviteStatus] = UNSET
    connection_id: Union[Unset, str] = UNSET
    at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        connection_id = self.connection_id

        at = self.at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if connection_id is not UNSET:
            field_dict["connectionId"] = connection_id
        if at is not UNSET:
            field_dict["at"] = at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, PurchaseOrderSupplierInviteStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_purchase_order_supplier_invite_status(_status)

        connection_id = d.pop("connectionId", UNSET)

        at = d.pop("at", UNSET)

        purchase_order_supplier_invite = cls(
            status=status,
            connection_id=connection_id,
            at=at,
        )

        purchase_order_supplier_invite.additional_properties = d
        return purchase_order_supplier_invite

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
