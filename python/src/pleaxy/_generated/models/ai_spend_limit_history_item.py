from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ai_spend_limit_history_item_action import (
    AiSpendLimitHistoryItemAction,
    check_ai_spend_limit_history_item_action,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AiSpendLimitHistoryItem")


@_attrs_define
class AiSpendLimitHistoryItem:
    """
    Attributes:
        at (Union[Unset, str]):
        by (Union[Unset, str]):
        action (Union[Unset, AiSpendLimitHistoryItemAction]):
        amount (Union[Unset, float]):
        read_back (Union[Unset, float]):
        error (Union[Unset, str]):
    """

    at: Union[Unset, str] = UNSET
    by: Union[Unset, str] = UNSET
    action: Union[Unset, AiSpendLimitHistoryItemAction] = UNSET
    amount: Union[Unset, float] = UNSET
    read_back: Union[Unset, float] = UNSET
    error: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        at = self.at

        by = self.by

        action: Union[Unset, str] = UNSET
        if not isinstance(self.action, Unset):
            action = self.action

        amount = self.amount

        read_back = self.read_back

        error = self.error

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if by is not UNSET:
            field_dict["by"] = by
        if action is not UNSET:
            field_dict["action"] = action
        if amount is not UNSET:
            field_dict["amount"] = amount
        if read_back is not UNSET:
            field_dict["readBack"] = read_back
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        at = d.pop("at", UNSET)

        by = d.pop("by", UNSET)

        _action = d.pop("action", UNSET)
        action: Union[Unset, AiSpendLimitHistoryItemAction]
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = check_ai_spend_limit_history_item_action(_action)

        amount = d.pop("amount", UNSET)

        read_back = d.pop("readBack", UNSET)

        error = d.pop("error", UNSET)

        ai_spend_limit_history_item = cls(
            at=at,
            by=by,
            action=action,
            amount=amount,
            read_back=read_back,
            error=error,
        )

        ai_spend_limit_history_item.additional_properties = d
        return ai_spend_limit_history_item

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
