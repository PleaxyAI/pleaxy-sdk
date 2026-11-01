from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.put_focus_destination_input_format import (
    PutFocusDestinationInputFormat,
    check_put_focus_destination_input_format,
)
from ..models.put_focus_destination_input_include import (
    PutFocusDestinationInputInclude,
    check_put_focus_destination_input_include,
)
from ..models.put_focus_destination_input_version import (
    PutFocusDestinationInputVersion,
    check_put_focus_destination_input_version,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutFocusDestinationInput")


@_attrs_define
class PutFocusDestinationInput:
    """
    Attributes:
        bucket (str):
        region (str):
        prefix (Union[Unset, str]):
        role_arn (Union[Unset, str]):
        format_ (Union[Unset, PutFocusDestinationInputFormat]):
        version (Union[Unset, PutFocusDestinationInputVersion]):
        include (Union[Unset, PutFocusDestinationInputInclude]):
    """

    bucket: str
    region: str
    prefix: Union[Unset, str] = UNSET
    role_arn: Union[Unset, str] = UNSET
    format_: Union[Unset, PutFocusDestinationInputFormat] = UNSET
    version: Union[Unset, PutFocusDestinationInputVersion] = UNSET
    include: Union[Unset, PutFocusDestinationInputInclude] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bucket = self.bucket

        region = self.region

        prefix = self.prefix

        role_arn = self.role_arn

        format_: Union[Unset, str] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_

        version: Union[Unset, str] = UNSET
        if not isinstance(self.version, Unset):
            version = self.version

        include: Union[Unset, str] = UNSET
        if not isinstance(self.include, Unset):
            include = self.include

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bucket": bucket,
                "region": region,
            }
        )
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if role_arn is not UNSET:
            field_dict["roleArn"] = role_arn
        if format_ is not UNSET:
            field_dict["format"] = format_
        if version is not UNSET:
            field_dict["version"] = version
        if include is not UNSET:
            field_dict["include"] = include

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        bucket = d.pop("bucket")

        region = d.pop("region")

        prefix = d.pop("prefix", UNSET)

        role_arn = d.pop("roleArn", UNSET)

        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, PutFocusDestinationInputFormat]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = check_put_focus_destination_input_format(_format_)

        _version = d.pop("version", UNSET)
        version: Union[Unset, PutFocusDestinationInputVersion]
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = check_put_focus_destination_input_version(_version)

        _include = d.pop("include", UNSET)
        include: Union[Unset, PutFocusDestinationInputInclude]
        if isinstance(_include, Unset):
            include = UNSET
        else:
            include = check_put_focus_destination_input_include(_include)

        put_focus_destination_input = cls(
            bucket=bucket,
            region=region,
            prefix=prefix,
            role_arn=role_arn,
            format_=format_,
            version=version,
            include=include,
        )

        put_focus_destination_input.additional_properties = d
        return put_focus_destination_input

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
