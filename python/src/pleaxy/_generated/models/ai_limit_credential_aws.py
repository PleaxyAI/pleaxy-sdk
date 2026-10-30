from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AiLimitCredentialAws")


@_attrs_define
class AiLimitCredentialAws:
    """
    Attributes:
        role_arn (Union[Unset, str]):
        external_id (Union[Unset, str]):
        execution_role_arn (Union[Unset, str]):
        deny_policy_arn (Union[Unset, str]):
        role_names (Union[Unset, List[str]]):
    """

    role_arn: Union[Unset, str] = UNSET
    external_id: Union[Unset, str] = UNSET
    execution_role_arn: Union[Unset, str] = UNSET
    deny_policy_arn: Union[Unset, str] = UNSET
    role_names: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        role_arn = self.role_arn

        external_id = self.external_id

        execution_role_arn = self.execution_role_arn

        deny_policy_arn = self.deny_policy_arn

        role_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.role_names, Unset):
            role_names = self.role_names

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if role_arn is not UNSET:
            field_dict["roleArn"] = role_arn
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if execution_role_arn is not UNSET:
            field_dict["executionRoleArn"] = execution_role_arn
        if deny_policy_arn is not UNSET:
            field_dict["denyPolicyArn"] = deny_policy_arn
        if role_names is not UNSET:
            field_dict["roleNames"] = role_names

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        role_arn = d.pop("roleArn", UNSET)

        external_id = d.pop("externalId", UNSET)

        execution_role_arn = d.pop("executionRoleArn", UNSET)

        deny_policy_arn = d.pop("denyPolicyArn", UNSET)

        role_names = cast(List[str], d.pop("roleNames", UNSET))

        ai_limit_credential_aws = cls(
            role_arn=role_arn,
            external_id=external_id,
            execution_role_arn=execution_role_arn,
            deny_policy_arn=deny_policy_arn,
            role_names=role_names,
        )

        ai_limit_credential_aws.additional_properties = d
        return ai_limit_credential_aws

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
