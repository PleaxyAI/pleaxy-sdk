from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenPurchaseOrderDeposit")


@_attrs_define
class OpenPurchaseOrderDeposit:
    """
    Attributes:
        invoice_id (Union[Unset, str]):
        external_invoice_number (Union[Unset, str]):
        currency (Union[Unset, str]):
        owed (Union[Unset, float]):
        available (Union[Unset, float]):
        paid_on (Union[Unset, str]):
        prepayment (Union[Unset, bool]):
        reference (Union[Unset, str]):
    """

    invoice_id: Union[Unset, str] = UNSET
    external_invoice_number: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    owed: Union[Unset, float] = UNSET
    available: Union[Unset, float] = UNSET
    paid_on: Union[Unset, str] = UNSET
    prepayment: Union[Unset, bool] = UNSET
    reference: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoice_id = self.invoice_id

        external_invoice_number = self.external_invoice_number

        currency = self.currency

        owed = self.owed

        available = self.available

        paid_on = self.paid_on

        prepayment = self.prepayment

        reference = self.reference

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invoice_id is not UNSET:
            field_dict["invoiceId"] = invoice_id
        if external_invoice_number is not UNSET:
            field_dict["externalInvoiceNumber"] = external_invoice_number
        if currency is not UNSET:
            field_dict["currency"] = currency
        if owed is not UNSET:
            field_dict["owed"] = owed
        if available is not UNSET:
            field_dict["available"] = available
        if paid_on is not UNSET:
            field_dict["paidOn"] = paid_on
        if prepayment is not UNSET:
            field_dict["prepayment"] = prepayment
        if reference is not UNSET:
            field_dict["reference"] = reference

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        invoice_id = d.pop("invoiceId", UNSET)

        external_invoice_number = d.pop("externalInvoiceNumber", UNSET)

        currency = d.pop("currency", UNSET)

        owed = d.pop("owed", UNSET)

        available = d.pop("available", UNSET)

        paid_on = d.pop("paidOn", UNSET)

        prepayment = d.pop("prepayment", UNSET)

        reference = d.pop("reference", UNSET)

        open_purchase_order_deposit = cls(
            invoice_id=invoice_id,
            external_invoice_number=external_invoice_number,
            currency=currency,
            owed=owed,
            available=available,
            paid_on=paid_on,
            prepayment=prepayment,
            reference=reference,
        )

        open_purchase_order_deposit.additional_properties = d
        return open_purchase_order_deposit

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
