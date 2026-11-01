from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FocusSourceViewS3")


@_attrs_define
class FocusSourceViewS3:
    """
    Attributes:
        endpoint (Union[Unset, str]):
        region (Union[Unset, str]):
        bucket (Union[Unset, str]):
        prefix (Union[Unset, str]):
        access_key_id (Union[Unset, str]):
        key_hint (Union[Unset, str]):
    """

    endpoint: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    bucket: Union[Unset, str] = UNSET
    prefix: Union[Unset, str] = UNSET
    access_key_id: Union[Unset, str] = UNSET
    key_hint: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        endpoint = self.endpoint

        region = self.region

        bucket = self.bucket

        prefix = self.prefix

        access_key_id = self.access_key_id

        key_hint = self.key_hint

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if region is not UNSET:
            field_dict["region"] = region
        if bucket is not UNSET:
            field_dict["bucket"] = bucket
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if access_key_id is not UNSET:
            field_dict["accessKeyId"] = access_key_id
        if key_hint is not UNSET:
            field_dict["keyHint"] = key_hint

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        endpoint = d.pop("endpoint", UNSET)

        region = d.pop("region", UNSET)

        bucket = d.pop("bucket", UNSET)

        prefix = d.pop("prefix", UNSET)

        access_key_id = d.pop("accessKeyId", UNSET)

        key_hint = d.pop("keyHint", UNSET)

        focus_source_view_s3 = cls(
            endpoint=endpoint,
            region=region,
            bucket=bucket,
            prefix=prefix,
            access_key_id=access_key_id,
            key_hint=key_hint,
        )

        focus_source_view_s3.additional_properties = d
        return focus_source_view_s3

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
