from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.assistant_read_cite_field import (
    AssistantReadCiteField,
    check_assistant_read_cite_field,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AssistantReadCite")


@_attrs_define
class AssistantReadCite:
    """
    Attributes:
        supplier_key (Union[Unset, str]):
        line_id (Union[Unset, str]):
        field (Union[Unset, AssistantReadCiteField]):
    """

    supplier_key: Union[Unset, str] = UNSET
    line_id: Union[Unset, str] = UNSET
    field: Union[Unset, AssistantReadCiteField] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        supplier_key = self.supplier_key

        line_id = self.line_id

        field: Union[Unset, str] = UNSET
        if not isinstance(self.field, Unset):
            field = self.field

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if supplier_key is not UNSET:
            field_dict["supplierKey"] = supplier_key
        if line_id is not UNSET:
            field_dict["lineId"] = line_id
        if field is not UNSET:
            field_dict["field"] = field

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        supplier_key = d.pop("supplierKey", UNSET)

        line_id = d.pop("lineId", UNSET)

        _field = d.pop("field", UNSET)
        field: Union[Unset, AssistantReadCiteField]
        if isinstance(_field, Unset):
            field = UNSET
        else:
            field = check_assistant_read_cite_field(_field)

        assistant_read_cite = cls(
            supplier_key=supplier_key,
            line_id=line_id,
            field=field,
        )

        assistant_read_cite.additional_properties = d
        return assistant_read_cite

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
