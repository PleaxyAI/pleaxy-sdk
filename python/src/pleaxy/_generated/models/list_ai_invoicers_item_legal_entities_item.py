from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_ai_invoicers_item_legal_entities_item_region import (
    ListAiInvoicersItemLegalEntitiesItemRegion,
    check_list_ai_invoicers_item_legal_entities_item_region,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListAiInvoicersItemLegalEntitiesItem")


@_attrs_define
class ListAiInvoicersItemLegalEntitiesItem:
    """
    Attributes:
        region (Union[Unset, ListAiInvoicersItemLegalEntitiesItemRegion]):
        name (Union[Unset, str]):
        country (Union[Unset, str]):
    """

    region: Union[Unset, ListAiInvoicersItemLegalEntitiesItemRegion] = UNSET
    name: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        region: Union[Unset, str] = UNSET
        if not isinstance(self.region, Unset):
            region = self.region

        name = self.name

        country = self.country

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if region is not UNSET:
            field_dict["region"] = region
        if name is not UNSET:
            field_dict["name"] = name
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _region = d.pop("region", UNSET)
        region: Union[Unset, ListAiInvoicersItemLegalEntitiesItemRegion]
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = check_list_ai_invoicers_item_legal_entities_item_region(_region)

        name = d.pop("name", UNSET)

        country = d.pop("country", UNSET)

        list_ai_invoicers_item_legal_entities_item = cls(
            region=region,
            name=name,
            country=country,
        )

        list_ai_invoicers_item_legal_entities_item.additional_properties = d
        return list_ai_invoicers_item_legal_entities_item

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
