from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_invoice_result_supplier_credit_note_po_effect_type_1_kind import (
    GetInvoiceResultSupplierCreditNotePoEffectType1Kind,
    check_get_invoice_result_supplier_credit_note_po_effect_type_1_kind,
)
from ..models.get_invoice_result_supplier_credit_note_po_effect_type_1_why import (
    GetInvoiceResultSupplierCreditNotePoEffectType1Why,
    check_get_invoice_result_supplier_credit_note_po_effect_type_1_why,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetInvoiceResultSupplierCreditNotePoEffectType1")


@_attrs_define
class GetInvoiceResultSupplierCreditNotePoEffectType1:
    """
    Attributes:
        kind (Union[Unset, GetInvoiceResultSupplierCreditNotePoEffectType1Kind]):
        why (Union[Unset, GetInvoiceResultSupplierCreditNotePoEffectType1Why]):
    """

    kind: Union[Unset, GetInvoiceResultSupplierCreditNotePoEffectType1Kind] = UNSET
    why: Union[Unset, GetInvoiceResultSupplierCreditNotePoEffectType1Why] = UNSET
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
        kind: Union[Unset, GetInvoiceResultSupplierCreditNotePoEffectType1Kind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_get_invoice_result_supplier_credit_note_po_effect_type_1_kind(
                _kind
            )

        _why = d.pop("why", UNSET)
        why: Union[Unset, GetInvoiceResultSupplierCreditNotePoEffectType1Why]
        if isinstance(_why, Unset):
            why = UNSET
        else:
            why = check_get_invoice_result_supplier_credit_note_po_effect_type_1_why(
                _why
            )

        get_invoice_result_supplier_credit_note_po_effect_type_1 = cls(
            kind=kind,
            why=why,
        )

        get_invoice_result_supplier_credit_note_po_effect_type_1.additional_properties = d
        return get_invoice_result_supplier_credit_note_po_effect_type_1

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
