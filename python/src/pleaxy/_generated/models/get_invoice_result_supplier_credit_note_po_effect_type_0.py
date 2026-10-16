from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_invoice_result_supplier_credit_note_po_effect_type_0_kind import (
    GetInvoiceResultSupplierCreditNotePoEffectType0Kind,
    check_get_invoice_result_supplier_credit_note_po_effect_type_0_kind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetInvoiceResultSupplierCreditNotePoEffectType0")


@_attrs_define
class GetInvoiceResultSupplierCreditNotePoEffectType0:
    """
    Attributes:
        kind (Union[Unset, GetInvoiceResultSupplierCreditNotePoEffectType0Kind]):
        po (Union[Unset, str]):
        po_line_no (Union[Unset, float]):
        amount (Union[Unset, float]):
        qty (Union[Unset, float]):
    """

    kind: Union[Unset, GetInvoiceResultSupplierCreditNotePoEffectType0Kind] = UNSET
    po: Union[Unset, str] = UNSET
    po_line_no: Union[Unset, float] = UNSET
    amount: Union[Unset, float] = UNSET
    qty: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        po = self.po

        po_line_no = self.po_line_no

        amount = self.amount

        qty = self.qty

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if po is not UNSET:
            field_dict["po"] = po
        if po_line_no is not UNSET:
            field_dict["poLineNo"] = po_line_no
        if amount is not UNSET:
            field_dict["amount"] = amount
        if qty is not UNSET:
            field_dict["qty"] = qty

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, GetInvoiceResultSupplierCreditNotePoEffectType0Kind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_get_invoice_result_supplier_credit_note_po_effect_type_0_kind(
                _kind
            )

        po = d.pop("po", UNSET)

        po_line_no = d.pop("poLineNo", UNSET)

        amount = d.pop("amount", UNSET)

        qty = d.pop("qty", UNSET)

        get_invoice_result_supplier_credit_note_po_effect_type_0 = cls(
            kind=kind,
            po=po,
            po_line_no=po_line_no,
            amount=amount,
            qty=qty,
        )

        get_invoice_result_supplier_credit_note_po_effect_type_0.additional_properties = d
        return get_invoice_result_supplier_credit_note_po_effect_type_0

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
