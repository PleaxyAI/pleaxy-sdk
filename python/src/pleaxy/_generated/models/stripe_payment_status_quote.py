from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.stripe_payment_status_quote_currency import (
    StripePaymentStatusQuoteCurrency,
    check_stripe_payment_status_quote_currency,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="StripePaymentStatusQuote")


@_attrs_define
class StripePaymentStatusQuote:
    """
    Attributes:
        amount (Union[Unset, float]):
        fee (Union[Unset, float]):
        total (Union[Unset, float]):
        currency (Union[Unset, StripePaymentStatusQuoteCurrency]):
    """

    amount: Union[Unset, float] = UNSET
    fee: Union[Unset, float] = UNSET
    total: Union[Unset, float] = UNSET
    currency: Union[Unset, StripePaymentStatusQuoteCurrency] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount

        fee = self.fee

        total = self.total

        currency: Union[Unset, str] = UNSET
        if not isinstance(self.currency, Unset):
            currency = self.currency

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if fee is not UNSET:
            field_dict["fee"] = fee
        if total is not UNSET:
            field_dict["total"] = total
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amount = d.pop("amount", UNSET)

        fee = d.pop("fee", UNSET)

        total = d.pop("total", UNSET)

        _currency = d.pop("currency", UNSET)
        currency: Union[Unset, StripePaymentStatusQuoteCurrency]
        if isinstance(_currency, Unset):
            currency = UNSET
        else:
            currency = check_stripe_payment_status_quote_currency(_currency)

        stripe_payment_status_quote = cls(
            amount=amount,
            fee=fee,
            total=total,
            currency=currency,
        )

        stripe_payment_status_quote.additional_properties = d
        return stripe_payment_status_quote

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
