from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_api_key_result_procurement_role import (
    CreateApiKeyResultProcurementRole,
    check_create_api_key_result_procurement_role,
)
from ..models.create_api_key_result_role import (
    CreateApiKeyResultRole,
    check_create_api_key_result_role,
)
from ..models.create_api_key_result_scopes_item import (
    CreateApiKeyResultScopesItem,
    check_create_api_key_result_scopes_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateApiKeyResult")


@_attrs_define
class CreateApiKeyResult:
    """
    Attributes:
        api_key (Union[Unset, str]):
        key_id (Union[Unset, str]):
        region_id (Union[Unset, str]):
        role (Union[Unset, CreateApiKeyResultRole]):
        procurement_role (Union[Unset, CreateApiKeyResultProcurementRole]):
        scopes (Union[Unset, List[CreateApiKeyResultScopesItem]]):
        label (Union[Unset, str]):
        created_at (Union[Unset, str]):
        created_by (Union[Unset, str]):
        revoked (Union[Unset, bool]):
    """

    api_key: Union[Unset, str] = UNSET
    key_id: Union[Unset, str] = UNSET
    region_id: Union[Unset, str] = UNSET
    role: Union[Unset, CreateApiKeyResultRole] = UNSET
    procurement_role: Union[Unset, CreateApiKeyResultProcurementRole] = UNSET
    scopes: Union[Unset, List[CreateApiKeyResultScopesItem]] = UNSET
    label: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by: Union[Unset, str] = UNSET
    revoked: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        api_key = self.api_key

        key_id = self.key_id

        region_id = self.region_id

        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role

        procurement_role: Union[Unset, str] = UNSET
        if not isinstance(self.procurement_role, Unset):
            procurement_role = self.procurement_role

        scopes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = []
            for scopes_item_data in self.scopes:
                scopes_item: str = scopes_item_data
                scopes.append(scopes_item)

        label = self.label

        created_at = self.created_at

        created_by = self.created_by

        revoked = self.revoked

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_key is not UNSET:
            field_dict["apiKey"] = api_key
        if key_id is not UNSET:
            field_dict["keyId"] = key_id
        if region_id is not UNSET:
            field_dict["regionId"] = region_id
        if role is not UNSET:
            field_dict["role"] = role
        if procurement_role is not UNSET:
            field_dict["procurementRole"] = procurement_role
        if scopes is not UNSET:
            field_dict["scopes"] = scopes
        if label is not UNSET:
            field_dict["label"] = label
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if revoked is not UNSET:
            field_dict["revoked"] = revoked

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        api_key = d.pop("apiKey", UNSET)

        key_id = d.pop("keyId", UNSET)

        region_id = d.pop("regionId", UNSET)

        _role = d.pop("role", UNSET)
        role: Union[Unset, CreateApiKeyResultRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = check_create_api_key_result_role(_role)

        _procurement_role = d.pop("procurementRole", UNSET)
        procurement_role: Union[Unset, CreateApiKeyResultProcurementRole]
        if isinstance(_procurement_role, Unset):
            procurement_role = UNSET
        else:
            procurement_role = check_create_api_key_result_procurement_role(
                _procurement_role
            )

        scopes = []
        _scopes = d.pop("scopes", UNSET)
        for scopes_item_data in _scopes or []:
            scopes_item = check_create_api_key_result_scopes_item(scopes_item_data)

            scopes.append(scopes_item)

        label = d.pop("label", UNSET)

        created_at = d.pop("createdAt", UNSET)

        created_by = d.pop("createdBy", UNSET)

        revoked = d.pop("revoked", UNSET)

        create_api_key_result = cls(
            api_key=api_key,
            key_id=key_id,
            region_id=region_id,
            role=role,
            procurement_role=procurement_role,
            scopes=scopes,
            label=label,
            created_at=created_at,
            created_by=created_by,
            revoked=revoked,
        )

        create_api_key_result.additional_properties = d
        return create_api_key_result

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
