from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AiSavingRecommendationDetail")


@_attrs_define
class AiSavingRecommendationDetail:
    """
    Attributes:
        interactive_rate (Union[Unset, float]):
        batch_rate (Union[Unset, float]):
        input_rate (Union[Unset, float]):
        cached_rate (Union[Unset, float]):
        cached_share (Union[Unset, float]):
        days_used (Union[Unset, float]):
        steady_hours_per_day (Union[Unset, float]):
        reservable_units (Union[Unset, float]):
    """

    interactive_rate: Union[Unset, float] = UNSET
    batch_rate: Union[Unset, float] = UNSET
    input_rate: Union[Unset, float] = UNSET
    cached_rate: Union[Unset, float] = UNSET
    cached_share: Union[Unset, float] = UNSET
    days_used: Union[Unset, float] = UNSET
    steady_hours_per_day: Union[Unset, float] = UNSET
    reservable_units: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        interactive_rate = self.interactive_rate

        batch_rate = self.batch_rate

        input_rate = self.input_rate

        cached_rate = self.cached_rate

        cached_share = self.cached_share

        days_used = self.days_used

        steady_hours_per_day = self.steady_hours_per_day

        reservable_units = self.reservable_units

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interactive_rate is not UNSET:
            field_dict["interactiveRate"] = interactive_rate
        if batch_rate is not UNSET:
            field_dict["batchRate"] = batch_rate
        if input_rate is not UNSET:
            field_dict["inputRate"] = input_rate
        if cached_rate is not UNSET:
            field_dict["cachedRate"] = cached_rate
        if cached_share is not UNSET:
            field_dict["cachedShare"] = cached_share
        if days_used is not UNSET:
            field_dict["daysUsed"] = days_used
        if steady_hours_per_day is not UNSET:
            field_dict["steadyHoursPerDay"] = steady_hours_per_day
        if reservable_units is not UNSET:
            field_dict["reservableUnits"] = reservable_units

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        interactive_rate = d.pop("interactiveRate", UNSET)

        batch_rate = d.pop("batchRate", UNSET)

        input_rate = d.pop("inputRate", UNSET)

        cached_rate = d.pop("cachedRate", UNSET)

        cached_share = d.pop("cachedShare", UNSET)

        days_used = d.pop("daysUsed", UNSET)

        steady_hours_per_day = d.pop("steadyHoursPerDay", UNSET)

        reservable_units = d.pop("reservableUnits", UNSET)

        ai_saving_recommendation_detail = cls(
            interactive_rate=interactive_rate,
            batch_rate=batch_rate,
            input_rate=input_rate,
            cached_rate=cached_rate,
            cached_share=cached_share,
            days_used=days_used,
            steady_hours_per_day=steady_hours_per_day,
            reservable_units=reservable_units,
        )

        ai_saving_recommendation_detail.additional_properties = d
        return ai_saving_recommendation_detail

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
