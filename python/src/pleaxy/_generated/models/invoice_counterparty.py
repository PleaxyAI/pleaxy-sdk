from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_counterparty_cloud_provider import (
    InvoiceCounterpartyCloudProvider,
    check_invoice_counterparty_cloud_provider,
)
from ..models.invoice_counterparty_feed_readiness import (
    InvoiceCounterpartyFeedReadiness,
    check_invoice_counterparty_feed_readiness,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_counterparty_open_purchase_orders_item import (
        InvoiceCounterpartyOpenPurchaseOrdersItem,
    )


T = TypeVar("T", bound="InvoiceCounterparty")


@_attrs_define
class InvoiceCounterparty:
    """
    Attributes:
        connection_id (Union[Unset, str]):
        name (Union[Unset, str]):
        currency (Union[Unset, str]):
        currencies (Union[Unset, List[str]]):
        payment_currency (Union[Unset, str]):
        open_purchase_orders (Union[Unset, List['InvoiceCounterpartyOpenPurchaseOrdersItem']]):
        invoice_feed_enabled (Union[Unset, bool]):
        invoice_feed_updated_at (Union[Unset, str]):
        feed_readiness (Union[Unset, InvoiceCounterpartyFeedReadiness]):
        feed_accepted_count (Union[Unset, float]):
        feed_last_accepted_at (Union[Unset, str]):
        feed_last_valid_at (Union[Unset, str]):
        feed_valid_count (Union[Unset, float]):
        approved_at (Union[Unset, str]):
        multiple_connections (Union[Unset, bool]):
        off_platform (Union[Unset, bool]):
        cloud_provider (Union[Unset, InvoiceCounterpartyCloudProvider]):
    """

    connection_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    currencies: Union[Unset, List[str]] = UNSET
    payment_currency: Union[Unset, str] = UNSET
    open_purchase_orders: Union[
        Unset, List["InvoiceCounterpartyOpenPurchaseOrdersItem"]
    ] = UNSET
    invoice_feed_enabled: Union[Unset, bool] = UNSET
    invoice_feed_updated_at: Union[Unset, str] = UNSET
    feed_readiness: Union[Unset, InvoiceCounterpartyFeedReadiness] = UNSET
    feed_accepted_count: Union[Unset, float] = UNSET
    feed_last_accepted_at: Union[Unset, str] = UNSET
    feed_last_valid_at: Union[Unset, str] = UNSET
    feed_valid_count: Union[Unset, float] = UNSET
    approved_at: Union[Unset, str] = UNSET
    multiple_connections: Union[Unset, bool] = UNSET
    off_platform: Union[Unset, bool] = UNSET
    cloud_provider: Union[Unset, InvoiceCounterpartyCloudProvider] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_id = self.connection_id

        name = self.name

        currency = self.currency

        currencies: Union[Unset, List[str]] = UNSET
        if not isinstance(self.currencies, Unset):
            currencies = self.currencies

        payment_currency = self.payment_currency

        open_purchase_orders: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.open_purchase_orders, Unset):
            open_purchase_orders = []
            for open_purchase_orders_item_data in self.open_purchase_orders:
                open_purchase_orders_item = open_purchase_orders_item_data.to_dict()
                open_purchase_orders.append(open_purchase_orders_item)

        invoice_feed_enabled = self.invoice_feed_enabled

        invoice_feed_updated_at = self.invoice_feed_updated_at

        feed_readiness: Union[Unset, str] = UNSET
        if not isinstance(self.feed_readiness, Unset):
            feed_readiness = self.feed_readiness

        feed_accepted_count = self.feed_accepted_count

        feed_last_accepted_at = self.feed_last_accepted_at

        feed_last_valid_at = self.feed_last_valid_at

        feed_valid_count = self.feed_valid_count

        approved_at = self.approved_at

        multiple_connections = self.multiple_connections

        off_platform = self.off_platform

        cloud_provider: Union[Unset, str] = UNSET
        if not isinstance(self.cloud_provider, Unset):
            cloud_provider = self.cloud_provider

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connection_id is not UNSET:
            field_dict["connectionId"] = connection_id
        if name is not UNSET:
            field_dict["name"] = name
        if currency is not UNSET:
            field_dict["currency"] = currency
        if currencies is not UNSET:
            field_dict["currencies"] = currencies
        if payment_currency is not UNSET:
            field_dict["paymentCurrency"] = payment_currency
        if open_purchase_orders is not UNSET:
            field_dict["openPurchaseOrders"] = open_purchase_orders
        if invoice_feed_enabled is not UNSET:
            field_dict["invoiceFeedEnabled"] = invoice_feed_enabled
        if invoice_feed_updated_at is not UNSET:
            field_dict["invoiceFeedUpdatedAt"] = invoice_feed_updated_at
        if feed_readiness is not UNSET:
            field_dict["feedReadiness"] = feed_readiness
        if feed_accepted_count is not UNSET:
            field_dict["feedAcceptedCount"] = feed_accepted_count
        if feed_last_accepted_at is not UNSET:
            field_dict["feedLastAcceptedAt"] = feed_last_accepted_at
        if feed_last_valid_at is not UNSET:
            field_dict["feedLastValidAt"] = feed_last_valid_at
        if feed_valid_count is not UNSET:
            field_dict["feedValidCount"] = feed_valid_count
        if approved_at is not UNSET:
            field_dict["approvedAt"] = approved_at
        if multiple_connections is not UNSET:
            field_dict["multipleConnections"] = multiple_connections
        if off_platform is not UNSET:
            field_dict["offPlatform"] = off_platform
        if cloud_provider is not UNSET:
            field_dict["cloudProvider"] = cloud_provider

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_counterparty_open_purchase_orders_item import (
            InvoiceCounterpartyOpenPurchaseOrdersItem,
        )

        d = src_dict.copy()
        connection_id = d.pop("connectionId", UNSET)

        name = d.pop("name", UNSET)

        currency = d.pop("currency", UNSET)

        currencies = cast(List[str], d.pop("currencies", UNSET))

        payment_currency = d.pop("paymentCurrency", UNSET)

        open_purchase_orders = []
        _open_purchase_orders = d.pop("openPurchaseOrders", UNSET)
        for open_purchase_orders_item_data in _open_purchase_orders or []:
            open_purchase_orders_item = (
                InvoiceCounterpartyOpenPurchaseOrdersItem.from_dict(
                    open_purchase_orders_item_data
                )
            )

            open_purchase_orders.append(open_purchase_orders_item)

        invoice_feed_enabled = d.pop("invoiceFeedEnabled", UNSET)

        invoice_feed_updated_at = d.pop("invoiceFeedUpdatedAt", UNSET)

        _feed_readiness = d.pop("feedReadiness", UNSET)
        feed_readiness: Union[Unset, InvoiceCounterpartyFeedReadiness]
        if isinstance(_feed_readiness, Unset):
            feed_readiness = UNSET
        else:
            feed_readiness = check_invoice_counterparty_feed_readiness(_feed_readiness)

        feed_accepted_count = d.pop("feedAcceptedCount", UNSET)

        feed_last_accepted_at = d.pop("feedLastAcceptedAt", UNSET)

        feed_last_valid_at = d.pop("feedLastValidAt", UNSET)

        feed_valid_count = d.pop("feedValidCount", UNSET)

        approved_at = d.pop("approvedAt", UNSET)

        multiple_connections = d.pop("multipleConnections", UNSET)

        off_platform = d.pop("offPlatform", UNSET)

        _cloud_provider = d.pop("cloudProvider", UNSET)
        cloud_provider: Union[Unset, InvoiceCounterpartyCloudProvider]
        if isinstance(_cloud_provider, Unset):
            cloud_provider = UNSET
        else:
            cloud_provider = check_invoice_counterparty_cloud_provider(_cloud_provider)

        invoice_counterparty = cls(
            connection_id=connection_id,
            name=name,
            currency=currency,
            currencies=currencies,
            payment_currency=payment_currency,
            open_purchase_orders=open_purchase_orders,
            invoice_feed_enabled=invoice_feed_enabled,
            invoice_feed_updated_at=invoice_feed_updated_at,
            feed_readiness=feed_readiness,
            feed_accepted_count=feed_accepted_count,
            feed_last_accepted_at=feed_last_accepted_at,
            feed_last_valid_at=feed_last_valid_at,
            feed_valid_count=feed_valid_count,
            approved_at=approved_at,
            multiple_connections=multiple_connections,
            off_platform=off_platform,
            cloud_provider=cloud_provider,
        )

        invoice_counterparty.additional_properties = d
        return invoice_counterparty

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
