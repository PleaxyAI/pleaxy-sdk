from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sourcing_comparison_responder_evaluation_by_criterion import (
        SourcingComparisonResponderEvaluationByCriterion,
    )


T = TypeVar("T", bound="SourcingComparisonResponderEvaluation")


@_attrs_define
class SourcingComparisonResponderEvaluation:
    """
    Attributes:
        by_criterion (Union[Unset, SourcingComparisonResponderEvaluationByCriterion]):
    """

    by_criterion: Union[Unset, "SourcingComparisonResponderEvaluationByCriterion"] = (
        UNSET
    )
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        by_criterion: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.by_criterion, Unset):
            by_criterion = self.by_criterion.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if by_criterion is not UNSET:
            field_dict["byCriterion"] = by_criterion

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sourcing_comparison_responder_evaluation_by_criterion import (
            SourcingComparisonResponderEvaluationByCriterion,
        )

        d = src_dict.copy()
        _by_criterion = d.pop("byCriterion", UNSET)
        by_criterion: Union[Unset, SourcingComparisonResponderEvaluationByCriterion]
        if isinstance(_by_criterion, Unset):
            by_criterion = UNSET
        else:
            by_criterion = SourcingComparisonResponderEvaluationByCriterion.from_dict(
                _by_criterion
            )

        sourcing_comparison_responder_evaluation = cls(
            by_criterion=by_criterion,
        )

        sourcing_comparison_responder_evaluation.additional_properties = d
        return sourcing_comparison_responder_evaluation

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
