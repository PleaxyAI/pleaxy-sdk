from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.automation_rule_condition import AutomationRuleCondition


T = TypeVar("T", bound="AutomationRule")


@_attrs_define
class AutomationRule:
    """
    Attributes:
        id (str):
        label (Union[Unset, str]):
        conditions (Union[Unset, AutomationRuleCondition]):
        auto_approve (Union[Unset, bool]):
        enabled (Union[Unset, bool]):
        created_at (Union[Unset, str]):
    """

    id: str
    label: Union[Unset, str] = UNSET
    conditions: Union[Unset, "AutomationRuleCondition"] = UNSET
    auto_approve: Union[Unset, bool] = UNSET
    enabled: Union[Unset, bool] = UNSET
    created_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        label = self.label

        conditions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = self.conditions.to_dict()

        auto_approve = self.auto_approve

        enabled = self.enabled

        created_at = self.created_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if auto_approve is not UNSET:
            field_dict["autoApprove"] = auto_approve
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.automation_rule_condition import AutomationRuleCondition

        d = src_dict.copy()
        id = d.pop("id")

        label = d.pop("label", UNSET)

        _conditions = d.pop("conditions", UNSET)
        conditions: Union[Unset, AutomationRuleCondition]
        if isinstance(_conditions, Unset):
            conditions = UNSET
        else:
            conditions = AutomationRuleCondition.from_dict(_conditions)

        auto_approve = d.pop("autoApprove", UNSET)

        enabled = d.pop("enabled", UNSET)

        created_at = d.pop("createdAt", UNSET)

        automation_rule = cls(
            id=id,
            label=label,
            conditions=conditions,
            auto_approve=auto_approve,
            enabled=enabled,
            created_at=created_at,
        )

        automation_rule.additional_properties = d
        return automation_rule

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
