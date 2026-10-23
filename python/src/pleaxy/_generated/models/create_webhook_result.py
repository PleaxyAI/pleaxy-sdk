from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_webhook_result_events_item import (
    CreateWebhookResultEventsItem,
    check_create_webhook_result_events_item,
)
from ..models.create_webhook_result_last_error_code import (
    CreateWebhookResultLastErrorCode,
    check_create_webhook_result_last_error_code,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWebhookResult")


@_attrs_define
class CreateWebhookResult:
    """
    Attributes:
        id (str):
        url (Union[Unset, str]):
        description (Union[Unset, str]):
        events (Union[Unset, List[CreateWebhookResultEventsItem]]):
        enabled (Union[Unset, bool]):
        created_at (Union[Unset, str]):
        created_by (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        last_attempt_at (Union[Unset, str]):
        last_status (Union[Unset, float]):
        last_error_code (Union[Unset, CreateWebhookResultLastErrorCode]):
        last_success_at (Union[Unset, str]):
        failed_deliveries (Union[Unset, float]):
        secret_hint (Union[Unset, str]):
        secret (Union[Unset, str]):
    """

    id: str
    url: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    events: Union[Unset, List[CreateWebhookResultEventsItem]] = UNSET
    enabled: Union[Unset, bool] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    last_attempt_at: Union[Unset, str] = UNSET
    last_status: Union[Unset, float] = UNSET
    last_error_code: Union[Unset, CreateWebhookResultLastErrorCode] = UNSET
    last_success_at: Union[Unset, str] = UNSET
    failed_deliveries: Union[Unset, float] = UNSET
    secret_hint: Union[Unset, str] = UNSET
    secret: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        url = self.url

        description = self.description

        events: Union[Unset, List[str]] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item: str = events_item_data
                events.append(events_item)

        enabled = self.enabled

        created_at = self.created_at

        created_by = self.created_by

        updated_at = self.updated_at

        last_attempt_at = self.last_attempt_at

        last_status = self.last_status

        last_error_code: Union[Unset, str] = UNSET
        if not isinstance(self.last_error_code, Unset):
            last_error_code = self.last_error_code

        last_success_at = self.last_success_at

        failed_deliveries = self.failed_deliveries

        secret_hint = self.secret_hint

        secret = self.secret

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if description is not UNSET:
            field_dict["description"] = description
        if events is not UNSET:
            field_dict["events"] = events
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if last_attempt_at is not UNSET:
            field_dict["lastAttemptAt"] = last_attempt_at
        if last_status is not UNSET:
            field_dict["lastStatus"] = last_status
        if last_error_code is not UNSET:
            field_dict["lastErrorCode"] = last_error_code
        if last_success_at is not UNSET:
            field_dict["lastSuccessAt"] = last_success_at
        if failed_deliveries is not UNSET:
            field_dict["failedDeliveries"] = failed_deliveries
        if secret_hint is not UNSET:
            field_dict["secretHint"] = secret_hint
        if secret is not UNSET:
            field_dict["secret"] = secret

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url", UNSET)

        description = d.pop("description", UNSET)

        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = check_create_webhook_result_events_item(events_item_data)

            events.append(events_item)

        enabled = d.pop("enabled", UNSET)

        created_at = d.pop("createdAt", UNSET)

        created_by = d.pop("createdBy", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        last_attempt_at = d.pop("lastAttemptAt", UNSET)

        last_status = d.pop("lastStatus", UNSET)

        _last_error_code = d.pop("lastErrorCode", UNSET)
        last_error_code: Union[Unset, CreateWebhookResultLastErrorCode]
        if isinstance(_last_error_code, Unset):
            last_error_code = UNSET
        else:
            last_error_code = check_create_webhook_result_last_error_code(
                _last_error_code
            )

        last_success_at = d.pop("lastSuccessAt", UNSET)

        failed_deliveries = d.pop("failedDeliveries", UNSET)

        secret_hint = d.pop("secretHint", UNSET)

        secret = d.pop("secret", UNSET)

        create_webhook_result = cls(
            id=id,
            url=url,
            description=description,
            events=events,
            enabled=enabled,
            created_at=created_at,
            created_by=created_by,
            updated_at=updated_at,
            last_attempt_at=last_attempt_at,
            last_status=last_status,
            last_error_code=last_error_code,
            last_success_at=last_success_at,
            failed_deliveries=failed_deliveries,
            secret_hint=secret_hint,
            secret=secret,
        )

        create_webhook_result.additional_properties = d
        return create_webhook_result

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
