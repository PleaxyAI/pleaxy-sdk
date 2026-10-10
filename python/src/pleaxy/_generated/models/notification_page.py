from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification import Notification


T = TypeVar("T", bound="NotificationPage")


@_attrs_define
class NotificationPage:
    """
    Attributes:
        items (Union[Unset, List['Notification']]):
        next_cursor (Union[Unset, str]):
        unread_count (Union[Unset, float]):
    """

    items: Union[Unset, List["Notification"]] = UNSET
    next_cursor: Union[Unset, str] = UNSET
    unread_count: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        next_cursor = self.next_cursor

        unread_count = self.unread_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if items is not UNSET:
            field_dict["items"] = items
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor
        if unread_count is not UNSET:
            field_dict["unreadCount"] = unread_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.notification import Notification

        d = src_dict.copy()
        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = Notification.from_dict(items_item_data)

            items.append(items_item)

        next_cursor = d.pop("nextCursor", UNSET)

        unread_count = d.pop("unreadCount", UNSET)

        notification_page = cls(
            items=items,
            next_cursor=next_cursor,
            unread_count=unread_count,
        )

        notification_page.additional_properties = d
        return notification_page

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
