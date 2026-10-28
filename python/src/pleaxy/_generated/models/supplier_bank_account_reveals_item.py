from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.supplier_bank_account_reveals_item_by import (
        SupplierBankAccountRevealsItemBy,
    )


T = TypeVar("T", bound="SupplierBankAccountRevealsItem")


@_attrs_define
class SupplierBankAccountRevealsItem:
    """
    Attributes:
        at (Union[Unset, str]):
        by (Union[Unset, SupplierBankAccountRevealsItemBy]):
    """

    at: Union[Unset, str] = UNSET
    by: Union[Unset, "SupplierBankAccountRevealsItemBy"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        at = self.at

        by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.by, Unset):
            by = self.by.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if by is not UNSET:
            field_dict["by"] = by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.supplier_bank_account_reveals_item_by import (
            SupplierBankAccountRevealsItemBy,
        )

        d = src_dict.copy()
        at = d.pop("at", UNSET)

        _by = d.pop("by", UNSET)
        by: Union[Unset, SupplierBankAccountRevealsItemBy]
        if isinstance(_by, Unset):
            by = UNSET
        else:
            by = SupplierBankAccountRevealsItemBy.from_dict(_by)

        supplier_bank_account_reveals_item = cls(
            at=at,
            by=by,
        )

        supplier_bank_account_reveals_item.additional_properties = d
        return supplier_bank_account_reveals_item

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
