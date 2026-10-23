from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_delivery_last_error_code import (
    WebhookDeliveryLastErrorCode,
    check_webhook_delivery_last_error_code,
)
from ..models.webhook_delivery_status import (
    WebhookDeliveryStatus,
    check_webhook_delivery_status,
)
from ..models.webhook_delivery_type import (
    WebhookDeliveryType,
    check_webhook_delivery_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookDelivery")


@_attrs_define
class WebhookDelivery:
    """
    Attributes:
        event_id (Union[Unset, str]):
        endpoint_id (Union[Unset, str]):
        type (Union[Unset, WebhookDeliveryType]):
        status (Union[Unset, WebhookDeliveryStatus]):
        attempts (Union[Unset, float]):
        created_at (Union[Unset, str]):
        next_attempt_at (Union[Unset, str]):
        last_attempt_at (Union[Unset, str]):
        last_status (Union[Unset, float]):
        last_error_code (Union[Unset, WebhookDeliveryLastErrorCode]):
        delivered_at (Union[Unset, str]):
    """

    event_id: Union[Unset, str] = UNSET
    endpoint_id: Union[Unset, str] = UNSET
    type: Union[Unset, WebhookDeliveryType] = UNSET
    status: Union[Unset, WebhookDeliveryStatus] = UNSET
    attempts: Union[Unset, float] = UNSET
    created_at: Union[Unset, str] = UNSET
    next_attempt_at: Union[Unset, str] = UNSET
    last_attempt_at: Union[Unset, str] = UNSET
    last_status: Union[Unset, float] = UNSET
    last_error_code: Union[Unset, WebhookDeliveryLastErrorCode] = UNSET
    delivered_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_id = self.event_id

        endpoint_id = self.endpoint_id

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        attempts = self.attempts

        created_at = self.created_at

        next_attempt_at = self.next_attempt_at

        last_attempt_at = self.last_attempt_at

        last_status = self.last_status

        last_error_code: Union[Unset, str] = UNSET
        if not isinstance(self.last_error_code, Unset):
            last_error_code = self.last_error_code

        delivered_at = self.delivered_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_id is not UNSET:
            field_dict["eventId"] = event_id
        if endpoint_id is not UNSET:
            field_dict["endpointId"] = endpoint_id
        if type is not UNSET:
            field_dict["type"] = type
        if status is not UNSET:
            field_dict["status"] = status
        if attempts is not UNSET:
            field_dict["attempts"] = attempts
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if next_attempt_at is not UNSET:
            field_dict["nextAttemptAt"] = next_attempt_at
        if last_attempt_at is not UNSET:
            field_dict["lastAttemptAt"] = last_attempt_at
        if last_status is not UNSET:
            field_dict["lastStatus"] = last_status
        if last_error_code is not UNSET:
            field_dict["lastErrorCode"] = last_error_code
        if delivered_at is not UNSET:
            field_dict["deliveredAt"] = delivered_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        event_id = d.pop("eventId", UNSET)

        endpoint_id = d.pop("endpointId", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, WebhookDeliveryType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = check_webhook_delivery_type(_type)

        _status = d.pop("status", UNSET)
        status: Union[Unset, WebhookDeliveryStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_webhook_delivery_status(_status)

        attempts = d.pop("attempts", UNSET)

        created_at = d.pop("createdAt", UNSET)

        next_attempt_at = d.pop("nextAttemptAt", UNSET)

        last_attempt_at = d.pop("lastAttemptAt", UNSET)

        last_status = d.pop("lastStatus", UNSET)

        _last_error_code = d.pop("lastErrorCode", UNSET)
        last_error_code: Union[Unset, WebhookDeliveryLastErrorCode]
        if isinstance(_last_error_code, Unset):
            last_error_code = UNSET
        else:
            last_error_code = check_webhook_delivery_last_error_code(_last_error_code)

        delivered_at = d.pop("deliveredAt", UNSET)

        webhook_delivery = cls(
            event_id=event_id,
            endpoint_id=endpoint_id,
            type=type,
            status=status,
            attempts=attempts,
            created_at=created_at,
            next_attempt_at=next_attempt_at,
            last_attempt_at=last_attempt_at,
            last_status=last_status,
            last_error_code=last_error_code,
            delivered_at=delivered_at,
        )

        webhook_delivery.additional_properties = d
        return webhook_delivery

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
