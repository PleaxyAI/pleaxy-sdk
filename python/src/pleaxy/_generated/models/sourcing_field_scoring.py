from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sourcing_field_scoring_option_points import (
        SourcingFieldScoringOptionPoints,
    )


T = TypeVar("T", bound="SourcingFieldScoring")


@_attrs_define
class SourcingFieldScoring:
    """
    Attributes:
        weight (Union[Unset, float]):
        option_points (Union[Unset, SourcingFieldScoringOptionPoints]):
    """

    weight: Union[Unset, float] = UNSET
    option_points: Union[Unset, "SourcingFieldScoringOptionPoints"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        weight = self.weight

        option_points: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.option_points, Unset):
            option_points = self.option_points.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if weight is not UNSET:
            field_dict["weight"] = weight
        if option_points is not UNSET:
            field_dict["optionPoints"] = option_points

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sourcing_field_scoring_option_points import (
            SourcingFieldScoringOptionPoints,
        )

        d = src_dict.copy()
        weight = d.pop("weight", UNSET)

        _option_points = d.pop("optionPoints", UNSET)
        option_points: Union[Unset, SourcingFieldScoringOptionPoints]
        if isinstance(_option_points, Unset):
            option_points = UNSET
        else:
            option_points = SourcingFieldScoringOptionPoints.from_dict(_option_points)

        sourcing_field_scoring = cls(
            weight=weight,
            option_points=option_points,
        )

        sourcing_field_scoring.additional_properties = d
        return sourcing_field_scoring

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
