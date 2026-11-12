from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SourcingResponseLine")


@_attrs_define
class SourcingResponseLine:
    """
    Attributes:
        line_id (Union[Unset, str]):
        unit_price (Union[Unset, float]):
        lead_time_days (Union[Unset, float]):
        note (Union[Unset, str]):
    """

    line_id: Union[Unset, str] = UNSET
    unit_price: Union[Unset, float] = UNSET
    lead_time_days: Union[Unset, float] = UNSET
    note: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        line_id = self.line_id

        unit_price = self.unit_price

        lead_time_days = self.lead_time_days

        note = self.note

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if line_id is not UNSET:
            field_dict["lineId"] = line_id
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if lead_time_days is not UNSET:
            field_dict["leadTimeDays"] = lead_time_days
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        line_id = d.pop("lineId", UNSET)

        unit_price = d.pop("unitPrice", UNSET)

        lead_time_days = d.pop("leadTimeDays", UNSET)

        note = d.pop("note", UNSET)

        sourcing_response_line = cls(
            line_id=line_id,
            unit_price=unit_price,
            lead_time_days=lead_time_days,
            note=note,
        )

        sourcing_response_line.additional_properties = d
        return sourcing_response_line

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
