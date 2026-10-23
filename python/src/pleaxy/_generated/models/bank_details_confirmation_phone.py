from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bank_details_confirmation_phone_method import (
    BankDetailsConfirmationPhoneMethod,
    check_bank_details_confirmation_phone_method,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BankDetailsConfirmationPhone")


@_attrs_define
class BankDetailsConfirmationPhone:
    """
    Attributes:
        method (Union[Unset, BankDetailsConfirmationPhoneMethod]):
        contact_name (Union[Unset, str]):
        phone_number (Union[Unset, str]):
        note (Union[Unset, str]):
    """

    method: Union[Unset, BankDetailsConfirmationPhoneMethod] = UNSET
    contact_name: Union[Unset, str] = UNSET
    phone_number: Union[Unset, str] = UNSET
    note: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        method: Union[Unset, str] = UNSET
        if not isinstance(self.method, Unset):
            method = self.method

        contact_name = self.contact_name

        phone_number = self.phone_number

        note = self.note

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if method is not UNSET:
            field_dict["method"] = method
        if contact_name is not UNSET:
            field_dict["contactName"] = contact_name
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _method = d.pop("method", UNSET)
        method: Union[Unset, BankDetailsConfirmationPhoneMethod]
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = check_bank_details_confirmation_phone_method(_method)

        contact_name = d.pop("contactName", UNSET)

        phone_number = d.pop("phoneNumber", UNSET)

        note = d.pop("note", UNSET)

        bank_details_confirmation_phone = cls(
            method=method,
            contact_name=contact_name,
            phone_number=phone_number,
            note=note,
        )

        bank_details_confirmation_phone.additional_properties = d
        return bank_details_confirmation_phone

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
