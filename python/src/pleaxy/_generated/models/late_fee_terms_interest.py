from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.late_fee_terms_interest_per import (
    LateFeeTermsInterestPer,
    check_late_fee_terms_interest_per,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="LateFeeTermsInterest")


@_attrs_define
class LateFeeTermsInterest:
    """
    Attributes:
        rate_pct (Union[Unset, float]):
        per (Union[Unset, LateFeeTermsInterestPer]):
    """

    rate_pct: Union[Unset, float] = UNSET
    per: Union[Unset, LateFeeTermsInterestPer] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rate_pct = self.rate_pct

        per: Union[Unset, str] = UNSET
        if not isinstance(self.per, Unset):
            per = self.per

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rate_pct is not UNSET:
            field_dict["ratePct"] = rate_pct
        if per is not UNSET:
            field_dict["per"] = per

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        rate_pct = d.pop("ratePct", UNSET)

        _per = d.pop("per", UNSET)
        per: Union[Unset, LateFeeTermsInterestPer]
        if isinstance(_per, Unset):
            per = UNSET
        else:
            per = check_late_fee_terms_interest_per(_per)

        late_fee_terms_interest = cls(
            rate_pct=rate_pct,
            per=per,
        )

        late_fee_terms_interest.additional_properties = d
        return late_fee_terms_interest

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
