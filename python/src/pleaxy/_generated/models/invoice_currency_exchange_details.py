from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceCurrencyExchangeDetails")


@_attrs_define
class InvoiceCurrencyExchangeDetails:
    """
    Attributes:
        source_currency_code (Union[Unset, str]):
        target_currency_code (Union[Unset, str]):
        rate (Union[Unset, float]):
        rate_date (Union[Unset, str]):
        rate_source (Union[Unset, str]):
    """

    source_currency_code: Union[Unset, str] = UNSET
    target_currency_code: Union[Unset, str] = UNSET
    rate: Union[Unset, float] = UNSET
    rate_date: Union[Unset, str] = UNSET
    rate_source: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source_currency_code = self.source_currency_code

        target_currency_code = self.target_currency_code

        rate = self.rate

        rate_date = self.rate_date

        rate_source = self.rate_source

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source_currency_code is not UNSET:
            field_dict["sourceCurrencyCode"] = source_currency_code
        if target_currency_code is not UNSET:
            field_dict["targetCurrencyCode"] = target_currency_code
        if rate is not UNSET:
            field_dict["rate"] = rate
        if rate_date is not UNSET:
            field_dict["rateDate"] = rate_date
        if rate_source is not UNSET:
            field_dict["rateSource"] = rate_source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        source_currency_code = d.pop("sourceCurrencyCode", UNSET)

        target_currency_code = d.pop("targetCurrencyCode", UNSET)

        rate = d.pop("rate", UNSET)

        rate_date = d.pop("rateDate", UNSET)

        rate_source = d.pop("rateSource", UNSET)

        invoice_currency_exchange_details = cls(
            source_currency_code=source_currency_code,
            target_currency_code=target_currency_code,
            rate=rate,
            rate_date=rate_date,
            rate_source=rate_source,
        )

        invoice_currency_exchange_details.additional_properties = d
        return invoice_currency_exchange_details

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
