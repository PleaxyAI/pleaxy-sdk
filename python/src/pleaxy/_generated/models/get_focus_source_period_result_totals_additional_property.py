from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetFocusSourcePeriodResultTotalsAdditionalProperty")


@_attrs_define
class GetFocusSourcePeriodResultTotalsAdditionalProperty:
    """
    Attributes:
        billed (Union[Unset, float]):
        effective (Union[Unset, float]):
    """

    billed: Union[Unset, float] = UNSET
    effective: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        billed = self.billed

        effective = self.effective

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if billed is not UNSET:
            field_dict["billed"] = billed
        if effective is not UNSET:
            field_dict["effective"] = effective

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        billed = d.pop("billed", UNSET)

        effective = d.pop("effective", UNSET)

        get_focus_source_period_result_totals_additional_property = cls(
            billed=billed,
            effective=effective,
        )

        get_focus_source_period_result_totals_additional_property.additional_properties = d
        return get_focus_source_period_result_totals_additional_property

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
