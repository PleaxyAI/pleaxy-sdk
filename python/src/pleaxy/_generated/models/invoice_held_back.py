from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_held_back_state import (
    InvoiceHeldBackState,
    check_invoice_held_back_state,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_held_back_paid_later import InvoiceHeldBackPaidLater


T = TypeVar("T", bound="InvoiceHeldBack")


@_attrs_define
class InvoiceHeldBack:
    """
    Attributes:
        amount (Union[Unset, float]):
        net (Union[Unset, float]):
        tax (Union[Unset, float]):
        claim_id (Union[Unset, str]):
        decision_id (Union[Unset, str]):
        at (Union[Unset, str]):
        state (Union[Unset, InvoiceHeldBackState]):
        carried_by (Union[Unset, str]):
        under_protest (Union[Unset, bool]):
        paid_later (Union[Unset, InvoiceHeldBackPaidLater]):
        closed_at (Union[Unset, str]):
    """

    amount: Union[Unset, float] = UNSET
    net: Union[Unset, float] = UNSET
    tax: Union[Unset, float] = UNSET
    claim_id: Union[Unset, str] = UNSET
    decision_id: Union[Unset, str] = UNSET
    at: Union[Unset, str] = UNSET
    state: Union[Unset, InvoiceHeldBackState] = UNSET
    carried_by: Union[Unset, str] = UNSET
    under_protest: Union[Unset, bool] = UNSET
    paid_later: Union[Unset, "InvoiceHeldBackPaidLater"] = UNSET
    closed_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount

        net = self.net

        tax = self.tax

        claim_id = self.claim_id

        decision_id = self.decision_id

        at = self.at

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state

        carried_by = self.carried_by

        under_protest = self.under_protest

        paid_later: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.paid_later, Unset):
            paid_later = self.paid_later.to_dict()

        closed_at = self.closed_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if net is not UNSET:
            field_dict["net"] = net
        if tax is not UNSET:
            field_dict["tax"] = tax
        if claim_id is not UNSET:
            field_dict["claimId"] = claim_id
        if decision_id is not UNSET:
            field_dict["decisionId"] = decision_id
        if at is not UNSET:
            field_dict["at"] = at
        if state is not UNSET:
            field_dict["state"] = state
        if carried_by is not UNSET:
            field_dict["carriedBy"] = carried_by
        if under_protest is not UNSET:
            field_dict["underProtest"] = under_protest
        if paid_later is not UNSET:
            field_dict["paidLater"] = paid_later
        if closed_at is not UNSET:
            field_dict["closedAt"] = closed_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_held_back_paid_later import InvoiceHeldBackPaidLater

        d = src_dict.copy()
        amount = d.pop("amount", UNSET)

        net = d.pop("net", UNSET)

        tax = d.pop("tax", UNSET)

        claim_id = d.pop("claimId", UNSET)

        decision_id = d.pop("decisionId", UNSET)

        at = d.pop("at", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, InvoiceHeldBackState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = check_invoice_held_back_state(_state)

        carried_by = d.pop("carriedBy", UNSET)

        under_protest = d.pop("underProtest", UNSET)

        _paid_later = d.pop("paidLater", UNSET)
        paid_later: Union[Unset, InvoiceHeldBackPaidLater]
        if isinstance(_paid_later, Unset):
            paid_later = UNSET
        else:
            paid_later = InvoiceHeldBackPaidLater.from_dict(_paid_later)

        closed_at = d.pop("closedAt", UNSET)

        invoice_held_back = cls(
            amount=amount,
            net=net,
            tax=tax,
            claim_id=claim_id,
            decision_id=decision_id,
            at=at,
            state=state,
            carried_by=carried_by,
            under_protest=under_protest,
            paid_later=paid_later,
            closed_at=closed_at,
        )

        invoice_held_back.additional_properties = d
        return invoice_held_back

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
