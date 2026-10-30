from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cloud_connection_data_sources_item import (
    CloudConnectionDataSourcesItem,
    check_cloud_connection_data_sources_item,
)
from ..models.cloud_connection_last_sync_error_code import (
    CloudConnectionLastSyncErrorCode,
    check_cloud_connection_last_sync_error_code,
)
from ..models.cloud_connection_last_sync_status import (
    CloudConnectionLastSyncStatus,
    check_cloud_connection_last_sync_status,
)
from ..models.cloud_connection_provider import (
    CloudConnectionProvider,
    check_cloud_connection_provider,
)
from ..models.cloud_connection_status import (
    CloudConnectionStatus,
    check_cloud_connection_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cloud_ai_sync_state import CloudAiSyncState
    from ..models.cloud_bulk_account_view import CloudBulkAccountView
    from ..models.cloud_connection_azure import CloudConnectionAzure
    from ..models.cloud_connection_billing import CloudConnectionBilling
    from ..models.cloud_connection_gcp import CloudConnectionGcp
    from ..models.cloud_connection_oci import CloudConnectionOci
    from ..models.cloud_setup_view import CloudSetupView


T = TypeVar("T", bound="CloudConnection")


@_attrs_define
class CloudConnection:
    """
    Attributes:
        id (str):
        provider (Union[Unset, CloudConnectionProvider]):
        account_label (Union[Unset, str]):
        detail (Union[Unset, str]):
        spend (Union[Unset, float]):
        status (Union[Unset, CloudConnectionStatus]):
        connected_at (Union[Unset, str]):
        setup (Union[Unset, CloudSetupView]):
        bulk (Union[Unset, CloudBulkAccountView]):
        role_arn (Union[Unset, str]):
        external_id (Union[Unset, str]):
        aws_account_id (Union[Unset, str]):
        last_synced_at (Union[Unset, str]):
        last_sync_status (Union[Unset, CloudConnectionLastSyncStatus]):
        last_sync_error (Union[Unset, str]):
        last_sync_error_code (Union[Unset, CloudConnectionLastSyncErrorCode]):
        ai_sync (Union[Unset, CloudAiSyncState]):
        data_sources (Union[Unset, List[CloudConnectionDataSourcesItem]]):
        billing (Union[Unset, CloudConnectionBilling]):
        gcp (Union[Unset, CloudConnectionGcp]):
        oci (Union[Unset, CloudConnectionOci]):
        azure (Union[Unset, CloudConnectionAzure]):
    """

    id: str
    provider: Union[Unset, CloudConnectionProvider] = UNSET
    account_label: Union[Unset, str] = UNSET
    detail: Union[Unset, str] = UNSET
    spend: Union[Unset, float] = UNSET
    status: Union[Unset, CloudConnectionStatus] = UNSET
    connected_at: Union[Unset, str] = UNSET
    setup: Union[Unset, "CloudSetupView"] = UNSET
    bulk: Union[Unset, "CloudBulkAccountView"] = UNSET
    role_arn: Union[Unset, str] = UNSET
    external_id: Union[Unset, str] = UNSET
    aws_account_id: Union[Unset, str] = UNSET
    last_synced_at: Union[Unset, str] = UNSET
    last_sync_status: Union[Unset, CloudConnectionLastSyncStatus] = UNSET
    last_sync_error: Union[Unset, str] = UNSET
    last_sync_error_code: Union[Unset, CloudConnectionLastSyncErrorCode] = UNSET
    ai_sync: Union[Unset, "CloudAiSyncState"] = UNSET
    data_sources: Union[Unset, List[CloudConnectionDataSourcesItem]] = UNSET
    billing: Union[Unset, "CloudConnectionBilling"] = UNSET
    gcp: Union[Unset, "CloudConnectionGcp"] = UNSET
    oci: Union[Unset, "CloudConnectionOci"] = UNSET
    azure: Union[Unset, "CloudConnectionAzure"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        provider: Union[Unset, str] = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider

        account_label = self.account_label

        detail = self.detail

        spend = self.spend

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        connected_at = self.connected_at

        setup: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.setup, Unset):
            setup = self.setup.to_dict()

        bulk: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bulk, Unset):
            bulk = self.bulk.to_dict()

        role_arn = self.role_arn

        external_id = self.external_id

        aws_account_id = self.aws_account_id

        last_synced_at = self.last_synced_at

        last_sync_status: Union[Unset, str] = UNSET
        if not isinstance(self.last_sync_status, Unset):
            last_sync_status = self.last_sync_status

        last_sync_error = self.last_sync_error

        last_sync_error_code: Union[Unset, str] = UNSET
        if not isinstance(self.last_sync_error_code, Unset):
            last_sync_error_code = self.last_sync_error_code

        ai_sync: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ai_sync, Unset):
            ai_sync = self.ai_sync.to_dict()

        data_sources: Union[Unset, List[str]] = UNSET
        if not isinstance(self.data_sources, Unset):
            data_sources = []
            for data_sources_item_data in self.data_sources:
                data_sources_item: str = data_sources_item_data
                data_sources.append(data_sources_item)

        billing: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.billing, Unset):
            billing = self.billing.to_dict()

        gcp: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.gcp, Unset):
            gcp = self.gcp.to_dict()

        oci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.oci, Unset):
            oci = self.oci.to_dict()

        azure: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.azure, Unset):
            azure = self.azure.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if provider is not UNSET:
            field_dict["provider"] = provider
        if account_label is not UNSET:
            field_dict["accountLabel"] = account_label
        if detail is not UNSET:
            field_dict["detail"] = detail
        if spend is not UNSET:
            field_dict["spend"] = spend
        if status is not UNSET:
            field_dict["status"] = status
        if connected_at is not UNSET:
            field_dict["connectedAt"] = connected_at
        if setup is not UNSET:
            field_dict["setup"] = setup
        if bulk is not UNSET:
            field_dict["bulk"] = bulk
        if role_arn is not UNSET:
            field_dict["roleArn"] = role_arn
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if aws_account_id is not UNSET:
            field_dict["awsAccountId"] = aws_account_id
        if last_synced_at is not UNSET:
            field_dict["lastSyncedAt"] = last_synced_at
        if last_sync_status is not UNSET:
            field_dict["lastSyncStatus"] = last_sync_status
        if last_sync_error is not UNSET:
            field_dict["lastSyncError"] = last_sync_error
        if last_sync_error_code is not UNSET:
            field_dict["lastSyncErrorCode"] = last_sync_error_code
        if ai_sync is not UNSET:
            field_dict["aiSync"] = ai_sync
        if data_sources is not UNSET:
            field_dict["dataSources"] = data_sources
        if billing is not UNSET:
            field_dict["billing"] = billing
        if gcp is not UNSET:
            field_dict["gcp"] = gcp
        if oci is not UNSET:
            field_dict["oci"] = oci
        if azure is not UNSET:
            field_dict["azure"] = azure

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cloud_ai_sync_state import CloudAiSyncState
        from ..models.cloud_bulk_account_view import CloudBulkAccountView
        from ..models.cloud_connection_azure import CloudConnectionAzure
        from ..models.cloud_connection_billing import CloudConnectionBilling
        from ..models.cloud_connection_gcp import CloudConnectionGcp
        from ..models.cloud_connection_oci import CloudConnectionOci
        from ..models.cloud_setup_view import CloudSetupView

        d = src_dict.copy()
        id = d.pop("id")

        _provider = d.pop("provider", UNSET)
        provider: Union[Unset, CloudConnectionProvider]
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = check_cloud_connection_provider(_provider)

        account_label = d.pop("accountLabel", UNSET)

        detail = d.pop("detail", UNSET)

        spend = d.pop("spend", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CloudConnectionStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_cloud_connection_status(_status)

        connected_at = d.pop("connectedAt", UNSET)

        _setup = d.pop("setup", UNSET)
        setup: Union[Unset, CloudSetupView]
        if isinstance(_setup, Unset):
            setup = UNSET
        else:
            setup = CloudSetupView.from_dict(_setup)

        _bulk = d.pop("bulk", UNSET)
        bulk: Union[Unset, CloudBulkAccountView]
        if isinstance(_bulk, Unset):
            bulk = UNSET
        else:
            bulk = CloudBulkAccountView.from_dict(_bulk)

        role_arn = d.pop("roleArn", UNSET)

        external_id = d.pop("externalId", UNSET)

        aws_account_id = d.pop("awsAccountId", UNSET)

        last_synced_at = d.pop("lastSyncedAt", UNSET)

        _last_sync_status = d.pop("lastSyncStatus", UNSET)
        last_sync_status: Union[Unset, CloudConnectionLastSyncStatus]
        if isinstance(_last_sync_status, Unset):
            last_sync_status = UNSET
        else:
            last_sync_status = check_cloud_connection_last_sync_status(
                _last_sync_status
            )

        last_sync_error = d.pop("lastSyncError", UNSET)

        _last_sync_error_code = d.pop("lastSyncErrorCode", UNSET)
        last_sync_error_code: Union[Unset, CloudConnectionLastSyncErrorCode]
        if isinstance(_last_sync_error_code, Unset):
            last_sync_error_code = UNSET
        else:
            last_sync_error_code = check_cloud_connection_last_sync_error_code(
                _last_sync_error_code
            )

        _ai_sync = d.pop("aiSync", UNSET)
        ai_sync: Union[Unset, CloudAiSyncState]
        if isinstance(_ai_sync, Unset):
            ai_sync = UNSET
        else:
            ai_sync = CloudAiSyncState.from_dict(_ai_sync)

        data_sources = []
        _data_sources = d.pop("dataSources", UNSET)
        for data_sources_item_data in _data_sources or []:
            data_sources_item = check_cloud_connection_data_sources_item(
                data_sources_item_data
            )

            data_sources.append(data_sources_item)

        _billing = d.pop("billing", UNSET)
        billing: Union[Unset, CloudConnectionBilling]
        if isinstance(_billing, Unset):
            billing = UNSET
        else:
            billing = CloudConnectionBilling.from_dict(_billing)

        _gcp = d.pop("gcp", UNSET)
        gcp: Union[Unset, CloudConnectionGcp]
        if isinstance(_gcp, Unset):
            gcp = UNSET
        else:
            gcp = CloudConnectionGcp.from_dict(_gcp)

        _oci = d.pop("oci", UNSET)
        oci: Union[Unset, CloudConnectionOci]
        if isinstance(_oci, Unset):
            oci = UNSET
        else:
            oci = CloudConnectionOci.from_dict(_oci)

        _azure = d.pop("azure", UNSET)
        azure: Union[Unset, CloudConnectionAzure]
        if isinstance(_azure, Unset):
            azure = UNSET
        else:
            azure = CloudConnectionAzure.from_dict(_azure)

        cloud_connection = cls(
            id=id,
            provider=provider,
            account_label=account_label,
            detail=detail,
            spend=spend,
            status=status,
            connected_at=connected_at,
            setup=setup,
            bulk=bulk,
            role_arn=role_arn,
            external_id=external_id,
            aws_account_id=aws_account_id,
            last_synced_at=last_synced_at,
            last_sync_status=last_sync_status,
            last_sync_error=last_sync_error,
            last_sync_error_code=last_sync_error_code,
            ai_sync=ai_sync,
            data_sources=data_sources,
            billing=billing,
            gcp=gcp,
            oci=oci,
            azure=azure,
        )

        cloud_connection.additional_properties = d
        return cloud_connection

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
