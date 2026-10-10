from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.purchase_order_supplier_view_quote_document_content_type import (
    PurchaseOrderSupplierViewQuoteDocumentContentType,
    check_purchase_order_supplier_view_quote_document_content_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PurchaseOrderSupplierViewQuoteDocument")


@_attrs_define
class PurchaseOrderSupplierViewQuoteDocument:
    """
    Attributes:
        import_id (Union[Unset, str]):
        file_name (Union[Unset, str]):
        content_type (Union[Unset, PurchaseOrderSupplierViewQuoteDocumentContentType]):
        added_at (Union[Unset, str]):
        quote_number (Union[Unset, str]):
        valid_until (Union[Unset, str]):
    """

    import_id: Union[Unset, str] = UNSET
    file_name: Union[Unset, str] = UNSET
    content_type: Union[Unset, PurchaseOrderSupplierViewQuoteDocumentContentType] = (
        UNSET
    )
    added_at: Union[Unset, str] = UNSET
    quote_number: Union[Unset, str] = UNSET
    valid_until: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        import_id = self.import_id

        file_name = self.file_name

        content_type: Union[Unset, str] = UNSET
        if not isinstance(self.content_type, Unset):
            content_type = self.content_type

        added_at = self.added_at

        quote_number = self.quote_number

        valid_until = self.valid_until

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
        if quote_number is not UNSET:
            field_dict["quoteNumber"] = quote_number
        if valid_until is not UNSET:
            field_dict["validUntil"] = valid_until

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        import_id = d.pop("importId", UNSET)

        file_name = d.pop("fileName", UNSET)

        _content_type = d.pop("contentType", UNSET)
        content_type: Union[Unset, PurchaseOrderSupplierViewQuoteDocumentContentType]
        if isinstance(_content_type, Unset):
            content_type = UNSET
        else:
            content_type = (
                check_purchase_order_supplier_view_quote_document_content_type(
                    _content_type
                )
            )

        added_at = d.pop("addedAt", UNSET)

        quote_number = d.pop("quoteNumber", UNSET)

        valid_until = d.pop("validUntil", UNSET)

        purchase_order_supplier_view_quote_document = cls(
            import_id=import_id,
            file_name=file_name,
            content_type=content_type,
            added_at=added_at,
            quote_number=quote_number,
            valid_until=valid_until,
        )

        purchase_order_supplier_view_quote_document.additional_properties = d
        return purchase_order_supplier_view_quote_document

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
