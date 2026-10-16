from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.supplier_remittance_view_file_content_type import (
    SupplierRemittanceViewFileContentType,
    check_supplier_remittance_view_file_content_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SupplierRemittanceViewFile")


@_attrs_define
class SupplierRemittanceViewFile:
    """
    Attributes:
        file_name (Union[Unset, str]):
        content_type (Union[Unset, SupplierRemittanceViewFileContentType]):
        size_bytes (Union[Unset, float]):
    """

    file_name: Union[Unset, str] = UNSET
    content_type: Union[Unset, SupplierRemittanceViewFileContentType] = UNSET
    size_bytes: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        file_name = self.file_name

        content_type: Union[Unset, str] = UNSET
        if not isinstance(self.content_type, Unset):
            content_type = self.content_type

        size_bytes = self.size_bytes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        file_name = d.pop("fileName", UNSET)

        _content_type = d.pop("contentType", UNSET)
        content_type: Union[Unset, SupplierRemittanceViewFileContentType]
        if isinstance(_content_type, Unset):
            content_type = UNSET
        else:
            content_type = check_supplier_remittance_view_file_content_type(
                _content_type
            )

        size_bytes = d.pop("sizeBytes", UNSET)

        supplier_remittance_view_file = cls(
            file_name=file_name,
            content_type=content_type,
            size_bytes=size_bytes,
        )

        supplier_remittance_view_file.additional_properties = d
        return supplier_remittance_view_file

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
