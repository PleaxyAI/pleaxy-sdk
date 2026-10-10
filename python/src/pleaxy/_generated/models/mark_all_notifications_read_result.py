from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MarkAllNotificationsReadResult")


@_attrs_define
class MarkAllNotificationsReadResult:
    """
    Attributes:
        updated (Union[Unset, float]):
        remaining (Union[Unset, bool]):
        next_cursor (Union[Unset, str]):
    """

    updated: Union[Unset, float] = UNSET
    remaining: Union[Unset, bool] = UNSET
    next_cursor: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        updated = self.updated

        remaining = self.remaining

        next_cursor = self.next_cursor

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if updated is not UNSET:
            field_dict["updated"] = updated
        if remaining is not UNSET:
            field_dict["remaining"] = remaining
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        updated = d.pop("updated", UNSET)

        remaining = d.pop("remaining", UNSET)

        next_cursor = d.pop("nextCursor", UNSET)

        mark_all_notifications_read_result = cls(
            updated=updated,
            remaining=remaining,
            next_cursor=next_cursor,
        )

        mark_all_notifications_read_result.additional_properties = d
        return mark_all_notifications_read_result

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
