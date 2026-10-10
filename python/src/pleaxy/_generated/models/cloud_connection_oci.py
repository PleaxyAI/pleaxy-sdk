from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudConnectionOci")


@_attrs_define
class CloudConnectionOci:
    """
    Attributes:
        home_region (Union[Unset, str]):
        key_fingerprint (Union[Unset, str]):
    """

    home_region: Union[Unset, str] = UNSET
    key_fingerprint: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        home_region = self.home_region

        key_fingerprint = self.key_fingerprint

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if home_region is not UNSET:
            field_dict["homeRegion"] = home_region
        if key_fingerprint is not UNSET:
            field_dict["keyFingerprint"] = key_fingerprint

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        home_region = d.pop("homeRegion", UNSET)

        key_fingerprint = d.pop("keyFingerprint", UNSET)

        cloud_connection_oci = cls(
            home_region=home_region,
            key_fingerprint=key_fingerprint,
        )

        cloud_connection_oci.additional_properties = d
        return cloud_connection_oci

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
