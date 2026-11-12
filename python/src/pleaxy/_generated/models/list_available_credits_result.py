from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_available_credits_result_credit_settlement import (
    ListAvailableCreditsResultCreditSettlement,
    check_list_available_credits_result_credit_settlement,
)
from ..models.list_available_credits_result_locked import (
    ListAvailableCreditsResultLocked,
    check_list_available_credits_result_locked,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_available_credits_result_credits_item import (
        ListAvailableCreditsResultCreditsItem,
    )
    from ..models.list_available_credits_result_pending_item import (
        ListAvailableCreditsResultPendingItem,
    )


T = TypeVar("T", bound="ListAvailableCreditsResult")


@_attrs_define
class ListAvailableCreditsResult:
    """
    Attributes:
        amount_due (Union[Unset, float]):
        currency (Union[Unset, str]):
        credits_ (Union[Unset, List['ListAvailableCreditsResultCreditsItem']]):
        pending (Union[Unset, List['ListAvailableCreditsResultPendingItem']]):
        suggested_total (Union[Unset, float]):
        locked (Union[Unset, ListAvailableCreditsResultLocked]):
        credit_settlement (Union[Unset, ListAvailableCreditsResultCreditSettlement]):
    """

    amount_due: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    credits_: Union[Unset, List["ListAvailableCreditsResultCreditsItem"]] = UNSET
    pending: Union[Unset, List["ListAvailableCreditsResultPendingItem"]] = UNSET
    suggested_total: Union[Unset, float] = UNSET
    locked: Union[Unset, ListAvailableCreditsResultLocked] = UNSET
    credit_settlement: Union[Unset, ListAvailableCreditsResultCreditSettlement] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount_due = self.amount_due

        currency = self.currency

        credits_: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.credits_, Unset):
            credits_ = []
            for credits_item_data in self.credits_:
                credits_item = credits_item_data.to_dict()
                credits_.append(credits_item)

        pending: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.pending, Unset):
            pending = []
            for pending_item_data in self.pending:
                pending_item = pending_item_data.to_dict()
                pending.append(pending_item)

        suggested_total = self.suggested_total

        locked: Union[Unset, str] = UNSET
        if not isinstance(self.locked, Unset):
            locked = self.locked

        credit_settlement: Union[Unset, str] = UNSET
        if not isinstance(self.credit_settlement, Unset):
            credit_settlement = self.credit_settlement

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount_due is not UNSET:
            field_dict["amountDue"] = amount_due
        if currency is not UNSET:
            field_dict["currency"] = currency
        if credits_ is not UNSET:
            field_dict["credits"] = credits_
        if pending is not UNSET:
            field_dict["pending"] = pending
        if suggested_total is not UNSET:
            field_dict["suggestedTotal"] = suggested_total
        if locked is not UNSET:
            field_dict["locked"] = locked
        if credit_settlement is not UNSET:
            field_dict["creditSettlement"] = credit_settlement

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.list_available_credits_result_credits_item import (
            ListAvailableCreditsResultCreditsItem,
        )
        from ..models.list_available_credits_result_pending_item import (
            ListAvailableCreditsResultPendingItem,
        )

        d = src_dict.copy()
        amount_due = d.pop("amountDue", UNSET)

        currency = d.pop("currency", UNSET)

        credits_ = []
        _credits_ = d.pop("credits", UNSET)
        for credits_item_data in _credits_ or []:
            credits_item = ListAvailableCreditsResultCreditsItem.from_dict(
                credits_item_data
            )

            credits_.append(credits_item)

        pending = []
        _pending = d.pop("pending", UNSET)
        for pending_item_data in _pending or []:
            pending_item = ListAvailableCreditsResultPendingItem.from_dict(
                pending_item_data
            )

            pending.append(pending_item)

        suggested_total = d.pop("suggestedTotal", UNSET)

        _locked = d.pop("locked", UNSET)
        locked: Union[Unset, ListAvailableCreditsResultLocked]
        if isinstance(_locked, Unset):
            locked = UNSET
        else:
            locked = check_list_available_credits_result_locked(_locked)

        _credit_settlement = d.pop("creditSettlement", UNSET)
        credit_settlement: Union[Unset, ListAvailableCreditsResultCreditSettlement]
        if isinstance(_credit_settlement, Unset):
            credit_settlement = UNSET
        else:
            credit_settlement = check_list_available_credits_result_credit_settlement(
                _credit_settlement
            )

        list_available_credits_result = cls(
            amount_due=amount_due,
            currency=currency,
            credits_=credits_,
            pending=pending,
            suggested_total=suggested_total,
            locked=locked,
            credit_settlement=credit_settlement,
        )

        list_available_credits_result.additional_properties = d
        return list_available_credits_result

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
