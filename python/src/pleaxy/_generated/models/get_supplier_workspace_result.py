from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_buyer_view import InvoiceBuyerView
    from ..models.invoice_supplier_view import InvoiceSupplierView
    from ..models.purchase_order import PurchaseOrder
    from ..models.purchase_order_supplier_view import PurchaseOrderSupplierView


T = TypeVar("T", bound="GetSupplierWorkspaceResult")


@_attrs_define
class GetSupplierWorkspaceResult:
    """
    Attributes:
        recent_incoming_p_os (Union[Unset, List[Union['PurchaseOrder', 'PurchaseOrderSupplierView']]]):
        recent_supplier_invoices (Union[Unset, List[Union['InvoiceBuyerView', 'InvoiceSupplierView']]]):
        incoming_p_os (Union[Unset, List[Union['PurchaseOrder', 'PurchaseOrderSupplierView']]]):
        supplier_invoices (Union[Unset, List[Union['InvoiceBuyerView', 'InvoiceSupplierView']]]):
    """

    recent_incoming_p_os: Union[
        Unset, List[Union["PurchaseOrder", "PurchaseOrderSupplierView"]]
    ] = UNSET
    recent_supplier_invoices: Union[
        Unset, List[Union["InvoiceBuyerView", "InvoiceSupplierView"]]
    ] = UNSET
    incoming_p_os: Union[
        Unset, List[Union["PurchaseOrder", "PurchaseOrderSupplierView"]]
    ] = UNSET
    supplier_invoices: Union[
        Unset, List[Union["InvoiceBuyerView", "InvoiceSupplierView"]]
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.invoice_buyer_view import InvoiceBuyerView
        from ..models.purchase_order import PurchaseOrder

        recent_incoming_p_os: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.recent_incoming_p_os, Unset):
            recent_incoming_p_os = []
            for recent_incoming_p_os_item_data in self.recent_incoming_p_os:
                recent_incoming_p_os_item: Dict[str, Any]
                if isinstance(recent_incoming_p_os_item_data, PurchaseOrder):
                    recent_incoming_p_os_item = recent_incoming_p_os_item_data.to_dict()
                else:
                    recent_incoming_p_os_item = recent_incoming_p_os_item_data.to_dict()

                recent_incoming_p_os.append(recent_incoming_p_os_item)

        recent_supplier_invoices: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.recent_supplier_invoices, Unset):
            recent_supplier_invoices = []
            for recent_supplier_invoices_item_data in self.recent_supplier_invoices:
                recent_supplier_invoices_item: Dict[str, Any]
                if isinstance(recent_supplier_invoices_item_data, InvoiceBuyerView):
                    recent_supplier_invoices_item = (
                        recent_supplier_invoices_item_data.to_dict()
                    )
                else:
                    recent_supplier_invoices_item = (
                        recent_supplier_invoices_item_data.to_dict()
                    )

                recent_supplier_invoices.append(recent_supplier_invoices_item)

        incoming_p_os: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.incoming_p_os, Unset):
            incoming_p_os = []
            for incoming_p_os_item_data in self.incoming_p_os:
                incoming_p_os_item: Dict[str, Any]
                if isinstance(incoming_p_os_item_data, PurchaseOrder):
                    incoming_p_os_item = incoming_p_os_item_data.to_dict()
                else:
                    incoming_p_os_item = incoming_p_os_item_data.to_dict()

                incoming_p_os.append(incoming_p_os_item)

        supplier_invoices: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.supplier_invoices, Unset):
            supplier_invoices = []
            for supplier_invoices_item_data in self.supplier_invoices:
                supplier_invoices_item: Dict[str, Any]
                if isinstance(supplier_invoices_item_data, InvoiceBuyerView):
                    supplier_invoices_item = supplier_invoices_item_data.to_dict()
                else:
                    supplier_invoices_item = supplier_invoices_item_data.to_dict()

                supplier_invoices.append(supplier_invoices_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if recent_incoming_p_os is not UNSET:
            field_dict["recentIncomingPOs"] = recent_incoming_p_os
        if recent_supplier_invoices is not UNSET:
            field_dict["recentSupplierInvoices"] = recent_supplier_invoices
        if incoming_p_os is not UNSET:
            field_dict["incomingPOs"] = incoming_p_os
        if supplier_invoices is not UNSET:
            field_dict["supplierInvoices"] = supplier_invoices

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_buyer_view import InvoiceBuyerView
        from ..models.invoice_supplier_view import InvoiceSupplierView
        from ..models.purchase_order import PurchaseOrder
        from ..models.purchase_order_supplier_view import PurchaseOrderSupplierView

        d = src_dict.copy()
        recent_incoming_p_os = []
        _recent_incoming_p_os = d.pop("recentIncomingPOs", UNSET)
        for recent_incoming_p_os_item_data in _recent_incoming_p_os or []:

            def _parse_recent_incoming_p_os_item(
                data: object,
            ) -> Union["PurchaseOrder", "PurchaseOrderSupplierView"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    recent_incoming_p_os_item_type_0 = PurchaseOrder.from_dict(data)

                    return recent_incoming_p_os_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                recent_incoming_p_os_item_type_1 = PurchaseOrderSupplierView.from_dict(
                    data
                )

                return recent_incoming_p_os_item_type_1

            recent_incoming_p_os_item = _parse_recent_incoming_p_os_item(
                recent_incoming_p_os_item_data
            )

            recent_incoming_p_os.append(recent_incoming_p_os_item)

        recent_supplier_invoices = []
        _recent_supplier_invoices = d.pop("recentSupplierInvoices", UNSET)
        for recent_supplier_invoices_item_data in _recent_supplier_invoices or []:

            def _parse_recent_supplier_invoices_item(
                data: object,
            ) -> Union["InvoiceBuyerView", "InvoiceSupplierView"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    recent_supplier_invoices_item_type_0 = InvoiceBuyerView.from_dict(
                        data
                    )

                    return recent_supplier_invoices_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                recent_supplier_invoices_item_type_1 = InvoiceSupplierView.from_dict(
                    data
                )

                return recent_supplier_invoices_item_type_1

            recent_supplier_invoices_item = _parse_recent_supplier_invoices_item(
                recent_supplier_invoices_item_data
            )

            recent_supplier_invoices.append(recent_supplier_invoices_item)

        incoming_p_os = []
        _incoming_p_os = d.pop("incomingPOs", UNSET)
        for incoming_p_os_item_data in _incoming_p_os or []:

            def _parse_incoming_p_os_item(
                data: object,
            ) -> Union["PurchaseOrder", "PurchaseOrderSupplierView"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    incoming_p_os_item_type_0 = PurchaseOrder.from_dict(data)

                    return incoming_p_os_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                incoming_p_os_item_type_1 = PurchaseOrderSupplierView.from_dict(data)

                return incoming_p_os_item_type_1

            incoming_p_os_item = _parse_incoming_p_os_item(incoming_p_os_item_data)

            incoming_p_os.append(incoming_p_os_item)

        supplier_invoices = []
        _supplier_invoices = d.pop("supplierInvoices", UNSET)
        for supplier_invoices_item_data in _supplier_invoices or []:

            def _parse_supplier_invoices_item(
                data: object,
            ) -> Union["InvoiceBuyerView", "InvoiceSupplierView"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    supplier_invoices_item_type_0 = InvoiceBuyerView.from_dict(data)

                    return supplier_invoices_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                supplier_invoices_item_type_1 = InvoiceSupplierView.from_dict(data)

                return supplier_invoices_item_type_1

            supplier_invoices_item = _parse_supplier_invoices_item(
                supplier_invoices_item_data
            )

            supplier_invoices.append(supplier_invoices_item)

        get_supplier_workspace_result = cls(
            recent_incoming_p_os=recent_incoming_p_os,
            recent_supplier_invoices=recent_supplier_invoices,
            incoming_p_os=incoming_p_os,
            supplier_invoices=supplier_invoices,
        )

        get_supplier_workspace_result.additional_properties = d
        return get_supplier_workspace_result

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
