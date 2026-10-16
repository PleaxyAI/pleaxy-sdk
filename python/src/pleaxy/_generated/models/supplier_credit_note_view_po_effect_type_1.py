from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.supplier_credit_note_view_po_effect_type_1_kind import (
    SupplierCreditNoteViewPoEffectType1Kind,
    check_supplier_credit_note_view_po_effect_type_1_kind,
)
from ..models.supplier_credit_note_view_po_effect_type_1_why import (
    SupplierCreditNoteViewPoEffectType1Why,
    check_supplier_credit_note_view_po_effect_type_1_why,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SupplierCreditNoteViewPoEffectType1")


@_attrs_define
class SupplierCreditNoteViewPoEffectType1:
    """
    Attributes:
        kind (Union[Unset, SupplierCreditNoteViewPoEffectType1Kind]):
        why (Union[Unset, SupplierCreditNoteViewPoEffectType1Why]):
    """

    kind: Union[Unset, SupplierCreditNoteViewPoEffectType1Kind] = UNSET
    why: Union[Unset, SupplierCreditNoteViewPoEffectType1Why] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        why: Union[Unset, str] = UNSET
        if not isinstance(self.why, Unset):
            why = self.why

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if why is not UNSET:
            field_dict["why"] = why

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, SupplierCreditNoteViewPoEffectType1Kind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_supplier_credit_note_view_po_effect_type_1_kind(_kind)

        _why = d.pop("why", UNSET)
        why: Union[Unset, SupplierCreditNoteViewPoEffectType1Why]
        if isinstance(_why, Unset):
            why = UNSET
        else:
            why = check_supplier_credit_note_view_po_effect_type_1_why(_why)

        supplier_credit_note_view_po_effect_type_1 = cls(
            kind=kind,
            why=why,
        )

        supplier_credit_note_view_po_effect_type_1.additional_properties = d
        return supplier_credit_note_view_po_effect_type_1

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
