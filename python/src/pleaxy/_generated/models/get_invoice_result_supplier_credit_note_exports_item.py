from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetInvoiceResultSupplierCreditNoteExportsItem")


@_attrs_define
class GetInvoiceResultSupplierCreditNoteExportsItem:
    """
    Attributes:
        export_id (Union[Unset, str]):
        exported_at (Union[Unset, str]):
    """

    export_id: Union[Unset, str] = UNSET
    exported_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        export_id = self.export_id

        exported_at = self.exported_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if export_id is not UNSET:
            field_dict["exportId"] = export_id
        if exported_at is not UNSET:
            field_dict["exportedAt"] = exported_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        export_id = d.pop("exportId", UNSET)

        exported_at = d.pop("exportedAt", UNSET)

        get_invoice_result_supplier_credit_note_exports_item = cls(
            export_id=export_id,
            exported_at=exported_at,
        )

        get_invoice_result_supplier_credit_note_exports_item.additional_properties = d
        return get_invoice_result_supplier_credit_note_exports_item

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
