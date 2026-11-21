from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AiProviderTwilio")


@_attrs_define
class AiProviderTwilio:
    """
    Attributes:
        account_sid (Union[Unset, str]):
        key_sid (Union[Unset, str]):
    """

    account_sid: Union[Unset, str] = UNSET
    key_sid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_sid = self.account_sid

        key_sid = self.key_sid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_sid is not UNSET:
            field_dict["accountSid"] = account_sid
        if key_sid is not UNSET:
            field_dict["keySid"] = key_sid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_sid = d.pop("accountSid", UNSET)

        key_sid = d.pop("keySid", UNSET)

        ai_provider_twilio = cls(
            account_sid=account_sid,
            key_sid=key_sid,
        )

        ai_provider_twilio.additional_properties = d
        return ai_provider_twilio

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
