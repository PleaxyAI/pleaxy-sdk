from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.supplier_bank_account_approval_by_side import (
    SupplierBankAccountApprovalBySide,
    check_supplier_bank_account_approval_by_side,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SupplierBankAccountApprovalBy")


@_attrs_define
class SupplierBankAccountApprovalBy:
    """
    Attributes:
        sub (Union[Unset, str]):
        name (Union[Unset, str]):
        side (Union[Unset, SupplierBankAccountApprovalBySide]):
    """

    sub: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    side: Union[Unset, SupplierBankAccountApprovalBySide] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sub = self.sub

        name = self.name

        side: Union[Unset, str] = UNSET
        if not isinstance(self.side, Unset):
            side = self.side

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sub is not UNSET:
            field_dict["sub"] = sub
        if name is not UNSET:
            field_dict["name"] = name
        if side is not UNSET:
            field_dict["side"] = side

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sub = d.pop("sub", UNSET)

        name = d.pop("name", UNSET)

        _side = d.pop("side", UNSET)
        side: Union[Unset, SupplierBankAccountApprovalBySide]
        if isinstance(_side, Unset):
            side = UNSET
        else:
            side = check_supplier_bank_account_approval_by_side(_side)

        supplier_bank_account_approval_by = cls(
            sub=sub,
            name=name,
            side=side,
        )

        supplier_bank_account_approval_by.additional_properties = d
        return supplier_bank_account_approval_by

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
