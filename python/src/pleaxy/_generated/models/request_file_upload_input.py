from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.request_file_upload_input_content_type import (
    RequestFileUploadInputContentType,
    check_request_file_upload_input_content_type,
)

T = TypeVar("T", bound="RequestFileUploadInput")


@_attrs_define
class RequestFileUploadInput:
    """
    Attributes:
        content_type (RequestFileUploadInputContentType): PDF, image, Word, Excel, CSV or text, up to 25 MB.
    """

    content_type: RequestFileUploadInputContentType
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content_type: str = self.content_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contentType": content_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        content_type = check_request_file_upload_input_content_type(
            d.pop("contentType")
        )

        request_file_upload_input = cls(
            content_type=content_type,
        )

        request_file_upload_input.additional_properties = d
        return request_file_upload_input

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
