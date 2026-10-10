from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.feed_attempt_format import FeedAttemptFormat, check_feed_attempt_format
from ..models.feed_attempt_mode import FeedAttemptMode, check_feed_attempt_mode
from ..models.feed_attempt_outcome import FeedAttemptOutcome, check_feed_attempt_outcome
from ..types import UNSET, Unset

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
        invoice_number (Union[Unset, str]):
        invoice_id (Union[Unset, str]):
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
    invoice_number: Union[Unset, str] = UNSET
    invoice_id: Union[Unset, str] = UNSET
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

        invoice_number = self.invoice_number

        invoice_id = self.invoice_id

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
        if invoice_number is not UNSET:
            field_dict["invoiceNumber"] = invoice_number
        if invoice_id is not UNSET:
            field_dict["invoiceId"] = invoice_id
        if key_id is not UNSET:
            field_dict["keyId"] = key_id
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
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

        invoice_number = d.pop("invoiceNumber", UNSET)

        invoice_id = d.pop("invoiceId", UNSET)

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
            invoice_number=invoice_number,
            invoice_id=invoice_id,
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
