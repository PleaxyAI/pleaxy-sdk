from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.focus_destination_view_destination_type_0_format import (
    FocusDestinationViewDestinationType0Format,
    check_focus_destination_view_destination_type_0_format,
)
from ..models.focus_destination_view_destination_type_0_include import (
    FocusDestinationViewDestinationType0Include,
    check_focus_destination_view_destination_type_0_include,
)
from ..models.focus_destination_view_destination_type_0_provider import (
    FocusDestinationViewDestinationType0Provider,
    check_focus_destination_view_destination_type_0_provider,
)
from ..models.focus_destination_view_destination_type_0_status import (
    FocusDestinationViewDestinationType0Status,
    check_focus_destination_view_destination_type_0_status,
)
from ..models.focus_destination_view_destination_type_0_version import (
    FocusDestinationViewDestinationType0Version,
    check_focus_destination_view_destination_type_0_version,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.focus_delivery import FocusDelivery


T = TypeVar("T", bound="FocusDestinationViewDestinationType0")


@_attrs_define
class FocusDestinationViewDestinationType0:
    """
    Attributes:
        provider (Union[Unset, FocusDestinationViewDestinationType0Provider]):
        status (Union[Unset, FocusDestinationViewDestinationType0Status]):
        created_at (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        version (Union[Unset, FocusDestinationViewDestinationType0Version]):
        include (Union[Unset, FocusDestinationViewDestinationType0Include]):
        format_ (Union[Unset, FocusDestinationViewDestinationType0Format]):
        bucket (Union[Unset, str]):
        prefix (Union[Unset, str]):
        region (Union[Unset, str]):
        external_id (Union[Unset, str]):
        role_arn (Union[Unset, str]):
        aws_account_id (Union[Unset, str]):
        last_delivery (Union[Unset, FocusDelivery]):
    """

    provider: Union[Unset, FocusDestinationViewDestinationType0Provider] = UNSET
    status: Union[Unset, FocusDestinationViewDestinationType0Status] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    version: Union[Unset, FocusDestinationViewDestinationType0Version] = UNSET
    include: Union[Unset, FocusDestinationViewDestinationType0Include] = UNSET
    format_: Union[Unset, FocusDestinationViewDestinationType0Format] = UNSET
    bucket: Union[Unset, str] = UNSET
    prefix: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    external_id: Union[Unset, str] = UNSET
    role_arn: Union[Unset, str] = UNSET
    aws_account_id: Union[Unset, str] = UNSET
    last_delivery: Union[Unset, "FocusDelivery"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        provider: Union[Unset, str] = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        created_at = self.created_at

        updated_at = self.updated_at

        version: Union[Unset, str] = UNSET
        if not isinstance(self.version, Unset):
            version = self.version

        include: Union[Unset, str] = UNSET
        if not isinstance(self.include, Unset):
            include = self.include

        format_: Union[Unset, str] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_

        bucket = self.bucket

        prefix = self.prefix

        region = self.region

        external_id = self.external_id

        role_arn = self.role_arn

        aws_account_id = self.aws_account_id

        last_delivery: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.last_delivery, Unset):
            last_delivery = self.last_delivery.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if provider is not UNSET:
            field_dict["provider"] = provider
        if status is not UNSET:
            field_dict["status"] = status
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if version is not UNSET:
            field_dict["version"] = version
        if include is not UNSET:
            field_dict["include"] = include
        if format_ is not UNSET:
            field_dict["format"] = format_
        if bucket is not UNSET:
            field_dict["bucket"] = bucket
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if region is not UNSET:
            field_dict["region"] = region
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if role_arn is not UNSET:
            field_dict["roleArn"] = role_arn
        if aws_account_id is not UNSET:
            field_dict["awsAccountId"] = aws_account_id
        if last_delivery is not UNSET:
            field_dict["lastDelivery"] = last_delivery

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.focus_delivery import FocusDelivery

        d = src_dict.copy()
        _provider = d.pop("provider", UNSET)
        provider: Union[Unset, FocusDestinationViewDestinationType0Provider]
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = check_focus_destination_view_destination_type_0_provider(
                _provider
            )

        _status = d.pop("status", UNSET)
        status: Union[Unset, FocusDestinationViewDestinationType0Status]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_focus_destination_view_destination_type_0_status(_status)

        created_at = d.pop("createdAt", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        _version = d.pop("version", UNSET)
        version: Union[Unset, FocusDestinationViewDestinationType0Version]
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = check_focus_destination_view_destination_type_0_version(_version)

        _include = d.pop("include", UNSET)
        include: Union[Unset, FocusDestinationViewDestinationType0Include]
        if isinstance(_include, Unset):
            include = UNSET
        else:
            include = check_focus_destination_view_destination_type_0_include(_include)

        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, FocusDestinationViewDestinationType0Format]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = check_focus_destination_view_destination_type_0_format(_format_)

        bucket = d.pop("bucket", UNSET)

        prefix = d.pop("prefix", UNSET)

        region = d.pop("region", UNSET)

        external_id = d.pop("externalId", UNSET)

        role_arn = d.pop("roleArn", UNSET)

        aws_account_id = d.pop("awsAccountId", UNSET)

        _last_delivery = d.pop("lastDelivery", UNSET)
        last_delivery: Union[Unset, FocusDelivery]
        if isinstance(_last_delivery, Unset):
            last_delivery = UNSET
        else:
            last_delivery = FocusDelivery.from_dict(_last_delivery)

        focus_destination_view_destination_type_0 = cls(
            provider=provider,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            version=version,
            include=include,
            format_=format_,
            bucket=bucket,
            prefix=prefix,
            region=region,
            external_id=external_id,
            role_arn=role_arn,
            aws_account_id=aws_account_id,
            last_delivery=last_delivery,
        )

        focus_destination_view_destination_type_0.additional_properties = d
        return focus_destination_view_destination_type_0

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
