from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_renewal_rule_last_run import AiRenewalRuleLastRun
    from ..models.ai_renewal_rule_last_uncovered_run import (
        AiRenewalRuleLastUncoveredRun,
    )
    from ..models.ai_renewal_rule_uncovered_drafted import AiRenewalRuleUncoveredDrafted


T = TypeVar("T", bound="AiRenewalRule")


@_attrs_define
class AiRenewalRule:
    """
    Attributes:
        enabled (Union[Unset, bool]):
        day_of_month (Union[Unset, float]):
        owner_sub (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        drafted_for (Union[Unset, str]):
        last_run (Union[Unset, AiRenewalRuleLastRun]):
        draft_uncovered (Union[Unset, bool]):
        uncovered_checked_on (Union[Unset, str]):
        uncovered_drafted (Union[Unset, AiRenewalRuleUncoveredDrafted]):
        last_uncovered_run (Union[Unset, AiRenewalRuleLastUncoveredRun]):
    """

    enabled: Union[Unset, bool] = UNSET
    day_of_month: Union[Unset, float] = UNSET
    owner_sub: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    drafted_for: Union[Unset, str] = UNSET
    last_run: Union[Unset, "AiRenewalRuleLastRun"] = UNSET
    draft_uncovered: Union[Unset, bool] = UNSET
    uncovered_checked_on: Union[Unset, str] = UNSET
    uncovered_drafted: Union[Unset, "AiRenewalRuleUncoveredDrafted"] = UNSET
    last_uncovered_run: Union[Unset, "AiRenewalRuleLastUncoveredRun"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled

        day_of_month = self.day_of_month

        owner_sub = self.owner_sub

        updated_at = self.updated_at

        drafted_for = self.drafted_for

        last_run: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.last_run, Unset):
            last_run = self.last_run.to_dict()

        draft_uncovered = self.draft_uncovered

        uncovered_checked_on = self.uncovered_checked_on

        uncovered_drafted: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.uncovered_drafted, Unset):
            uncovered_drafted = self.uncovered_drafted.to_dict()

        last_uncovered_run: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.last_uncovered_run, Unset):
            last_uncovered_run = self.last_uncovered_run.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if day_of_month is not UNSET:
            field_dict["dayOfMonth"] = day_of_month
        if owner_sub is not UNSET:
            field_dict["ownerSub"] = owner_sub
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if drafted_for is not UNSET:
            field_dict["draftedFor"] = drafted_for
        if last_run is not UNSET:
            field_dict["lastRun"] = last_run
        if draft_uncovered is not UNSET:
            field_dict["draftUncovered"] = draft_uncovered
        if uncovered_checked_on is not UNSET:
            field_dict["uncoveredCheckedOn"] = uncovered_checked_on
        if uncovered_drafted is not UNSET:
            field_dict["uncoveredDrafted"] = uncovered_drafted
        if last_uncovered_run is not UNSET:
            field_dict["lastUncoveredRun"] = last_uncovered_run

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ai_renewal_rule_last_run import AiRenewalRuleLastRun
        from ..models.ai_renewal_rule_last_uncovered_run import (
            AiRenewalRuleLastUncoveredRun,
        )
        from ..models.ai_renewal_rule_uncovered_drafted import (
            AiRenewalRuleUncoveredDrafted,
        )

        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        day_of_month = d.pop("dayOfMonth", UNSET)

        owner_sub = d.pop("ownerSub", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        drafted_for = d.pop("draftedFor", UNSET)

        _last_run = d.pop("lastRun", UNSET)
        last_run: Union[Unset, AiRenewalRuleLastRun]
        if isinstance(_last_run, Unset):
            last_run = UNSET
        else:
            last_run = AiRenewalRuleLastRun.from_dict(_last_run)

        draft_uncovered = d.pop("draftUncovered", UNSET)

        uncovered_checked_on = d.pop("uncoveredCheckedOn", UNSET)

        _uncovered_drafted = d.pop("uncoveredDrafted", UNSET)
        uncovered_drafted: Union[Unset, AiRenewalRuleUncoveredDrafted]
        if isinstance(_uncovered_drafted, Unset):
            uncovered_drafted = UNSET
        else:
            uncovered_drafted = AiRenewalRuleUncoveredDrafted.from_dict(
                _uncovered_drafted
            )

        _last_uncovered_run = d.pop("lastUncoveredRun", UNSET)
        last_uncovered_run: Union[Unset, AiRenewalRuleLastUncoveredRun]
        if isinstance(_last_uncovered_run, Unset):
            last_uncovered_run = UNSET
        else:
            last_uncovered_run = AiRenewalRuleLastUncoveredRun.from_dict(
                _last_uncovered_run
            )

        ai_renewal_rule = cls(
            enabled=enabled,
            day_of_month=day_of_month,
            owner_sub=owner_sub,
            updated_at=updated_at,
            drafted_for=drafted_for,
            last_run=last_run,
            draft_uncovered=draft_uncovered,
            uncovered_checked_on=uncovered_checked_on,
            uncovered_drafted=uncovered_drafted,
            last_uncovered_run=last_uncovered_run,
        )

        ai_renewal_rule.additional_properties = d
        return ai_renewal_rule

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
