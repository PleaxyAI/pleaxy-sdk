from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.purchase_order_supplier_view_prior_invoiced_basis import (
    PurchaseOrderSupplierViewPriorInvoicedBasis,
    check_purchase_order_supplier_view_prior_invoiced_basis,
)
from ..models.purchase_order_supplier_view_prior_invoiced_source_system import (
    PurchaseOrderSupplierViewPriorInvoicedSourceSystem,
    check_purchase_order_supplier_view_prior_invoiced_source_system,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PurchaseOrderSupplierViewPriorInvoiced")


@_attrs_define
class PurchaseOrderSupplierViewPriorInvoiced:
    """
    Attributes:
        amount (Union[Unset, float]):
        currency (Union[Unset, str]):
        basis (Union[Unset, PurchaseOrderSupplierViewPriorInvoicedBasis]):
        source_system (Union[Unset, PurchaseOrderSupplierViewPriorInvoicedSourceSystem]):
        imported_at (Union[Unset, str]):
    """

    amount: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    basis: Union[Unset, PurchaseOrderSupplierViewPriorInvoicedBasis] = UNSET
    source_system: Union[Unset, PurchaseOrderSupplierViewPriorInvoicedSourceSystem] = (
        UNSET
    )
    imported_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount

        currency = self.currency

        basis: Union[Unset, str] = UNSET
        if not isinstance(self.basis, Unset):
            basis = self.basis

        source_system: Union[Unset, str] = UNSET
        if not isinstance(self.source_system, Unset):
            source_system = self.source_system

        imported_at = self.imported_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if basis is not UNSET:
            field_dict["basis"] = basis
        if source_system is not UNSET:
            field_dict["sourceSystem"] = source_system
        if imported_at is not UNSET:
            field_dict["importedAt"] = imported_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        _basis = d.pop("basis", UNSET)
        basis: Union[Unset, PurchaseOrderSupplierViewPriorInvoicedBasis]
        if isinstance(_basis, Unset):
            basis = UNSET
        else:
            basis = check_purchase_order_supplier_view_prior_invoiced_basis(_basis)

        _source_system = d.pop("sourceSystem", UNSET)
        source_system: Union[Unset, PurchaseOrderSupplierViewPriorInvoicedSourceSystem]
        if isinstance(_source_system, Unset):
            source_system = UNSET
        else:
            source_system = (
                check_purchase_order_supplier_view_prior_invoiced_source_system(
                    _source_system
                )
            )

        imported_at = d.pop("importedAt", UNSET)

        purchase_order_supplier_view_prior_invoiced = cls(
            amount=amount,
            currency=currency,
            basis=basis,
            source_system=source_system,
            imported_at=imported_at,
        )

        purchase_order_supplier_view_prior_invoiced.additional_properties = d
        return purchase_order_supplier_view_prior_invoiced

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
