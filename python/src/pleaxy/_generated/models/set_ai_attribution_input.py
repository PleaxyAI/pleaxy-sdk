from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ai_attribution_rule_input import AiAttributionRuleInput


T = TypeVar("T", bound="SetAiAttributionInput")


@_attrs_define
class SetAiAttributionInput:
    """
    Attributes:
        rules (List['AiAttributionRuleInput']): Every rule, in order: first match wins. At most 200.
        version (float): The version the rules were read at (GetAiAttribution's version); 0 for the first save.
    """

    rules: List["AiAttributionRuleInput"]
    version: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rules = []
        for rules_item_data in self.rules:
            rules_item = rules_item_data.to_dict()
            rules.append(rules_item)

        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rules": rules,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ai_attribution_rule_input import AiAttributionRuleInput

        d = src_dict.copy()
        rules = []
        _rules = d.pop("rules")
        for rules_item_data in _rules:
            rules_item = AiAttributionRuleInput.from_dict(rules_item_data)

            rules.append(rules_item)

        version = d.pop("version")

        set_ai_attribution_input = cls(
            rules=rules,
            version=version,
        )

        set_ai_attribution_input.additional_properties = d
        return set_ai_attribution_input

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
