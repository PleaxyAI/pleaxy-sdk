from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.remittance_view_payment_method import (
    RemittanceViewPaymentMethod,
    check_remittance_view_payment_method,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_breakdown_entry import InvoiceBreakdownEntry
    from ..models.remittance_view_payment_net_paid import RemittanceViewPaymentNetPaid
    from ..models.remittance_view_payment_paid_in_other_currency import (
        RemittanceViewPaymentPaidInOtherCurrency,
    )


T = TypeVar("T", bound="RemittanceViewPayment")


@_attrs_define
class RemittanceViewPayment:
    """
    Attributes:
        method (Union[Unset, RemittanceViewPaymentMethod]):
        payment_date (Union[Unset, str]):
        reference (Union[Unset, str]):
        recorded_at (Union[Unset, str]):
        advice_version (Union[Unset, float]):
        withheld (Union[Unset, List['InvoiceBreakdownEntry']]):
        net_paid (Union[Unset, RemittanceViewPaymentNetPaid]):
        paid_in_other_currency (Union[Unset, RemittanceViewPaymentPaidInOtherCurrency]):
    """

    method: Union[Unset, RemittanceViewPaymentMethod] = UNSET
    payment_date: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    recorded_at: Union[Unset, str] = UNSET
    advice_version: Union[Unset, float] = UNSET
    withheld: Union[Unset, List["InvoiceBreakdownEntry"]] = UNSET
    net_paid: Union[Unset, "RemittanceViewPaymentNetPaid"] = UNSET
    paid_in_other_currency: Union[Unset, "RemittanceViewPaymentPaidInOtherCurrency"] = (
        UNSET
    )
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        method: Union[Unset, str] = UNSET
        if not isinstance(self.method, Unset):
            method = self.method

        payment_date = self.payment_date

        reference = self.reference

        recorded_at = self.recorded_at

        advice_version = self.advice_version

        withheld: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.withheld, Unset):
            withheld = []
            for withheld_item_data in self.withheld:
                withheld_item = withheld_item_data.to_dict()
                withheld.append(withheld_item)

        net_paid: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.net_paid, Unset):
            net_paid = self.net_paid.to_dict()

        paid_in_other_currency: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.paid_in_other_currency, Unset):
            paid_in_other_currency = self.paid_in_other_currency.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if withheld is not UNSET:
            field_dict["withheld"] = withheld
        if net_paid is not UNSET:
            field_dict["netPaid"] = net_paid
        if paid_in_other_currency is not UNSET:
            field_dict["paidInOtherCurrency"] = paid_in_other_currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_breakdown_entry import InvoiceBreakdownEntry
        from ..models.remittance_view_payment_net_paid import (
            RemittanceViewPaymentNetPaid,
        )
        from ..models.remittance_view_payment_paid_in_other_currency import (
            RemittanceViewPaymentPaidInOtherCurrency,
        )

        d = src_dict.copy()
        _method = d.pop("method", UNSET)
        method: Union[Unset, RemittanceViewPaymentMethod]
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = check_remittance_view_payment_method(_method)

        payment_date = d.pop("paymentDate", UNSET)

        reference = d.pop("reference", UNSET)

        recorded_at = d.pop("recordedAt", UNSET)

        advice_version = d.pop("adviceVersion", UNSET)

        withheld = []
        _withheld = d.pop("withheld", UNSET)
        for withheld_item_data in _withheld or []:
            withheld_item = InvoiceBreakdownEntry.from_dict(withheld_item_data)

            withheld.append(withheld_item)

        _net_paid = d.pop("netPaid", UNSET)
        net_paid: Union[Unset, RemittanceViewPaymentNetPaid]
        if isinstance(_net_paid, Unset):
            net_paid = UNSET
        else:
            net_paid = RemittanceViewPaymentNetPaid.from_dict(_net_paid)

        _paid_in_other_currency = d.pop("paidInOtherCurrency", UNSET)
        paid_in_other_currency: Union[Unset, RemittanceViewPaymentPaidInOtherCurrency]
        if isinstance(_paid_in_other_currency, Unset):
            paid_in_other_currency = UNSET
        else:
            paid_in_other_currency = RemittanceViewPaymentPaidInOtherCurrency.from_dict(
                _paid_in_other_currency
            )

        remittance_view_payment = cls(
            method=method,
            payment_date=payment_date,
            reference=reference,
            recorded_at=recorded_at,
            advice_version=advice_version,
            withheld=withheld,
            net_paid=net_paid,
            paid_in_other_currency=paid_in_other_currency,
        )

        remittance_view_payment.additional_properties = d
        return remittance_view_payment

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
