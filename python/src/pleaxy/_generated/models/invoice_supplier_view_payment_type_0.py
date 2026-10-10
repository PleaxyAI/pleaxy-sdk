from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_supplier_view_payment_type_0_method import (
    InvoiceSupplierViewPaymentType0Method,
    check_invoice_supplier_view_payment_type_0_method,
)
from ..models.invoice_supplier_view_payment_type_0_status import (
    InvoiceSupplierViewPaymentType0Status,
    check_invoice_supplier_view_payment_type_0_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_breakdown_entry import InvoiceBreakdownEntry
    from ..models.invoice_supplier_view_payment_type_0_paid_amount import (
        InvoiceSupplierViewPaymentType0PaidAmount,
    )


T = TypeVar("T", bound="InvoiceSupplierViewPaymentType0")


@_attrs_define
class InvoiceSupplierViewPaymentType0:
    """
    Attributes:
        withholdings (Union[Unset, List['InvoiceBreakdownEntry']]):
        method (Union[Unset, InvoiceSupplierViewPaymentType0Method]):
        payment_date (Union[Unset, str]):
        reference (Union[Unset, str]):
        recorded_at (Union[Unset, str]):
        advice_version (Union[Unset, float]):
        paid_amount (Union[Unset, InvoiceSupplierViewPaymentType0PaidAmount]):
        status (Union[Unset, InvoiceSupplierViewPaymentType0Status]):
    """

    withholdings: Union[Unset, List["InvoiceBreakdownEntry"]] = UNSET
    method: Union[Unset, InvoiceSupplierViewPaymentType0Method] = UNSET
    payment_date: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    recorded_at: Union[Unset, str] = UNSET
    advice_version: Union[Unset, float] = UNSET
    paid_amount: Union[Unset, "InvoiceSupplierViewPaymentType0PaidAmount"] = UNSET
    status: Union[Unset, InvoiceSupplierViewPaymentType0Status] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        withholdings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.withholdings, Unset):
            withholdings = []
            for withholdings_item_data in self.withholdings:
                withholdings_item = withholdings_item_data.to_dict()
                withholdings.append(withholdings_item)

        method: Union[Unset, str] = UNSET
        if not isinstance(self.method, Unset):
            method = self.method

        payment_date = self.payment_date

        reference = self.reference

        recorded_at = self.recorded_at

        advice_version = self.advice_version

        paid_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.paid_amount, Unset):
            paid_amount = self.paid_amount.to_dict()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if withholdings is not UNSET:
            field_dict["withholdings"] = withholdings
        if method is not UNSET:
            field_dict["method"] = method
        if payment_date is not UNSET:
            field_dict["paymentDate"] = payment_date
        if reference is not UNSET:
            field_dict["reference"] = reference
        if recorded_at is not UNSET:
            field_dict["recordedAt"] = recorded_at
        if advice_version is not UNSET:
            field_dict["adviceVersion"] = advice_version
        if paid_amount is not UNSET:
            field_dict["paidAmount"] = paid_amount
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_breakdown_entry import InvoiceBreakdownEntry
        from ..models.invoice_supplier_view_payment_type_0_paid_amount import (
            InvoiceSupplierViewPaymentType0PaidAmount,
        )

        d = src_dict.copy()
        withholdings = []
        _withholdings = d.pop("withholdings", UNSET)
        for withholdings_item_data in _withholdings or []:
            withholdings_item = InvoiceBreakdownEntry.from_dict(withholdings_item_data)

            withholdings.append(withholdings_item)

        _method = d.pop("method", UNSET)
        method: Union[Unset, InvoiceSupplierViewPaymentType0Method]
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = check_invoice_supplier_view_payment_type_0_method(_method)

        payment_date = d.pop("paymentDate", UNSET)

        reference = d.pop("reference", UNSET)

        recorded_at = d.pop("recordedAt", UNSET)

        advice_version = d.pop("adviceVersion", UNSET)

        _paid_amount = d.pop("paidAmount", UNSET)
        paid_amount: Union[Unset, InvoiceSupplierViewPaymentType0PaidAmount]
        if isinstance(_paid_amount, Unset):
            paid_amount = UNSET
        else:
            paid_amount = InvoiceSupplierViewPaymentType0PaidAmount.from_dict(
                _paid_amount
            )

        _status = d.pop("status", UNSET)
        status: Union[Unset, InvoiceSupplierViewPaymentType0Status]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_invoice_supplier_view_payment_type_0_status(_status)

        invoice_supplier_view_payment_type_0 = cls(
            withholdings=withholdings,
            method=method,
            payment_date=payment_date,
            reference=reference,
            recorded_at=recorded_at,
            advice_version=advice_version,
            paid_amount=paid_amount,
            status=status,
        )

        invoice_supplier_view_payment_type_0.additional_properties = d
        return invoice_supplier_view_payment_type_0

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
