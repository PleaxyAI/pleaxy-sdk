from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sourcing_round_feedback import (
    SourcingRoundFeedback,
    check_sourcing_round_feedback,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sourcing_round_feedback_by_supplier import (
        SourcingRoundFeedbackBySupplier,
    )


T = TypeVar("T", bound="SourcingRound")


@_attrs_define
class SourcingRound:
    """
    Attributes:
        round_ (Union[Unset, float]):
        supplier_keys (Union[Unset, List[str]]):
        due_at (Union[Unset, str]):
        feedback (Union[Unset, SourcingRoundFeedback]):
        feedback_by_supplier (Union[Unset, SourcingRoundFeedbackBySupplier]):
        opened_at (Union[Unset, str]):
        opened_by (Union[Unset, str]):
        closed_at (Union[Unset, str]):
    """

    round_: Union[Unset, float] = UNSET
    supplier_keys: Union[Unset, List[str]] = UNSET
    due_at: Union[Unset, str] = UNSET
    feedback: Union[Unset, SourcingRoundFeedback] = UNSET
    feedback_by_supplier: Union[Unset, "SourcingRoundFeedbackBySupplier"] = UNSET
    opened_at: Union[Unset, str] = UNSET
    opened_by: Union[Unset, str] = UNSET
    closed_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        round_ = self.round_

        supplier_keys: Union[Unset, List[str]] = UNSET
        if not isinstance(self.supplier_keys, Unset):
            supplier_keys = self.supplier_keys

        due_at = self.due_at

        feedback: Union[Unset, str] = UNSET
        if not isinstance(self.feedback, Unset):
            feedback = self.feedback

        feedback_by_supplier: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.feedback_by_supplier, Unset):
            feedback_by_supplier = self.feedback_by_supplier.to_dict()

        opened_at = self.opened_at

        opened_by = self.opened_by

        closed_at = self.closed_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if round_ is not UNSET:
            field_dict["round"] = round_
        if supplier_keys is not UNSET:
            field_dict["supplierKeys"] = supplier_keys
        if due_at is not UNSET:
            field_dict["dueAt"] = due_at
        if feedback is not UNSET:
            field_dict["feedback"] = feedback
        if feedback_by_supplier is not UNSET:
            field_dict["feedbackBySupplier"] = feedback_by_supplier
        if opened_at is not UNSET:
            field_dict["openedAt"] = opened_at
        if opened_by is not UNSET:
            field_dict["openedBy"] = opened_by
        if closed_at is not UNSET:
            field_dict["closedAt"] = closed_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sourcing_round_feedback_by_supplier import (
            SourcingRoundFeedbackBySupplier,
        )

        d = src_dict.copy()
        round_ = d.pop("round", UNSET)

        supplier_keys = cast(List[str], d.pop("supplierKeys", UNSET))

        due_at = d.pop("dueAt", UNSET)

        _feedback = d.pop("feedback", UNSET)
        feedback: Union[Unset, SourcingRoundFeedback]
        if isinstance(_feedback, Unset):
            feedback = UNSET
        else:
            feedback = check_sourcing_round_feedback(_feedback)

        _feedback_by_supplier = d.pop("feedbackBySupplier", UNSET)
        feedback_by_supplier: Union[Unset, SourcingRoundFeedbackBySupplier]
        if isinstance(_feedback_by_supplier, Unset):
            feedback_by_supplier = UNSET
        else:
            feedback_by_supplier = SourcingRoundFeedbackBySupplier.from_dict(
                _feedback_by_supplier
            )

        opened_at = d.pop("openedAt", UNSET)

        opened_by = d.pop("openedBy", UNSET)

        closed_at = d.pop("closedAt", UNSET)

        sourcing_round = cls(
            round_=round_,
            supplier_keys=supplier_keys,
            due_at=due_at,
            feedback=feedback,
            feedback_by_supplier=feedback_by_supplier,
            opened_at=opened_at,
            opened_by=opened_by,
            closed_at=closed_at,
        )

        sourcing_round.additional_properties = d
        return sourcing_round

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
