from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inbound_email import InboundEmail


T = TypeVar("T", bound="PurchaseOrderEmails")


@_attrs_define
class PurchaseOrderEmails:
    """
    Attributes:
        address (Union[Unset, str]):
        emails (Union[Unset, List['InboundEmail']]):
    """

    address: Union[Unset, str] = UNSET
    emails: Union[Unset, List["InboundEmail"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address = self.address

        emails: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.emails, Unset):
            emails = []
            for emails_item_data in self.emails:
                emails_item = emails_item_data.to_dict()
                emails.append(emails_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if emails is not UNSET:
            field_dict["emails"] = emails

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.inbound_email import InboundEmail

        d = src_dict.copy()
        address = d.pop("address", UNSET)

        emails = []
        _emails = d.pop("emails", UNSET)
        for emails_item_data in _emails or []:
            emails_item = InboundEmail.from_dict(emails_item_data)

            emails.append(emails_item)

        purchase_order_emails = cls(
            address=address,
            emails=emails,
        )

        purchase_order_emails.additional_properties = d
        return purchase_order_emails

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
