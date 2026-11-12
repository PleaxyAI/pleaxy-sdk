from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sourcing_weighted_score_by_criterion import (
        SourcingWeightedScoreByCriterion,
    )


T = TypeVar("T", bound="SourcingWeightedScore")


@_attrs_define
class SourcingWeightedScore:
    """
    Attributes:
        total (Union[None, Unset, float]):
        by_criterion (Union[Unset, SourcingWeightedScoreByCriterion]):
    """

    total: Union[None, Unset, float] = UNSET
    by_criterion: Union[Unset, "SourcingWeightedScoreByCriterion"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total: Union[None, Unset, float]
        if isinstance(self.total, Unset):
            total = UNSET
        else:
            total = self.total

        by_criterion: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.by_criterion, Unset):
            by_criterion = self.by_criterion.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if by_criterion is not UNSET:
            field_dict["byCriterion"] = by_criterion

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sourcing_weighted_score_by_criterion import (
            SourcingWeightedScoreByCriterion,
        )

        d = src_dict.copy()

        def _parse_total(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        total = _parse_total(d.pop("total", UNSET))

        _by_criterion = d.pop("byCriterion", UNSET)
        by_criterion: Union[Unset, SourcingWeightedScoreByCriterion]
        if isinstance(_by_criterion, Unset):
            by_criterion = UNSET
        else:
            by_criterion = SourcingWeightedScoreByCriterion.from_dict(_by_criterion)

        sourcing_weighted_score = cls(
            total=total,
            by_criterion=by_criterion,
        )

        sourcing_weighted_score.additional_properties = d
        return sourcing_weighted_score

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
