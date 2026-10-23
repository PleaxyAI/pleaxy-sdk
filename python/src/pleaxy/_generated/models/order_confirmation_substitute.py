from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderConfirmationSubstitute")


@_attrs_define
class OrderConfirmationSubstitute:
    """
    Attributes:
        supplier_part_id (Union[Unset, str]):
        name (Union[Unset, str]):
        catalog_item_id (Union[Unset, str]):
        unit (Union[Unset, str]):
    """

    supplier_part_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    catalog_item_id: Union[Unset, str] = UNSET
    unit: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        supplier_part_id = self.supplier_part_id

        name = self.name

        catalog_item_id = self.catalog_item_id

        unit = self.unit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if supplier_part_id is not UNSET:
            field_dict["supplierPartId"] = supplier_part_id
        if name is not UNSET:
            field_dict["name"] = name
        if catalog_item_id is not UNSET:
            field_dict["catalogItemId"] = catalog_item_id
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        supplier_part_id = d.pop("supplierPartId", UNSET)

        name = d.pop("name", UNSET)

        catalog_item_id = d.pop("catalogItemId", UNSET)

        unit = d.pop("unit", UNSET)

        order_confirmation_substitute = cls(
            supplier_part_id=supplier_part_id,
            name=name,
            catalog_item_id=catalog_item_id,
            unit=unit,
        )

        order_confirmation_substitute.additional_properties = d
        return order_confirmation_substitute

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
