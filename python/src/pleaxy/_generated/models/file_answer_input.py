from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FileAnswerInput")


@_attrs_define
class FileAnswerInput:
    """
    Attributes:
        file_id (str): The fileId the upload-url route returned
        file_name (str):
        content_type (str):
    """

    file_id: str
    file_name: str
    content_type: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        file_id = self.file_id

        file_name = self.file_name

        content_type = self.content_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fileId": file_id,
                "fileName": file_name,
                "contentType": content_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        file_id = d.pop("fileId")

        file_name = d.pop("fileName")

        content_type = d.pop("contentType")

        file_answer_input = cls(
            file_id=file_id,
            file_name=file_name,
            content_type=content_type,
        )

        file_answer_input.additional_properties = d
        return file_answer_input

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
