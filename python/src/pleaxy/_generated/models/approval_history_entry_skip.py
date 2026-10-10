from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.approval_history_entry_skip_rule import (
    ApprovalHistoryEntrySkipRule,
    check_approval_history_entry_skip_rule,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApprovalHistoryEntrySkip")


@_attrs_define
class ApprovalHistoryEntrySkip:
    """
    Attributes:
        rule (Union[Unset, ApprovalHistoryEntrySkipRule]):
        stage_label (Union[Unset, str]):
        employee_key (Union[Unset, str]):
    """

    rule: Union[Unset, ApprovalHistoryEntrySkipRule] = UNSET
    stage_label: Union[Unset, str] = UNSET
    employee_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rule: Union[Unset, str] = UNSET
        if not isinstance(self.rule, Unset):
            rule = self.rule

        stage_label = self.stage_label

        employee_key = self.employee_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rule is not UNSET:
            field_dict["rule"] = rule
        if stage_label is not UNSET:
            field_dict["stageLabel"] = stage_label
        if employee_key is not UNSET:
            field_dict["employeeKey"] = employee_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _rule = d.pop("rule", UNSET)
        rule: Union[Unset, ApprovalHistoryEntrySkipRule]
        if isinstance(_rule, Unset):
            rule = UNSET
        else:
            rule = check_approval_history_entry_skip_rule(_rule)

        stage_label = d.pop("stageLabel", UNSET)

        employee_key = d.pop("employeeKey", UNSET)

        approval_history_entry_skip = cls(
            rule=rule,
            stage_label=stage_label,
            employee_key=employee_key,
        )

        approval_history_entry_skip.additional_properties = d
        return approval_history_entry_skip

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
