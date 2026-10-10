from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudConnectionGcp")


@_attrs_define
class CloudConnectionGcp:
    """
    Attributes:
        billing_account_id (Union[Unset, str]):
        provider_id (Union[Unset, str]):
    """

    billing_account_id: Union[Unset, str] = UNSET
    provider_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        billing_account_id = self.billing_account_id

        provider_id = self.provider_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if billing_account_id is not UNSET:
            field_dict["billingAccountId"] = billing_account_id
        if provider_id is not UNSET:
            field_dict["providerId"] = provider_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        billing_account_id = d.pop("billingAccountId", UNSET)

        provider_id = d.pop("providerId", UNSET)

        cloud_connection_gcp = cls(
            billing_account_id=billing_account_id,
            provider_id=provider_id,
        )

        cloud_connection_gcp.additional_properties = d
        return cloud_connection_gcp

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
