from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_stripe_payment_payment_method_type import (
    InvoiceStripePaymentPaymentMethodType,
    check_invoice_stripe_payment_payment_method_type,
)
from ..models.invoice_stripe_payment_state import (
    InvoiceStripePaymentState,
    check_invoice_stripe_payment_state,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceStripePayment")


@_attrs_define
class InvoiceStripePayment:
    """
    Attributes:
        account_id (Union[Unset, str]):
        checkout_session_id (Union[Unset, str]):
        checkout_expires_at (Union[Unset, str]):
        fee_cents (Union[Unset, float]):
        total_cents (Union[Unset, float]):
        state (Union[Unset, InvoiceStripePaymentState]):
        payment_intent_id (Union[Unset, str]):
        payment_method_type (Union[Unset, InvoiceStripePaymentPaymentMethodType]):
        started_at (Union[Unset, str]):
        started_by (Union[Unset, str]):
        started_by_name (Union[Unset, str]):
        succeeded_at (Union[Unset, str]):
    """

    account_id: Union[Unset, str] = UNSET
    checkout_session_id: Union[Unset, str] = UNSET
    checkout_expires_at: Union[Unset, str] = UNSET
    fee_cents: Union[Unset, float] = UNSET
    total_cents: Union[Unset, float] = UNSET
    state: Union[Unset, InvoiceStripePaymentState] = UNSET
    payment_intent_id: Union[Unset, str] = UNSET
    payment_method_type: Union[Unset, InvoiceStripePaymentPaymentMethodType] = UNSET
    started_at: Union[Unset, str] = UNSET
    started_by: Union[Unset, str] = UNSET
    started_by_name: Union[Unset, str] = UNSET
    succeeded_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id

        checkout_session_id = self.checkout_session_id

        checkout_expires_at = self.checkout_expires_at

        fee_cents = self.fee_cents

        total_cents = self.total_cents

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state

        payment_intent_id = self.payment_intent_id

        payment_method_type: Union[Unset, str] = UNSET
        if not isinstance(self.payment_method_type, Unset):
            payment_method_type = self.payment_method_type

        started_at = self.started_at

        started_by = self.started_by

        started_by_name = self.started_by_name

        succeeded_at = self.succeeded_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if checkout_session_id is not UNSET:
            field_dict["checkoutSessionId"] = checkout_session_id
        if checkout_expires_at is not UNSET:
            field_dict["checkoutExpiresAt"] = checkout_expires_at
        if fee_cents is not UNSET:
            field_dict["feeCents"] = fee_cents
        if total_cents is not UNSET:
            field_dict["totalCents"] = total_cents
        if state is not UNSET:
            field_dict["state"] = state
        if payment_intent_id is not UNSET:
            field_dict["paymentIntentId"] = payment_intent_id
        if payment_method_type is not UNSET:
            field_dict["paymentMethodType"] = payment_method_type
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if started_by is not UNSET:
            field_dict["startedBy"] = started_by
        if started_by_name is not UNSET:
            field_dict["startedByName"] = started_by_name
        if succeeded_at is not UNSET:
            field_dict["succeededAt"] = succeeded_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_id = d.pop("accountId", UNSET)

        checkout_session_id = d.pop("checkoutSessionId", UNSET)

        checkout_expires_at = d.pop("checkoutExpiresAt", UNSET)

        fee_cents = d.pop("feeCents", UNSET)

        total_cents = d.pop("totalCents", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, InvoiceStripePaymentState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = check_invoice_stripe_payment_state(_state)

        payment_intent_id = d.pop("paymentIntentId", UNSET)

        _payment_method_type = d.pop("paymentMethodType", UNSET)
        payment_method_type: Union[Unset, InvoiceStripePaymentPaymentMethodType]
        if isinstance(_payment_method_type, Unset):
            payment_method_type = UNSET
        else:
            payment_method_type = check_invoice_stripe_payment_payment_method_type(
                _payment_method_type
            )

        started_at = d.pop("startedAt", UNSET)

        started_by = d.pop("startedBy", UNSET)

        started_by_name = d.pop("startedByName", UNSET)

        succeeded_at = d.pop("succeededAt", UNSET)

        invoice_stripe_payment = cls(
            account_id=account_id,
            checkout_session_id=checkout_session_id,
            checkout_expires_at=checkout_expires_at,
            fee_cents=fee_cents,
            total_cents=total_cents,
            state=state,
            payment_intent_id=payment_intent_id,
            payment_method_type=payment_method_type,
            started_at=started_at,
            started_by=started_by,
            started_by_name=started_by_name,
            succeeded_at=succeeded_at,
        )

        invoice_stripe_payment.additional_properties = d
        return invoice_stripe_payment

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
