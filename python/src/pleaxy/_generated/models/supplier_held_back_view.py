from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.supplier_held_back_view_state import (
    SupplierHeldBackViewState,
    check_supplier_held_back_view_state,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.supplier_held_back_view_paid_later import (
        SupplierHeldBackViewPaidLater,
    )


T = TypeVar("T", bound="SupplierHeldBackView")


@_attrs_define
class SupplierHeldBackView:
    """
    Attributes:
        at (Union[Unset, str]):
        amount (Union[Unset, float]):
        state (Union[Unset, SupplierHeldBackViewState]):
        carried_by (Union[Unset, str]):
        paid_later (Union[Unset, SupplierHeldBackViewPaidLater]):
        closed_at (Union[Unset, str]):
        held (Union[Unset, float]):
    """

    at: Union[Unset, str] = UNSET
    amount: Union[Unset, float] = UNSET
    state: Union[Unset, SupplierHeldBackViewState] = UNSET
    carried_by: Union[Unset, str] = UNSET
    paid_later: Union[Unset, "SupplierHeldBackViewPaidLater"] = UNSET
    closed_at: Union[Unset, str] = UNSET
    held: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        at = self.at

        amount = self.amount

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state

        carried_by = self.carried_by

        paid_later: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.paid_later, Unset):
            paid_later = self.paid_later.to_dict()

        closed_at = self.closed_at

        held = self.held

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if amount is not UNSET:
            field_dict["amount"] = amount
        if state is not UNSET:
            field_dict["state"] = state
        if carried_by is not UNSET:
            field_dict["carriedBy"] = carried_by
        if paid_later is not UNSET:
            field_dict["paidLater"] = paid_later
        if closed_at is not UNSET:
            field_dict["closedAt"] = closed_at
        if held is not UNSET:
            field_dict["held"] = held

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.supplier_held_back_view_paid_later import (
            SupplierHeldBackViewPaidLater,
        )

        d = src_dict.copy()
        at = d.pop("at", UNSET)

        amount = d.pop("amount", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, SupplierHeldBackViewState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = check_supplier_held_back_view_state(_state)

        carried_by = d.pop("carriedBy", UNSET)

        _paid_later = d.pop("paidLater", UNSET)
        paid_later: Union[Unset, SupplierHeldBackViewPaidLater]
        if isinstance(_paid_later, Unset):
            paid_later = UNSET
        else:
            paid_later = SupplierHeldBackViewPaidLater.from_dict(_paid_later)

        closed_at = d.pop("closedAt", UNSET)

        held = d.pop("held", UNSET)

        supplier_held_back_view = cls(
            at=at,
            amount=amount,
            state=state,
            carried_by=carried_by,
            paid_later=paid_later,
            closed_at=closed_at,
            held=held,
        )

        supplier_held_back_view.additional_properties = d
        return supplier_held_back_view

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
