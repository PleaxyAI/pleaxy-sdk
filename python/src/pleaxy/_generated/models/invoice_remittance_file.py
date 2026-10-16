from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_remittance_file_content_type import (
    InvoiceRemittanceFileContentType,
    check_invoice_remittance_file_content_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceRemittanceFile")


@_attrs_define
class InvoiceRemittanceFile:
    """
    Attributes:
        file_id (Union[Unset, str]):
        file_name (Union[Unset, str]):
        content_type (Union[Unset, InvoiceRemittanceFileContentType]):
        size_bytes (Union[Unset, float]):
    """

    file_id: Union[Unset, str] = UNSET
    file_name: Union[Unset, str] = UNSET
    content_type: Union[Unset, InvoiceRemittanceFileContentType] = UNSET
    size_bytes: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        file_id = self.file_id

        file_name = self.file_name

        content_type: Union[Unset, str] = UNSET
        if not isinstance(self.content_type, Unset):
            content_type = self.content_type

        size_bytes = self.size_bytes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_id is not UNSET:
            field_dict["fileId"] = file_id
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if size_bytes is not UNSET:
            field_dict["sizeBytes"] = size_bytes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        file_id = d.pop("fileId", UNSET)

        file_name = d.pop("fileName", UNSET)

        _content_type = d.pop("contentType", UNSET)
        content_type: Union[Unset, InvoiceRemittanceFileContentType]
        if isinstance(_content_type, Unset):
            content_type = UNSET
        else:
            content_type = check_invoice_remittance_file_content_type(_content_type)

        size_bytes = d.pop("sizeBytes", UNSET)

        invoice_remittance_file = cls(
            file_id=file_id,
            file_name=file_name,
            content_type=content_type,
            size_bytes=size_bytes,
        )

        invoice_remittance_file.additional_properties = d
        return invoice_remittance_file

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
