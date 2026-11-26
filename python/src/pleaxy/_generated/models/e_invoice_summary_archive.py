from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EInvoiceSummaryArchive")


@_attrs_define
class EInvoiceSummaryArchive:
    """
    Attributes:
        key (Union[Unset, str]):
        sha256 (Union[Unset, str]):
        retain_until_year (Union[Unset, float]):
    """

    key: Union[Unset, str] = UNSET
    sha256: Union[Unset, str] = UNSET
    retain_until_year: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key

        sha256 = self.sha256

        retain_until_year = self.retain_until_year

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if sha256 is not UNSET:
            field_dict["sha256"] = sha256
        if retain_until_year is not UNSET:
            field_dict["retainUntilYear"] = retain_until_year

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key = d.pop("key", UNSET)

        sha256 = d.pop("sha256", UNSET)

        retain_until_year = d.pop("retainUntilYear", UNSET)

        e_invoice_summary_archive = cls(
            key=key,
            sha256=sha256,
            retain_until_year=retain_until_year,
        )

        e_invoice_summary_archive.additional_properties = d
        return e_invoice_summary_archive

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
