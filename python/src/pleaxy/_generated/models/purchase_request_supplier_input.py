from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PurchaseRequestSupplierInput")


@_attrs_define
class PurchaseRequestSupplierInput:
    """
    Attributes:
        name (str): The supplier's name, as the requester knows it.
        supplier_connection_id (Union[Unset, str]): A supplier on the workspace's supplier list.
        supplier_region_id (Union[Unset, str]): A connected supplier's workspace region.
    """

    name: str
    supplier_connection_id: Union[Unset, str] = UNSET
    supplier_region_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        supplier_connection_id = self.supplier_connection_id

        supplier_region_id = self.supplier_region_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if supplier_connection_id is not UNSET:
            field_dict["supplierConnectionId"] = supplier_connection_id
        if supplier_region_id is not UNSET:
            field_dict["supplierRegionId"] = supplier_region_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        supplier_connection_id = d.pop("supplierConnectionId", UNSET)

        supplier_region_id = d.pop("supplierRegionId", UNSET)

        purchase_request_supplier_input = cls(
            name=name,
            supplier_connection_id=supplier_connection_id,
            supplier_region_id=supplier_region_id,
        )

        purchase_request_supplier_input.additional_properties = d
        return purchase_request_supplier_input

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
