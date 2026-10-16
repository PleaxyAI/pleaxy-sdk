from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListInvoicesItemSupplierInvoicePaymentType0PaidAmount")


@_attrs_define
class ListInvoicesItemSupplierInvoicePaymentType0PaidAmount:
    """
    Attributes:
        amount (Union[Unset, float]):
        currency (Union[Unset, str]):
        rate (Union[Unset, float]):
        rate_date (Union[Unset, str]):
    """

    amount: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    rate: Union[Unset, float] = UNSET
    rate_date: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount

        currency = self.currency

        rate = self.rate

        rate_date = self.rate_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if rate is not UNSET:
            field_dict["rate"] = rate
        if rate_date is not UNSET:
            field_dict["rateDate"] = rate_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        rate = d.pop("rate", UNSET)

        rate_date = d.pop("rateDate", UNSET)

        list_invoices_item_supplier_invoice_payment_type_0_paid_amount = cls(
            amount=amount,
            currency=currency,
            rate=rate,
            rate_date=rate_date,
        )

        list_invoices_item_supplier_invoice_payment_type_0_paid_amount.additional_properties = d
        return list_invoices_item_supplier_invoice_payment_type_0_paid_amount

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
