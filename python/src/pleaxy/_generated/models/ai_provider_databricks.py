from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AiProviderDatabricks")


@_attrs_define
class AiProviderDatabricks:
    """
    Attributes:
        host (Union[Unset, str]):
        client_id (Union[Unset, str]):
        warehouse_id (Union[Unset, str]):
    """

    host: Union[Unset, str] = UNSET
    client_id: Union[Unset, str] = UNSET
    warehouse_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        host = self.host

        client_id = self.client_id

        warehouse_id = self.warehouse_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if host is not UNSET:
            field_dict["host"] = host
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if warehouse_id is not UNSET:
            field_dict["warehouseId"] = warehouse_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        host = d.pop("host", UNSET)

        client_id = d.pop("clientId", UNSET)

        warehouse_id = d.pop("warehouseId", UNSET)

        ai_provider_databricks = cls(
            host=host,
            client_id=client_id,
            warehouse_id=warehouse_id,
        )

        ai_provider_databricks.additional_properties = d
        return ai_provider_databricks

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
