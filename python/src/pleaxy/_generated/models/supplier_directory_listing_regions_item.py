from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SupplierDirectoryListingRegionsItem")


@_attrs_define
class SupplierDirectoryListingRegionsItem:
    """
    Attributes:
        region_name (Union[Unset, str]):
        directory_id (Union[Unset, str]):
    """

    region_name: Union[Unset, str] = UNSET
    directory_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        region_name = self.region_name

        directory_id = self.directory_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if region_name is not UNSET:
            field_dict["regionName"] = region_name
        if directory_id is not UNSET:
            field_dict["directoryId"] = directory_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        region_name = d.pop("regionName", UNSET)

        directory_id = d.pop("directoryId", UNSET)

        supplier_directory_listing_regions_item = cls(
            region_name=region_name,
            directory_id=directory_id,
        )

        supplier_directory_listing_regions_item.additional_properties = d
        return supplier_directory_listing_regions_item

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
