from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.supplier_bank_account_learned_from_side import (
    SupplierBankAccountLearnedFromSide,
    check_supplier_bank_account_learned_from_side,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SupplierBankAccountLearnedFrom")


@_attrs_define
class SupplierBankAccountLearnedFrom:
    """
    Attributes:
        invoice_id (Union[Unset, str]):
        side (Union[Unset, SupplierBankAccountLearnedFromSide]):
    """

    invoice_id: Union[Unset, str] = UNSET
    side: Union[Unset, SupplierBankAccountLearnedFromSide] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoice_id = self.invoice_id

        side: Union[Unset, str] = UNSET
        if not isinstance(self.side, Unset):
            side = self.side

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invoice_id is not UNSET:
            field_dict["invoiceId"] = invoice_id
        if side is not UNSET:
            field_dict["side"] = side

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        invoice_id = d.pop("invoiceId", UNSET)

        _side = d.pop("side", UNSET)
        side: Union[Unset, SupplierBankAccountLearnedFromSide]
        if isinstance(_side, Unset):
            side = UNSET
        else:
            side = check_supplier_bank_account_learned_from_side(_side)

        supplier_bank_account_learned_from = cls(
            invoice_id=invoice_id,
            side=side,
        )

        supplier_bank_account_learned_from.additional_properties = d
        return supplier_bank_account_learned_from

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
