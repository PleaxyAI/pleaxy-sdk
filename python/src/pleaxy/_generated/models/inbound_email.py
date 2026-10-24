from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.inbound_email_kind import InboundEmailKind, check_inbound_email_kind
from ..models.inbound_email_outcome import (
    InboundEmailOutcome,
    check_inbound_email_outcome,
)
from ..models.inbound_email_reason_code import (
    InboundEmailReasonCode,
    check_inbound_email_reason_code,
)
from ..models.inbound_email_trust import InboundEmailTrust, check_inbound_email_trust
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inbound_email_attachments_item import InboundEmailAttachmentsItem
    from ..models.inbound_email_decision import InboundEmailDecision
    from ..models.inbound_email_draft import InboundEmailDraft
    from ..models.inbound_email_reason_params import InboundEmailReasonParams
    from ..models.inbound_email_result import InboundEmailResult


T = TypeVar("T", bound="InboundEmail")


@_attrs_define
class InboundEmail:
    """
    Attributes:
        id (str):
        po_id (Union[Unset, str]):
        from_ (Union[Unset, str]):
        from_name (Union[Unset, str]):
        subject (Union[Unset, str]):
        received_at (Union[Unset, str]):
        trust (Union[Unset, InboundEmailTrust]):
        kind (Union[Unset, InboundEmailKind]):
        outcome (Union[Unset, InboundEmailOutcome]):
        reason_code (Union[Unset, InboundEmailReasonCode]):
        reason (Union[Unset, str]):
        reason_message_id (Union[Unset, str]):
        reason_params (Union[Unset, InboundEmailReasonParams]):
        summary (Union[Unset, str]):
        text (Union[Unset, str]):
        attachments (Union[Unset, List['InboundEmailAttachmentsItem']]):
        draft (Union[Unset, InboundEmailDraft]):
        result (Union[Unset, InboundEmailResult]):
        decision (Union[Unset, InboundEmailDecision]):
    """

    id: str
    po_id: Union[Unset, str] = UNSET
    from_: Union[Unset, str] = UNSET
    from_name: Union[Unset, str] = UNSET
    subject: Union[Unset, str] = UNSET
    received_at: Union[Unset, str] = UNSET
    trust: Union[Unset, InboundEmailTrust] = UNSET
    kind: Union[Unset, InboundEmailKind] = UNSET
    outcome: Union[Unset, InboundEmailOutcome] = UNSET
    reason_code: Union[Unset, InboundEmailReasonCode] = UNSET
    reason: Union[Unset, str] = UNSET
    reason_message_id: Union[Unset, str] = UNSET
    reason_params: Union[Unset, "InboundEmailReasonParams"] = UNSET
    summary: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    attachments: Union[Unset, List["InboundEmailAttachmentsItem"]] = UNSET
    draft: Union[Unset, "InboundEmailDraft"] = UNSET
    result: Union[Unset, "InboundEmailResult"] = UNSET
    decision: Union[Unset, "InboundEmailDecision"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        po_id = self.po_id

        from_ = self.from_

        from_name = self.from_name

        subject = self.subject

        received_at = self.received_at

        trust: Union[Unset, str] = UNSET
        if not isinstance(self.trust, Unset):
            trust = self.trust

        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        outcome: Union[Unset, str] = UNSET
        if not isinstance(self.outcome, Unset):
            outcome = self.outcome

        reason_code: Union[Unset, str] = UNSET
        if not isinstance(self.reason_code, Unset):
            reason_code = self.reason_code

        reason = self.reason

        reason_message_id = self.reason_message_id

        reason_params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reason_params, Unset):
            reason_params = self.reason_params.to_dict()

        summary = self.summary

        text = self.text

        attachments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)

        draft: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.draft, Unset):
            draft = self.draft.to_dict()

        result: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        decision: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.decision, Unset):
            decision = self.decision.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if po_id is not UNSET:
            field_dict["poId"] = po_id
        if from_ is not UNSET:
            field_dict["from"] = from_
        if from_name is not UNSET:
            field_dict["fromName"] = from_name
        if subject is not UNSET:
            field_dict["subject"] = subject
        if received_at is not UNSET:
            field_dict["receivedAt"] = received_at
        if trust is not UNSET:
            field_dict["trust"] = trust
        if kind is not UNSET:
            field_dict["kind"] = kind
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if reason_code is not UNSET:
            field_dict["reasonCode"] = reason_code
        if reason is not UNSET:
            field_dict["reason"] = reason
        if reason_message_id is not UNSET:
            field_dict["reasonMessageId"] = reason_message_id
        if reason_params is not UNSET:
            field_dict["reasonParams"] = reason_params
        if summary is not UNSET:
            field_dict["summary"] = summary
        if text is not UNSET:
            field_dict["text"] = text
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if draft is not UNSET:
            field_dict["draft"] = draft
        if result is not UNSET:
            field_dict["result"] = result
        if decision is not UNSET:
            field_dict["decision"] = decision

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.inbound_email_attachments_item import InboundEmailAttachmentsItem
        from ..models.inbound_email_decision import InboundEmailDecision
        from ..models.inbound_email_draft import InboundEmailDraft
        from ..models.inbound_email_reason_params import InboundEmailReasonParams
        from ..models.inbound_email_result import InboundEmailResult

        d = src_dict.copy()
        id = d.pop("id")

        po_id = d.pop("poId", UNSET)

        from_ = d.pop("from", UNSET)

        from_name = d.pop("fromName", UNSET)

        subject = d.pop("subject", UNSET)

        received_at = d.pop("receivedAt", UNSET)

        _trust = d.pop("trust", UNSET)
        trust: Union[Unset, InboundEmailTrust]
        if isinstance(_trust, Unset):
            trust = UNSET
        else:
            trust = check_inbound_email_trust(_trust)

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, InboundEmailKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_inbound_email_kind(_kind)

        _outcome = d.pop("outcome", UNSET)
        outcome: Union[Unset, InboundEmailOutcome]
        if isinstance(_outcome, Unset):
            outcome = UNSET
        else:
            outcome = check_inbound_email_outcome(_outcome)

        _reason_code = d.pop("reasonCode", UNSET)
        reason_code: Union[Unset, InboundEmailReasonCode]
        if isinstance(_reason_code, Unset):
            reason_code = UNSET
        else:
            reason_code = check_inbound_email_reason_code(_reason_code)

        reason = d.pop("reason", UNSET)

        reason_message_id = d.pop("reasonMessageId", UNSET)

        _reason_params = d.pop("reasonParams", UNSET)
        reason_params: Union[Unset, InboundEmailReasonParams]
        if isinstance(_reason_params, Unset):
            reason_params = UNSET
        else:
            reason_params = InboundEmailReasonParams.from_dict(_reason_params)

        summary = d.pop("summary", UNSET)

        text = d.pop("text", UNSET)

        attachments = []
        _attachments = d.pop("attachments", UNSET)
        for attachments_item_data in _attachments or []:
            attachments_item = InboundEmailAttachmentsItem.from_dict(
                attachments_item_data
            )

            attachments.append(attachments_item)

        _draft = d.pop("draft", UNSET)
        draft: Union[Unset, InboundEmailDraft]
        if isinstance(_draft, Unset):
            draft = UNSET
        else:
            draft = InboundEmailDraft.from_dict(_draft)

        _result = d.pop("result", UNSET)
        result: Union[Unset, InboundEmailResult]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = InboundEmailResult.from_dict(_result)

        _decision = d.pop("decision", UNSET)
        decision: Union[Unset, InboundEmailDecision]
        if isinstance(_decision, Unset):
            decision = UNSET
        else:
            decision = InboundEmailDecision.from_dict(_decision)

        inbound_email = cls(
            id=id,
            po_id=po_id,
            from_=from_,
            from_name=from_name,
            subject=subject,
            received_at=received_at,
            trust=trust,
            kind=kind,
            outcome=outcome,
            reason_code=reason_code,
            reason=reason,
            reason_message_id=reason_message_id,
            reason_params=reason_params,
            summary=summary,
            text=text,
            attachments=attachments,
            draft=draft,
            result=result,
            decision=decision,
        )

        inbound_email.additional_properties = d
        return inbound_email

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
