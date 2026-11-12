from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SourcingComparisonNoAnswerItem")


@_attrs_define
class SourcingComparisonNoAnswerItem:
    """
    Attributes:
        supplier_key (Union[Unset, str]):
        supplier_name (Union[Unset, str]):
    """

    supplier_key: Union[Unset, str] = UNSET
    supplier_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        supplier_key = self.supplier_key

        supplier_name = self.supplier_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if supplier_key is not UNSET:
            field_dict["supplierKey"] = supplier_key
        if supplier_name is not UNSET:
            field_dict["supplierName"] = supplier_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        supplier_key = d.pop("supplierKey", UNSET)

        supplier_name = d.pop("supplierName", UNSET)

        sourcing_comparison_no_answer_item = cls(
            supplier_key=supplier_key,
            supplier_name=supplier_name,
        )

        sourcing_comparison_no_answer_item.additional_properties = d
        return sourcing_comparison_no_answer_item

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
