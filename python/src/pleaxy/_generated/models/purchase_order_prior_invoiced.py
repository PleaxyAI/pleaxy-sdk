from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.purchase_order_prior_invoiced_basis import (
    PurchaseOrderPriorInvoicedBasis,
    check_purchase_order_prior_invoiced_basis,
)
from ..models.purchase_order_prior_invoiced_source_system import (
    PurchaseOrderPriorInvoicedSourceSystem,
    check_purchase_order_prior_invoiced_source_system,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PurchaseOrderPriorInvoiced")


@_attrs_define
class PurchaseOrderPriorInvoiced:
    """
    Attributes:
        amount (Union[Unset, float]):
        currency (Union[Unset, str]):
        basis (Union[Unset, PurchaseOrderPriorInvoicedBasis]):
        source_system (Union[Unset, PurchaseOrderPriorInvoicedSourceSystem]):
        import_id (Union[Unset, str]):
        file_name (Union[Unset, str]):
        imported_at (Union[Unset, str]):
        imported_by (Union[Unset, str]):
    """

    amount: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    basis: Union[Unset, PurchaseOrderPriorInvoicedBasis] = UNSET
    source_system: Union[Unset, PurchaseOrderPriorInvoicedSourceSystem] = UNSET
    import_id: Union[Unset, str] = UNSET
    file_name: Union[Unset, str] = UNSET
    imported_at: Union[Unset, str] = UNSET
    imported_by: Union[Unset, str] = UNSET
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

        import_id = self.import_id

        file_name = self.file_name

        imported_at = self.imported_at

        imported_by = self.imported_by

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
        if import_id is not UNSET:
            field_dict["importId"] = import_id
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if imported_at is not UNSET:
            field_dict["importedAt"] = imported_at
        if imported_by is not UNSET:
            field_dict["importedBy"] = imported_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        _basis = d.pop("basis", UNSET)
        basis: Union[Unset, PurchaseOrderPriorInvoicedBasis]
        if isinstance(_basis, Unset):
            basis = UNSET
        else:
            basis = check_purchase_order_prior_invoiced_basis(_basis)

        _source_system = d.pop("sourceSystem", UNSET)
        source_system: Union[Unset, PurchaseOrderPriorInvoicedSourceSystem]
        if isinstance(_source_system, Unset):
            source_system = UNSET
        else:
            source_system = check_purchase_order_prior_invoiced_source_system(
                _source_system
            )

        import_id = d.pop("importId", UNSET)

        file_name = d.pop("fileName", UNSET)

        imported_at = d.pop("importedAt", UNSET)

        imported_by = d.pop("importedBy", UNSET)

        purchase_order_prior_invoiced = cls(
            amount=amount,
            currency=currency,
            basis=basis,
            source_system=source_system,
            import_id=import_id,
            file_name=file_name,
            imported_at=imported_at,
            imported_by=imported_by,
        )

        purchase_order_prior_invoiced.additional_properties = d
        return purchase_order_prior_invoiced

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
