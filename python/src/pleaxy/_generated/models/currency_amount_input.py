from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amount_breakdown_input import AmountBreakdownInput
    from ..models.currency_exchange_details_input import CurrencyExchangeDetailsInput


T = TypeVar("T", bound="CurrencyAmountInput")


@_attrs_define
class CurrencyAmountInput:
    """
    Attributes:
        currency_code (str): ISO 4217. Must differ from the invoice's currency.
        currency_exchange_details (CurrencyExchangeDetailsInput):
        total_amount (Union[Unset, float]): Required on paymentCurrencyAmount: the amount owed in this currency.
            Optional on taxCurrencyAmount.
        total_amount_before_tax (Union[Unset, float]):
        amount_breakdown (Union[Unset, AmountBreakdownInput]):
    """

    currency_code: str
    currency_exchange_details: "CurrencyExchangeDetailsInput"
    total_amount: Union[Unset, float] = UNSET
    total_amount_before_tax: Union[Unset, float] = UNSET
    amount_breakdown: Union[Unset, "AmountBreakdownInput"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        currency_code = self.currency_code

        currency_exchange_details = self.currency_exchange_details.to_dict()

        total_amount = self.total_amount

        total_amount_before_tax = self.total_amount_before_tax

        amount_breakdown: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.amount_breakdown, Unset):
            amount_breakdown = self.amount_breakdown.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currencyCode": currency_code,
                "currencyExchangeDetails": currency_exchange_details,
            }
        )
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if total_amount_before_tax is not UNSET:
            field_dict["totalAmountBeforeTax"] = total_amount_before_tax
        if amount_breakdown is not UNSET:
            field_dict["amountBreakdown"] = amount_breakdown

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.amount_breakdown_input import AmountBreakdownInput
        from ..models.currency_exchange_details_input import (
            CurrencyExchangeDetailsInput,
        )

        d = src_dict.copy()
        currency_code = d.pop("currencyCode")

        currency_exchange_details = CurrencyExchangeDetailsInput.from_dict(
            d.pop("currencyExchangeDetails")
        )

        total_amount = d.pop("totalAmount", UNSET)

        total_amount_before_tax = d.pop("totalAmountBeforeTax", UNSET)

        _amount_breakdown = d.pop("amountBreakdown", UNSET)
        amount_breakdown: Union[Unset, AmountBreakdownInput]
        if isinstance(_amount_breakdown, Unset):
            amount_breakdown = UNSET
        else:
            amount_breakdown = AmountBreakdownInput.from_dict(_amount_breakdown)

        currency_amount_input = cls(
            currency_code=currency_code,
            currency_exchange_details=currency_exchange_details,
            total_amount=total_amount,
            total_amount_before_tax=total_amount_before_tax,
            amount_breakdown=amount_breakdown,
        )

        currency_amount_input.additional_properties = d
        return currency_amount_input

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
