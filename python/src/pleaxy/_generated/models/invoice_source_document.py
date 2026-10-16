from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_source_document_content_type import (
    InvoiceSourceDocumentContentType,
    check_invoice_source_document_content_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceSourceDocument")


@_attrs_define
class InvoiceSourceDocument:
    """
    Attributes:
        import_id (Union[Unset, str]):
        file_name (Union[Unset, str]):
        content_type (Union[Unset, InvoiceSourceDocumentContentType]):
        stated_po_number (Union[Unset, str]):
    """

    import_id: Union[Unset, str] = UNSET
    file_name: Union[Unset, str] = UNSET
    content_type: Union[Unset, InvoiceSourceDocumentContentType] = UNSET
    stated_po_number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        import_id = self.import_id

        file_name = self.file_name

        content_type: Union[Unset, str] = UNSET
        if not isinstance(self.content_type, Unset):
            content_type = self.content_type

        stated_po_number = self.stated_po_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if import_id is not UNSET:
            field_dict["importId"] = import_id
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if stated_po_number is not UNSET:
            field_dict["statedPoNumber"] = stated_po_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        import_id = d.pop("importId", UNSET)

        file_name = d.pop("fileName", UNSET)

        _content_type = d.pop("contentType", UNSET)
        content_type: Union[Unset, InvoiceSourceDocumentContentType]
        if isinstance(_content_type, Unset):
            content_type = UNSET
        else:
            content_type = check_invoice_source_document_content_type(_content_type)

        stated_po_number = d.pop("statedPoNumber", UNSET)

        invoice_source_document = cls(
            import_id=import_id,
            file_name=file_name,
            content_type=content_type,
            stated_po_number=stated_po_number,
        )

        invoice_source_document.additional_properties = d
        return invoice_source_document

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
