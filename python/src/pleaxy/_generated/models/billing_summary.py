from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.billing_summary_interval import (
    BillingSummaryInterval,
    check_billing_summary_interval,
)
from ..models.billing_summary_managed_by import (
    BillingSummaryManagedBy,
    check_billing_summary_managed_by,
)
from ..models.billing_summary_plan import BillingSummaryPlan, check_billing_summary_plan
from ..models.billing_summary_subscription_status import (
    BillingSummarySubscriptionStatus,
    check_billing_summary_subscription_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.billing_summary_available_plans_item import (
        BillingSummaryAvailablePlansItem,
    )
    from ..models.billing_summary_aws_marketplace import BillingSummaryAwsMarketplace
    from ..models.price_amount import PriceAmount


T = TypeVar("T", bound="BillingSummary")


@_attrs_define
class BillingSummary:
    """
    Attributes:
        billing_enabled (Union[Unset, bool]):
        plan (Union[Unset, BillingSummaryPlan]):
        managed_by (Union[Unset, BillingSummaryManagedBy]):
        aws_marketplace (Union[Unset, BillingSummaryAwsMarketplace]):
        has_billing_account (Union[Unset, bool]):
        subscription_status (Union[Unset, BillingSummarySubscriptionStatus]):
        current_period_end (Union[Unset, str]):
        cancel_at_period_end (Union[Unset, bool]):
        past_due_since (Union[Unset, str]):
        buyer_region_count (Union[Unset, float]):
        supplier_region_count (Union[Unset, float]):
        interval (Union[Unset, BillingSummaryInterval]):
        available_plans (Union[Unset, List['BillingSummaryAvailablePlansItem']]):
        current_price_label (Union[Unset, str]):
        current_price (Union[Unset, PriceAmount]):
        current_total_label (Union[Unset, str]):
        current_total (Union[Unset, PriceAmount]):
    """

    billing_enabled: Union[Unset, bool] = UNSET
    plan: Union[Unset, BillingSummaryPlan] = UNSET
    managed_by: Union[Unset, BillingSummaryManagedBy] = UNSET
    aws_marketplace: Union[Unset, "BillingSummaryAwsMarketplace"] = UNSET
    has_billing_account: Union[Unset, bool] = UNSET
    subscription_status: Union[Unset, BillingSummarySubscriptionStatus] = UNSET
    current_period_end: Union[Unset, str] = UNSET
    cancel_at_period_end: Union[Unset, bool] = UNSET
    past_due_since: Union[Unset, str] = UNSET
    buyer_region_count: Union[Unset, float] = UNSET
    supplier_region_count: Union[Unset, float] = UNSET
    interval: Union[Unset, BillingSummaryInterval] = UNSET
    available_plans: Union[Unset, List["BillingSummaryAvailablePlansItem"]] = UNSET
    current_price_label: Union[Unset, str] = UNSET
    current_price: Union[Unset, "PriceAmount"] = UNSET
    current_total_label: Union[Unset, str] = UNSET
    current_total: Union[Unset, "PriceAmount"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        billing_enabled = self.billing_enabled

        plan: Union[Unset, str] = UNSET
        if not isinstance(self.plan, Unset):
            plan = self.plan

        managed_by: Union[Unset, str] = UNSET
        if not isinstance(self.managed_by, Unset):
            managed_by = self.managed_by

        aws_marketplace: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aws_marketplace, Unset):
            aws_marketplace = self.aws_marketplace.to_dict()

        has_billing_account = self.has_billing_account

        subscription_status: Union[Unset, str] = UNSET
        if not isinstance(self.subscription_status, Unset):
            subscription_status = self.subscription_status

        current_period_end = self.current_period_end

        cancel_at_period_end = self.cancel_at_period_end

        past_due_since = self.past_due_since

        buyer_region_count = self.buyer_region_count

        supplier_region_count = self.supplier_region_count

        interval: Union[Unset, str] = UNSET
        if not isinstance(self.interval, Unset):
            interval = self.interval

        available_plans: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.available_plans, Unset):
            available_plans = []
            for available_plans_item_data in self.available_plans:
                available_plans_item = available_plans_item_data.to_dict()
                available_plans.append(available_plans_item)

        current_price_label = self.current_price_label

        current_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.current_price, Unset):
            current_price = self.current_price.to_dict()

        current_total_label = self.current_total_label

        current_total: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.current_total, Unset):
            current_total = self.current_total.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if billing_enabled is not UNSET:
            field_dict["billingEnabled"] = billing_enabled
        if plan is not UNSET:
            field_dict["plan"] = plan
        if managed_by is not UNSET:
            field_dict["managedBy"] = managed_by
        if aws_marketplace is not UNSET:
            field_dict["awsMarketplace"] = aws_marketplace
        if has_billing_account is not UNSET:
            field_dict["hasBillingAccount"] = has_billing_account
        if subscription_status is not UNSET:
            field_dict["subscriptionStatus"] = subscription_status
        if current_period_end is not UNSET:
            field_dict["currentPeriodEnd"] = current_period_end
        if cancel_at_period_end is not UNSET:
            field_dict["cancelAtPeriodEnd"] = cancel_at_period_end
        if past_due_since is not UNSET:
            field_dict["pastDueSince"] = past_due_since
        if buyer_region_count is not UNSET:
            field_dict["buyerRegionCount"] = buyer_region_count
        if supplier_region_count is not UNSET:
            field_dict["supplierRegionCount"] = supplier_region_count
        if interval is not UNSET:
            field_dict["interval"] = interval
        if available_plans is not UNSET:
            field_dict["availablePlans"] = available_plans
        if current_price_label is not UNSET:
            field_dict["currentPriceLabel"] = current_price_label
        if current_price is not UNSET:
            field_dict["currentPrice"] = current_price
        if current_total_label is not UNSET:
            field_dict["currentTotalLabel"] = current_total_label
        if current_total is not UNSET:
            field_dict["currentTotal"] = current_total

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.billing_summary_available_plans_item import (
            BillingSummaryAvailablePlansItem,
        )
        from ..models.billing_summary_aws_marketplace import (
            BillingSummaryAwsMarketplace,
        )
        from ..models.price_amount import PriceAmount

        d = src_dict.copy()
        billing_enabled = d.pop("billingEnabled", UNSET)

        _plan = d.pop("plan", UNSET)
        plan: Union[Unset, BillingSummaryPlan]
        if isinstance(_plan, Unset):
            plan = UNSET
        else:
            plan = check_billing_summary_plan(_plan)

        _managed_by = d.pop("managedBy", UNSET)
        managed_by: Union[Unset, BillingSummaryManagedBy]
        if isinstance(_managed_by, Unset):
            managed_by = UNSET
        else:
            managed_by = check_billing_summary_managed_by(_managed_by)

        _aws_marketplace = d.pop("awsMarketplace", UNSET)
        aws_marketplace: Union[Unset, BillingSummaryAwsMarketplace]
        if isinstance(_aws_marketplace, Unset):
            aws_marketplace = UNSET
        else:
            aws_marketplace = BillingSummaryAwsMarketplace.from_dict(_aws_marketplace)

        has_billing_account = d.pop("hasBillingAccount", UNSET)

        _subscription_status = d.pop("subscriptionStatus", UNSET)
        subscription_status: Union[Unset, BillingSummarySubscriptionStatus]
        if isinstance(_subscription_status, Unset):
            subscription_status = UNSET
        else:
            subscription_status = check_billing_summary_subscription_status(
                _subscription_status
            )

        current_period_end = d.pop("currentPeriodEnd", UNSET)

        cancel_at_period_end = d.pop("cancelAtPeriodEnd", UNSET)

        past_due_since = d.pop("pastDueSince", UNSET)

        buyer_region_count = d.pop("buyerRegionCount", UNSET)

        supplier_region_count = d.pop("supplierRegionCount", UNSET)

        _interval = d.pop("interval", UNSET)
        interval: Union[Unset, BillingSummaryInterval]
        if isinstance(_interval, Unset):
            interval = UNSET
        else:
            interval = check_billing_summary_interval(_interval)

        available_plans = []
        _available_plans = d.pop("availablePlans", UNSET)
        for available_plans_item_data in _available_plans or []:
            available_plans_item = BillingSummaryAvailablePlansItem.from_dict(
                available_plans_item_data
            )

            available_plans.append(available_plans_item)

        current_price_label = d.pop("currentPriceLabel", UNSET)

        _current_price = d.pop("currentPrice", UNSET)
        current_price: Union[Unset, PriceAmount]
        if isinstance(_current_price, Unset):
            current_price = UNSET
        else:
            current_price = PriceAmount.from_dict(_current_price)

        current_total_label = d.pop("currentTotalLabel", UNSET)

        _current_total = d.pop("currentTotal", UNSET)
        current_total: Union[Unset, PriceAmount]
        if isinstance(_current_total, Unset):
            current_total = UNSET
        else:
            current_total = PriceAmount.from_dict(_current_total)

        billing_summary = cls(
            billing_enabled=billing_enabled,
            plan=plan,
            managed_by=managed_by,
            aws_marketplace=aws_marketplace,
            has_billing_account=has_billing_account,
            subscription_status=subscription_status,
            current_period_end=current_period_end,
            cancel_at_period_end=cancel_at_period_end,
            past_due_since=past_due_since,
            buyer_region_count=buyer_region_count,
            supplier_region_count=supplier_region_count,
            interval=interval,
            available_plans=available_plans,
            current_price_label=current_price_label,
            current_price=current_price,
            current_total_label=current_total_label,
            current_total=current_total,
        )

        billing_summary.additional_properties = d
        return billing_summary

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
