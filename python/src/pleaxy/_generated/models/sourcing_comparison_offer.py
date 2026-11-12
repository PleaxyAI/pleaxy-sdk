from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SourcingComparisonOffer")


@_attrs_define
class SourcingComparisonOffer:
    """
    Attributes:
        supplier_key (Union[Unset, str]):
        unit_price (Union[None, Unset, float]):
        line_total (Union[None, Unset, float]):
        lead_time_days (Union[None, Unset, float]):
        note (Union[Unset, str]):
        lowest (Union[Unset, bool]):
        meets_needed_by (Union[None, Unset, bool]):
    """

    supplier_key: Union[Unset, str] = UNSET
    unit_price: Union[None, Unset, float] = UNSET
    line_total: Union[None, Unset, float] = UNSET
    lead_time_days: Union[None, Unset, float] = UNSET
    note: Union[Unset, str] = UNSET
    lowest: Union[Unset, bool] = UNSET
    meets_needed_by: Union[None, Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        supplier_key = self.supplier_key

        unit_price: Union[None, Unset, float]
        if isinstance(self.unit_price, Unset):
            unit_price = UNSET
        else:
            unit_price = self.unit_price

        line_total: Union[None, Unset, float]
        if isinstance(self.line_total, Unset):
            line_total = UNSET
        else:
            line_total = self.line_total

        lead_time_days: Union[None, Unset, float]
        if isinstance(self.lead_time_days, Unset):
            lead_time_days = UNSET
        else:
            lead_time_days = self.lead_time_days

        note = self.note

        lowest = self.lowest

        meets_needed_by: Union[None, Unset, bool]
        if isinstance(self.meets_needed_by, Unset):
            meets_needed_by = UNSET
        else:
            meets_needed_by = self.meets_needed_by

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if supplier_key is not UNSET:
            field_dict["supplierKey"] = supplier_key
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if line_total is not UNSET:
            field_dict["lineTotal"] = line_total
        if lead_time_days is not UNSET:
            field_dict["leadTimeDays"] = lead_time_days
        if note is not UNSET:
            field_dict["note"] = note
        if lowest is not UNSET:
            field_dict["lowest"] = lowest
        if meets_needed_by is not UNSET:
            field_dict["meetsNeededBy"] = meets_needed_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        supplier_key = d.pop("supplierKey", UNSET)

        def _parse_unit_price(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        unit_price = _parse_unit_price(d.pop("unitPrice", UNSET))

        def _parse_line_total(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        line_total = _parse_line_total(d.pop("lineTotal", UNSET))

        def _parse_lead_time_days(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        lead_time_days = _parse_lead_time_days(d.pop("leadTimeDays", UNSET))

        note = d.pop("note", UNSET)

        lowest = d.pop("lowest", UNSET)

        def _parse_meets_needed_by(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        meets_needed_by = _parse_meets_needed_by(d.pop("meetsNeededBy", UNSET))

        sourcing_comparison_offer = cls(
            supplier_key=supplier_key,
            unit_price=unit_price,
            line_total=line_total,
            lead_time_days=lead_time_days,
            note=note,
            lowest=lowest,
            meets_needed_by=meets_needed_by,
        )

        sourcing_comparison_offer.additional_properties = d
        return sourcing_comparison_offer

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
