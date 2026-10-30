from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ai_provider_last_sync_error_code import (
    AiProviderLastSyncErrorCode,
    check_ai_provider_last_sync_error_code,
)
from ..models.ai_provider_last_sync_status import (
    AiProviderLastSyncStatus,
    check_ai_provider_last_sync_status,
)
from ..models.ai_provider_provider import AiProviderProvider, check_ai_provider_provider
from ..models.ai_provider_status import AiProviderStatus, check_ai_provider_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_provider_credit_price import AiProviderCreditPrice
    from ..models.ai_provider_snowflake import AiProviderSnowflake


T = TypeVar("T", bound="AiProvider")


@_attrs_define
class AiProvider:
    """
    Attributes:
        id (str):
        provider (Union[Unset, AiProviderProvider]):
        account_label (Union[Unset, str]):
        key_hint (Union[Unset, str]):
        status (Union[Unset, AiProviderStatus]):
        connected_at (Union[Unset, str]):
        connected_by (Union[Unset, str]):
        snowflake (Union[Unset, AiProviderSnowflake]):
        credit_price (Union[Unset, AiProviderCreditPrice]):
        supplier_connection_id (Union[Unset, str]):
        last_synced_at (Union[Unset, str]):
        last_sync_status (Union[Unset, AiProviderLastSyncStatus]):
        last_sync_error (Union[Unset, str]):
        last_sync_error_code (Union[Unset, AiProviderLastSyncErrorCode]):
        currency (Union[Unset, str]):
    """

    id: str
    provider: Union[Unset, AiProviderProvider] = UNSET
    account_label: Union[Unset, str] = UNSET
    key_hint: Union[Unset, str] = UNSET
    status: Union[Unset, AiProviderStatus] = UNSET
    connected_at: Union[Unset, str] = UNSET
    connected_by: Union[Unset, str] = UNSET
    snowflake: Union[Unset, "AiProviderSnowflake"] = UNSET
    credit_price: Union[Unset, "AiProviderCreditPrice"] = UNSET
    supplier_connection_id: Union[Unset, str] = UNSET
    last_synced_at: Union[Unset, str] = UNSET
    last_sync_status: Union[Unset, AiProviderLastSyncStatus] = UNSET
    last_sync_error: Union[Unset, str] = UNSET
    last_sync_error_code: Union[Unset, AiProviderLastSyncErrorCode] = UNSET
    currency: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        provider: Union[Unset, str] = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider

        account_label = self.account_label

        key_hint = self.key_hint

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        connected_at = self.connected_at

        connected_by = self.connected_by

        snowflake: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.snowflake, Unset):
            snowflake = self.snowflake.to_dict()

        credit_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credit_price, Unset):
            credit_price = self.credit_price.to_dict()

        supplier_connection_id = self.supplier_connection_id

        last_synced_at = self.last_synced_at

        last_sync_status: Union[Unset, str] = UNSET
        if not isinstance(self.last_sync_status, Unset):
            last_sync_status = self.last_sync_status

        last_sync_error = self.last_sync_error

        last_sync_error_code: Union[Unset, str] = UNSET
        if not isinstance(self.last_sync_error_code, Unset):
            last_sync_error_code = self.last_sync_error_code

        currency = self.currency

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
        if key_hint is not UNSET:
            field_dict["keyHint"] = key_hint
        if status is not UNSET:
            field_dict["status"] = status
        if connected_at is not UNSET:
            field_dict["connectedAt"] = connected_at
        if connected_by is not UNSET:
            field_dict["connectedBy"] = connected_by
        if snowflake is not UNSET:
            field_dict["snowflake"] = snowflake
        if credit_price is not UNSET:
            field_dict["creditPrice"] = credit_price
        if supplier_connection_id is not UNSET:
            field_dict["supplierConnectionId"] = supplier_connection_id
        if last_synced_at is not UNSET:
            field_dict["lastSyncedAt"] = last_synced_at
        if last_sync_status is not UNSET:
            field_dict["lastSyncStatus"] = last_sync_status
        if last_sync_error is not UNSET:
            field_dict["lastSyncError"] = last_sync_error
        if last_sync_error_code is not UNSET:
            field_dict["lastSyncErrorCode"] = last_sync_error_code
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ai_provider_credit_price import AiProviderCreditPrice
        from ..models.ai_provider_snowflake import AiProviderSnowflake

        d = src_dict.copy()
        id = d.pop("id")

        _provider = d.pop("provider", UNSET)
        provider: Union[Unset, AiProviderProvider]
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = check_ai_provider_provider(_provider)

        account_label = d.pop("accountLabel", UNSET)

        key_hint = d.pop("keyHint", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, AiProviderStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_ai_provider_status(_status)

        connected_at = d.pop("connectedAt", UNSET)

        connected_by = d.pop("connectedBy", UNSET)

        _snowflake = d.pop("snowflake", UNSET)
        snowflake: Union[Unset, AiProviderSnowflake]
        if isinstance(_snowflake, Unset):
            snowflake = UNSET
        else:
            snowflake = AiProviderSnowflake.from_dict(_snowflake)

        _credit_price = d.pop("creditPrice", UNSET)
        credit_price: Union[Unset, AiProviderCreditPrice]
        if isinstance(_credit_price, Unset):
            credit_price = UNSET
        else:
            credit_price = AiProviderCreditPrice.from_dict(_credit_price)

        supplier_connection_id = d.pop("supplierConnectionId", UNSET)

        last_synced_at = d.pop("lastSyncedAt", UNSET)

        _last_sync_status = d.pop("lastSyncStatus", UNSET)
        last_sync_status: Union[Unset, AiProviderLastSyncStatus]
        if isinstance(_last_sync_status, Unset):
            last_sync_status = UNSET
        else:
            last_sync_status = check_ai_provider_last_sync_status(_last_sync_status)

        last_sync_error = d.pop("lastSyncError", UNSET)

        _last_sync_error_code = d.pop("lastSyncErrorCode", UNSET)
        last_sync_error_code: Union[Unset, AiProviderLastSyncErrorCode]
        if isinstance(_last_sync_error_code, Unset):
            last_sync_error_code = UNSET
        else:
            last_sync_error_code = check_ai_provider_last_sync_error_code(
                _last_sync_error_code
            )

        currency = d.pop("currency", UNSET)

        ai_provider = cls(
            id=id,
            provider=provider,
            account_label=account_label,
            key_hint=key_hint,
            status=status,
            connected_at=connected_at,
            connected_by=connected_by,
            snowflake=snowflake,
            credit_price=credit_price,
            supplier_connection_id=supplier_connection_id,
            last_synced_at=last_synced_at,
            last_sync_status=last_sync_status,
            last_sync_error=last_sync_error,
            last_sync_error_code=last_sync_error_code,
            currency=currency,
        )

        ai_provider.additional_properties = d
        return ai_provider

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
