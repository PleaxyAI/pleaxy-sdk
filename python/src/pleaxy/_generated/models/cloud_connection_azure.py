from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cloud_connection_azure_agreement_type import (
    CloudConnectionAzureAgreementType,
    check_cloud_connection_azure_agreement_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudConnectionAzure")


@_attrs_define
class CloudConnectionAzure:
    """
    Attributes:
        scope_display_name (Union[Unset, str]):
        agreement_type (Union[Unset, CloudConnectionAzureAgreementType]):
    """

    scope_display_name: Union[Unset, str] = UNSET
    agreement_type: Union[Unset, CloudConnectionAzureAgreementType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scope_display_name = self.scope_display_name

        agreement_type: Union[Unset, str] = UNSET
        if not isinstance(self.agreement_type, Unset):
            agreement_type = self.agreement_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scope_display_name is not UNSET:
            field_dict["scopeDisplayName"] = scope_display_name
        if agreement_type is not UNSET:
            field_dict["agreementType"] = agreement_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        scope_display_name = d.pop("scopeDisplayName", UNSET)

        _agreement_type = d.pop("agreementType", UNSET)
        agreement_type: Union[Unset, CloudConnectionAzureAgreementType]
        if isinstance(_agreement_type, Unset):
            agreement_type = UNSET
        else:
            agreement_type = check_cloud_connection_azure_agreement_type(
                _agreement_type
            )

        cloud_connection_azure = cls(
            scope_display_name=scope_display_name,
            agreement_type=agreement_type,
        )

        cloud_connection_azure.additional_properties = d
        return cloud_connection_azure

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
