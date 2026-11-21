from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_invoice_vat_category import (
    EInvoiceVatCategory,
    check_e_invoice_vat_category,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EInvoiceVat")


@_attrs_define
class EInvoiceVat:
    """
    Attributes:
        category (Union[Unset, EInvoiceVatCategory]):
        rate (Union[Unset, float]):
    """

    category: Union[Unset, EInvoiceVatCategory] = UNSET
    rate: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category: Union[Unset, str] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category

        rate = self.rate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if rate is not UNSET:
            field_dict["rate"] = rate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _category = d.pop("category", UNSET)
        category: Union[Unset, EInvoiceVatCategory]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = check_e_invoice_vat_category(_category)

        rate = d.pop("rate", UNSET)

        e_invoice_vat = cls(
            category=category,
            rate=rate,
        )

        e_invoice_vat.additional_properties = d
        return e_invoice_vat

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
