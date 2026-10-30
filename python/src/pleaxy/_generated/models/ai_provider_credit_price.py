from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ai_provider_credit_price_kind import (
    AiProviderCreditPriceKind,
    check_ai_provider_credit_price_kind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AiProviderCreditPrice")


@_attrs_define
class AiProviderCreditPrice:
    """
    Attributes:
        amount (Union[Unset, float]):
        currency (Union[Unset, str]):
        kind (Union[Unset, AiProviderCreditPriceKind]):
    """

    amount: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    kind: Union[Unset, AiProviderCreditPriceKind] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount

        currency = self.currency

        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if kind is not UNSET:
            field_dict["kind"] = kind

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, AiProviderCreditPriceKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_ai_provider_credit_price_kind(_kind)

        ai_provider_credit_price = cls(
            amount=amount,
            currency=currency,
            kind=kind,
        )

        ai_provider_credit_price.additional_properties = d
        return ai_provider_credit_price

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
