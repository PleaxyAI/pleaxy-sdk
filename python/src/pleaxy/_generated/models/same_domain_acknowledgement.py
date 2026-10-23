from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SameDomainAcknowledgement")


@_attrs_define
class SameDomainAcknowledgement:
    """
    Attributes:
        domain (Union[Unset, str]):
        company_ids (Union[Unset, List[str]]):
        at (Union[Unset, str]):
    """

    domain: Union[Unset, str] = UNSET
    company_ids: Union[Unset, List[str]] = UNSET
    at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        domain = self.domain

        company_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.company_ids, Unset):
            company_ids = self.company_ids

        at = self.at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if domain is not UNSET:
            field_dict["domain"] = domain
        if company_ids is not UNSET:
            field_dict["companyIds"] = company_ids
        if at is not UNSET:
            field_dict["at"] = at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        domain = d.pop("domain", UNSET)

        company_ids = cast(List[str], d.pop("companyIds", UNSET))

        at = d.pop("at", UNSET)

        same_domain_acknowledgement = cls(
            domain=domain,
            company_ids=company_ids,
            at=at,
        )

        same_domain_acknowledgement.additional_properties = d
        return same_domain_acknowledgement

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
