from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_webhooks_result_event_types_item import (
    ListWebhooksResultEventTypesItem,
    check_list_webhooks_result_event_types_item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_endpoint_view import WebhookEndpointView


T = TypeVar("T", bound="ListWebhooksResult")


@_attrs_define
class ListWebhooksResult:
    """
    Attributes:
        endpoints (Union[Unset, List['WebhookEndpointView']]):
        event_types (Union[Unset, List[ListWebhooksResultEventTypesItem]]):
    """

    endpoints: Union[Unset, List["WebhookEndpointView"]] = UNSET
    event_types: Union[Unset, List[ListWebhooksResultEventTypesItem]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        endpoints: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.endpoints, Unset):
            endpoints = []
            for endpoints_item_data in self.endpoints:
                endpoints_item = endpoints_item_data.to_dict()
                endpoints.append(endpoints_item)

        event_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.event_types, Unset):
            event_types = []
            for event_types_item_data in self.event_types:
                event_types_item: str = event_types_item_data
                event_types.append(event_types_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if endpoints is not UNSET:
            field_dict["endpoints"] = endpoints
        if event_types is not UNSET:
            field_dict["eventTypes"] = event_types

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.webhook_endpoint_view import WebhookEndpointView

        d = src_dict.copy()
        endpoints = []
        _endpoints = d.pop("endpoints", UNSET)
        for endpoints_item_data in _endpoints or []:
            endpoints_item = WebhookEndpointView.from_dict(endpoints_item_data)

            endpoints.append(endpoints_item)

        event_types = []
        _event_types = d.pop("eventTypes", UNSET)
        for event_types_item_data in _event_types or []:
            event_types_item = check_list_webhooks_result_event_types_item(
                event_types_item_data
            )

            event_types.append(event_types_item)

        list_webhooks_result = cls(
            endpoints=endpoints,
            event_types=event_types,
        )

        list_webhooks_result.additional_properties = d
        return list_webhooks_result

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
