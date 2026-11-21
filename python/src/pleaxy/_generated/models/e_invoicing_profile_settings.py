from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.e_invoicing_profile_settings_electronic_address import (
        EInvoicingProfileSettingsElectronicAddress,
    )


T = TypeVar("T", bound="EInvoicingProfileSettings")


@_attrs_define
class EInvoicingProfileSettings:
    """
    Attributes:
        contact_name (Union[Unset, str]):
        contact_phone (Union[Unset, str]):
        contact_email (Union[Unset, str]):
        electronic_address (Union[Unset, EInvoicingProfileSettingsElectronicAddress]):
        buyer_reference (Union[Unset, str]):
    """

    contact_name: Union[Unset, str] = UNSET
    contact_phone: Union[Unset, str] = UNSET
    contact_email: Union[Unset, str] = UNSET
    electronic_address: Union[Unset, "EInvoicingProfileSettingsElectronicAddress"] = (
        UNSET
    )
    buyer_reference: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contact_name = self.contact_name

        contact_phone = self.contact_phone

        contact_email = self.contact_email

        electronic_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.electronic_address, Unset):
            electronic_address = self.electronic_address.to_dict()

        buyer_reference = self.buyer_reference

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contact_name is not UNSET:
            field_dict["contactName"] = contact_name
        if contact_phone is not UNSET:
            field_dict["contactPhone"] = contact_phone
        if contact_email is not UNSET:
            field_dict["contactEmail"] = contact_email
        if electronic_address is not UNSET:
            field_dict["electronicAddress"] = electronic_address
        if buyer_reference is not UNSET:
            field_dict["buyerReference"] = buyer_reference

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.e_invoicing_profile_settings_electronic_address import (
            EInvoicingProfileSettingsElectronicAddress,
        )

        d = src_dict.copy()
        contact_name = d.pop("contactName", UNSET)

        contact_phone = d.pop("contactPhone", UNSET)

        contact_email = d.pop("contactEmail", UNSET)

        _electronic_address = d.pop("electronicAddress", UNSET)
        electronic_address: Union[Unset, EInvoicingProfileSettingsElectronicAddress]
        if isinstance(_electronic_address, Unset):
            electronic_address = UNSET
        else:
            electronic_address = EInvoicingProfileSettingsElectronicAddress.from_dict(
                _electronic_address
            )

        buyer_reference = d.pop("buyerReference", UNSET)

        e_invoicing_profile_settings = cls(
            contact_name=contact_name,
            contact_phone=contact_phone,
            contact_email=contact_email,
            electronic_address=electronic_address,
            buyer_reference=buyer_reference,
        )

        e_invoicing_profile_settings.additional_properties = d
        return e_invoicing_profile_settings

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
