from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.supplier_payment_problem_view_kind import (
    SupplierPaymentProblemViewKind,
    check_supplier_payment_problem_view_kind,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.supplier_payment_problem_view_answer import (
        SupplierPaymentProblemViewAnswer,
    )


T = TypeVar("T", bound="SupplierPaymentProblemView")


@_attrs_define
class SupplierPaymentProblemView:
    """
    Attributes:
        at (Union[Unset, str]):
        kind (Union[Unset, SupplierPaymentProblemViewKind]):
        amount_received (Union[Unset, float]):
        note (Union[Unset, str]):
        by (Union[Unset, str]):
        by_name (Union[Unset, str]):
        resolved_at (Union[Unset, str]):
        answer (Union[Unset, SupplierPaymentProblemViewAnswer]):
    """

    at: Union[Unset, str] = UNSET
    kind: Union[Unset, SupplierPaymentProblemViewKind] = UNSET
    amount_received: Union[Unset, float] = UNSET
    note: Union[Unset, str] = UNSET
    by: Union[Unset, str] = UNSET
    by_name: Union[Unset, str] = UNSET
    resolved_at: Union[Unset, str] = UNSET
    answer: Union[Unset, "SupplierPaymentProblemViewAnswer"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        at = self.at

        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        amount_received = self.amount_received

        note = self.note

        by = self.by

        by_name = self.by_name

        resolved_at = self.resolved_at

        answer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.answer, Unset):
            answer = self.answer.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if kind is not UNSET:
            field_dict["kind"] = kind
        if amount_received is not UNSET:
            field_dict["amountReceived"] = amount_received
        if note is not UNSET:
            field_dict["note"] = note
        if by is not UNSET:
            field_dict["by"] = by
        if by_name is not UNSET:
            field_dict["byName"] = by_name
        if resolved_at is not UNSET:
            field_dict["resolvedAt"] = resolved_at
        if answer is not UNSET:
            field_dict["answer"] = answer

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.supplier_payment_problem_view_answer import (
            SupplierPaymentProblemViewAnswer,
        )

        d = src_dict.copy()
        at = d.pop("at", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, SupplierPaymentProblemViewKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_supplier_payment_problem_view_kind(_kind)

        amount_received = d.pop("amountReceived", UNSET)

        note = d.pop("note", UNSET)

        by = d.pop("by", UNSET)

        by_name = d.pop("byName", UNSET)

        resolved_at = d.pop("resolvedAt", UNSET)

        _answer = d.pop("answer", UNSET)
        answer: Union[Unset, SupplierPaymentProblemViewAnswer]
        if isinstance(_answer, Unset):
            answer = UNSET
        else:
            answer = SupplierPaymentProblemViewAnswer.from_dict(_answer)

        supplier_payment_problem_view = cls(
            at=at,
            kind=kind,
            amount_received=amount_received,
            note=note,
            by=by,
            by_name=by_name,
            resolved_at=resolved_at,
            answer=answer,
        )

        supplier_payment_problem_view.additional_properties = d
        return supplier_payment_problem_view

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
