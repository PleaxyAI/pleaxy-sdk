from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.feed_attempt_format import FeedAttemptFormat, check_feed_attempt_format
from ..models.feed_attempt_mode import FeedAttemptMode, check_feed_attempt_mode
from ..models.feed_attempt_outcome import FeedAttemptOutcome, check_feed_attempt_outcome
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feed_attempt_params import FeedAttemptParams


T = TypeVar("T", bound="FeedAttempt")


@_attrs_define
class FeedAttempt:
    """
    Attributes:
        at (Union[Unset, str]):
        mode (Union[Unset, FeedAttemptMode]):
        format_ (Union[Unset, FeedAttemptFormat]):
        outcome (Union[Unset, FeedAttemptOutcome]):
        status (Union[Unset, float]):
        code (Union[Unset, str]):
        message (Union[Unset, str]):
        message_id (Union[Unset, str]):
        params (Union[Unset, FeedAttemptParams]):
        invoice_number (Union[Unset, str]):
        invoice_id (Union[Unset, str]):
        credit_note_id (Union[Unset, str]):
        key_id (Union[Unset, str]):
        cursor (Union[Unset, str]):
    """

    at: Union[Unset, str] = UNSET
    mode: Union[Unset, FeedAttemptMode] = UNSET
    format_: Union[Unset, FeedAttemptFormat] = UNSET
    outcome: Union[Unset, FeedAttemptOutcome] = UNSET
    status: Union[Unset, float] = UNSET
    code: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    message_id: Union[Unset, str] = UNSET
    params: Union[Unset, "FeedAttemptParams"] = UNSET
    invoice_number: Union[Unset, str] = UNSET
    invoice_id: Union[Unset, str] = UNSET
    credit_note_id: Union[Unset, str] = UNSET
    key_id: Union[Unset, str] = UNSET
    cursor: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        at = self.at

        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode

        format_: Union[Unset, str] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_

        outcome: Union[Unset, str] = UNSET
        if not isinstance(self.outcome, Unset):
            outcome = self.outcome

        status = self.status

        code = self.code

        message = self.message

        message_id = self.message_id

        params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        invoice_number = self.invoice_number

        invoice_id = self.invoice_id

        credit_note_id = self.credit_note_id

        key_id = self.key_id

        cursor = self.cursor

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if mode is not UNSET:
            field_dict["mode"] = mode
        if format_ is not UNSET:
            field_dict["format"] = format_
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if status is not UNSET:
            field_dict["status"] = status
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if params is not UNSET:
            field_dict["params"] = params
        if invoice_number is not UNSET:
            field_dict["invoiceNumber"] = invoice_number
        if invoice_id is not UNSET:
            field_dict["invoiceId"] = invoice_id
        if credit_note_id is not UNSET:
            field_dict["creditNoteId"] = credit_note_id
        if key_id is not UNSET:
            field_dict["keyId"] = key_id
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.feed_attempt_params import FeedAttemptParams

        d = src_dict.copy()
        at = d.pop("at", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, FeedAttemptMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = check_feed_attempt_mode(_mode)

        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, FeedAttemptFormat]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = check_feed_attempt_format(_format_)

        _outcome = d.pop("outcome", UNSET)
        outcome: Union[Unset, FeedAttemptOutcome]
        if isinstance(_outcome, Unset):
            outcome = UNSET
        else:
            outcome = check_feed_attempt_outcome(_outcome)

        status = d.pop("status", UNSET)

        code = d.pop("code", UNSET)

        message = d.pop("message", UNSET)

        message_id = d.pop("messageId", UNSET)

        _params = d.pop("params", UNSET)
        params: Union[Unset, FeedAttemptParams]
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = FeedAttemptParams.from_dict(_params)

        invoice_number = d.pop("invoiceNumber", UNSET)

        invoice_id = d.pop("invoiceId", UNSET)

        credit_note_id = d.pop("creditNoteId", UNSET)

        key_id = d.pop("keyId", UNSET)

        cursor = d.pop("cursor", UNSET)

        feed_attempt = cls(
            at=at,
            mode=mode,
            format_=format_,
            outcome=outcome,
            status=status,
            code=code,
            message=message,
            message_id=message_id,
            params=params,
            invoice_number=invoice_number,
            invoice_id=invoice_id,
            credit_note_id=credit_note_id,
            key_id=key_id,
            cursor=cursor,
        )

        feed_attempt.additional_properties = d
        return feed_attempt

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
