from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.supplier_risk_missing_documents_state import (
    SupplierRiskMissingDocumentsState,
    check_supplier_risk_missing_documents_state,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SupplierRiskMissingDocuments")


@_attrs_define
class SupplierRiskMissingDocuments:
    """
    Attributes:
        state (Union[Unset, SupplierRiskMissingDocumentsState]):
        fields (Union[Unset, List[str]]):
    """

    state: Union[Unset, SupplierRiskMissingDocumentsState] = UNSET
    fields: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state

        fields: Union[Unset, List[str]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _state = d.pop("state", UNSET)
        state: Union[Unset, SupplierRiskMissingDocumentsState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = check_supplier_risk_missing_documents_state(_state)

        fields = cast(List[str], d.pop("fields", UNSET))

        supplier_risk_missing_documents = cls(
            state=state,
            fields=fields,
        )

        supplier_risk_missing_documents.additional_properties = d
        return supplier_risk_missing_documents

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
