from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MapFocusIssuerInput")


@_attrs_define
class MapFocusIssuerInput:
    """
    Attributes:
        supplier_connection_id (Union[None, Unset, str]):
    """

    supplier_connection_id: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        supplier_connection_id: Union[None, Unset, str]
        if isinstance(self.supplier_connection_id, Unset):
            supplier_connection_id = UNSET
        else:
            supplier_connection_id = self.supplier_connection_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if supplier_connection_id is not UNSET:
            field_dict["supplierConnectionId"] = supplier_connection_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_supplier_connection_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        supplier_connection_id = _parse_supplier_connection_id(
            d.pop("supplierConnectionId", UNSET)
        )

        map_focus_issuer_input = cls(
            supplier_connection_id=supplier_connection_id,
        )

        map_focus_issuer_input.additional_properties = d
        return map_focus_issuer_input

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
