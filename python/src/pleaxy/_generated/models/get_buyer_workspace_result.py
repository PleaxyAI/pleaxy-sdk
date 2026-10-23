from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cloud_connection import CloudConnection
    from ..models.invoice_buyer_view import InvoiceBuyerView
    from ..models.invoice_supplier_view import InvoiceSupplierView
    from ..models.purchase_order import PurchaseOrder
    from ..models.purchase_order_supplier_view import PurchaseOrderSupplierView


T = TypeVar("T", bound="GetBuyerWorkspaceResult")


@_attrs_define
class GetBuyerWorkspaceResult:
    """
    Attributes:
        viewer_is_sole_invoice_reviewer (Union[Unset, bool]):
        recent_purchase_orders (Union[Unset, List[Union['PurchaseOrder', 'PurchaseOrderSupplierView']]]):
        recent_invoices (Union[Unset, List[Union['InvoiceBuyerView', 'InvoiceSupplierView']]]):
        cloud_connections (Union[Unset, List['CloudConnection']]):
        purchase_orders (Union[Unset, List[Union['PurchaseOrder', 'PurchaseOrderSupplierView']]]):
        invoices (Union[Unset, List[Union['InvoiceBuyerView', 'InvoiceSupplierView']]]):
    """

    viewer_is_sole_invoice_reviewer: Union[Unset, bool] = UNSET
    recent_purchase_orders: Union[
        Unset, List[Union["PurchaseOrder", "PurchaseOrderSupplierView"]]
    ] = UNSET
    recent_invoices: Union[
        Unset, List[Union["InvoiceBuyerView", "InvoiceSupplierView"]]
    ] = UNSET
    cloud_connections: Union[Unset, List["CloudConnection"]] = UNSET
    purchase_orders: Union[
        Unset, List[Union["PurchaseOrder", "PurchaseOrderSupplierView"]]
    ] = UNSET
    invoices: Union[Unset, List[Union["InvoiceBuyerView", "InvoiceSupplierView"]]] = (
        UNSET
    )
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.invoice_buyer_view import InvoiceBuyerView
        from ..models.purchase_order import PurchaseOrder

        viewer_is_sole_invoice_reviewer = self.viewer_is_sole_invoice_reviewer

        recent_purchase_orders: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.recent_purchase_orders, Unset):
            recent_purchase_orders = []
            for recent_purchase_orders_item_data in self.recent_purchase_orders:
                recent_purchase_orders_item: Dict[str, Any]
                if isinstance(recent_purchase_orders_item_data, PurchaseOrder):
                    recent_purchase_orders_item = (
                        recent_purchase_orders_item_data.to_dict()
                    )
                else:
                    recent_purchase_orders_item = (
                        recent_purchase_orders_item_data.to_dict()
                    )

                recent_purchase_orders.append(recent_purchase_orders_item)

        recent_invoices: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.recent_invoices, Unset):
            recent_invoices = []
            for recent_invoices_item_data in self.recent_invoices:
                recent_invoices_item: Dict[str, Any]
                if isinstance(recent_invoices_item_data, InvoiceBuyerView):
                    recent_invoices_item = recent_invoices_item_data.to_dict()
                else:
                    recent_invoices_item = recent_invoices_item_data.to_dict()

                recent_invoices.append(recent_invoices_item)

        cloud_connections: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.cloud_connections, Unset):
            cloud_connections = []
            for cloud_connections_item_data in self.cloud_connections:
                cloud_connections_item = cloud_connections_item_data.to_dict()
                cloud_connections.append(cloud_connections_item)

        purchase_orders: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.purchase_orders, Unset):
            purchase_orders = []
            for purchase_orders_item_data in self.purchase_orders:
                purchase_orders_item: Dict[str, Any]
                if isinstance(purchase_orders_item_data, PurchaseOrder):
                    purchase_orders_item = purchase_orders_item_data.to_dict()
                else:
                    purchase_orders_item = purchase_orders_item_data.to_dict()

                purchase_orders.append(purchase_orders_item)

        invoices: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.invoices, Unset):
            invoices = []
            for invoices_item_data in self.invoices:
                invoices_item: Dict[str, Any]
                if isinstance(invoices_item_data, InvoiceBuyerView):
                    invoices_item = invoices_item_data.to_dict()
                else:
                    invoices_item = invoices_item_data.to_dict()

                invoices.append(invoices_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if viewer_is_sole_invoice_reviewer is not UNSET:
            field_dict["viewerIsSoleInvoiceReviewer"] = viewer_is_sole_invoice_reviewer
        if recent_purchase_orders is not UNSET:
            field_dict["recentPurchaseOrders"] = recent_purchase_orders
        if recent_invoices is not UNSET:
            field_dict["recentInvoices"] = recent_invoices
        if cloud_connections is not UNSET:
            field_dict["cloudConnections"] = cloud_connections
        if purchase_orders is not UNSET:
            field_dict["purchaseOrders"] = purchase_orders
        if invoices is not UNSET:
            field_dict["invoices"] = invoices

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cloud_connection import CloudConnection
        from ..models.invoice_buyer_view import InvoiceBuyerView
        from ..models.invoice_supplier_view import InvoiceSupplierView
        from ..models.purchase_order import PurchaseOrder
        from ..models.purchase_order_supplier_view import PurchaseOrderSupplierView

        d = src_dict.copy()
        viewer_is_sole_invoice_reviewer = d.pop("viewerIsSoleInvoiceReviewer", UNSET)

        recent_purchase_orders = []
        _recent_purchase_orders = d.pop("recentPurchaseOrders", UNSET)
        for recent_purchase_orders_item_data in _recent_purchase_orders or []:

            def _parse_recent_purchase_orders_item(
                data: object,
            ) -> Union["PurchaseOrder", "PurchaseOrderSupplierView"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    recent_purchase_orders_item_type_0 = PurchaseOrder.from_dict(data)

                    return recent_purchase_orders_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                recent_purchase_orders_item_type_1 = (
                    PurchaseOrderSupplierView.from_dict(data)
                )

                return recent_purchase_orders_item_type_1

            recent_purchase_orders_item = _parse_recent_purchase_orders_item(
                recent_purchase_orders_item_data
            )

            recent_purchase_orders.append(recent_purchase_orders_item)

        recent_invoices = []
        _recent_invoices = d.pop("recentInvoices", UNSET)
        for recent_invoices_item_data in _recent_invoices or []:

            def _parse_recent_invoices_item(
                data: object,
            ) -> Union["InvoiceBuyerView", "InvoiceSupplierView"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    recent_invoices_item_type_0 = InvoiceBuyerView.from_dict(data)

                    return recent_invoices_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                recent_invoices_item_type_1 = InvoiceSupplierView.from_dict(data)

                return recent_invoices_item_type_1

            recent_invoices_item = _parse_recent_invoices_item(
                recent_invoices_item_data
            )

            recent_invoices.append(recent_invoices_item)

        cloud_connections = []
        _cloud_connections = d.pop("cloudConnections", UNSET)
        for cloud_connections_item_data in _cloud_connections or []:
            cloud_connections_item = CloudConnection.from_dict(
                cloud_connections_item_data
            )

            cloud_connections.append(cloud_connections_item)

        purchase_orders = []
        _purchase_orders = d.pop("purchaseOrders", UNSET)
        for purchase_orders_item_data in _purchase_orders or []:

            def _parse_purchase_orders_item(
                data: object,
            ) -> Union["PurchaseOrder", "PurchaseOrderSupplierView"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    purchase_orders_item_type_0 = PurchaseOrder.from_dict(data)

                    return purchase_orders_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                purchase_orders_item_type_1 = PurchaseOrderSupplierView.from_dict(data)

                return purchase_orders_item_type_1

            purchase_orders_item = _parse_purchase_orders_item(
                purchase_orders_item_data
            )

            purchase_orders.append(purchase_orders_item)

        invoices = []
        _invoices = d.pop("invoices", UNSET)
        for invoices_item_data in _invoices or []:

            def _parse_invoices_item(
                data: object,
            ) -> Union["InvoiceBuyerView", "InvoiceSupplierView"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    invoices_item_type_0 = InvoiceBuyerView.from_dict(data)

                    return invoices_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                invoices_item_type_1 = InvoiceSupplierView.from_dict(data)

                return invoices_item_type_1

            invoices_item = _parse_invoices_item(invoices_item_data)

            invoices.append(invoices_item)

        get_buyer_workspace_result = cls(
            viewer_is_sole_invoice_reviewer=viewer_is_sole_invoice_reviewer,
            recent_purchase_orders=recent_purchase_orders,
            recent_invoices=recent_invoices,
            cloud_connections=cloud_connections,
            purchase_orders=purchase_orders,
            invoices=invoices,
        )

        get_buyer_workspace_result.additional_properties = d
        return get_buyer_workspace_result

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
