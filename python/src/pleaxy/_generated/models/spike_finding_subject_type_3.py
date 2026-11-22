from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.spike_finding_subject_type_3_kind import (
    SpikeFindingSubjectType3Kind,
    check_spike_finding_subject_type_3_kind,
)
from ..models.spike_finding_subject_type_3_provider import (
    SpikeFindingSubjectType3Provider,
    check_spike_finding_subject_type_3_provider,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SpikeFindingSubjectType3")


@_attrs_define
class SpikeFindingSubjectType3:
    """
    Attributes:
        kind (Union[Unset, SpikeFindingSubjectType3Kind]):
        key (Union[Unset, str]):
        connection_id (Union[Unset, str]):
        provider (Union[Unset, SpikeFindingSubjectType3Provider]):
        account (Union[Unset, str]):
        service (Union[Unset, str]):
        currency (Union[Unset, str]):
    """

    kind: Union[Unset, SpikeFindingSubjectType3Kind] = UNSET
    key: Union[Unset, str] = UNSET
    connection_id: Union[Unset, str] = UNSET
    provider: Union[Unset, SpikeFindingSubjectType3Provider] = UNSET
    account: Union[Unset, str] = UNSET
    service: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        key = self.key

        connection_id = self.connection_id

        provider: Union[Unset, str] = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider

        account = self.account

        service = self.service

        currency = self.currency

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if key is not UNSET:
            field_dict["key"] = key
        if connection_id is not UNSET:
            field_dict["connectionId"] = connection_id
        if provider is not UNSET:
            field_dict["provider"] = provider
        if account is not UNSET:
            field_dict["account"] = account
        if service is not UNSET:
            field_dict["service"] = service
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, SpikeFindingSubjectType3Kind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_spike_finding_subject_type_3_kind(_kind)

        key = d.pop("key", UNSET)

        connection_id = d.pop("connectionId", UNSET)

        _provider = d.pop("provider", UNSET)
        provider: Union[Unset, SpikeFindingSubjectType3Provider]
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = check_spike_finding_subject_type_3_provider(_provider)

        account = d.pop("account", UNSET)

        service = d.pop("service", UNSET)

        currency = d.pop("currency", UNSET)

        spike_finding_subject_type_3 = cls(
            kind=kind,
            key=key,
            connection_id=connection_id,
            provider=provider,
            account=account,
            service=service,
            currency=currency,
        )

        spike_finding_subject_type_3.additional_properties = d
        return spike_finding_subject_type_3

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
