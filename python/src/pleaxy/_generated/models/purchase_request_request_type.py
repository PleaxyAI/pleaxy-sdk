from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PurchaseRequestRequestType")


@_attrs_define
class PurchaseRequestRequestType:
    """
    Attributes:
        id (str):
        name (Union[Unset, str]):
        version (Union[Unset, float]):
    """

    id: str
    name: Union[Unset, str] = UNSET
    version: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name", UNSET)

        version = d.pop("version", UNSET)

        purchase_request_request_type = cls(
            id=id,
            name=name,
            version=version,
        )

        purchase_request_request_type.additional_properties = d
        return purchase_request_request_type

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
