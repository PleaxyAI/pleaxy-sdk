from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BillingSummaryAwsMarketplace")


@_attrs_define
class BillingSummaryAwsMarketplace:
    """
    Attributes:
        regions_covered (Union[Unset, float]):
        ends_at (Union[Unset, str]):
    """

    regions_covered: Union[Unset, float] = UNSET
    ends_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        regions_covered = self.regions_covered

        ends_at = self.ends_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if regions_covered is not UNSET:
            field_dict["regionsCovered"] = regions_covered
        if ends_at is not UNSET:
            field_dict["endsAt"] = ends_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        regions_covered = d.pop("regionsCovered", UNSET)

        ends_at = d.pop("endsAt", UNSET)

        billing_summary_aws_marketplace = cls(
            regions_covered=regions_covered,
            ends_at=ends_at,
        )

        billing_summary_aws_marketplace.additional_properties = d
        return billing_summary_aws_marketplace

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
