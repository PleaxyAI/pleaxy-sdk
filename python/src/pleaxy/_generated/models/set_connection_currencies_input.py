from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetConnectionCurrenciesInput")


@_attrs_define
class SetConnectionCurrenciesInput:
    """
    Attributes:
        billing_currency (Union[None, Unset, str]): "Bills in": the currency a supplier with no Pleaxy account invoices
            you in, the default for new orders and invoices to it. Refused for a supplier with an account, whose own
            currencies rule. null removes it (your currency is then the default).
        payment_currency (Union[None, Unset, str]): "Pay in": the currency you usually pay this supplier in, the default
            payment currency on its new invoices. For a supplier with an account, one it accepts. null removes it.
    """

    billing_currency: Union[None, Unset, str] = UNSET
    payment_currency: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        billing_currency: Union[None, Unset, str]
        if isinstance(self.billing_currency, Unset):
            billing_currency = UNSET
        else:
            billing_currency = self.billing_currency

        payment_currency: Union[None, Unset, str]
        if isinstance(self.payment_currency, Unset):
            payment_currency = UNSET
        else:
            payment_currency = self.payment_currency

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if billing_currency is not UNSET:
            field_dict["billingCurrency"] = billing_currency
        if payment_currency is not UNSET:
            field_dict["paymentCurrency"] = payment_currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_billing_currency(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        billing_currency = _parse_billing_currency(d.pop("billingCurrency", UNSET))

        def _parse_payment_currency(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        payment_currency = _parse_payment_currency(d.pop("paymentCurrency", UNSET))

        set_connection_currencies_input = cls(
            billing_currency=billing_currency,
            payment_currency=payment_currency,
        )

        set_connection_currencies_input.additional_properties = d
        return set_connection_currencies_input

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
