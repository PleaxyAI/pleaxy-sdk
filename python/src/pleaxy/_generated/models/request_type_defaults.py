from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.request_type_defaults_line_type import (
    RequestTypeDefaultsLineType,
    check_request_type_defaults_line_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RequestTypeDefaults")


@_attrs_define
class RequestTypeDefaults:
    """
    Attributes:
        gl_code (Union[Unset, str]):
        line_type (Union[Unset, RequestTypeDefaultsLineType]):
    """

    gl_code: Union[Unset, str] = UNSET
    line_type: Union[Unset, RequestTypeDefaultsLineType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        gl_code = self.gl_code

        line_type: Union[Unset, str] = UNSET
        if not isinstance(self.line_type, Unset):
            line_type = self.line_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gl_code is not UNSET:
            field_dict["glCode"] = gl_code
        if line_type is not UNSET:
            field_dict["lineType"] = line_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        gl_code = d.pop("glCode", UNSET)

        _line_type = d.pop("lineType", UNSET)
        line_type: Union[Unset, RequestTypeDefaultsLineType]
        if isinstance(_line_type, Unset):
            line_type = UNSET
        else:
            line_type = check_request_type_defaults_line_type(_line_type)

        request_type_defaults = cls(
            gl_code=gl_code,
            line_type=line_type,
        )

        request_type_defaults.additional_properties = d
        return request_type_defaults

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
