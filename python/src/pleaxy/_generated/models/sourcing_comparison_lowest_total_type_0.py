from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SourcingComparisonLowestTotalType0")


@_attrs_define
class SourcingComparisonLowestTotalType0:
    """
    Attributes:
        supplier_key (Union[Unset, str]):
        total (Union[Unset, float]):
    """

    supplier_key: Union[Unset, str] = UNSET
    total: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        supplier_key = self.supplier_key

        total = self.total

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if supplier_key is not UNSET:
            field_dict["supplierKey"] = supplier_key
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        supplier_key = d.pop("supplierKey", UNSET)

        total = d.pop("total", UNSET)

        sourcing_comparison_lowest_total_type_0 = cls(
            supplier_key=supplier_key,
            total=total,
        )

        sourcing_comparison_lowest_total_type_0.additional_properties = d
        return sourcing_comparison_lowest_total_type_0

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
