from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetAiLimitCredentialInput")


@_attrs_define
class SetAiLimitCredentialInput:
    """
    Attributes:
        role_arn (Union[Unset, str]): AWS: the limits role the setup script created (budgets only), never the read-only
            billing role.
        execution_role_arn (Union[Unset, str]): AWS, for a ceiling that stops spend: the budget action's execution role
            (trusting budgets.amazonaws.com).
        deny_policy_arn (Union[Unset, str]): AWS: the deny policy the budget action attaches at 100%.
        role_names (Union[Unset, List[str]]): AWS: the roles (names, not ARNs) the deny policy is attached to, e.g. the
            ones your apps call Bedrock with.
        service_account_email (Union[Unset, str]): Google Cloud: the limits service account (Billing Account Costs
            Manager, plus spend caps where wanted).
        client_id (Union[Unset, str]): Azure: the limits app registration's client id (Cost Management Contributor on
            the billing profile).
        key (Union[Unset, str]): OpenAI and Anthropic: a separate admin key for the limits, never the read key. Stored
            encrypted, never returned.
        notify_email (Union[Unset, str]): Who the provider emails when a ceiling is reached (AWS budget actions, Azure
            budgets).
    """

    role_arn: Union[Unset, str] = UNSET
    execution_role_arn: Union[Unset, str] = UNSET
    deny_policy_arn: Union[Unset, str] = UNSET
    role_names: Union[Unset, List[str]] = UNSET
    service_account_email: Union[Unset, str] = UNSET
    client_id: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    notify_email: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        role_arn = self.role_arn

        execution_role_arn = self.execution_role_arn

        deny_policy_arn = self.deny_policy_arn

        role_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.role_names, Unset):
            role_names = self.role_names

        service_account_email = self.service_account_email

        client_id = self.client_id

        key = self.key

        notify_email = self.notify_email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if role_arn is not UNSET:
            field_dict["roleArn"] = role_arn
        if execution_role_arn is not UNSET:
            field_dict["executionRoleArn"] = execution_role_arn
        if deny_policy_arn is not UNSET:
            field_dict["denyPolicyArn"] = deny_policy_arn
        if role_names is not UNSET:
            field_dict["roleNames"] = role_names
        if service_account_email is not UNSET:
            field_dict["serviceAccountEmail"] = service_account_email
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if key is not UNSET:
            field_dict["key"] = key
        if notify_email is not UNSET:
            field_dict["notifyEmail"] = notify_email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        role_arn = d.pop("roleArn", UNSET)

        execution_role_arn = d.pop("executionRoleArn", UNSET)

        deny_policy_arn = d.pop("denyPolicyArn", UNSET)

        role_names = cast(List[str], d.pop("roleNames", UNSET))

        service_account_email = d.pop("serviceAccountEmail", UNSET)

        client_id = d.pop("clientId", UNSET)

        key = d.pop("key", UNSET)

        notify_email = d.pop("notifyEmail", UNSET)

        set_ai_limit_credential_input = cls(
            role_arn=role_arn,
            execution_role_arn=execution_role_arn,
            deny_policy_arn=deny_policy_arn,
            role_names=role_names,
            service_account_email=service_account_email,
            client_id=client_id,
            key=key,
            notify_email=notify_email,
        )

        set_ai_limit_credential_input.additional_properties = d
        return set_ai_limit_credential_input

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
