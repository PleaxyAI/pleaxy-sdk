from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_renewal_rule_last_uncovered_run_drafts_item import (
        AiRenewalRuleLastUncoveredRunDraftsItem,
    )


T = TypeVar("T", bound="AiRenewalRuleLastUncoveredRun")


@_attrs_define
class AiRenewalRuleLastUncoveredRun:
    """
    Attributes:
        at (Union[Unset, str]):
        period (Union[Unset, str]):
        drafts (Union[Unset, List['AiRenewalRuleLastUncoveredRunDraftsItem']]):
    """

    at: Union[Unset, str] = UNSET
    period: Union[Unset, str] = UNSET
    drafts: Union[Unset, List["AiRenewalRuleLastUncoveredRunDraftsItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        at = self.at

        period = self.period

        drafts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.drafts, Unset):
            drafts = []
            for drafts_item_data in self.drafts:
                drafts_item = drafts_item_data.to_dict()
                drafts.append(drafts_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if period is not UNSET:
            field_dict["period"] = period
        if drafts is not UNSET:
            field_dict["drafts"] = drafts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ai_renewal_rule_last_uncovered_run_drafts_item import (
            AiRenewalRuleLastUncoveredRunDraftsItem,
        )

        d = src_dict.copy()
        at = d.pop("at", UNSET)

        period = d.pop("period", UNSET)

        drafts = []
        _drafts = d.pop("drafts", UNSET)
        for drafts_item_data in _drafts or []:
            drafts_item = AiRenewalRuleLastUncoveredRunDraftsItem.from_dict(
                drafts_item_data
            )

            drafts.append(drafts_item)

        ai_renewal_rule_last_uncovered_run = cls(
            at=at,
            period=period,
            drafts=drafts,
        )

        ai_renewal_rule_last_uncovered_run.additional_properties = d
        return ai_renewal_rule_last_uncovered_run

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
