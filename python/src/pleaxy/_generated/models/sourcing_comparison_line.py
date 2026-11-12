from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sourcing_comparison_offer import SourcingComparisonOffer


T = TypeVar("T", bound="SourcingComparisonLine")


@_attrs_define
class SourcingComparisonLine:
    """
    Attributes:
        line_id (Union[Unset, str]):
        name (Union[Unset, str]):
        qty (Union[Unset, float]):
        unit (Union[Unset, str]):
        needed_by (Union[Unset, str]):
        target_unit_price (Union[Unset, float]):
        offers (Union[Unset, List['SourcingComparisonOffer']]):
    """

    line_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    qty: Union[Unset, float] = UNSET
    unit: Union[Unset, str] = UNSET
    needed_by: Union[Unset, str] = UNSET
    target_unit_price: Union[Unset, float] = UNSET
    offers: Union[Unset, List["SourcingComparisonOffer"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        line_id = self.line_id

        name = self.name

        qty = self.qty

        unit = self.unit

        needed_by = self.needed_by

        target_unit_price = self.target_unit_price

        offers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.offers, Unset):
            offers = []
            for offers_item_data in self.offers:
                offers_item = offers_item_data.to_dict()
                offers.append(offers_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if line_id is not UNSET:
            field_dict["lineId"] = line_id
        if name is not UNSET:
            field_dict["name"] = name
        if qty is not UNSET:
            field_dict["qty"] = qty
        if unit is not UNSET:
            field_dict["unit"] = unit
        if needed_by is not UNSET:
            field_dict["neededBy"] = needed_by
        if target_unit_price is not UNSET:
            field_dict["targetUnitPrice"] = target_unit_price
        if offers is not UNSET:
            field_dict["offers"] = offers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sourcing_comparison_offer import SourcingComparisonOffer

        d = src_dict.copy()
        line_id = d.pop("lineId", UNSET)

        name = d.pop("name", UNSET)

        qty = d.pop("qty", UNSET)

        unit = d.pop("unit", UNSET)

        needed_by = d.pop("neededBy", UNSET)

        target_unit_price = d.pop("targetUnitPrice", UNSET)

        offers = []
        _offers = d.pop("offers", UNSET)
        for offers_item_data in _offers or []:
            offers_item = SourcingComparisonOffer.from_dict(offers_item_data)

            offers.append(offers_item)

        sourcing_comparison_line = cls(
            line_id=line_id,
            name=name,
            qty=qty,
            unit=unit,
            needed_by=needed_by,
            target_unit_price=target_unit_price,
            offers=offers,
        )

        sourcing_comparison_line.additional_properties = d
        return sourcing_comparison_line

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
