from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AwsCloudConnectionInit")


@_attrs_define
class AwsCloudConnectionInit:
    """
    Attributes:
        connection_id (Union[Unset, str]):
        platform_aws_account_id (Union[Unset, str]):
        external_id (Union[Unset, str]):
        cloud_formation_template_url (Union[Unset, str]):
    """

    connection_id: Union[Unset, str] = UNSET
    platform_aws_account_id: Union[Unset, str] = UNSET
    external_id: Union[Unset, str] = UNSET
    cloud_formation_template_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_id = self.connection_id

        platform_aws_account_id = self.platform_aws_account_id

        external_id = self.external_id

        cloud_formation_template_url = self.cloud_formation_template_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connection_id is not UNSET:
            field_dict["connectionId"] = connection_id
        if platform_aws_account_id is not UNSET:
            field_dict["platformAwsAccountId"] = platform_aws_account_id
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if cloud_formation_template_url is not UNSET:
            field_dict["cloudFormationTemplateUrl"] = cloud_formation_template_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        connection_id = d.pop("connectionId", UNSET)

        platform_aws_account_id = d.pop("platformAwsAccountId", UNSET)

        external_id = d.pop("externalId", UNSET)

        cloud_formation_template_url = d.pop("cloudFormationTemplateUrl", UNSET)

        aws_cloud_connection_init = cls(
            connection_id=connection_id,
            platform_aws_account_id=platform_aws_account_id,
            external_id=external_id,
            cloud_formation_template_url=cloud_formation_template_url,
        )

        aws_cloud_connection_init.additional_properties = d
        return aws_cloud_connection_init

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
