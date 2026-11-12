from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_activity_entry_actor_side import (
    InvoiceActivityEntryActorSide,
    check_invoice_activity_entry_actor_side,
)
from ..models.invoice_activity_entry_kind import (
    InvoiceActivityEntryKind,
    check_invoice_activity_entry_kind,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_comment_view import DocumentCommentView
    from ..models.invoice_activity_entry_data import InvoiceActivityEntryData


T = TypeVar("T", bound="InvoiceActivityEntry")


@_attrs_define
class InvoiceActivityEntry:
    """
    Attributes:
        id (str):
        at (Union[Unset, str]):
        kind (Union[Unset, InvoiceActivityEntryKind]):
        actor_name (Union[Unset, str]):
        actor_key (Union[Unset, str]):
        actor_side (Union[Unset, InvoiceActivityEntryActorSide]):
        data (Union[Unset, InvoiceActivityEntryData]):
        comment (Union[Unset, DocumentCommentView]):
    """

    id: str
    at: Union[Unset, str] = UNSET
    kind: Union[Unset, InvoiceActivityEntryKind] = UNSET
    actor_name: Union[Unset, str] = UNSET
    actor_key: Union[Unset, str] = UNSET
    actor_side: Union[Unset, InvoiceActivityEntryActorSide] = UNSET
    data: Union[Unset, "InvoiceActivityEntryData"] = UNSET
    comment: Union[Unset, "DocumentCommentView"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        at = self.at

        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        actor_name = self.actor_name

        actor_key = self.actor_key

        actor_side: Union[Unset, str] = UNSET
        if not isinstance(self.actor_side, Unset):
            actor_side = self.actor_side

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        comment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.comment, Unset):
            comment = self.comment.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if at is not UNSET:
            field_dict["at"] = at
        if kind is not UNSET:
            field_dict["kind"] = kind
        if actor_name is not UNSET:
            field_dict["actorName"] = actor_name
        if actor_key is not UNSET:
            field_dict["actorKey"] = actor_key
        if actor_side is not UNSET:
            field_dict["actorSide"] = actor_side
        if data is not UNSET:
            field_dict["data"] = data
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.document_comment_view import DocumentCommentView
        from ..models.invoice_activity_entry_data import InvoiceActivityEntryData

        d = src_dict.copy()
        id = d.pop("id")

        at = d.pop("at", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, InvoiceActivityEntryKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_invoice_activity_entry_kind(_kind)

        actor_name = d.pop("actorName", UNSET)

        actor_key = d.pop("actorKey", UNSET)

        _actor_side = d.pop("actorSide", UNSET)
        actor_side: Union[Unset, InvoiceActivityEntryActorSide]
        if isinstance(_actor_side, Unset):
            actor_side = UNSET
        else:
            actor_side = check_invoice_activity_entry_actor_side(_actor_side)

        _data = d.pop("data", UNSET)
        data: Union[Unset, InvoiceActivityEntryData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = InvoiceActivityEntryData.from_dict(_data)

        _comment = d.pop("comment", UNSET)
        comment: Union[Unset, DocumentCommentView]
        if isinstance(_comment, Unset):
            comment = UNSET
        else:
            comment = DocumentCommentView.from_dict(_comment)

        invoice_activity_entry = cls(
            id=id,
            at=at,
            kind=kind,
            actor_name=actor_name,
            actor_key=actor_key,
            actor_side=actor_side,
            data=data,
            comment=comment,
        )

        invoice_activity_entry.additional_properties = d
        return invoice_activity_entry

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
