from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_payment_problem_kind import (
    InvoicePaymentProblemKind,
    check_invoice_payment_problem_kind,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_payment_problem_answer import InvoicePaymentProblemAnswer


T = TypeVar("T", bound="InvoicePaymentProblem")


@_attrs_define
class InvoicePaymentProblem:
    """
    Attributes:
        kind (Union[Unset, InvoicePaymentProblemKind]):
        amount_received (Union[Unset, float]):
        note (Union[Unset, str]):
        at (Union[Unset, str]):
        by (Union[Unset, str]):
        by_name (Union[Unset, str]):
        answer (Union[Unset, InvoicePaymentProblemAnswer]):
        resolved_at (Union[Unset, str]):
    """

    kind: Union[Unset, InvoicePaymentProblemKind] = UNSET
    amount_received: Union[Unset, float] = UNSET
    note: Union[Unset, str] = UNSET
    at: Union[Unset, str] = UNSET
    by: Union[Unset, str] = UNSET
    by_name: Union[Unset, str] = UNSET
    answer: Union[Unset, "InvoicePaymentProblemAnswer"] = UNSET
    resolved_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        amount_received = self.amount_received

        note = self.note

        at = self.at

        by = self.by

        by_name = self.by_name

        answer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.answer, Unset):
            answer = self.answer.to_dict()

        resolved_at = self.resolved_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if amount_received is not UNSET:
            field_dict["amountReceived"] = amount_received
        if note is not UNSET:
            field_dict["note"] = note
        if at is not UNSET:
            field_dict["at"] = at
        if by is not UNSET:
            field_dict["by"] = by
        if by_name is not UNSET:
            field_dict["byName"] = by_name
        if answer is not UNSET:
            field_dict["answer"] = answer
        if resolved_at is not UNSET:
            field_dict["resolvedAt"] = resolved_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_payment_problem_answer import InvoicePaymentProblemAnswer

        d = src_dict.copy()
        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, InvoicePaymentProblemKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_invoice_payment_problem_kind(_kind)

        amount_received = d.pop("amountReceived", UNSET)

        note = d.pop("note", UNSET)

        at = d.pop("at", UNSET)

        by = d.pop("by", UNSET)

        by_name = d.pop("byName", UNSET)

        _answer = d.pop("answer", UNSET)
        answer: Union[Unset, InvoicePaymentProblemAnswer]
        if isinstance(_answer, Unset):
            answer = UNSET
        else:
            answer = InvoicePaymentProblemAnswer.from_dict(_answer)

        resolved_at = d.pop("resolvedAt", UNSET)

        invoice_payment_problem = cls(
            kind=kind,
            amount_received=amount_received,
            note=note,
            at=at,
            by=by,
            by_name=by_name,
            answer=answer,
            resolved_at=resolved_at,
        )

        invoice_payment_problem.additional_properties = d
        return invoice_payment_problem

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
