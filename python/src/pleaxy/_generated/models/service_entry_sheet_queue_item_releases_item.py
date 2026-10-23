from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceEntrySheetQueueItemReleasesItem")


@_attrs_define
class ServiceEntrySheetQueueItemReleasesItem:
    """
    Attributes:
        id (str):
        invoice_number (Union[Unset, str]):
        amount (Union[Unset, float]):
        currency (Union[Unset, str]):
    """

    id: str
    invoice_number: Union[Unset, str] = UNSET
    amount: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        invoice_number = self.invoice_number

        amount = self.amount

        currency = self.currency

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if invoice_number is not UNSET:
            field_dict["invoiceNumber"] = invoice_number
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        invoice_number = d.pop("invoiceNumber", UNSET)

        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        service_entry_sheet_queue_item_releases_item = cls(
            id=id,
            invoice_number=invoice_number,
            amount=amount,
            currency=currency,
        )

        service_entry_sheet_queue_item_releases_item.additional_properties = d
        return service_entry_sheet_queue_item_releases_item

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
