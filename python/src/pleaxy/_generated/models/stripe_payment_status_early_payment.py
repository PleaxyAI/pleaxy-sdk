from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stripe_payment_status_early_payment_quote import (
        StripePaymentStatusEarlyPaymentQuote,
    )


T = TypeVar("T", bound="StripePaymentStatusEarlyPayment")


@_attrs_define
class StripePaymentStatusEarlyPayment:
    """
    Attributes:
        percent (Union[Unset, float]):
        amount (Union[Unset, float]):
        deadline (Union[Unset, str]):
        quote (Union[Unset, StripePaymentStatusEarlyPaymentQuote]):
        taken (Union[Unset, bool]):
    """

    percent: Union[Unset, float] = UNSET
    amount: Union[Unset, float] = UNSET
    deadline: Union[Unset, str] = UNSET
    quote: Union[Unset, "StripePaymentStatusEarlyPaymentQuote"] = UNSET
    taken: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        percent = self.percent

        amount = self.amount

        deadline = self.deadline

        quote: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.quote, Unset):
            quote = self.quote.to_dict()

        taken = self.taken

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if percent is not UNSET:
            field_dict["percent"] = percent
        if amount is not UNSET:
            field_dict["amount"] = amount
        if deadline is not UNSET:
            field_dict["deadline"] = deadline
        if quote is not UNSET:
            field_dict["quote"] = quote
        if taken is not UNSET:
            field_dict["taken"] = taken

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.stripe_payment_status_early_payment_quote import (
            StripePaymentStatusEarlyPaymentQuote,
        )

        d = src_dict.copy()
        percent = d.pop("percent", UNSET)

        amount = d.pop("amount", UNSET)

        deadline = d.pop("deadline", UNSET)

        _quote = d.pop("quote", UNSET)
        quote: Union[Unset, StripePaymentStatusEarlyPaymentQuote]
        if isinstance(_quote, Unset):
            quote = UNSET
        else:
            quote = StripePaymentStatusEarlyPaymentQuote.from_dict(_quote)

        taken = d.pop("taken", UNSET)

        stripe_payment_status_early_payment = cls(
            percent=percent,
            amount=amount,
            deadline=deadline,
            quote=quote,
            taken=taken,
        )

        stripe_payment_status_early_payment.additional_properties = d
        return stripe_payment_status_early_payment

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
