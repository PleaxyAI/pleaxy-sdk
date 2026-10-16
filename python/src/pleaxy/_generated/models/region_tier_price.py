from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.price_amount import PriceAmount


T = TypeVar("T", bound="RegionTierPrice")


@_attrs_define
class RegionTierPrice:
    """
    Attributes:
        from_region (Union[Unset, float]):
        to_region (Union[None, Unset, float]):
        price (Union[Unset, PriceAmount]):
    """

    from_region: Union[Unset, float] = UNSET
    to_region: Union[None, Unset, float] = UNSET
    price: Union[Unset, "PriceAmount"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from_region = self.from_region

        to_region: Union[None, Unset, float]
        if isinstance(self.to_region, Unset):
            to_region = UNSET
        else:
            to_region = self.to_region

        price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_region is not UNSET:
            field_dict["fromRegion"] = from_region
        if to_region is not UNSET:
            field_dict["toRegion"] = to_region
        if price is not UNSET:
            field_dict["price"] = price

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.price_amount import PriceAmount

        d = src_dict.copy()
        from_region = d.pop("fromRegion", UNSET)

        def _parse_to_region(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        to_region = _parse_to_region(d.pop("toRegion", UNSET))

        _price = d.pop("price", UNSET)
        price: Union[Unset, PriceAmount]
        if isinstance(_price, Unset):
            price = UNSET
        else:
            price = PriceAmount.from_dict(_price)

        region_tier_price = cls(
            from_region=from_region,
            to_region=to_region,
            price=price,
        )

        region_tier_price.additional_properties = d
        return region_tier_price

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
