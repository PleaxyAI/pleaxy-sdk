from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DiscoverAzureScopesInput")


@_attrs_define
class DiscoverAzureScopesInput:
    """
    Attributes:
        azure_connection_id (str): The connectionId returned by POST .../cloud-connections/azure/init. The audience is
            looked up server-side, never taken from the client.
        azure_tenant_id (str): The Microsoft Entra tenant the app was registered in (GUID).
        azure_client_id (str): The app registration's Application (client) ID (GUID).
        azure_billing_account_id (str): The Microsoft Customer Agreement billing account ID (<guid>:<guid>_YYYY-MM-DD).
            Read directly: an app with only Billing profile reader can't list billing accounts.
        azure_billing_profile_id (str): The billing profile ID the app has Billing profile reader on.
    """

    azure_connection_id: str
    azure_tenant_id: str
    azure_client_id: str
    azure_billing_account_id: str
    azure_billing_profile_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        azure_connection_id = self.azure_connection_id

        azure_tenant_id = self.azure_tenant_id

        azure_client_id = self.azure_client_id

        azure_billing_account_id = self.azure_billing_account_id

        azure_billing_profile_id = self.azure_billing_profile_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "azureConnectionId": azure_connection_id,
                "azureTenantId": azure_tenant_id,
                "azureClientId": azure_client_id,
                "azureBillingAccountId": azure_billing_account_id,
                "azureBillingProfileId": azure_billing_profile_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        azure_connection_id = d.pop("azureConnectionId")

        azure_tenant_id = d.pop("azureTenantId")

        azure_client_id = d.pop("azureClientId")

        azure_billing_account_id = d.pop("azureBillingAccountId")

        azure_billing_profile_id = d.pop("azureBillingProfileId")

        discover_azure_scopes_input = cls(
            azure_connection_id=azure_connection_id,
            azure_tenant_id=azure_tenant_id,
            azure_client_id=azure_client_id,
            azure_billing_account_id=azure_billing_account_id,
            azure_billing_profile_id=azure_billing_profile_id,
        )

        discover_azure_scopes_input.additional_properties = d
        return discover_azure_scopes_input

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
