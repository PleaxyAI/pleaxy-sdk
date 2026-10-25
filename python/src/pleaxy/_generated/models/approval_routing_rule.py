from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.approval_routing_rule_action import (
    ApprovalRoutingRuleAction,
    check_approval_routing_rule_action,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApprovalRoutingRule")


@_attrs_define
class ApprovalRoutingRule:
    """
    Attributes:
        id (str):
        index (Union[Unset, float]):
        action (Union[Unset, ApprovalRoutingRuleAction]):
        label (Union[Unset, str]):
    """

    id: str
    index: Union[Unset, float] = UNSET
    action: Union[Unset, ApprovalRoutingRuleAction] = UNSET
    label: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        index = self.index

        action: Union[Unset, str] = UNSET
        if not isinstance(self.action, Unset):
            action = self.action

        label = self.label

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if index is not UNSET:
            field_dict["index"] = index
        if action is not UNSET:
            field_dict["action"] = action
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        index = d.pop("index", UNSET)

        _action = d.pop("action", UNSET)
        action: Union[Unset, ApprovalRoutingRuleAction]
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = check_approval_routing_rule_action(_action)

        label = d.pop("label", UNSET)

        approval_routing_rule = cls(
            id=id,
            index=index,
            action=action,
            label=label,
        )

        approval_routing_rule.additional_properties = d
        return approval_routing_rule

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
