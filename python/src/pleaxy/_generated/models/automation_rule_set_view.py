from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.automation_rule_set_view_process import (
    AutomationRuleSetViewProcess,
    check_automation_rule_set_view_process,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.automation_rule import AutomationRule


T = TypeVar("T", bound="AutomationRuleSetView")


@_attrs_define
class AutomationRuleSetView:
    """
    Attributes:
        process (Union[Unset, AutomationRuleSetViewProcess]):
        rules (Union[Unset, List['AutomationRule']]):
        auto_approve_allowed (Union[Unset, bool]):
    """

    process: Union[Unset, AutomationRuleSetViewProcess] = UNSET
    rules: Union[Unset, List["AutomationRule"]] = UNSET
    auto_approve_allowed: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        process: Union[Unset, str] = UNSET
        if not isinstance(self.process, Unset):
            process = self.process

        rules: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rules, Unset):
            rules = []
            for rules_item_data in self.rules:
                rules_item = rules_item_data.to_dict()
                rules.append(rules_item)

        auto_approve_allowed = self.auto_approve_allowed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if process is not UNSET:
            field_dict["process"] = process
        if rules is not UNSET:
            field_dict["rules"] = rules
        if auto_approve_allowed is not UNSET:
            field_dict["autoApproveAllowed"] = auto_approve_allowed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.automation_rule import AutomationRule

        d = src_dict.copy()
        _process = d.pop("process", UNSET)
        process: Union[Unset, AutomationRuleSetViewProcess]
        if isinstance(_process, Unset):
            process = UNSET
        else:
            process = check_automation_rule_set_view_process(_process)

        rules = []
        _rules = d.pop("rules", UNSET)
        for rules_item_data in _rules or []:
            rules_item = AutomationRule.from_dict(rules_item_data)

            rules.append(rules_item)

        auto_approve_allowed = d.pop("autoApproveAllowed", UNSET)

        automation_rule_set_view = cls(
            process=process,
            rules=rules,
            auto_approve_allowed=auto_approve_allowed,
        )

        automation_rule_set_view.additional_properties = d
        return automation_rule_set_view

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
