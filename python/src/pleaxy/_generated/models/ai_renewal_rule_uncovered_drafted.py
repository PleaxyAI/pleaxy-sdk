from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AiRenewalRuleUncoveredDrafted")


@_attrs_define
class AiRenewalRuleUncoveredDrafted:
    """
    Attributes:
        period (Union[Unset, str]):
        invoicer_ids (Union[Unset, List[str]]):
    """

    period: Union[Unset, str] = UNSET
    invoicer_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        period = self.period

        invoicer_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.invoicer_ids, Unset):
            invoicer_ids = self.invoicer_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if period is not UNSET:
            field_dict["period"] = period
        if invoicer_ids is not UNSET:
            field_dict["invoicerIds"] = invoicer_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        period = d.pop("period", UNSET)

        invoicer_ids = cast(List[str], d.pop("invoicerIds", UNSET))

        ai_renewal_rule_uncovered_drafted = cls(
            period=period,
            invoicer_ids=invoicer_ids,
        )

        ai_renewal_rule_uncovered_drafted.additional_properties = d
        return ai_renewal_rule_uncovered_drafted

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
