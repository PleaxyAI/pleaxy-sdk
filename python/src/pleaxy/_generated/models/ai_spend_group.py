from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ai_spend_group_invoicer import (
    AiSpendGroupInvoicer,
    check_ai_spend_group_invoicer,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_meter_quantity import AiMeterQuantity
    from ..models.ai_purchase_order_line_remaining import AiPurchaseOrderLineRemaining
    from ..models.ai_service_figure import AiServiceFigure


T = TypeVar("T", bound="AiSpendGroup")


@_attrs_define
class AiSpendGroup:
    """
    Attributes:
        key (Union[Unset, str]):
        label (Union[Unset, str]):
        invoicer (Union[Unset, AiSpendGroupInvoicer]):
        invoicer_id (Union[Unset, str]):
        currency (Union[Unset, str]):
        month_to_date (Union[Unset, float]):
        forecast (Union[Unset, float]):
        last_month (Union[Unset, float]):
        change_pct (Union[Unset, float]):
        quantities (Union[Unset, List['AiMeterQuantity']]):
        purchase_orders (Union[Unset, List['AiPurchaseOrderLineRemaining']]):
        services (Union[Unset, List['AiServiceFigure']]):
    """

    key: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    invoicer: Union[Unset, AiSpendGroupInvoicer] = UNSET
    invoicer_id: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    month_to_date: Union[Unset, float] = UNSET
    forecast: Union[Unset, float] = UNSET
    last_month: Union[Unset, float] = UNSET
    change_pct: Union[Unset, float] = UNSET
    quantities: Union[Unset, List["AiMeterQuantity"]] = UNSET
    purchase_orders: Union[Unset, List["AiPurchaseOrderLineRemaining"]] = UNSET
    services: Union[Unset, List["AiServiceFigure"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key

        label = self.label

        invoicer: Union[Unset, str] = UNSET
        if not isinstance(self.invoicer, Unset):
            invoicer = self.invoicer

        invoicer_id = self.invoicer_id

        currency = self.currency

        month_to_date = self.month_to_date

        forecast = self.forecast

        last_month = self.last_month

        change_pct = self.change_pct

        quantities: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.quantities, Unset):
            quantities = []
            for quantities_item_data in self.quantities:
                quantities_item = quantities_item_data.to_dict()
                quantities.append(quantities_item)

        purchase_orders: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.purchase_orders, Unset):
            purchase_orders = []
            for purchase_orders_item_data in self.purchase_orders:
                purchase_orders_item = purchase_orders_item_data.to_dict()
                purchase_orders.append(purchase_orders_item)

        services: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.services, Unset):
            services = []
            for services_item_data in self.services:
                services_item = services_item_data.to_dict()
                services.append(services_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if label is not UNSET:
            field_dict["label"] = label
        if invoicer is not UNSET:
            field_dict["invoicer"] = invoicer
        if invoicer_id is not UNSET:
            field_dict["invoicerId"] = invoicer_id
        if currency is not UNSET:
            field_dict["currency"] = currency
        if month_to_date is not UNSET:
            field_dict["monthToDate"] = month_to_date
        if forecast is not UNSET:
            field_dict["forecast"] = forecast
        if last_month is not UNSET:
            field_dict["lastMonth"] = last_month
        if change_pct is not UNSET:
            field_dict["changePct"] = change_pct
        if quantities is not UNSET:
            field_dict["quantities"] = quantities
        if purchase_orders is not UNSET:
            field_dict["purchaseOrders"] = purchase_orders
        if services is not UNSET:
            field_dict["services"] = services

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ai_meter_quantity import AiMeterQuantity
        from ..models.ai_purchase_order_line_remaining import (
            AiPurchaseOrderLineRemaining,
        )
        from ..models.ai_service_figure import AiServiceFigure

        d = src_dict.copy()
        key = d.pop("key", UNSET)

        label = d.pop("label", UNSET)

        _invoicer = d.pop("invoicer", UNSET)
        invoicer: Union[Unset, AiSpendGroupInvoicer]
        if isinstance(_invoicer, Unset):
            invoicer = UNSET
        else:
            invoicer = check_ai_spend_group_invoicer(_invoicer)

        invoicer_id = d.pop("invoicerId", UNSET)

        currency = d.pop("currency", UNSET)

        month_to_date = d.pop("monthToDate", UNSET)

        forecast = d.pop("forecast", UNSET)

        last_month = d.pop("lastMonth", UNSET)

        change_pct = d.pop("changePct", UNSET)

        quantities = []
        _quantities = d.pop("quantities", UNSET)
        for quantities_item_data in _quantities or []:
            quantities_item = AiMeterQuantity.from_dict(quantities_item_data)

            quantities.append(quantities_item)

        purchase_orders = []
        _purchase_orders = d.pop("purchaseOrders", UNSET)
        for purchase_orders_item_data in _purchase_orders or []:
            purchase_orders_item = AiPurchaseOrderLineRemaining.from_dict(
                purchase_orders_item_data
            )

            purchase_orders.append(purchase_orders_item)

        services = []
        _services = d.pop("services", UNSET)
        for services_item_data in _services or []:
            services_item = AiServiceFigure.from_dict(services_item_data)

            services.append(services_item)

        ai_spend_group = cls(
            key=key,
            label=label,
            invoicer=invoicer,
            invoicer_id=invoicer_id,
            currency=currency,
            month_to_date=month_to_date,
            forecast=forecast,
            last_month=last_month,
            change_pct=change_pct,
            quantities=quantities,
            purchase_orders=purchase_orders,
            services=services,
        )

        ai_spend_group.additional_properties = d
        return ai_spend_group

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
