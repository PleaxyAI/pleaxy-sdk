from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SubstituteItemInput")


@_attrs_define
class SubstituteItemInput:
    """
    Attributes:
        supplier_part_id (str):
        name (str):
    """

    supplier_part_id: str
    name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        supplier_part_id = self.supplier_part_id

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "supplierPartId": supplier_part_id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        supplier_part_id = d.pop("supplierPartId")

        name = d.pop("name")

        substitute_item_input = cls(
            supplier_part_id=supplier_part_id,
            name=name,
        )

        substitute_item_input.additional_properties = d
        return substitute_item_input

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
