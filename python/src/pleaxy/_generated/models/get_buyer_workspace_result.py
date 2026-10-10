from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Type,
    TypeVar,
    Union,
)

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
        cloud_connections (Union[Unset, List['CloudConnection']]):
        purchase_orders (Union[Unset, List[Union['PurchaseOrder', 'PurchaseOrderSupplierView']]]):
        invoices (Union[Unset, List[Union['InvoiceBuyerView', 'InvoiceSupplierView']]]):
        viewer_is_sole_invoice_reviewer (Union[Unset, bool]):
    """

    cloud_connections: Union[Unset, List["CloudConnection"]] = UNSET
    purchase_orders: Union[
        Unset, List[Union["PurchaseOrder", "PurchaseOrderSupplierView"]]
    ] = UNSET
    invoices: Union[Unset, List[Union["InvoiceBuyerView", "InvoiceSupplierView"]]] = (
        UNSET
    )
    viewer_is_sole_invoice_reviewer: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.invoice_buyer_view import InvoiceBuyerView
        from ..models.purchase_order import PurchaseOrder

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

        viewer_is_sole_invoice_reviewer = self.viewer_is_sole_invoice_reviewer

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cloud_connections is not UNSET:
            field_dict["cloudConnections"] = cloud_connections
        if purchase_orders is not UNSET:
            field_dict["purchaseOrders"] = purchase_orders
        if invoices is not UNSET:
            field_dict["invoices"] = invoices
        if viewer_is_sole_invoice_reviewer is not UNSET:
            field_dict["viewerIsSoleInvoiceReviewer"] = viewer_is_sole_invoice_reviewer

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cloud_connection import CloudConnection
        from ..models.invoice_buyer_view import InvoiceBuyerView
        from ..models.invoice_supplier_view import InvoiceSupplierView
        from ..models.purchase_order import PurchaseOrder
        from ..models.purchase_order_supplier_view import PurchaseOrderSupplierView

        d = src_dict.copy()
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

        viewer_is_sole_invoice_reviewer = d.pop("viewerIsSoleInvoiceReviewer", UNSET)

        get_buyer_workspace_result = cls(
            cloud_connections=cloud_connections,
            purchase_orders=purchase_orders,
            invoices=invoices,
            viewer_is_sole_invoice_reviewer=viewer_is_sole_invoice_reviewer,
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
