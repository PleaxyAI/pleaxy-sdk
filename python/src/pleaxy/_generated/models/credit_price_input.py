from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.credit_price_input_kind import (
    CreditPriceInputKind,
    check_credit_price_input_kind,
)

T = TypeVar("T", bound="CreditPriceInput")


@_attrs_define
class CreditPriceInput:
    """
    Attributes:
        amount (float):
        currency (str):
        kind (CreditPriceInputKind):
    """

    amount: float
    currency: str
    kind: CreditPriceInputKind
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount

        currency = self.currency

        kind: str = self.kind

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "currency": currency,
                "kind": kind,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amount = d.pop("amount")

        currency = d.pop("currency")

        kind = check_credit_price_input_kind(d.pop("kind"))

        credit_price_input = cls(
            amount=amount,
            currency=currency,
            kind=kind,
        )

        credit_price_input.additional_properties = d
        return credit_price_input

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
