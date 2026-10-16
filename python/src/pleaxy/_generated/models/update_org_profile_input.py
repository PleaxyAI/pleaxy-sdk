from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_org_profile_input_geography_preset_id import (
    UpdateOrgProfileInputGeographyPresetId,
    check_update_org_profile_input_geography_preset_id,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.postal_address_input import PostalAddressInput


T = TypeVar("T", bound="UpdateOrgProfileInput")


@_attrs_define
class UpdateOrgProfileInput:
    """
    Attributes:
        region_name (Union[Unset, str]):
        company_name (Union[Unset, str]):
        billing_email (Union[Unset, str]):
        billing_address (Union[Unset, str]):
        billing_address_parts (Union[Unset, PostalAddressInput]):
        tax_id (Union[Unset, str]):
        currency (Union[Unset, str]):
        other_currencies (Union[Unset, List[str]]):
        payment_currencies (Union[Unset, List[str]]):
        primary_contact_name (Union[Unset, str]):
        primary_contact_email (Union[Unset, str]):
        countries (Union[Unset, List[str]]):
        time_zone (Union[Unset, str]):
        listed_in_directory (Union[Unset, bool]):
        geography_preset_id (Union[Unset, UpdateOrgProfileInputGeographyPresetId]):
    """

    region_name: Union[Unset, str] = UNSET
    company_name: Union[Unset, str] = UNSET
    billing_email: Union[Unset, str] = UNSET
    billing_address: Union[Unset, str] = UNSET
    billing_address_parts: Union[Unset, "PostalAddressInput"] = UNSET
    tax_id: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    other_currencies: Union[Unset, List[str]] = UNSET
    payment_currencies: Union[Unset, List[str]] = UNSET
    primary_contact_name: Union[Unset, str] = UNSET
    primary_contact_email: Union[Unset, str] = UNSET
    countries: Union[Unset, List[str]] = UNSET
    time_zone: Union[Unset, str] = UNSET
    listed_in_directory: Union[Unset, bool] = UNSET
    geography_preset_id: Union[Unset, UpdateOrgProfileInputGeographyPresetId] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        region_name = self.region_name

        company_name = self.company_name

        billing_email = self.billing_email

        billing_address = self.billing_address

        billing_address_parts: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.billing_address_parts, Unset):
            billing_address_parts = self.billing_address_parts.to_dict()

        tax_id = self.tax_id

        currency = self.currency

        other_currencies: Union[Unset, List[str]] = UNSET
        if not isinstance(self.other_currencies, Unset):
            other_currencies = self.other_currencies

        payment_currencies: Union[Unset, List[str]] = UNSET
        if not isinstance(self.payment_currencies, Unset):
            payment_currencies = self.payment_currencies

        primary_contact_name = self.primary_contact_name

        primary_contact_email = self.primary_contact_email

        countries: Union[Unset, List[str]] = UNSET
        if not isinstance(self.countries, Unset):
            countries = self.countries

        time_zone = self.time_zone

        listed_in_directory = self.listed_in_directory

        geography_preset_id: Union[Unset, str] = UNSET
        if not isinstance(self.geography_preset_id, Unset):
            geography_preset_id = self.geography_preset_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if region_name is not UNSET:
            field_dict["regionName"] = region_name
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if billing_email is not UNSET:
            field_dict["billingEmail"] = billing_email
        if billing_address is not UNSET:
            field_dict["billingAddress"] = billing_address
        if billing_address_parts is not UNSET:
            field_dict["billingAddressParts"] = billing_address_parts
        if tax_id is not UNSET:
            field_dict["taxId"] = tax_id
        if currency is not UNSET:
            field_dict["currency"] = currency
        if other_currencies is not UNSET:
            field_dict["otherCurrencies"] = other_currencies
        if payment_currencies is not UNSET:
            field_dict["paymentCurrencies"] = payment_currencies
        if primary_contact_name is not UNSET:
            field_dict["primaryContactName"] = primary_contact_name
        if primary_contact_email is not UNSET:
            field_dict["primaryContactEmail"] = primary_contact_email
        if countries is not UNSET:
            field_dict["countries"] = countries
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if listed_in_directory is not UNSET:
            field_dict["listedInDirectory"] = listed_in_directory
        if geography_preset_id is not UNSET:
            field_dict["geographyPresetId"] = geography_preset_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.postal_address_input import PostalAddressInput

        d = src_dict.copy()
        region_name = d.pop("regionName", UNSET)

        company_name = d.pop("companyName", UNSET)

        billing_email = d.pop("billingEmail", UNSET)

        billing_address = d.pop("billingAddress", UNSET)

        _billing_address_parts = d.pop("billingAddressParts", UNSET)
        billing_address_parts: Union[Unset, PostalAddressInput]
        if isinstance(_billing_address_parts, Unset):
            billing_address_parts = UNSET
        else:
            billing_address_parts = PostalAddressInput.from_dict(_billing_address_parts)

        tax_id = d.pop("taxId", UNSET)

        currency = d.pop("currency", UNSET)

        other_currencies = cast(List[str], d.pop("otherCurrencies", UNSET))

        payment_currencies = cast(List[str], d.pop("paymentCurrencies", UNSET))

        primary_contact_name = d.pop("primaryContactName", UNSET)

        primary_contact_email = d.pop("primaryContactEmail", UNSET)

        countries = cast(List[str], d.pop("countries", UNSET))

        time_zone = d.pop("timeZone", UNSET)

        listed_in_directory = d.pop("listedInDirectory", UNSET)

        _geography_preset_id = d.pop("geographyPresetId", UNSET)
        geography_preset_id: Union[Unset, UpdateOrgProfileInputGeographyPresetId]
        if isinstance(_geography_preset_id, Unset):
            geography_preset_id = UNSET
        else:
            geography_preset_id = check_update_org_profile_input_geography_preset_id(
                _geography_preset_id
            )

        update_org_profile_input = cls(
            region_name=region_name,
            company_name=company_name,
            billing_email=billing_email,
            billing_address=billing_address,
            billing_address_parts=billing_address_parts,
            tax_id=tax_id,
            currency=currency,
            other_currencies=other_currencies,
            payment_currencies=payment_currencies,
            primary_contact_name=primary_contact_name,
            primary_contact_email=primary_contact_email,
            countries=countries,
            time_zone=time_zone,
            listed_in_directory=listed_in_directory,
            geography_preset_id=geography_preset_id,
        )

        update_org_profile_input.additional_properties = d
        return update_org_profile_input

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
