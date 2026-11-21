from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.datadog_connection_input_site import (
    DatadogConnectionInputSite,
    check_datadog_connection_input_site,
)

T = TypeVar("T", bound="DatadogConnectionInput")


@_attrs_define
class DatadogConnectionInput:
    """
    Attributes:
        site (DatadogConnectionInputSite):
        api_key (str):
    """

    site: DatadogConnectionInputSite
    api_key: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        site: str = self.site

        api_key = self.api_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "site": site,
                "apiKey": api_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        site = check_datadog_connection_input_site(d.pop("site"))

        api_key = d.pop("apiKey")

        datadog_connection_input = cls(
            site=site,
            api_key=api_key,
        )

        datadog_connection_input.additional_properties = d
        return datadog_connection_input

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
