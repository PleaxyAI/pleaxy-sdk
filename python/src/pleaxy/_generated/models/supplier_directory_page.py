from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.supplier_directory_listing import SupplierDirectoryListing


T = TypeVar("T", bound="SupplierDirectoryPage")


@_attrs_define
class SupplierDirectoryPage:
    """
    Attributes:
        suppliers (Union[Unset, List['SupplierDirectoryListing']]):
        total (Union[Unset, float]):
        next_offset (Union[Unset, float]):
    """

    suppliers: Union[Unset, List["SupplierDirectoryListing"]] = UNSET
    total: Union[Unset, float] = UNSET
    next_offset: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        suppliers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.suppliers, Unset):
            suppliers = []
            for suppliers_item_data in self.suppliers:
                suppliers_item = suppliers_item_data.to_dict()
                suppliers.append(suppliers_item)

        total = self.total

        next_offset = self.next_offset

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if suppliers is not UNSET:
            field_dict["suppliers"] = suppliers
        if total is not UNSET:
            field_dict["total"] = total
        if next_offset is not UNSET:
            field_dict["nextOffset"] = next_offset

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.supplier_directory_listing import SupplierDirectoryListing

        d = src_dict.copy()
        suppliers = []
        _suppliers = d.pop("suppliers", UNSET)
        for suppliers_item_data in _suppliers or []:
            suppliers_item = SupplierDirectoryListing.from_dict(suppliers_item_data)

            suppliers.append(suppliers_item)

        total = d.pop("total", UNSET)

        next_offset = d.pop("nextOffset", UNSET)

        supplier_directory_page = cls(
            suppliers=suppliers,
            total=total,
            next_offset=next_offset,
        )

        supplier_directory_page.additional_properties = d
        return supplier_directory_page

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
