from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.price_amount_interval import (
    PriceAmountInterval,
    check_price_amount_interval,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PriceAmount")


@_attrs_define
class PriceAmount:
    """
    Attributes:
        amount (Union[Unset, float]):
        currency (Union[Unset, str]):
        interval (Union[Unset, PriceAmountInterval]):
    """

    amount: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    interval: Union[Unset, PriceAmountInterval] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount

        currency = self.currency

        interval: Union[Unset, str] = UNSET
        if not isinstance(self.interval, Unset):
            interval = self.interval

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if interval is not UNSET:
            field_dict["interval"] = interval

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        _interval = d.pop("interval", UNSET)
        interval: Union[Unset, PriceAmountInterval]
        if isinstance(_interval, Unset):
            interval = UNSET
        else:
            interval = check_price_amount_interval(_interval)

        price_amount = cls(
            amount=amount,
            currency=currency,
            interval=interval,
        )

        price_amount.additional_properties = d
        return price_amount

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
