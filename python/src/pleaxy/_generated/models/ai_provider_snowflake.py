from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AiProviderSnowflake")


@_attrs_define
class AiProviderSnowflake:
    """
    Attributes:
        account (Union[Unset, str]):
        user (Union[Unset, str]):
        warehouse (Union[Unset, str]):
        role (Union[Unset, str]):
        public_key_pem (Union[Unset, str]):
        public_key_fingerprint (Union[Unset, str]):
    """

    account: Union[Unset, str] = UNSET
    user: Union[Unset, str] = UNSET
    warehouse: Union[Unset, str] = UNSET
    role: Union[Unset, str] = UNSET
    public_key_pem: Union[Unset, str] = UNSET
    public_key_fingerprint: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account = self.account

        user = self.user

        warehouse = self.warehouse

        role = self.role

        public_key_pem = self.public_key_pem

        public_key_fingerprint = self.public_key_fingerprint

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account is not UNSET:
            field_dict["account"] = account
        if user is not UNSET:
            field_dict["user"] = user
        if warehouse is not UNSET:
            field_dict["warehouse"] = warehouse
        if role is not UNSET:
            field_dict["role"] = role
        if public_key_pem is not UNSET:
            field_dict["publicKeyPem"] = public_key_pem
        if public_key_fingerprint is not UNSET:
            field_dict["publicKeyFingerprint"] = public_key_fingerprint

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account = d.pop("account", UNSET)

        user = d.pop("user", UNSET)

        warehouse = d.pop("warehouse", UNSET)

        role = d.pop("role", UNSET)

        public_key_pem = d.pop("publicKeyPem", UNSET)

        public_key_fingerprint = d.pop("publicKeyFingerprint", UNSET)

        ai_provider_snowflake = cls(
            account=account,
            user=user,
            warehouse=warehouse,
            role=role,
            public_key_pem=public_key_pem,
            public_key_fingerprint=public_key_fingerprint,
        )

        ai_provider_snowflake.additional_properties = d
        return ai_provider_snowflake

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
