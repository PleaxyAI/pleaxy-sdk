from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AiProviderZoom")


@_attrs_define
class AiProviderZoom:
    """
    Attributes:
        account_id (Union[Unset, str]):
        client_id (Union[Unset, str]):
    """

    account_id: Union[Unset, str] = UNSET
    client_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id

        client_id = self.client_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if client_id is not UNSET:
            field_dict["clientId"] = client_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_id = d.pop("accountId", UNSET)

        client_id = d.pop("clientId", UNSET)

        ai_provider_zoom = cls(
            account_id=account_id,
            client_id=client_id,
        )

        ai_provider_zoom.additional_properties = d
        return ai_provider_zoom

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
