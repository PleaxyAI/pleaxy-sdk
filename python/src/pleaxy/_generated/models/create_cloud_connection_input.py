from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_cloud_connection_input_data_sources_item import (
    CreateCloudConnectionInputDataSourcesItem,
    check_create_cloud_connection_input_data_sources_item,
)
from ..models.create_cloud_connection_input_oci_home_region import (
    CreateCloudConnectionInputOciHomeRegion,
    check_create_cloud_connection_input_oci_home_region,
)
from ..models.create_cloud_connection_input_provider import (
    CreateCloudConnectionInputProvider,
    check_create_cloud_connection_input_provider,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateCloudConnectionInput")


@_attrs_define
class CreateCloudConnectionInput:
    """
    Attributes:
        provider (CreateCloudConnectionInputProvider):
        account_label (str):
        detail (Union[Unset, str]): Buyer-typed account identifier for a demo (simulated) connection - required for
            azure, optional for gcp/oci. Ignored by a real connector: AWS derives the account ID from AssumeRole, GCP the
            billing account ID from the export, OCI shows the verified tenancy.
        role_arn (Union[Unset, str]): AWS only, required - the IAM Role ARN the buyer created in their own account (via
            the CloudFormation/CDK/CLI script from POST .../cloud-connections/aws/init) and pasted back here.
        aws_connection_id (Union[Unset, str]): AWS only, required - the connectionId returned by POST .../cloud-
            connections/aws/init, linking this verify call back to the externalId generated server-side for that pending
            connection. Never the externalId itself - that's looked up server-side, never trusted from the client.
        gcp_connection_id (Union[Unset, str]): GCP only, when its connector is on - the connectionId returned by POST
            .../cloud-connections/gcp/init. The binding itself is looked up server-side, never taken from the client.
        gcp_project_number (Union[Unset, str]): GCP only - the export project's number (digits).
        gcp_service_account_email (Union[Unset, str]): GCP only - the service account the setup script created, in the
            export project.
        gcp_export_table (Union[Unset, str]): GCP only - project.dataset.gcp_billing_export_v1_XXXXXX_XXXXXX_XXXXXX
            (standard usage cost export).
        oci_connection_id (Union[Unset, str]): OCI only, when its connector is on - the connectionId returned by POST
            .../cloud-connections/oci/init. The key pair is looked up server-side, never taken from the client.
        oci_tenancy_ocid (Union[Unset, str]): OCI only - the tenancy OCID (ocid1.tenancy.oc1..…).
        oci_user_ocid (Union[Unset, str]): OCI only - the OCID of the pleaxy-billing user the setup script created
            (ocid1.user.oc1..…).
        oci_home_region (Union[Unset, CreateCloudConnectionInputOciHomeRegion]): OCI only - the tenancy's home region,
            one of the regions POST .../oci/init lists.
        azure_connection_id (Union[Unset, str]): Azure only, when its connector is on - the connectionId returned by
            POST .../cloud-connections/azure/init. The audience is looked up server-side, never taken from the client.
        azure_billing_account_id (Union[Unset, str]): Azure only - the billing account of the billing profile picked
            from POST .../azure/discover (<guid>:<guid>_YYYY-MM-DD).
        azure_billing_profile_id (Union[Unset, str]): Azure only - the billing profile picked from POST
            .../azure/discover.
        azure_tenant_id (Union[Unset, str]): Not accepted here: verify uses only the tenant ID that POST
            .../azure/discover proved. Declared so that a request carrying it is refused (400) rather than silently
            stripped.
        azure_client_id (Union[Unset, str]): Not accepted here, like azureTenantId: verify uses only the app (client) ID
            discover proved.
        supplier_contact_email (Union[Unset, str]):
        data_sources (Union[Unset, List[CreateCloudConnectionInputDataSourcesItem]]): What Pleaxy may read through this
            connection: `invoices` (finalized invoices) and/or `current_cost` (month-to-date cost). Omitted: both. Pleaxy
            never calls the provider for a source left out, including on a manual sync - some providers bill the customer
            per request for current-period cost (AWS Cost Explorer).
    """

    provider: CreateCloudConnectionInputProvider
    account_label: str
    detail: Union[Unset, str] = UNSET
    role_arn: Union[Unset, str] = UNSET
    aws_connection_id: Union[Unset, str] = UNSET
    gcp_connection_id: Union[Unset, str] = UNSET
    gcp_project_number: Union[Unset, str] = UNSET
    gcp_service_account_email: Union[Unset, str] = UNSET
    gcp_export_table: Union[Unset, str] = UNSET
    oci_connection_id: Union[Unset, str] = UNSET
    oci_tenancy_ocid: Union[Unset, str] = UNSET
    oci_user_ocid: Union[Unset, str] = UNSET
    oci_home_region: Union[Unset, CreateCloudConnectionInputOciHomeRegion] = UNSET
    azure_connection_id: Union[Unset, str] = UNSET
    azure_billing_account_id: Union[Unset, str] = UNSET
    azure_billing_profile_id: Union[Unset, str] = UNSET
    azure_tenant_id: Union[Unset, str] = UNSET
    azure_client_id: Union[Unset, str] = UNSET
    supplier_contact_email: Union[Unset, str] = UNSET
    data_sources: Union[Unset, List[CreateCloudConnectionInputDataSourcesItem]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        provider: str = self.provider

        account_label = self.account_label

        detail = self.detail

        role_arn = self.role_arn

        aws_connection_id = self.aws_connection_id

        gcp_connection_id = self.gcp_connection_id

        gcp_project_number = self.gcp_project_number

        gcp_service_account_email = self.gcp_service_account_email

        gcp_export_table = self.gcp_export_table

        oci_connection_id = self.oci_connection_id

        oci_tenancy_ocid = self.oci_tenancy_ocid

        oci_user_ocid = self.oci_user_ocid

        oci_home_region: Union[Unset, str] = UNSET
        if not isinstance(self.oci_home_region, Unset):
            oci_home_region = self.oci_home_region

        azure_connection_id = self.azure_connection_id

        azure_billing_account_id = self.azure_billing_account_id

        azure_billing_profile_id = self.azure_billing_profile_id

        azure_tenant_id = self.azure_tenant_id

        azure_client_id = self.azure_client_id

        supplier_contact_email = self.supplier_contact_email

        data_sources: Union[Unset, List[str]] = UNSET
        if not isinstance(self.data_sources, Unset):
            data_sources = []
            for data_sources_item_data in self.data_sources:
                data_sources_item: str = data_sources_item_data
                data_sources.append(data_sources_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "accountLabel": account_label,
            }
        )
        if detail is not UNSET:
            field_dict["detail"] = detail
        if role_arn is not UNSET:
            field_dict["roleArn"] = role_arn
        if aws_connection_id is not UNSET:
            field_dict["awsConnectionId"] = aws_connection_id
        if gcp_connection_id is not UNSET:
            field_dict["gcpConnectionId"] = gcp_connection_id
        if gcp_project_number is not UNSET:
            field_dict["gcpProjectNumber"] = gcp_project_number
        if gcp_service_account_email is not UNSET:
            field_dict["gcpServiceAccountEmail"] = gcp_service_account_email
        if gcp_export_table is not UNSET:
            field_dict["gcpExportTable"] = gcp_export_table
        if oci_connection_id is not UNSET:
            field_dict["ociConnectionId"] = oci_connection_id
        if oci_tenancy_ocid is not UNSET:
            field_dict["ociTenancyOcid"] = oci_tenancy_ocid
        if oci_user_ocid is not UNSET:
            field_dict["ociUserOcid"] = oci_user_ocid
        if oci_home_region is not UNSET:
            field_dict["ociHomeRegion"] = oci_home_region
        if azure_connection_id is not UNSET:
            field_dict["azureConnectionId"] = azure_connection_id
        if azure_billing_account_id is not UNSET:
            field_dict["azureBillingAccountId"] = azure_billing_account_id
        if azure_billing_profile_id is not UNSET:
            field_dict["azureBillingProfileId"] = azure_billing_profile_id
        if azure_tenant_id is not UNSET:
            field_dict["azureTenantId"] = azure_tenant_id
        if azure_client_id is not UNSET:
            field_dict["azureClientId"] = azure_client_id
        if supplier_contact_email is not UNSET:
            field_dict["supplierContactEmail"] = supplier_contact_email
        if data_sources is not UNSET:
            field_dict["dataSources"] = data_sources

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        provider = check_create_cloud_connection_input_provider(d.pop("provider"))

        account_label = d.pop("accountLabel")

        detail = d.pop("detail", UNSET)

        role_arn = d.pop("roleArn", UNSET)

        aws_connection_id = d.pop("awsConnectionId", UNSET)

        gcp_connection_id = d.pop("gcpConnectionId", UNSET)

        gcp_project_number = d.pop("gcpProjectNumber", UNSET)

        gcp_service_account_email = d.pop("gcpServiceAccountEmail", UNSET)

        gcp_export_table = d.pop("gcpExportTable", UNSET)

        oci_connection_id = d.pop("ociConnectionId", UNSET)

        oci_tenancy_ocid = d.pop("ociTenancyOcid", UNSET)

        oci_user_ocid = d.pop("ociUserOcid", UNSET)

        _oci_home_region = d.pop("ociHomeRegion", UNSET)
        oci_home_region: Union[Unset, CreateCloudConnectionInputOciHomeRegion]
        if isinstance(_oci_home_region, Unset):
            oci_home_region = UNSET
        else:
            oci_home_region = check_create_cloud_connection_input_oci_home_region(
                _oci_home_region
            )

        azure_connection_id = d.pop("azureConnectionId", UNSET)

        azure_billing_account_id = d.pop("azureBillingAccountId", UNSET)

        azure_billing_profile_id = d.pop("azureBillingProfileId", UNSET)

        azure_tenant_id = d.pop("azureTenantId", UNSET)

        azure_client_id = d.pop("azureClientId", UNSET)

        supplier_contact_email = d.pop("supplierContactEmail", UNSET)

        data_sources = []
        _data_sources = d.pop("dataSources", UNSET)
        for data_sources_item_data in _data_sources or []:
            data_sources_item = check_create_cloud_connection_input_data_sources_item(
                data_sources_item_data
            )

            data_sources.append(data_sources_item)

        create_cloud_connection_input = cls(
            provider=provider,
            account_label=account_label,
            detail=detail,
            role_arn=role_arn,
            aws_connection_id=aws_connection_id,
            gcp_connection_id=gcp_connection_id,
            gcp_project_number=gcp_project_number,
            gcp_service_account_email=gcp_service_account_email,
            gcp_export_table=gcp_export_table,
            oci_connection_id=oci_connection_id,
            oci_tenancy_ocid=oci_tenancy_ocid,
            oci_user_ocid=oci_user_ocid,
            oci_home_region=oci_home_region,
            azure_connection_id=azure_connection_id,
            azure_billing_account_id=azure_billing_account_id,
            azure_billing_profile_id=azure_billing_profile_id,
            azure_tenant_id=azure_tenant_id,
            azure_client_id=azure_client_id,
            supplier_contact_email=supplier_contact_email,
            data_sources=data_sources,
        )

        create_cloud_connection_input.additional_properties = d
        return create_cloud_connection_input

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
