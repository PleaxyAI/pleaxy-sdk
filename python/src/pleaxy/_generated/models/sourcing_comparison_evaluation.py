from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sourcing_evaluation_criterion import SourcingEvaluationCriterion


T = TypeVar("T", bound="SourcingComparisonEvaluation")


@_attrs_define
class SourcingComparisonEvaluation:
    """
    Attributes:
        criteria (Union[Unset, List['SourcingEvaluationCriterion']]):
        evaluators (Union[Unset, float]):
        submitted (Union[Unset, float]):
        complete (Union[Unset, bool]):
        hidden (Union[Unset, bool]):
    """

    criteria: Union[Unset, List["SourcingEvaluationCriterion"]] = UNSET
    evaluators: Union[Unset, float] = UNSET
    submitted: Union[Unset, float] = UNSET
    complete: Union[Unset, bool] = UNSET
    hidden: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        criteria: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.criteria, Unset):
            criteria = []
            for criteria_item_data in self.criteria:
                criteria_item = criteria_item_data.to_dict()
                criteria.append(criteria_item)

        evaluators = self.evaluators

        submitted = self.submitted

        complete = self.complete

        hidden = self.hidden

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if criteria is not UNSET:
            field_dict["criteria"] = criteria
        if evaluators is not UNSET:
            field_dict["evaluators"] = evaluators
        if submitted is not UNSET:
            field_dict["submitted"] = submitted
        if complete is not UNSET:
            field_dict["complete"] = complete
        if hidden is not UNSET:
            field_dict["hidden"] = hidden

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sourcing_evaluation_criterion import SourcingEvaluationCriterion

        d = src_dict.copy()
        criteria = []
        _criteria = d.pop("criteria", UNSET)
        for criteria_item_data in _criteria or []:
            criteria_item = SourcingEvaluationCriterion.from_dict(criteria_item_data)

            criteria.append(criteria_item)

        evaluators = d.pop("evaluators", UNSET)

        submitted = d.pop("submitted", UNSET)

        complete = d.pop("complete", UNSET)

        hidden = d.pop("hidden", UNSET)

        sourcing_comparison_evaluation = cls(
            criteria=criteria,
            evaluators=evaluators,
            submitted=submitted,
            complete=complete,
            hidden=hidden,
        )

        sourcing_comparison_evaluation.additional_properties = d
        return sourcing_comparison_evaluation

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
