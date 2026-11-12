from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SourcingEvaluationAggregate")


@_attrs_define
class SourcingEvaluationAggregate:
    """
    Attributes:
        average (Union[None, Unset, float]):
        lowest (Union[None, Unset, float]):
        highest (Union[None, Unset, float]):
        count (Union[Unset, float]):
    """

    average: Union[None, Unset, float] = UNSET
    lowest: Union[None, Unset, float] = UNSET
    highest: Union[None, Unset, float] = UNSET
    count: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        average: Union[None, Unset, float]
        if isinstance(self.average, Unset):
            average = UNSET
        else:
            average = self.average

        lowest: Union[None, Unset, float]
        if isinstance(self.lowest, Unset):
            lowest = UNSET
        else:
            lowest = self.lowest

        highest: Union[None, Unset, float]
        if isinstance(self.highest, Unset):
            highest = UNSET
        else:
            highest = self.highest

        count = self.count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if average is not UNSET:
            field_dict["average"] = average
        if lowest is not UNSET:
            field_dict["lowest"] = lowest
        if highest is not UNSET:
            field_dict["highest"] = highest
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_average(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        average = _parse_average(d.pop("average", UNSET))

        def _parse_lowest(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        lowest = _parse_lowest(d.pop("lowest", UNSET))

        def _parse_highest(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        highest = _parse_highest(d.pop("highest", UNSET))

        count = d.pop("count", UNSET)

        sourcing_evaluation_aggregate = cls(
            average=average,
            lowest=lowest,
            highest=highest,
            count=count,
        )

        sourcing_evaluation_aggregate.additional_properties = d
        return sourcing_evaluation_aggregate

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
