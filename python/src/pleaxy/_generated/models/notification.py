from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notification_audience import (
    NotificationAudience,
    check_notification_audience,
)
from ..models.notification_type import NotificationType, check_notification_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_resolution import NotificationResolution
    from ..models.server_message_params import ServerMessageParams


T = TypeVar("T", bound="Notification")


@_attrs_define
class Notification:
    """
    Attributes:
        id (str):
        audience (Union[Unset, NotificationAudience]):
        recipient_employee_key (Union[Unset, str]):
        type (Union[Unset, NotificationType]):
        title (Union[Unset, str]):
        body (Union[Unset, str]):
        title_message_id (Union[Unset, str]):
        title_params (Union[Unset, ServerMessageParams]):
        body_message_id (Union[Unset, str]):
        body_params (Union[Unset, ServerMessageParams]):
        related_id (Union[Unset, str]):
        stage_id (Union[Unset, str]):
        buyer_workspace_id (Union[Unset, str]):
        created_at (Union[Unset, str]):
        read (Union[Unset, bool]):
        resolution (Union[Unset, NotificationResolution]):
    """

    id: str
    audience: Union[Unset, NotificationAudience] = UNSET
    recipient_employee_key: Union[Unset, str] = UNSET
    type: Union[Unset, NotificationType] = UNSET
    title: Union[Unset, str] = UNSET
    body: Union[Unset, str] = UNSET
    title_message_id: Union[Unset, str] = UNSET
    title_params: Union[Unset, "ServerMessageParams"] = UNSET
    body_message_id: Union[Unset, str] = UNSET
    body_params: Union[Unset, "ServerMessageParams"] = UNSET
    related_id: Union[Unset, str] = UNSET
    stage_id: Union[Unset, str] = UNSET
    buyer_workspace_id: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    read: Union[Unset, bool] = UNSET
    resolution: Union[Unset, "NotificationResolution"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        audience: Union[Unset, str] = UNSET
        if not isinstance(self.audience, Unset):
            audience = self.audience

        recipient_employee_key = self.recipient_employee_key

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type

        title = self.title

        body = self.body

        title_message_id = self.title_message_id

        title_params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.title_params, Unset):
            title_params = self.title_params.to_dict()

        body_message_id = self.body_message_id

        body_params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.body_params, Unset):
            body_params = self.body_params.to_dict()

        related_id = self.related_id

        stage_id = self.stage_id

        buyer_workspace_id = self.buyer_workspace_id

        created_at = self.created_at

        read = self.read

        resolution: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.resolution, Unset):
            resolution = self.resolution.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if audience is not UNSET:
            field_dict["audience"] = audience
        if recipient_employee_key is not UNSET:
            field_dict["recipientEmployeeKey"] = recipient_employee_key
        if type is not UNSET:
            field_dict["type"] = type
        if title is not UNSET:
            field_dict["title"] = title
        if body is not UNSET:
            field_dict["body"] = body
        if title_message_id is not UNSET:
            field_dict["titleMessageId"] = title_message_id
        if title_params is not UNSET:
            field_dict["titleParams"] = title_params
        if body_message_id is not UNSET:
            field_dict["bodyMessageId"] = body_message_id
        if body_params is not UNSET:
            field_dict["bodyParams"] = body_params
        if related_id is not UNSET:
            field_dict["relatedId"] = related_id
        if stage_id is not UNSET:
            field_dict["stageId"] = stage_id
        if buyer_workspace_id is not UNSET:
            field_dict["buyerWorkspaceId"] = buyer_workspace_id
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if read is not UNSET:
            field_dict["read"] = read
        if resolution is not UNSET:
            field_dict["resolution"] = resolution

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.notification_resolution import NotificationResolution
        from ..models.server_message_params import ServerMessageParams

        d = src_dict.copy()
        id = d.pop("id")

        _audience = d.pop("audience", UNSET)
        audience: Union[Unset, NotificationAudience]
        if isinstance(_audience, Unset):
            audience = UNSET
        else:
            audience = check_notification_audience(_audience)

        recipient_employee_key = d.pop("recipientEmployeeKey", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, NotificationType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = check_notification_type(_type)

        title = d.pop("title", UNSET)

        body = d.pop("body", UNSET)

        title_message_id = d.pop("titleMessageId", UNSET)

        _title_params = d.pop("titleParams", UNSET)
        title_params: Union[Unset, ServerMessageParams]
        if isinstance(_title_params, Unset):
            title_params = UNSET
        else:
            title_params = ServerMessageParams.from_dict(_title_params)

        body_message_id = d.pop("bodyMessageId", UNSET)

        _body_params = d.pop("bodyParams", UNSET)
        body_params: Union[Unset, ServerMessageParams]
        if isinstance(_body_params, Unset):
            body_params = UNSET
        else:
            body_params = ServerMessageParams.from_dict(_body_params)

        related_id = d.pop("relatedId", UNSET)

        stage_id = d.pop("stageId", UNSET)

        buyer_workspace_id = d.pop("buyerWorkspaceId", UNSET)

        created_at = d.pop("createdAt", UNSET)

        read = d.pop("read", UNSET)

        _resolution = d.pop("resolution", UNSET)
        resolution: Union[Unset, NotificationResolution]
        if isinstance(_resolution, Unset):
            resolution = UNSET
        else:
            resolution = NotificationResolution.from_dict(_resolution)

        notification = cls(
            id=id,
            audience=audience,
            recipient_employee_key=recipient_employee_key,
            type=type,
            title=title,
            body=body,
            title_message_id=title_message_id,
            title_params=title_params,
            body_message_id=body_message_id,
            body_params=body_params,
            related_id=related_id,
            stage_id=stage_id,
            buyer_workspace_id=buyer_workspace_id,
            created_at=created_at,
            read=read,
            resolution=resolution,
        )

        notification.additional_properties = d
        return notification

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
