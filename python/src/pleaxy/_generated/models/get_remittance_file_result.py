from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetRemittanceFileResult")


@_attrs_define
class GetRemittanceFileResult:
    """
    Attributes:
        url (Union[Unset, str]):
        file_name (Union[Unset, str]):
        content_type (Union[Unset, str]):
    """

    url: Union[Unset, str] = UNSET
    file_name: Union[Unset, str] = UNSET
    content_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url

        file_name = self.file_name

        content_type = self.content_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if content_type is not UNSET:
            field_dict["contentType"] = content_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url", UNSET)

        file_name = d.pop("fileName", UNSET)

        content_type = d.pop("contentType", UNSET)

        get_remittance_file_result = cls(
            url=url,
            file_name=file_name,
            content_type=content_type,
        )

        get_remittance_file_result.additional_properties = d
        return get_remittance_file_result

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
