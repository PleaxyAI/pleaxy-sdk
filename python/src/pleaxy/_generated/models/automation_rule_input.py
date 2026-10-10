from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.automation_rule_condition_input import AutomationRuleConditionInput


T = TypeVar("T", bound="AutomationRuleInput")


@_attrs_define
class AutomationRuleInput:
    """
    Attributes:
        label (str):
        conditions (AutomationRuleConditionInput):
        auto_approve (bool):
        enabled (bool):
        id (Union[Unset, str]): Omit to create a new rule - the server assigns an id.
    """

    label: str
    conditions: "AutomationRuleConditionInput"
    auto_approve: bool
    enabled: bool
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        label = self.label

        conditions = self.conditions.to_dict()

        auto_approve = self.auto_approve

        enabled = self.enabled

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "conditions": conditions,
                "autoApprove": auto_approve,
                "enabled": enabled,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.automation_rule_condition_input import (
            AutomationRuleConditionInput,
        )

        d = src_dict.copy()
        label = d.pop("label")

        conditions = AutomationRuleConditionInput.from_dict(d.pop("conditions"))

        auto_approve = d.pop("autoApprove")

        enabled = d.pop("enabled")

        id = d.pop("id", UNSET)

        automation_rule_input = cls(
            label=label,
            conditions=conditions,
            auto_approve=auto_approve,
            enabled=enabled,
            id=id,
        )

        automation_rule_input.additional_properties = d
        return automation_rule_input

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
