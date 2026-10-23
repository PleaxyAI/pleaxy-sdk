from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.receipt import Receipt
    from ..models.service_entry_sheet_queue_item_releases_item import (
        ServiceEntrySheetQueueItemReleasesItem,
    )


T = TypeVar("T", bound="ServiceEntrySheetQueueItem")


@_attrs_define
class ServiceEntrySheetQueueItem:
    """
    Attributes:
        receipt (Union[Unset, Receipt]):
        supplier (Union[Unset, str]):
        supplier_org_id (Union[Unset, str]):
        releases (Union[Unset, List['ServiceEntrySheetQueueItemReleasesItem']]):
    """

    receipt: Union[Unset, "Receipt"] = UNSET
    supplier: Union[Unset, str] = UNSET
    supplier_org_id: Union[Unset, str] = UNSET
    releases: Union[Unset, List["ServiceEntrySheetQueueItemReleasesItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        receipt: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.receipt, Unset):
            receipt = self.receipt.to_dict()

        supplier = self.supplier

        supplier_org_id = self.supplier_org_id

        releases: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.releases, Unset):
            releases = []
            for releases_item_data in self.releases:
                releases_item = releases_item_data.to_dict()
                releases.append(releases_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if receipt is not UNSET:
            field_dict["receipt"] = receipt
        if supplier is not UNSET:
            field_dict["supplier"] = supplier
        if supplier_org_id is not UNSET:
            field_dict["supplierOrgId"] = supplier_org_id
        if releases is not UNSET:
            field_dict["releases"] = releases

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.receipt import Receipt
        from ..models.service_entry_sheet_queue_item_releases_item import (
            ServiceEntrySheetQueueItemReleasesItem,
        )

        d = src_dict.copy()
        _receipt = d.pop("receipt", UNSET)
        receipt: Union[Unset, Receipt]
        if isinstance(_receipt, Unset):
            receipt = UNSET
        else:
            receipt = Receipt.from_dict(_receipt)

        supplier = d.pop("supplier", UNSET)

        supplier_org_id = d.pop("supplierOrgId", UNSET)

        releases = []
        _releases = d.pop("releases", UNSET)
        for releases_item_data in _releases or []:
            releases_item = ServiceEntrySheetQueueItemReleasesItem.from_dict(
                releases_item_data
            )

            releases.append(releases_item)

        service_entry_sheet_queue_item = cls(
            receipt=receipt,
            supplier=supplier,
            supplier_org_id=supplier_org_id,
            releases=releases,
        )

        service_entry_sheet_queue_item.additional_properties = d
        return service_entry_sheet_queue_item

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
