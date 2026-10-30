from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_attribution_response_unattributed_item import (
        AiAttributionResponseUnattributedItem,
    )
    from ..models.ai_attribution_response_unmatched_values_item import (
        AiAttributionResponseUnmatchedValuesItem,
    )
    from ..models.ai_attribution_rule_view import AiAttributionRuleView


T = TypeVar("T", bound="AiAttributionResponse")


@_attrs_define
class AiAttributionResponse:
    """
    Attributes:
        period (Union[Unset, str]):
        rules (Union[Unset, List['AiAttributionRuleView']]):
        version (Union[Unset, float]):
        updated_at (Union[Unset, str]):
        unattributed (Union[Unset, List['AiAttributionResponseUnattributedItem']]):
        unmatched_values (Union[Unset, List['AiAttributionResponseUnmatchedValuesItem']]):
    """

    period: Union[Unset, str] = UNSET
    rules: Union[Unset, List["AiAttributionRuleView"]] = UNSET
    version: Union[Unset, float] = UNSET
    updated_at: Union[Unset, str] = UNSET
    unattributed: Union[Unset, List["AiAttributionResponseUnattributedItem"]] = UNSET
    unmatched_values: Union[Unset, List["AiAttributionResponseUnmatchedValuesItem"]] = (
        UNSET
    )
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        period = self.period

        rules: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rules, Unset):
            rules = []
            for rules_item_data in self.rules:
                rules_item = rules_item_data.to_dict()
                rules.append(rules_item)

        version = self.version

        updated_at = self.updated_at

        unattributed: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.unattributed, Unset):
            unattributed = []
            for unattributed_item_data in self.unattributed:
                unattributed_item = unattributed_item_data.to_dict()
                unattributed.append(unattributed_item)

        unmatched_values: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.unmatched_values, Unset):
            unmatched_values = []
            for unmatched_values_item_data in self.unmatched_values:
                unmatched_values_item = unmatched_values_item_data.to_dict()
                unmatched_values.append(unmatched_values_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if period is not UNSET:
            field_dict["period"] = period
        if rules is not UNSET:
            field_dict["rules"] = rules
        if version is not UNSET:
            field_dict["version"] = version
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if unattributed is not UNSET:
            field_dict["unattributed"] = unattributed
        if unmatched_values is not UNSET:
            field_dict["unmatchedValues"] = unmatched_values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ai_attribution_response_unattributed_item import (
            AiAttributionResponseUnattributedItem,
        )
        from ..models.ai_attribution_response_unmatched_values_item import (
            AiAttributionResponseUnmatchedValuesItem,
        )
        from ..models.ai_attribution_rule_view import AiAttributionRuleView

        d = src_dict.copy()
        period = d.pop("period", UNSET)

        rules = []
        _rules = d.pop("rules", UNSET)
        for rules_item_data in _rules or []:
            rules_item = AiAttributionRuleView.from_dict(rules_item_data)

            rules.append(rules_item)

        version = d.pop("version", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        unattributed = []
        _unattributed = d.pop("unattributed", UNSET)
        for unattributed_item_data in _unattributed or []:
            unattributed_item = AiAttributionResponseUnattributedItem.from_dict(
                unattributed_item_data
            )

            unattributed.append(unattributed_item)

        unmatched_values = []
        _unmatched_values = d.pop("unmatchedValues", UNSET)
        for unmatched_values_item_data in _unmatched_values or []:
            unmatched_values_item = AiAttributionResponseUnmatchedValuesItem.from_dict(
                unmatched_values_item_data
            )

            unmatched_values.append(unmatched_values_item)

        ai_attribution_response = cls(
            period=period,
            rules=rules,
            version=version,
            updated_at=updated_at,
            unattributed=unattributed,
            unmatched_values=unmatched_values,
        )

        ai_attribution_response.additional_properties = d
        return ai_attribution_response

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
