from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AiLimitCredentialGcp")


@_attrs_define
class AiLimitCredentialGcp:
    """
    Attributes:
        service_account_email (Union[Unset, str]):
    """

    service_account_email: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_account_email = self.service_account_email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_account_email is not UNSET:
            field_dict["serviceAccountEmail"] = service_account_email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        service_account_email = d.pop("serviceAccountEmail", UNSET)

        ai_limit_credential_gcp = cls(
            service_account_email=service_account_email,
        )

        ai_limit_credential_gcp.additional_properties = d
        return ai_limit_credential_gcp

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
