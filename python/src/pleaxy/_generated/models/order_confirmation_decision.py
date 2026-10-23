from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.order_confirmation_decision_decision import (
    OrderConfirmationDecisionDecision,
    check_order_confirmation_decision_decision,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderConfirmationDecision")


@_attrs_define
class OrderConfirmationDecision:
    """
    Attributes:
        decision (Union[Unset, OrderConfirmationDecisionDecision]):
        at (Union[Unset, str]):
        version (Union[Unset, float]):
        reason (Union[Unset, str]):
    """

    decision: Union[Unset, OrderConfirmationDecisionDecision] = UNSET
    at: Union[Unset, str] = UNSET
    version: Union[Unset, float] = UNSET
    reason: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        decision: Union[Unset, str] = UNSET
        if not isinstance(self.decision, Unset):
            decision = self.decision

        at = self.at

        version = self.version

        reason = self.reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if decision is not UNSET:
            field_dict["decision"] = decision
        if at is not UNSET:
            field_dict["at"] = at
        if version is not UNSET:
            field_dict["version"] = version
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _decision = d.pop("decision", UNSET)
        decision: Union[Unset, OrderConfirmationDecisionDecision]
        if isinstance(_decision, Unset):
            decision = UNSET
        else:
            decision = check_order_confirmation_decision_decision(_decision)

        at = d.pop("at", UNSET)

        version = d.pop("version", UNSET)

        reason = d.pop("reason", UNSET)

        order_confirmation_decision = cls(
            decision=decision,
            at=at,
            version=version,
            reason=reason,
        )

        order_confirmation_decision.additional_properties = d
        return order_confirmation_decision

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
