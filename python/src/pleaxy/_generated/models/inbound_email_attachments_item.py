from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InboundEmailAttachmentsItem")


@_attrs_define
class InboundEmailAttachmentsItem:
    """
    Attributes:
        name (Union[Unset, str]):
        content_type (Union[Unset, str]):
        size (Union[Unset, float]):
    """

    name: Union[Unset, str] = UNSET
    content_type: Union[Unset, str] = UNSET
    size: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        content_type = self.content_type

        size = self.size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        content_type = d.pop("contentType", UNSET)

        size = d.pop("size", UNSET)

        inbound_email_attachments_item = cls(
            name=name,
            content_type=content_type,
            size=size,
        )

        inbound_email_attachments_item.additional_properties = d
        return inbound_email_attachments_item

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
