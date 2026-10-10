from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.stripe_payment_status_payment_method_type import (
    StripePaymentStatusPaymentMethodType,
    check_stripe_payment_status_payment_method_type,
)
from ..models.stripe_payment_status_reason import (
    StripePaymentStatusReason,
    check_stripe_payment_status_reason,
)
from ..models.stripe_payment_status_state import (
    StripePaymentStatusState,
    check_stripe_payment_status_state,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stripe_payment_status_quote import StripePaymentStatusQuote


T = TypeVar("T", bound="StripePaymentStatus")


@_attrs_define
class StripePaymentStatus:
    """
    Attributes:
        available (Union[Unset, bool]):
        reason (Union[Unset, StripePaymentStatusReason]):
        state (Union[Unset, StripePaymentStatusState]):
        payment_method_type (Union[Unset, StripePaymentStatusPaymentMethodType]):
        quote (Union[Unset, StripePaymentStatusQuote]):
    """

    available: Union[Unset, bool] = UNSET
    reason: Union[Unset, StripePaymentStatusReason] = UNSET
    state: Union[Unset, StripePaymentStatusState] = UNSET
    payment_method_type: Union[Unset, StripePaymentStatusPaymentMethodType] = UNSET
    quote: Union[Unset, "StripePaymentStatusQuote"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        available = self.available

        reason: Union[Unset, str] = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state

        payment_method_type: Union[Unset, str] = UNSET
        if not isinstance(self.payment_method_type, Unset):
            payment_method_type = self.payment_method_type

        quote: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.quote, Unset):
            quote = self.quote.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if available is not UNSET:
            field_dict["available"] = available
        if reason is not UNSET:
            field_dict["reason"] = reason
        if state is not UNSET:
            field_dict["state"] = state
        if payment_method_type is not UNSET:
            field_dict["paymentMethodType"] = payment_method_type
        if quote is not UNSET:
            field_dict["quote"] = quote

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.stripe_payment_status_quote import StripePaymentStatusQuote

        d = src_dict.copy()
        available = d.pop("available", UNSET)

        _reason = d.pop("reason", UNSET)
        reason: Union[Unset, StripePaymentStatusReason]
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = check_stripe_payment_status_reason(_reason)

        _state = d.pop("state", UNSET)
        state: Union[Unset, StripePaymentStatusState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = check_stripe_payment_status_state(_state)

        _payment_method_type = d.pop("paymentMethodType", UNSET)
        payment_method_type: Union[Unset, StripePaymentStatusPaymentMethodType]
        if isinstance(_payment_method_type, Unset):
            payment_method_type = UNSET
        else:
            payment_method_type = check_stripe_payment_status_payment_method_type(
                _payment_method_type
            )

        _quote = d.pop("quote", UNSET)
        quote: Union[Unset, StripePaymentStatusQuote]
        if isinstance(_quote, Unset):
            quote = UNSET
        else:
            quote = StripePaymentStatusQuote.from_dict(_quote)

        stripe_payment_status = cls(
            available=available,
            reason=reason,
            state=state,
            payment_method_type=payment_method_type,
            quote=quote,
        )

        stripe_payment_status.additional_properties = d
        return stripe_payment_status

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
