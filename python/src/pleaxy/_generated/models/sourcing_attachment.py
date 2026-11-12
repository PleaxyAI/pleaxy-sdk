from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sourcing_attachment_source import (
    SourcingAttachmentSource,
    check_sourcing_attachment_source,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SourcingAttachment")


@_attrs_define
class SourcingAttachment:
    """
    Attributes:
        id (str):
        file_name (Union[Unset, str]):
        content_type (Union[Unset, str]):
        size_bytes (Union[Unset, float]):
        added_at (Union[Unset, str]):
        source (Union[Unset, SourcingAttachmentSource]):
        shared (Union[Unset, bool]):
    """

    id: str
    file_name: Union[Unset, str] = UNSET
    content_type: Union[Unset, str] = UNSET
    size_bytes: Union[Unset, float] = UNSET
    added_at: Union[Unset, str] = UNSET
    source: Union[Unset, SourcingAttachmentSource] = UNSET
    shared: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        file_name = self.file_name

        content_type = self.content_type

        size_bytes = self.size_bytes

        added_at = self.added_at

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source

        shared = self.shared

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if size_bytes is not UNSET:
            field_dict["sizeBytes"] = size_bytes
        if added_at is not UNSET:
            field_dict["addedAt"] = added_at
        if source is not UNSET:
            field_dict["source"] = source
        if shared is not UNSET:
            field_dict["shared"] = shared

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        file_name = d.pop("fileName", UNSET)

        content_type = d.pop("contentType", UNSET)

        size_bytes = d.pop("sizeBytes", UNSET)

        added_at = d.pop("addedAt", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, SourcingAttachmentSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = check_sourcing_attachment_source(_source)

        shared = d.pop("shared", UNSET)

        sourcing_attachment = cls(
            id=id,
            file_name=file_name,
            content_type=content_type,
            size_bytes=size_bytes,
            added_at=added_at,
            source=source,
            shared=shared,
        )

        sourcing_attachment.additional_properties = d
        return sourcing_attachment

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
