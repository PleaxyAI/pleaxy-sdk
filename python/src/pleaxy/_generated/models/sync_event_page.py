from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sync_event import SyncEvent


T = TypeVar("T", bound="SyncEventPage")


@_attrs_define
class SyncEventPage:
    """
    Attributes:
        events (Union[Unset, List['SyncEvent']]):
        next_cursor (Union[Unset, str]):
        has_more (Union[Unset, bool]):
    """

    events: Union[Unset, List["SyncEvent"]] = UNSET
    next_cursor: Union[Unset, str] = UNSET
    has_more: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        events: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)

        next_cursor = self.next_cursor

        has_more = self.has_more

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if events is not UNSET:
            field_dict["events"] = events
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor
        if has_more is not UNSET:
            field_dict["hasMore"] = has_more

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sync_event import SyncEvent

        d = src_dict.copy()
        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = SyncEvent.from_dict(events_item_data)

            events.append(events_item)

        next_cursor = d.pop("nextCursor", UNSET)

        has_more = d.pop("hasMore", UNSET)

        sync_event_page = cls(
            events=events,
            next_cursor=next_cursor,
            has_more=has_more,
        )

        sync_event_page.additional_properties = d
        return sync_event_page

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
