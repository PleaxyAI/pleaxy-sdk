from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FocusS3CompatibleSourceInput")


@_attrs_define
class FocusS3CompatibleSourceInput:
    """
    Attributes:
        endpoint (str):
        region (str):
        bucket (str):
        access_key_id (str):
        secret_access_key (str):
        prefix (Union[Unset, str]):
    """

    endpoint: str
    region: str
    bucket: str
    access_key_id: str
    secret_access_key: str
    prefix: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        endpoint = self.endpoint

        region = self.region

        bucket = self.bucket

        access_key_id = self.access_key_id

        secret_access_key = self.secret_access_key

        prefix = self.prefix

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endpoint": endpoint,
                "region": region,
                "bucket": bucket,
                "accessKeyId": access_key_id,
                "secretAccessKey": secret_access_key,
            }
        )
        if prefix is not UNSET:
            field_dict["prefix"] = prefix

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        endpoint = d.pop("endpoint")

        region = d.pop("region")

        bucket = d.pop("bucket")

        access_key_id = d.pop("accessKeyId")

        secret_access_key = d.pop("secretAccessKey")

        prefix = d.pop("prefix", UNSET)

        focus_s3_compatible_source_input = cls(
            endpoint=endpoint,
            region=region,
            bucket=bucket,
            access_key_id=access_key_id,
            secret_access_key=secret_access_key,
            prefix=prefix,
        )

        focus_s3_compatible_source_input.additional_properties = d
        return focus_s3_compatible_source_input

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
