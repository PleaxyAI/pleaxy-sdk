from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FocusSourceViewAzure")


@_attrs_define
class FocusSourceViewAzure:
    """
    Attributes:
        storage_account (Union[Unset, str]):
        container (Union[Unset, str]):
        directory (Union[Unset, str]):
    """

    storage_account: Union[Unset, str] = UNSET
    container: Union[Unset, str] = UNSET
    directory: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        storage_account = self.storage_account

        container = self.container

        directory = self.directory

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if storage_account is not UNSET:
            field_dict["storageAccount"] = storage_account
        if container is not UNSET:
            field_dict["container"] = container
        if directory is not UNSET:
            field_dict["directory"] = directory

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        storage_account = d.pop("storageAccount", UNSET)

        container = d.pop("container", UNSET)

        directory = d.pop("directory", UNSET)

        focus_source_view_azure = cls(
            storage_account=storage_account,
            container=container,
            directory=directory,
        )

        focus_source_view_azure.additional_properties = d
        return focus_source_view_azure

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
