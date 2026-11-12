from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sourcing_round_feedback_by_supplier_additional_property_type_0_kind import (
    SourcingRoundFeedbackBySupplierAdditionalPropertyType0Kind,
    check_sourcing_round_feedback_by_supplier_additional_property_type_0_kind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SourcingRoundFeedbackBySupplierAdditionalPropertyType0")


@_attrs_define
class SourcingRoundFeedbackBySupplierAdditionalPropertyType0:
    """
    Attributes:
        kind (Union[Unset, SourcingRoundFeedbackBySupplierAdditionalPropertyType0Kind]):
        rank (Union[Unset, float]):
        of (Union[Unset, float]):
    """

    kind: Union[Unset, SourcingRoundFeedbackBySupplierAdditionalPropertyType0Kind] = (
        UNSET
    )
    rank: Union[Unset, float] = UNSET
    of: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        rank = self.rank

        of = self.of

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if rank is not UNSET:
            field_dict["rank"] = rank
        if of is not UNSET:
            field_dict["of"] = of

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, SourcingRoundFeedbackBySupplierAdditionalPropertyType0Kind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_sourcing_round_feedback_by_supplier_additional_property_type_0_kind(
                _kind
            )

        rank = d.pop("rank", UNSET)

        of = d.pop("of", UNSET)

        sourcing_round_feedback_by_supplier_additional_property_type_0 = cls(
            kind=kind,
            rank=rank,
            of=of,
        )

        sourcing_round_feedback_by_supplier_additional_property_type_0.additional_properties = d
        return sourcing_round_feedback_by_supplier_additional_property_type_0

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
