from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sync_event_document_type import (
    SyncEventDocumentType,
    check_sync_event_document_type,
)
from ..models.sync_event_type import SyncEventType, check_sync_event_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="SyncEvent")


@_attrs_define
class SyncEvent:
    """
    Attributes:
        id (str):
        at (Union[Unset, str]):
        type (Union[Unset, SyncEventType]):
        document_type (Union[Unset, SyncEventDocumentType]):
        document_id (Union[Unset, str]):
        buyer_workspace_id (Union[Unset, str]):
    """

    id: str
    at: Union[Unset, str] = UNSET
    type: Union[Unset, SyncEventType] = UNSET
    document_type: Union[Unset, SyncEventDocumentType] = UNSET
    document_id: Union[Unset, str] = UNSET
    buyer_workspace_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        at = self.at

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type

        document_type: Union[Unset, str] = UNSET
        if not isinstance(self.document_type, Unset):
            document_type = self.document_type

        document_id = self.document_id

        buyer_workspace_id = self.buyer_workspace_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if at is not UNSET:
            field_dict["at"] = at
        if type is not UNSET:
            field_dict["type"] = type
        if document_type is not UNSET:
            field_dict["documentType"] = document_type
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if buyer_workspace_id is not UNSET:
            field_dict["buyerWorkspaceId"] = buyer_workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        at = d.pop("at", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, SyncEventType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = check_sync_event_type(_type)

        _document_type = d.pop("documentType", UNSET)
        document_type: Union[Unset, SyncEventDocumentType]
        if isinstance(_document_type, Unset):
            document_type = UNSET
        else:
            document_type = check_sync_event_document_type(_document_type)

        document_id = d.pop("documentId", UNSET)

        buyer_workspace_id = d.pop("buyerWorkspaceId", UNSET)

        sync_event = cls(
            id=id,
            at=at,
            type=type,
            document_type=document_type,
            document_id=document_id,
            buyer_workspace_id=buyer_workspace_id,
        )

        sync_event.additional_properties = d
        return sync_event

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
