from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.module_offer_item import ModuleOfferItem, check_module_offer_item
from ..models.module_offer_kind import ModuleOfferKind, check_module_offer_kind
from ..models.module_offer_modules_item import (
    ModuleOfferModulesItem,
    check_module_offer_modules_item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.price_amount import PriceAmount


T = TypeVar("T", bound="ModuleOffer")


@_attrs_define
class ModuleOffer:
    """
    Attributes:
        item (Union[Unset, ModuleOfferItem]):
        kind (Union[Unset, ModuleOfferKind]):
        modules (Union[Unset, List[ModuleOfferModulesItem]]):
        monthly_price_label (Union[Unset, str]):
        monthly_price (Union[Unset, PriceAmount]):
        yearly_price_label (Union[Unset, str]):
        yearly_price (Union[Unset, PriceAmount]):
    """

    item: Union[Unset, ModuleOfferItem] = UNSET
    kind: Union[Unset, ModuleOfferKind] = UNSET
    modules: Union[Unset, List[ModuleOfferModulesItem]] = UNSET
    monthly_price_label: Union[Unset, str] = UNSET
    monthly_price: Union[Unset, "PriceAmount"] = UNSET
    yearly_price_label: Union[Unset, str] = UNSET
    yearly_price: Union[Unset, "PriceAmount"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        item: Union[Unset, str] = UNSET
        if not isinstance(self.item, Unset):
            item = self.item

        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        modules: Union[Unset, List[str]] = UNSET
        if not isinstance(self.modules, Unset):
            modules = []
            for modules_item_data in self.modules:
                modules_item: str = modules_item_data
                modules.append(modules_item)

        monthly_price_label = self.monthly_price_label

        monthly_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.monthly_price, Unset):
            monthly_price = self.monthly_price.to_dict()

        yearly_price_label = self.yearly_price_label

        yearly_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.yearly_price, Unset):
            yearly_price = self.yearly_price.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if item is not UNSET:
            field_dict["item"] = item
        if kind is not UNSET:
            field_dict["kind"] = kind
        if modules is not UNSET:
            field_dict["modules"] = modules
        if monthly_price_label is not UNSET:
            field_dict["monthlyPriceLabel"] = monthly_price_label
        if monthly_price is not UNSET:
            field_dict["monthlyPrice"] = monthly_price
        if yearly_price_label is not UNSET:
            field_dict["yearlyPriceLabel"] = yearly_price_label
        if yearly_price is not UNSET:
            field_dict["yearlyPrice"] = yearly_price

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.price_amount import PriceAmount

        d = src_dict.copy()
        _item = d.pop("item", UNSET)
        item: Union[Unset, ModuleOfferItem]
        if isinstance(_item, Unset):
            item = UNSET
        else:
            item = check_module_offer_item(_item)

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, ModuleOfferKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_module_offer_kind(_kind)

        modules = []
        _modules = d.pop("modules", UNSET)
        for modules_item_data in _modules or []:
            modules_item = check_module_offer_modules_item(modules_item_data)

            modules.append(modules_item)

        monthly_price_label = d.pop("monthlyPriceLabel", UNSET)

        _monthly_price = d.pop("monthlyPrice", UNSET)
        monthly_price: Union[Unset, PriceAmount]
        if isinstance(_monthly_price, Unset):
            monthly_price = UNSET
        else:
            monthly_price = PriceAmount.from_dict(_monthly_price)

        yearly_price_label = d.pop("yearlyPriceLabel", UNSET)

        _yearly_price = d.pop("yearlyPrice", UNSET)
        yearly_price: Union[Unset, PriceAmount]
        if isinstance(_yearly_price, Unset):
            yearly_price = UNSET
        else:
            yearly_price = PriceAmount.from_dict(_yearly_price)

        module_offer = cls(
            item=item,
            kind=kind,
            modules=modules,
            monthly_price_label=monthly_price_label,
            monthly_price=monthly_price,
            yearly_price_label=yearly_price_label,
            yearly_price=yearly_price,
        )

        module_offer.additional_properties = d
        return module_offer

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
