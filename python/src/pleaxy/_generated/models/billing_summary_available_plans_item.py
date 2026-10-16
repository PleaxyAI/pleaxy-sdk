from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.billing_summary_available_plans_item_plan import (
    BillingSummaryAvailablePlansItemPlan,
    check_billing_summary_available_plans_item_plan,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.price_amount import PriceAmount
    from ..models.region_tier_price import RegionTierPrice


T = TypeVar("T", bound="BillingSummaryAvailablePlansItem")


@_attrs_define
class BillingSummaryAvailablePlansItem:
    """
    Attributes:
        plan (Union[Unset, BillingSummaryAvailablePlansItemPlan]):
        monthly_price_label (Union[Unset, str]):
        monthly_price (Union[Unset, PriceAmount]):
        yearly_price_label (Union[Unset, str]):
        yearly_price (Union[Unset, PriceAmount]):
        additional_region_price_labels (Union[Unset, List[str]]):
        additional_region_prices (Union[Unset, List['RegionTierPrice']]):
    """

    plan: Union[Unset, BillingSummaryAvailablePlansItemPlan] = UNSET
    monthly_price_label: Union[Unset, str] = UNSET
    monthly_price: Union[Unset, "PriceAmount"] = UNSET
    yearly_price_label: Union[Unset, str] = UNSET
    yearly_price: Union[Unset, "PriceAmount"] = UNSET
    additional_region_price_labels: Union[Unset, List[str]] = UNSET
    additional_region_prices: Union[Unset, List["RegionTierPrice"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        plan: Union[Unset, str] = UNSET
        if not isinstance(self.plan, Unset):
            plan = self.plan

        monthly_price_label = self.monthly_price_label

        monthly_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.monthly_price, Unset):
            monthly_price = self.monthly_price.to_dict()

        yearly_price_label = self.yearly_price_label

        yearly_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.yearly_price, Unset):
            yearly_price = self.yearly_price.to_dict()

        additional_region_price_labels: Union[Unset, List[str]] = UNSET
        if not isinstance(self.additional_region_price_labels, Unset):
            additional_region_price_labels = self.additional_region_price_labels

        additional_region_prices: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.additional_region_prices, Unset):
            additional_region_prices = []
            for additional_region_prices_item_data in self.additional_region_prices:
                additional_region_prices_item = (
                    additional_region_prices_item_data.to_dict()
                )
                additional_region_prices.append(additional_region_prices_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if plan is not UNSET:
            field_dict["plan"] = plan
        if monthly_price_label is not UNSET:
            field_dict["monthlyPriceLabel"] = monthly_price_label
        if monthly_price is not UNSET:
            field_dict["monthlyPrice"] = monthly_price
        if yearly_price_label is not UNSET:
            field_dict["yearlyPriceLabel"] = yearly_price_label
        if yearly_price is not UNSET:
            field_dict["yearlyPrice"] = yearly_price
        if additional_region_price_labels is not UNSET:
            field_dict["additionalRegionPriceLabels"] = additional_region_price_labels
        if additional_region_prices is not UNSET:
            field_dict["additionalRegionPrices"] = additional_region_prices

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.price_amount import PriceAmount
        from ..models.region_tier_price import RegionTierPrice

        d = src_dict.copy()
        _plan = d.pop("plan", UNSET)
        plan: Union[Unset, BillingSummaryAvailablePlansItemPlan]
        if isinstance(_plan, Unset):
            plan = UNSET
        else:
            plan = check_billing_summary_available_plans_item_plan(_plan)

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

        additional_region_price_labels = cast(
            List[str], d.pop("additionalRegionPriceLabels", UNSET)
        )

        additional_region_prices = []
        _additional_region_prices = d.pop("additionalRegionPrices", UNSET)
        for additional_region_prices_item_data in _additional_region_prices or []:
            additional_region_prices_item = RegionTierPrice.from_dict(
                additional_region_prices_item_data
            )

            additional_region_prices.append(additional_region_prices_item)

        billing_summary_available_plans_item = cls(
            plan=plan,
            monthly_price_label=monthly_price_label,
            monthly_price=monthly_price,
            yearly_price_label=yearly_price_label,
            yearly_price=yearly_price,
            additional_region_price_labels=additional_region_price_labels,
            additional_region_prices=additional_region_prices,
        )

        billing_summary_available_plans_item.additional_properties = d
        return billing_summary_available_plans_item

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
