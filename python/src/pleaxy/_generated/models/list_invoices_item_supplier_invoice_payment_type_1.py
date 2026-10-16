from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_invoices_item_supplier_invoice_payment_type_1_payment_method_type import (
    ListInvoicesItemSupplierInvoicePaymentType1PaymentMethodType,
    check_list_invoices_item_supplier_invoice_payment_type_1_payment_method_type,
)
from ..models.list_invoices_item_supplier_invoice_payment_type_1_state import (
    ListInvoicesItemSupplierInvoicePaymentType1State,
    check_list_invoices_item_supplier_invoice_payment_type_1_state,
)
from ..models.list_invoices_item_supplier_invoice_payment_type_1_status import (
    ListInvoicesItemSupplierInvoicePaymentType1Status,
    check_list_invoices_item_supplier_invoice_payment_type_1_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListInvoicesItemSupplierInvoicePaymentType1")


@_attrs_define
class ListInvoicesItemSupplierInvoicePaymentType1:
    """
    Attributes:
        status (Union[Unset, ListInvoicesItemSupplierInvoicePaymentType1Status]):
        state (Union[Unset, ListInvoicesItemSupplierInvoicePaymentType1State]):
        payment_method_type (Union[Unset, ListInvoicesItemSupplierInvoicePaymentType1PaymentMethodType]):
        succeeded_at (Union[Unset, str]):
    """

    status: Union[Unset, ListInvoicesItemSupplierInvoicePaymentType1Status] = UNSET
    state: Union[Unset, ListInvoicesItemSupplierInvoicePaymentType1State] = UNSET
    payment_method_type: Union[
        Unset, ListInvoicesItemSupplierInvoicePaymentType1PaymentMethodType
    ] = UNSET
    succeeded_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state

        payment_method_type: Union[Unset, str] = UNSET
        if not isinstance(self.payment_method_type, Unset):
            payment_method_type = self.payment_method_type

        succeeded_at = self.succeeded_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if state is not UNSET:
            field_dict["state"] = state
        if payment_method_type is not UNSET:
            field_dict["paymentMethodType"] = payment_method_type
        if succeeded_at is not UNSET:
            field_dict["succeededAt"] = succeeded_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, ListInvoicesItemSupplierInvoicePaymentType1Status]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_list_invoices_item_supplier_invoice_payment_type_1_status(
                _status
            )

        _state = d.pop("state", UNSET)
        state: Union[Unset, ListInvoicesItemSupplierInvoicePaymentType1State]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = check_list_invoices_item_supplier_invoice_payment_type_1_state(
                _state
            )

        _payment_method_type = d.pop("paymentMethodType", UNSET)
        payment_method_type: Union[
            Unset, ListInvoicesItemSupplierInvoicePaymentType1PaymentMethodType
        ]
        if isinstance(_payment_method_type, Unset):
            payment_method_type = UNSET
        else:
            payment_method_type = check_list_invoices_item_supplier_invoice_payment_type_1_payment_method_type(
                _payment_method_type
            )

        succeeded_at = d.pop("succeededAt", UNSET)

        list_invoices_item_supplier_invoice_payment_type_1 = cls(
            status=status,
            state=state,
            payment_method_type=payment_method_type,
            succeeded_at=succeeded_at,
        )

        list_invoices_item_supplier_invoice_payment_type_1.additional_properties = d
        return list_invoices_item_supplier_invoice_payment_type_1

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
