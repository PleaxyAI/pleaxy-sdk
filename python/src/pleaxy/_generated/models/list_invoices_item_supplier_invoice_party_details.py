from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_party_details import InvoicePartyDetails


T = TypeVar("T", bound="ListInvoicesItemSupplierInvoicePartyDetails")


@_attrs_define
class ListInvoicesItemSupplierInvoicePartyDetails:
    """
    Attributes:
        supplier (Union[Unset, InvoicePartyDetails]):
        buyer (Union[Unset, InvoicePartyDetails]):
    """

    supplier: Union[Unset, "InvoicePartyDetails"] = UNSET
    buyer: Union[Unset, "InvoicePartyDetails"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        supplier: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.supplier, Unset):
            supplier = self.supplier.to_dict()

        buyer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.buyer, Unset):
            buyer = self.buyer.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if supplier is not UNSET:
            field_dict["supplier"] = supplier
        if buyer is not UNSET:
            field_dict["buyer"] = buyer

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_party_details import InvoicePartyDetails

        d = src_dict.copy()
        _supplier = d.pop("supplier", UNSET)
        supplier: Union[Unset, InvoicePartyDetails]
        if isinstance(_supplier, Unset):
            supplier = UNSET
        else:
            supplier = InvoicePartyDetails.from_dict(_supplier)

        _buyer = d.pop("buyer", UNSET)
        buyer: Union[Unset, InvoicePartyDetails]
        if isinstance(_buyer, Unset):
            buyer = UNSET
        else:
            buyer = InvoicePartyDetails.from_dict(_buyer)

        list_invoices_item_supplier_invoice_party_details = cls(
            supplier=supplier,
            buyer=buyer,
        )

        list_invoices_item_supplier_invoice_party_details.additional_properties = d
        return list_invoices_item_supplier_invoice_party_details

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
