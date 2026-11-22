from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SensitivityPreset")


@_attrs_define
class SensitivityPreset:
    """
    Attributes:
        spike_pct (Union[Unset, float]):
        pace_pct (Union[Unset, float]):
        min_amount (Union[Unset, float]):
    """

    spike_pct: Union[Unset, float] = UNSET
    pace_pct: Union[Unset, float] = UNSET
    min_amount: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        spike_pct = self.spike_pct

        pace_pct = self.pace_pct

        min_amount = self.min_amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if spike_pct is not UNSET:
            field_dict["spikePct"] = spike_pct
        if pace_pct is not UNSET:
            field_dict["pacePct"] = pace_pct
        if min_amount is not UNSET:
            field_dict["minAmount"] = min_amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        spike_pct = d.pop("spikePct", UNSET)

        pace_pct = d.pop("pacePct", UNSET)

        min_amount = d.pop("minAmount", UNSET)

        sensitivity_preset = cls(
            spike_pct=spike_pct,
            pace_pct=pace_pct,
            min_amount=min_amount,
        )

        sensitivity_preset.additional_properties = d
        return sensitivity_preset

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
