from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.spike_finding_subject_type_0_invoicer import (
    SpikeFindingSubjectType0Invoicer,
    check_spike_finding_subject_type_0_invoicer,
)
from ..models.spike_finding_subject_type_0_kind import (
    SpikeFindingSubjectType0Kind,
    check_spike_finding_subject_type_0_kind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SpikeFindingSubjectType0")


@_attrs_define
class SpikeFindingSubjectType0:
    """
    Attributes:
        kind (Union[Unset, SpikeFindingSubjectType0Kind]):
        key (Union[Unset, str]):
        invoicer_id (Union[Unset, str]):
        invoicer (Union[Unset, SpikeFindingSubjectType0Invoicer]):
        account (Union[Unset, str]):
        currency (Union[Unset, str]):
    """

    kind: Union[Unset, SpikeFindingSubjectType0Kind] = UNSET
    key: Union[Unset, str] = UNSET
    invoicer_id: Union[Unset, str] = UNSET
    invoicer: Union[Unset, SpikeFindingSubjectType0Invoicer] = UNSET
    account: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        key = self.key

        invoicer_id = self.invoicer_id

        invoicer: Union[Unset, str] = UNSET
        if not isinstance(self.invoicer, Unset):
            invoicer = self.invoicer

        account = self.account

        currency = self.currency

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if key is not UNSET:
            field_dict["key"] = key
        if invoicer_id is not UNSET:
            field_dict["invoicerId"] = invoicer_id
        if invoicer is not UNSET:
            field_dict["invoicer"] = invoicer
        if account is not UNSET:
            field_dict["account"] = account
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, SpikeFindingSubjectType0Kind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_spike_finding_subject_type_0_kind(_kind)

        key = d.pop("key", UNSET)

        invoicer_id = d.pop("invoicerId", UNSET)

        _invoicer = d.pop("invoicer", UNSET)
        invoicer: Union[Unset, SpikeFindingSubjectType0Invoicer]
        if isinstance(_invoicer, Unset):
            invoicer = UNSET
        else:
            invoicer = check_spike_finding_subject_type_0_invoicer(_invoicer)

        account = d.pop("account", UNSET)

        currency = d.pop("currency", UNSET)

        spike_finding_subject_type_0 = cls(
            kind=kind,
            key=key,
            invoicer_id=invoicer_id,
            invoicer=invoicer,
            account=account,
            currency=currency,
        )

        spike_finding_subject_type_0.additional_properties = d
        return spike_finding_subject_type_0

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
