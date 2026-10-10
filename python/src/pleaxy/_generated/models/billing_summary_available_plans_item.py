from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.billing_summary_available_plans_item_plan import (
    BillingSummaryAvailablePlansItemPlan,
    check_billing_summary_available_plans_item_plan,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BillingSummaryAvailablePlansItem")


@_attrs_define
class BillingSummaryAvailablePlansItem:
    """
    Attributes:
        plan (Union[Unset, BillingSummaryAvailablePlansItemPlan]):
        monthly_price_label (Union[Unset, str]):
        yearly_price_label (Union[Unset, str]):
        additional_region_price_labels (Union[Unset, List[str]]):
    """

    plan: Union[Unset, BillingSummaryAvailablePlansItemPlan] = UNSET
    monthly_price_label: Union[Unset, str] = UNSET
    yearly_price_label: Union[Unset, str] = UNSET
    additional_region_price_labels: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        plan: Union[Unset, str] = UNSET
        if not isinstance(self.plan, Unset):
            plan = self.plan

        monthly_price_label = self.monthly_price_label

        yearly_price_label = self.yearly_price_label

        additional_region_price_labels: Union[Unset, List[str]] = UNSET
        if not isinstance(self.additional_region_price_labels, Unset):
            additional_region_price_labels = self.additional_region_price_labels

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if plan is not UNSET:
            field_dict["plan"] = plan
        if monthly_price_label is not UNSET:
            field_dict["monthlyPriceLabel"] = monthly_price_label
        if yearly_price_label is not UNSET:
            field_dict["yearlyPriceLabel"] = yearly_price_label
        if additional_region_price_labels is not UNSET:
            field_dict["additionalRegionPriceLabels"] = additional_region_price_labels

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _plan = d.pop("plan", UNSET)
        plan: Union[Unset, BillingSummaryAvailablePlansItemPlan]
        if isinstance(_plan, Unset):
            plan = UNSET
        else:
            plan = check_billing_summary_available_plans_item_plan(_plan)

        monthly_price_label = d.pop("monthlyPriceLabel", UNSET)

        yearly_price_label = d.pop("yearlyPriceLabel", UNSET)

        additional_region_price_labels = cast(
            List[str], d.pop("additionalRegionPriceLabels", UNSET)
        )

        billing_summary_available_plans_item = cls(
            plan=plan,
            monthly_price_label=monthly_price_label,
            yearly_price_label=yearly_price_label,
            additional_region_price_labels=additional_region_price_labels,
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
