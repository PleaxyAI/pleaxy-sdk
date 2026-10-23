from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceDuplicateRef")


@_attrs_define
class InvoiceDuplicateRef:
    """
    Attributes:
        id (str):
        external_invoice_number (Union[Unset, str]):
        created_at (Union[Unset, str]):
    """

    id: str
    external_invoice_number: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        external_invoice_number = self.external_invoice_number

        created_at = self.created_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if external_invoice_number is not UNSET:
            field_dict["externalInvoiceNumber"] = external_invoice_number
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        external_invoice_number = d.pop("externalInvoiceNumber", UNSET)

        created_at = d.pop("createdAt", UNSET)

        invoice_duplicate_ref = cls(
            id=id,
            external_invoice_number=external_invoice_number,
            created_at=created_at,
        )

        invoice_duplicate_ref.additional_properties = d
        return invoice_duplicate_ref

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
