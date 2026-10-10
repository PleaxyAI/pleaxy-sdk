from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_buyer_view import InvoiceBuyerView
    from ..models.purchase_order import PurchaseOrder


T = TypeVar("T", bound="ApprovalQueueDecided")


@_attrs_define
class ApprovalQueueDecided:
    """
    Attributes:
        purchase_orders (Union[Unset, List['PurchaseOrder']]):
        invoices (Union[Unset, List['InvoiceBuyerView']]):
    """

    purchase_orders: Union[Unset, List["PurchaseOrder"]] = UNSET
    invoices: Union[Unset, List["InvoiceBuyerView"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        purchase_orders: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.purchase_orders, Unset):
            purchase_orders = []
            for purchase_orders_item_data in self.purchase_orders:
                purchase_orders_item = purchase_orders_item_data.to_dict()
                purchase_orders.append(purchase_orders_item)

        invoices: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.invoices, Unset):
            invoices = []
            for invoices_item_data in self.invoices:
                invoices_item = invoices_item_data.to_dict()
                invoices.append(invoices_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if purchase_orders is not UNSET:
            field_dict["purchaseOrders"] = purchase_orders
        if invoices is not UNSET:
            field_dict["invoices"] = invoices

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_buyer_view import InvoiceBuyerView
        from ..models.purchase_order import PurchaseOrder

        d = src_dict.copy()
        purchase_orders = []
        _purchase_orders = d.pop("purchaseOrders", UNSET)
        for purchase_orders_item_data in _purchase_orders or []:
            purchase_orders_item = PurchaseOrder.from_dict(purchase_orders_item_data)

            purchase_orders.append(purchase_orders_item)

        invoices = []
        _invoices = d.pop("invoices", UNSET)
        for invoices_item_data in _invoices or []:
            invoices_item = InvoiceBuyerView.from_dict(invoices_item_data)

            invoices.append(invoices_item)

        approval_queue_decided = cls(
            purchase_orders=purchase_orders,
            invoices=invoices,
        )

        approval_queue_decided.additional_properties = d
        return approval_queue_decided

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
