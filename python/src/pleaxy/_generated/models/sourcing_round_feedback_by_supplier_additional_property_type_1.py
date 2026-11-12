from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sourcing_round_feedback_by_supplier_additional_property_type_1_kind import (
    SourcingRoundFeedbackBySupplierAdditionalPropertyType1Kind,
    check_sourcing_round_feedback_by_supplier_additional_property_type_1_kind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SourcingRoundFeedbackBySupplierAdditionalPropertyType1")


@_attrs_define
class SourcingRoundFeedbackBySupplierAdditionalPropertyType1:
    """
    Attributes:
        kind (Union[Unset, SourcingRoundFeedbackBySupplierAdditionalPropertyType1Kind]):
        lowest (Union[Unset, bool]):
        gap_pct (Union[Unset, float]):
    """

    kind: Union[Unset, SourcingRoundFeedbackBySupplierAdditionalPropertyType1Kind] = (
        UNSET
    )
    lowest: Union[Unset, bool] = UNSET
    gap_pct: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        lowest = self.lowest

        gap_pct = self.gap_pct

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if lowest is not UNSET:
            field_dict["lowest"] = lowest
        if gap_pct is not UNSET:
            field_dict["gapPct"] = gap_pct

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, SourcingRoundFeedbackBySupplierAdditionalPropertyType1Kind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_sourcing_round_feedback_by_supplier_additional_property_type_1_kind(
                _kind
            )

        lowest = d.pop("lowest", UNSET)

        gap_pct = d.pop("gapPct", UNSET)

        sourcing_round_feedback_by_supplier_additional_property_type_1 = cls(
            kind=kind,
            lowest=lowest,
            gap_pct=gap_pct,
        )

        sourcing_round_feedback_by_supplier_additional_property_type_1.additional_properties = d
        return sourcing_round_feedback_by_supplier_additional_property_type_1

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
