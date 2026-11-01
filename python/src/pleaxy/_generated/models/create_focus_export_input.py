from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_focus_export_input_format import (
    CreateFocusExportInputFormat,
    check_create_focus_export_input_format,
)
from ..models.create_focus_export_input_include import (
    CreateFocusExportInputInclude,
    check_create_focus_export_input_include,
)
from ..models.create_focus_export_input_version import (
    CreateFocusExportInputVersion,
    check_create_focus_export_input_version,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateFocusExportInput")


@_attrs_define
class CreateFocusExportInput:
    """
    Attributes:
        from_ (str):
        to (str):
        version (Union[Unset, CreateFocusExportInputVersion]):
        include (Union[Unset, CreateFocusExportInputInclude]):
        format_ (Union[Unset, CreateFocusExportInputFormat]):
    """

    from_: str
    to: str
    version: Union[Unset, CreateFocusExportInputVersion] = UNSET
    include: Union[Unset, CreateFocusExportInputInclude] = UNSET
    format_: Union[Unset, CreateFocusExportInputFormat] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from_ = self.from_

        to = self.to

        version: Union[Unset, str] = UNSET
        if not isinstance(self.version, Unset):
            version = self.version

        include: Union[Unset, str] = UNSET
        if not isinstance(self.include, Unset):
            include = self.include

        format_: Union[Unset, str] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "to": to,
            }
        )
        if version is not UNSET:
            field_dict["version"] = version
        if include is not UNSET:
            field_dict["include"] = include
        if format_ is not UNSET:
            field_dict["format"] = format_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        from_ = d.pop("from")

        to = d.pop("to")

        _version = d.pop("version", UNSET)
        version: Union[Unset, CreateFocusExportInputVersion]
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = check_create_focus_export_input_version(_version)

        _include = d.pop("include", UNSET)
        include: Union[Unset, CreateFocusExportInputInclude]
        if isinstance(_include, Unset):
            include = UNSET
        else:
            include = check_create_focus_export_input_include(_include)

        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, CreateFocusExportInputFormat]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = check_create_focus_export_input_format(_format_)

        create_focus_export_input = cls(
            from_=from_,
            to=to,
            version=version,
            include=include,
            format_=format_,
        )

        create_focus_export_input.additional_properties = d
        return create_focus_export_input

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
