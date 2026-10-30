from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cloud_ai_sync_state_code import (
    CloudAiSyncStateCode,
    check_cloud_ai_sync_state_code,
)
from ..models.cloud_ai_sync_state_status import (
    CloudAiSyncStateStatus,
    check_cloud_ai_sync_state_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudAiSyncState")


@_attrs_define
class CloudAiSyncState:
    """
    Attributes:
        synced_at (Union[Unset, str]):
        status (Union[Unset, CloudAiSyncStateStatus]):
        code (Union[Unset, CloudAiSyncStateCode]):
        message (Union[Unset, str]):
    """

    synced_at: Union[Unset, str] = UNSET
    status: Union[Unset, CloudAiSyncStateStatus] = UNSET
    code: Union[Unset, CloudAiSyncStateCode] = UNSET
    message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        synced_at = self.synced_at

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        code: Union[Unset, str] = UNSET
        if not isinstance(self.code, Unset):
            code = self.code

        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if synced_at is not UNSET:
            field_dict["syncedAt"] = synced_at
        if status is not UNSET:
            field_dict["status"] = status
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        synced_at = d.pop("syncedAt", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CloudAiSyncStateStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_cloud_ai_sync_state_status(_status)

        _code = d.pop("code", UNSET)
        code: Union[Unset, CloudAiSyncStateCode]
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = check_cloud_ai_sync_state_code(_code)

        message = d.pop("message", UNSET)

        cloud_ai_sync_state = cls(
            synced_at=synced_at,
            status=status,
            code=code,
            message=message,
        )

        cloud_ai_sync_state.additional_properties = d
        return cloud_ai_sync_state

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
