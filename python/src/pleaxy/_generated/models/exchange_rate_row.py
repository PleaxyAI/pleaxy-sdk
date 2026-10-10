from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExchangeRateRow")


@_attrs_define
class ExchangeRateRow:
    """
    Attributes:
        currency (Union[Unset, str]):
        provider_rate (Union[Unset, float]):
        provider_as_of (Union[Unset, str]):
    """

    currency: Union[Unset, str] = UNSET
    provider_rate: Union[Unset, float] = UNSET
    provider_as_of: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        currency = self.currency

        provider_rate = self.provider_rate

        provider_as_of = self.provider_as_of

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency is not UNSET:
            field_dict["currency"] = currency
        if provider_rate is not UNSET:
            field_dict["providerRate"] = provider_rate
        if provider_as_of is not UNSET:
            field_dict["providerAsOf"] = provider_as_of

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        currency = d.pop("currency", UNSET)

        provider_rate = d.pop("providerRate", UNSET)

        provider_as_of = d.pop("providerAsOf", UNSET)

        exchange_rate_row = cls(
            currency=currency,
            provider_rate=provider_rate,
            provider_as_of=provider_as_of,
        )

        exchange_rate_row.additional_properties = d
        return exchange_rate_row

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
