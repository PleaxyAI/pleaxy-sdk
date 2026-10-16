from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UncreditedOriginal")


@_attrs_define
class UncreditedOriginal:
    """
    Attributes:
        invoice_id (Union[Unset, str]):
        external_invoice_number (Union[Unset, str]):
        uncredited (Union[Unset, float]):
        currency (Union[Unset, str]):
    """

    invoice_id: Union[Unset, str] = UNSET
    external_invoice_number: Union[Unset, str] = UNSET
    uncredited: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoice_id = self.invoice_id

        external_invoice_number = self.external_invoice_number

        uncredited = self.uncredited

        currency = self.currency

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invoice_id is not UNSET:
            field_dict["invoiceId"] = invoice_id
        if external_invoice_number is not UNSET:
            field_dict["externalInvoiceNumber"] = external_invoice_number
        if uncredited is not UNSET:
            field_dict["uncredited"] = uncredited
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        invoice_id = d.pop("invoiceId", UNSET)

        external_invoice_number = d.pop("externalInvoiceNumber", UNSET)

        uncredited = d.pop("uncredited", UNSET)

        currency = d.pop("currency", UNSET)

        uncredited_original = cls(
            invoice_id=invoice_id,
            external_invoice_number=external_invoice_number,
            uncredited=uncredited,
            currency=currency,
        )

        uncredited_original.additional_properties = d
        return uncredited_original

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
