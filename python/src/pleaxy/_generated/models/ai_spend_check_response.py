from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ai_spend_check_response_outcome import (
    AiSpendCheckResponseOutcome,
    check_ai_spend_check_response_outcome,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_spend_check_budget import AiSpendCheckBudget
    from ..models.ai_spend_check_purchase_order_line import (
        AiSpendCheckPurchaseOrderLine,
    )


T = TypeVar("T", bound="AiSpendCheckResponse")


@_attrs_define
class AiSpendCheckResponse:
    """
    Attributes:
        outcome (Union[Unset, AiSpendCheckResponseOutcome]):
        period (Union[Unset, str]):
        currency (Union[Unset, str]):
        month_to_date (Union[Unset, float]):
        forecast (Union[Unset, float]):
        purchase_orders (Union[Unset, List['AiSpendCheckPurchaseOrderLine']]):
        budget (Union[Unset, AiSpendCheckBudget]):
    """

    outcome: Union[Unset, AiSpendCheckResponseOutcome] = UNSET
    period: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    month_to_date: Union[Unset, float] = UNSET
    forecast: Union[Unset, float] = UNSET
    purchase_orders: Union[Unset, List["AiSpendCheckPurchaseOrderLine"]] = UNSET
    budget: Union[Unset, "AiSpendCheckBudget"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        outcome: Union[Unset, str] = UNSET
        if not isinstance(self.outcome, Unset):
            outcome = self.outcome

        period = self.period

        currency = self.currency

        month_to_date = self.month_to_date

        forecast = self.forecast

        purchase_orders: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.purchase_orders, Unset):
            purchase_orders = []
            for purchase_orders_item_data in self.purchase_orders:
                purchase_orders_item = purchase_orders_item_data.to_dict()
                purchase_orders.append(purchase_orders_item)

        budget: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.budget, Unset):
            budget = self.budget.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if period is not UNSET:
            field_dict["period"] = period
        if currency is not UNSET:
            field_dict["currency"] = currency
        if month_to_date is not UNSET:
            field_dict["monthToDate"] = month_to_date
        if forecast is not UNSET:
            field_dict["forecast"] = forecast
        if purchase_orders is not UNSET:
            field_dict["purchaseOrders"] = purchase_orders
        if budget is not UNSET:
            field_dict["budget"] = budget

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ai_spend_check_budget import AiSpendCheckBudget
        from ..models.ai_spend_check_purchase_order_line import (
            AiSpendCheckPurchaseOrderLine,
        )

        d = src_dict.copy()
        _outcome = d.pop("outcome", UNSET)
        outcome: Union[Unset, AiSpendCheckResponseOutcome]
        if isinstance(_outcome, Unset):
            outcome = UNSET
        else:
            outcome = check_ai_spend_check_response_outcome(_outcome)

        period = d.pop("period", UNSET)

        currency = d.pop("currency", UNSET)

        month_to_date = d.pop("monthToDate", UNSET)

        forecast = d.pop("forecast", UNSET)

        purchase_orders = []
        _purchase_orders = d.pop("purchaseOrders", UNSET)
        for purchase_orders_item_data in _purchase_orders or []:
            purchase_orders_item = AiSpendCheckPurchaseOrderLine.from_dict(
                purchase_orders_item_data
            )

            purchase_orders.append(purchase_orders_item)

        _budget = d.pop("budget", UNSET)
        budget: Union[Unset, AiSpendCheckBudget]
        if isinstance(_budget, Unset):
            budget = UNSET
        else:
            budget = AiSpendCheckBudget.from_dict(_budget)

        ai_spend_check_response = cls(
            outcome=outcome,
            period=period,
            currency=currency,
            month_to_date=month_to_date,
            forecast=forecast,
            purchase_orders=purchase_orders,
            budget=budget,
        )

        ai_spend_check_response.additional_properties = d
        return ai_spend_check_response

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
