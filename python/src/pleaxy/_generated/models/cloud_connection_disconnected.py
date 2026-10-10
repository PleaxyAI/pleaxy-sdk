from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cloud_connection_disconnected_provider import (
    CloudConnectionDisconnectedProvider,
    check_cloud_connection_disconnected_provider,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudConnectionDisconnected")


@_attrs_define
class CloudConnectionDisconnected:
    """
    Attributes:
        id (str):
        provider (Union[Unset, CloudConnectionDisconnectedProvider]):
        oci_key_fingerprint (Union[Unset, str]):
    """

    id: str
    provider: Union[Unset, CloudConnectionDisconnectedProvider] = UNSET
    oci_key_fingerprint: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        provider: Union[Unset, str] = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider

        oci_key_fingerprint = self.oci_key_fingerprint

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if provider is not UNSET:
            field_dict["provider"] = provider
        if oci_key_fingerprint is not UNSET:
            field_dict["ociKeyFingerprint"] = oci_key_fingerprint

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        _provider = d.pop("provider", UNSET)
        provider: Union[Unset, CloudConnectionDisconnectedProvider]
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = check_cloud_connection_disconnected_provider(_provider)

        oci_key_fingerprint = d.pop("ociKeyFingerprint", UNSET)

        cloud_connection_disconnected = cls(
            id=id,
            provider=provider,
            oci_key_fingerprint=oci_key_fingerprint,
        )

        cloud_connection_disconnected.additional_properties = d
        return cloud_connection_disconnected

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
