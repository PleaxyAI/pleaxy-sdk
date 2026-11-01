from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FocusDestinationSetup")


@_attrs_define
class FocusDestinationSetup:
    """
    Attributes:
        pleaxy_account_id (Union[Unset, str]):
        template_url (Union[Unset, str]):
        role_name (Union[Unset, str]):
        stack_name (Union[Unset, str]):
    """

    pleaxy_account_id: Union[Unset, str] = UNSET
    template_url: Union[Unset, str] = UNSET
    role_name: Union[Unset, str] = UNSET
    stack_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pleaxy_account_id = self.pleaxy_account_id

        template_url = self.template_url

        role_name = self.role_name

        stack_name = self.stack_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pleaxy_account_id is not UNSET:
            field_dict["pleaxyAccountId"] = pleaxy_account_id
        if template_url is not UNSET:
            field_dict["templateUrl"] = template_url
        if role_name is not UNSET:
            field_dict["roleName"] = role_name
        if stack_name is not UNSET:
            field_dict["stackName"] = stack_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pleaxy_account_id = d.pop("pleaxyAccountId", UNSET)

        template_url = d.pop("templateUrl", UNSET)

        role_name = d.pop("roleName", UNSET)

        stack_name = d.pop("stackName", UNSET)

        focus_destination_setup = cls(
            pleaxy_account_id=pleaxy_account_id,
            template_url=template_url,
            role_name=role_name,
            stack_name=stack_name,
        )

        focus_destination_setup.additional_properties = d
        return focus_destination_setup

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
