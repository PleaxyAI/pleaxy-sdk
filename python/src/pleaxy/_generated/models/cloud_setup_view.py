from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cloud_setup_view_state import (
    CloudSetupViewState,
    check_cloud_setup_view_state,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudSetupView")


@_attrs_define
class CloudSetupView:
    """
    Attributes:
        state (Union[Unset, CloudSetupViewState]):
        expires_at (Union[Unset, str]):
    """

    state: Union[Unset, CloudSetupViewState] = UNSET
    expires_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state

        expires_at = self.expires_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _state = d.pop("state", UNSET)
        state: Union[Unset, CloudSetupViewState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = check_cloud_setup_view_state(_state)

        expires_at = d.pop("expiresAt", UNSET)

        cloud_setup_view = cls(
            state=state,
            expires_at=expires_at,
        )

        cloud_setup_view.additional_properties = d
        return cloud_setup_view

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
