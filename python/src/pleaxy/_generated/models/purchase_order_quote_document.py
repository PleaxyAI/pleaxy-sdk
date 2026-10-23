from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.purchase_order_quote_document_content_type import (
    PurchaseOrderQuoteDocumentContentType,
    check_purchase_order_quote_document_content_type,
)
from ..models.purchase_order_quote_document_document_type import (
    PurchaseOrderQuoteDocumentDocumentType,
    check_purchase_order_quote_document_document_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PurchaseOrderQuoteDocument")


@_attrs_define
class PurchaseOrderQuoteDocument:
    """
    Attributes:
        import_id (Union[Unset, str]):
        file_name (Union[Unset, str]):
        content_type (Union[Unset, PurchaseOrderQuoteDocumentContentType]):
        added_at (Union[Unset, str]):
        added_by (Union[Unset, str]):
        quote_number (Union[Unset, str]):
        valid_until (Union[Unset, str]):
        document_type (Union[Unset, PurchaseOrderQuoteDocumentDocumentType]):
    """

    import_id: Union[Unset, str] = UNSET
    file_name: Union[Unset, str] = UNSET
    content_type: Union[Unset, PurchaseOrderQuoteDocumentContentType] = UNSET
    added_at: Union[Unset, str] = UNSET
    added_by: Union[Unset, str] = UNSET
    quote_number: Union[Unset, str] = UNSET
    valid_until: Union[Unset, str] = UNSET
    document_type: Union[Unset, PurchaseOrderQuoteDocumentDocumentType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        import_id = self.import_id

        file_name = self.file_name

        content_type: Union[Unset, str] = UNSET
        if not isinstance(self.content_type, Unset):
            content_type = self.content_type

        added_at = self.added_at

        added_by = self.added_by

        quote_number = self.quote_number

        valid_until = self.valid_until

        document_type: Union[Unset, str] = UNSET
        if not isinstance(self.document_type, Unset):
            document_type = self.document_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if import_id is not UNSET:
            field_dict["importId"] = import_id
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if added_at is not UNSET:
            field_dict["addedAt"] = added_at
        if added_by is not UNSET:
            field_dict["addedBy"] = added_by
        if quote_number is not UNSET:
            field_dict["quoteNumber"] = quote_number
        if valid_until is not UNSET:
            field_dict["validUntil"] = valid_until
        if document_type is not UNSET:
            field_dict["documentType"] = document_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        import_id = d.pop("importId", UNSET)

        file_name = d.pop("fileName", UNSET)

        _content_type = d.pop("contentType", UNSET)
        content_type: Union[Unset, PurchaseOrderQuoteDocumentContentType]
        if isinstance(_content_type, Unset):
            content_type = UNSET
        else:
            content_type = check_purchase_order_quote_document_content_type(
                _content_type
            )

        added_at = d.pop("addedAt", UNSET)

        added_by = d.pop("addedBy", UNSET)

        quote_number = d.pop("quoteNumber", UNSET)

        valid_until = d.pop("validUntil", UNSET)

        _document_type = d.pop("documentType", UNSET)
        document_type: Union[Unset, PurchaseOrderQuoteDocumentDocumentType]
        if isinstance(_document_type, Unset):
            document_type = UNSET
        else:
            document_type = check_purchase_order_quote_document_document_type(
                _document_type
            )

        purchase_order_quote_document = cls(
            import_id=import_id,
            file_name=file_name,
            content_type=content_type,
            added_at=added_at,
            added_by=added_by,
            quote_number=quote_number,
            valid_until=valid_until,
            document_type=document_type,
        )

        purchase_order_quote_document.additional_properties = d
        return purchase_order_quote_document

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
