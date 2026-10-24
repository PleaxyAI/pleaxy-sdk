from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.inbound_email_draft_kind import (
    InboundEmailDraftKind,
    check_inbound_email_draft_kind,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inbound_email_draft_confirmation import InboundEmailDraftConfirmation
    from ..models.inbound_email_draft_ship_notice import InboundEmailDraftShipNotice


T = TypeVar("T", bound="InboundEmailDraft")


@_attrs_define
class InboundEmailDraft:
    """
    Attributes:
        kind (Union[Unset, InboundEmailDraftKind]):
        summary (Union[Unset, str]):
        confirmation (Union[Unset, InboundEmailDraftConfirmation]):
        ship_notice (Union[Unset, InboundEmailDraftShipNotice]):
        payload_id (Union[Unset, str]):
    """

    kind: Union[Unset, InboundEmailDraftKind] = UNSET
    summary: Union[Unset, str] = UNSET
    confirmation: Union[Unset, "InboundEmailDraftConfirmation"] = UNSET
    ship_notice: Union[Unset, "InboundEmailDraftShipNotice"] = UNSET
    payload_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        summary = self.summary

        confirmation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.confirmation, Unset):
            confirmation = self.confirmation.to_dict()

        ship_notice: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ship_notice, Unset):
            ship_notice = self.ship_notice.to_dict()

        payload_id = self.payload_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if summary is not UNSET:
            field_dict["summary"] = summary
        if confirmation is not UNSET:
            field_dict["confirmation"] = confirmation
        if ship_notice is not UNSET:
            field_dict["shipNotice"] = ship_notice
        if payload_id is not UNSET:
            field_dict["payloadId"] = payload_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.inbound_email_draft_confirmation import (
            InboundEmailDraftConfirmation,
        )
        from ..models.inbound_email_draft_ship_notice import InboundEmailDraftShipNotice

        d = src_dict.copy()
        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, InboundEmailDraftKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_inbound_email_draft_kind(_kind)

        summary = d.pop("summary", UNSET)

        _confirmation = d.pop("confirmation", UNSET)
        confirmation: Union[Unset, InboundEmailDraftConfirmation]
        if isinstance(_confirmation, Unset):
            confirmation = UNSET
        else:
            confirmation = InboundEmailDraftConfirmation.from_dict(_confirmation)

        _ship_notice = d.pop("shipNotice", UNSET)
        ship_notice: Union[Unset, InboundEmailDraftShipNotice]
        if isinstance(_ship_notice, Unset):
            ship_notice = UNSET
        else:
            ship_notice = InboundEmailDraftShipNotice.from_dict(_ship_notice)

        payload_id = d.pop("payloadId", UNSET)

        inbound_email_draft = cls(
            kind=kind,
            summary=summary,
            confirmation=confirmation,
            ship_notice=ship_notice,
            payload_id=payload_id,
        )

        inbound_email_draft.additional_properties = d
        return inbound_email_draft

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
