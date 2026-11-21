from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EarlyPaymentStandingOffer")


@_attrs_define
class EarlyPaymentStandingOffer:
    """
    Attributes:
        percent (Union[Unset, float]):
        days_before_due (Union[Unset, float]):
        updated_at (Union[Unset, str]):
    """

    percent: Union[Unset, float] = UNSET
    days_before_due: Union[Unset, float] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        percent = self.percent

        days_before_due = self.days_before_due

        updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if percent is not UNSET:
            field_dict["percent"] = percent
        if days_before_due is not UNSET:
            field_dict["daysBeforeDue"] = days_before_due
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        percent = d.pop("percent", UNSET)

        days_before_due = d.pop("daysBeforeDue", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        early_payment_standing_offer = cls(
            percent=percent,
            days_before_due=days_before_due,
            updated_at=updated_at,
        )

        early_payment_standing_offer.additional_properties = d
        return early_payment_standing_offer

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
