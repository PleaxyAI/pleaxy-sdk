from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetAiRenewalRuleInput")


@_attrs_define
class SetAiRenewalRuleInput:
    """
    Attributes:
        enabled (bool): Whether next month's AI orders are drafted from the forecast.
        day_of_month (Union[Unset, float]): The day of the month (1-28) from which the drafts are raised. Default 25.
        draft_uncovered (Union[Unset, bool]): Whether Pleaxy also drafts an order for this month's spend no order covers
            (GetAiRecommendations' uncovered and accounts), once per provider or account a month, from the 3rd. Drafts only:
            a person reviews and submits them. Unchanged when absent.
    """

    enabled: bool
    day_of_month: Union[Unset, float] = UNSET
    draft_uncovered: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled

        day_of_month = self.day_of_month

        draft_uncovered = self.draft_uncovered

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
            }
        )
        if day_of_month is not UNSET:
            field_dict["dayOfMonth"] = day_of_month
        if draft_uncovered is not UNSET:
            field_dict["draftUncovered"] = draft_uncovered

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled")

        day_of_month = d.pop("dayOfMonth", UNSET)

        draft_uncovered = d.pop("draftUncovered", UNSET)

        set_ai_renewal_rule_input = cls(
            enabled=enabled,
            day_of_month=day_of_month,
            draft_uncovered=draft_uncovered,
        )

        set_ai_renewal_rule_input.additional_properties = d
        return set_ai_renewal_rule_input

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
