from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateFocusUploadResult")


@_attrs_define
class CreateFocusUploadResult:
    """
    Attributes:
        source_id (Union[Unset, str]):
        upload_id (Union[Unset, str]):
        upload_url (Union[Unset, str]):
        content_type (Union[Unset, str]):
        max_bytes (Union[Unset, float]):
    """

    source_id: Union[Unset, str] = UNSET
    upload_id: Union[Unset, str] = UNSET
    upload_url: Union[Unset, str] = UNSET
    content_type: Union[Unset, str] = UNSET
    max_bytes: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source_id = self.source_id

        upload_id = self.upload_id

        upload_url = self.upload_url

        content_type = self.content_type

        max_bytes = self.max_bytes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source_id is not UNSET:
            field_dict["sourceId"] = source_id
        if upload_id is not UNSET:
            field_dict["uploadId"] = upload_id
        if upload_url is not UNSET:
            field_dict["uploadUrl"] = upload_url
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if max_bytes is not UNSET:
            field_dict["maxBytes"] = max_bytes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        source_id = d.pop("sourceId", UNSET)

        upload_id = d.pop("uploadId", UNSET)

        upload_url = d.pop("uploadUrl", UNSET)

        content_type = d.pop("contentType", UNSET)

        max_bytes = d.pop("maxBytes", UNSET)

        create_focus_upload_result = cls(
            source_id=source_id,
            upload_id=upload_id,
            upload_url=upload_url,
            content_type=content_type,
            max_bytes=max_bytes,
        )

        create_focus_upload_result.additional_properties = d
        return create_focus_upload_result

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
