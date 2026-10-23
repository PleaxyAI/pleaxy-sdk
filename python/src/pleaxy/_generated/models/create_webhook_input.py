from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWebhookInput")


@_attrs_define
class CreateWebhookInput:
    """
    Attributes:
        url (str): https:// address on a host name that answers a POST with a 2xx within 10 seconds.
        description (Union[Unset, str]): Up to 100 characters, to tell endpoints apart.
        events (Union[Unset, List[str]]): The event types to send (ListSyncEvents' types for your side). Leave out, or
            send [], for all of them.
    """

    url: str
    description: Union[Unset, str] = UNSET
    events: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url

        description = self.description

        events: Union[Unset, List[str]] = UNSET
        if not isinstance(self.events, Unset):
            events = self.events

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        description = d.pop("description", UNSET)

        events = cast(List[str], d.pop("events", UNSET))

        create_webhook_input = cls(
            url=url,
            description=description,
            events=events,
        )

        create_webhook_input.additional_properties = d
        return create_webhook_input

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
