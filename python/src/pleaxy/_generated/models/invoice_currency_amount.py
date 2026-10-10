from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_currency_amount_amount_breakdown import (
        InvoiceCurrencyAmountAmountBreakdown,
    )
    from ..models.invoice_currency_exchange_details import (
        InvoiceCurrencyExchangeDetails,
    )


T = TypeVar("T", bound="InvoiceCurrencyAmount")


@_attrs_define
class InvoiceCurrencyAmount:
    """
    Attributes:
        currency_code (Union[Unset, str]):
        total_amount (Union[Unset, float]):
        total_amount_before_tax (Union[Unset, float]):
        amount_breakdown (Union[Unset, InvoiceCurrencyAmountAmountBreakdown]):
        currency_exchange_details (Union[Unset, InvoiceCurrencyExchangeDetails]):
    """

    currency_code: Union[Unset, str] = UNSET
    total_amount: Union[Unset, float] = UNSET
    total_amount_before_tax: Union[Unset, float] = UNSET
    amount_breakdown: Union[Unset, "InvoiceCurrencyAmountAmountBreakdown"] = UNSET
    currency_exchange_details: Union[Unset, "InvoiceCurrencyExchangeDetails"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        currency_code = self.currency_code

        total_amount = self.total_amount

        total_amount_before_tax = self.total_amount_before_tax

        amount_breakdown: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.amount_breakdown, Unset):
            amount_breakdown = self.amount_breakdown.to_dict()

        currency_exchange_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.currency_exchange_details, Unset):
            currency_exchange_details = self.currency_exchange_details.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency_code is not UNSET:
            field_dict["currencyCode"] = currency_code
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if total_amount_before_tax is not UNSET:
            field_dict["totalAmountBeforeTax"] = total_amount_before_tax
        if amount_breakdown is not UNSET:
            field_dict["amountBreakdown"] = amount_breakdown
        if currency_exchange_details is not UNSET:
            field_dict["currencyExchangeDetails"] = currency_exchange_details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_currency_amount_amount_breakdown import (
            InvoiceCurrencyAmountAmountBreakdown,
        )
        from ..models.invoice_currency_exchange_details import (
            InvoiceCurrencyExchangeDetails,
        )

        d = src_dict.copy()
        currency_code = d.pop("currencyCode", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        total_amount_before_tax = d.pop("totalAmountBeforeTax", UNSET)

        _amount_breakdown = d.pop("amountBreakdown", UNSET)
        amount_breakdown: Union[Unset, InvoiceCurrencyAmountAmountBreakdown]
        if isinstance(_amount_breakdown, Unset):
            amount_breakdown = UNSET
        else:
            amount_breakdown = InvoiceCurrencyAmountAmountBreakdown.from_dict(
                _amount_breakdown
            )

        _currency_exchange_details = d.pop("currencyExchangeDetails", UNSET)
        currency_exchange_details: Union[Unset, InvoiceCurrencyExchangeDetails]
        if isinstance(_currency_exchange_details, Unset):
            currency_exchange_details = UNSET
        else:
            currency_exchange_details = InvoiceCurrencyExchangeDetails.from_dict(
                _currency_exchange_details
            )

        invoice_currency_amount = cls(
            currency_code=currency_code,
            total_amount=total_amount,
            total_amount_before_tax=total_amount_before_tax,
            amount_breakdown=amount_breakdown,
            currency_exchange_details=currency_exchange_details,
        )

        invoice_currency_amount.additional_properties = d
        return invoice_currency_amount

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
