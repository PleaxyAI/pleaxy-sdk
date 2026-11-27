from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.supplier_directory_listing_regions_item import (
        SupplierDirectoryListingRegionsItem,
    )


T = TypeVar("T", bound="SupplierDirectoryListing")


@_attrs_define
class SupplierDirectoryListing:
    """
    Attributes:
        company_name (Union[Unset, str]):
        verified (Union[Unset, bool]):
        regions (Union[Unset, List['SupplierDirectoryListingRegionsItem']]):
        categories (Union[Unset, List[str]]):
        segments (Union[Unset, List[str]]):
        sponsored (Union[Unset, bool]):
        connection_id (Union[Unset, str]):
    """

    company_name: Union[Unset, str] = UNSET
    verified: Union[Unset, bool] = UNSET
    regions: Union[Unset, List["SupplierDirectoryListingRegionsItem"]] = UNSET
    categories: Union[Unset, List[str]] = UNSET
    segments: Union[Unset, List[str]] = UNSET
    sponsored: Union[Unset, bool] = UNSET
    connection_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        company_name = self.company_name

        verified = self.verified

        regions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.regions, Unset):
            regions = []
            for regions_item_data in self.regions:
                regions_item = regions_item_data.to_dict()
                regions.append(regions_item)

        categories: Union[Unset, List[str]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories

        segments: Union[Unset, List[str]] = UNSET
        if not isinstance(self.segments, Unset):
            segments = self.segments

        sponsored = self.sponsored

        connection_id = self.connection_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if verified is not UNSET:
            field_dict["verified"] = verified
        if regions is not UNSET:
            field_dict["regions"] = regions
        if categories is not UNSET:
            field_dict["categories"] = categories
        if segments is not UNSET:
            field_dict["segments"] = segments
        if sponsored is not UNSET:
            field_dict["sponsored"] = sponsored
        if connection_id is not UNSET:
            field_dict["connectionId"] = connection_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.supplier_directory_listing_regions_item import (
            SupplierDirectoryListingRegionsItem,
        )

        d = src_dict.copy()
        company_name = d.pop("companyName", UNSET)

        verified = d.pop("verified", UNSET)

        regions = []
        _regions = d.pop("regions", UNSET)
        for regions_item_data in _regions or []:
            regions_item = SupplierDirectoryListingRegionsItem.from_dict(
                regions_item_data
            )

            regions.append(regions_item)

        categories = cast(List[str], d.pop("categories", UNSET))

        segments = cast(List[str], d.pop("segments", UNSET))

        sponsored = d.pop("sponsored", UNSET)

        connection_id = d.pop("connectionId", UNSET)

        supplier_directory_listing = cls(
            company_name=company_name,
            verified=verified,
            regions=regions,
            categories=categories,
            segments=segments,
            sponsored=sponsored,
            connection_id=connection_id,
        )

        supplier_directory_listing.additional_properties = d
        return supplier_directory_listing

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
