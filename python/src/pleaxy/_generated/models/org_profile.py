from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.org_profile_role import OrgProfileRole, check_org_profile_role
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.geography import Geography
    from ..models.postal_address import PostalAddress


T = TypeVar("T", bound="OrgProfile")


@_attrs_define
class OrgProfile:
    """
    Attributes:
        id (str):
        role (Union[Unset, OrgProfileRole]):
        region_id (Union[Unset, str]):
        region_name (Union[Unset, str]):
        company_name (Union[Unset, str]):
        billing_email (Union[Unset, str]):
        billing_address (Union[Unset, str]):
        billing_address_parts (Union[Unset, PostalAddress]):
        tax_id (Union[Unset, str]):
        currency (Union[Unset, str]):
        other_currencies (Union[Unset, List[str]]):
        payment_currencies (Union[Unset, List[str]]):
        fx_warning_pct (Union[Unset, float]):
        countries (Union[Unset, List[str]]):
        geography (Union[Unset, Geography]):
        time_zone (Union[Unset, str]):
        primary_contact_name (Union[Unset, str]):
        primary_contact_email (Union[Unset, str]):
        created_at (Union[Unset, str]):
        verified (Union[Unset, bool]):
    """

    id: str
    role: Union[Unset, OrgProfileRole] = UNSET
    region_id: Union[Unset, str] = UNSET
    region_name: Union[Unset, str] = UNSET
    company_name: Union[Unset, str] = UNSET
    billing_email: Union[Unset, str] = UNSET
    billing_address: Union[Unset, str] = UNSET
    billing_address_parts: Union[Unset, "PostalAddress"] = UNSET
    tax_id: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    other_currencies: Union[Unset, List[str]] = UNSET
    payment_currencies: Union[Unset, List[str]] = UNSET
    fx_warning_pct: Union[Unset, float] = UNSET
    countries: Union[Unset, List[str]] = UNSET
    geography: Union[Unset, "Geography"] = UNSET
    time_zone: Union[Unset, str] = UNSET
    primary_contact_name: Union[Unset, str] = UNSET
    primary_contact_email: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    verified: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role

        region_id = self.region_id

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

        fx_warning_pct = self.fx_warning_pct

        countries: Union[Unset, List[str]] = UNSET
        if not isinstance(self.countries, Unset):
            countries = self.countries

        geography: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.geography, Unset):
            geography = self.geography.to_dict()

        time_zone = self.time_zone

        primary_contact_name = self.primary_contact_name

        primary_contact_email = self.primary_contact_email

        created_at = self.created_at

        verified = self.verified

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if role is not UNSET:
            field_dict["role"] = role
        if region_id is not UNSET:
            field_dict["regionId"] = region_id
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
        if fx_warning_pct is not UNSET:
            field_dict["fxWarningPct"] = fx_warning_pct
        if countries is not UNSET:
            field_dict["countries"] = countries
        if geography is not UNSET:
            field_dict["geography"] = geography
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if primary_contact_name is not UNSET:
            field_dict["primaryContactName"] = primary_contact_name
        if primary_contact_email is not UNSET:
            field_dict["primaryContactEmail"] = primary_contact_email
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if verified is not UNSET:
            field_dict["verified"] = verified

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.geography import Geography
        from ..models.postal_address import PostalAddress

        d = src_dict.copy()
        id = d.pop("id")

        _role = d.pop("role", UNSET)
        role: Union[Unset, OrgProfileRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = check_org_profile_role(_role)

        region_id = d.pop("regionId", UNSET)

        region_name = d.pop("regionName", UNSET)

        company_name = d.pop("companyName", UNSET)

        billing_email = d.pop("billingEmail", UNSET)

        billing_address = d.pop("billingAddress", UNSET)

        _billing_address_parts = d.pop("billingAddressParts", UNSET)
        billing_address_parts: Union[Unset, PostalAddress]
        if isinstance(_billing_address_parts, Unset):
            billing_address_parts = UNSET
        else:
            billing_address_parts = PostalAddress.from_dict(_billing_address_parts)

        tax_id = d.pop("taxId", UNSET)

        currency = d.pop("currency", UNSET)

        other_currencies = cast(List[str], d.pop("otherCurrencies", UNSET))

        payment_currencies = cast(List[str], d.pop("paymentCurrencies", UNSET))

        fx_warning_pct = d.pop("fxWarningPct", UNSET)

        countries = cast(List[str], d.pop("countries", UNSET))

        _geography = d.pop("geography", UNSET)
        geography: Union[Unset, Geography]
        if isinstance(_geography, Unset):
            geography = UNSET
        else:
            geography = Geography.from_dict(_geography)

        time_zone = d.pop("timeZone", UNSET)

        primary_contact_name = d.pop("primaryContactName", UNSET)

        primary_contact_email = d.pop("primaryContactEmail", UNSET)

        created_at = d.pop("createdAt", UNSET)

        verified = d.pop("verified", UNSET)

        org_profile = cls(
            id=id,
            role=role,
            region_id=region_id,
            region_name=region_name,
            company_name=company_name,
            billing_email=billing_email,
            billing_address=billing_address,
            billing_address_parts=billing_address_parts,
            tax_id=tax_id,
            currency=currency,
            other_currencies=other_currencies,
            payment_currencies=payment_currencies,
            fx_warning_pct=fx_warning_pct,
            countries=countries,
            geography=geography,
            time_zone=time_zone,
            primary_contact_name=primary_contact_name,
            primary_contact_email=primary_contact_email,
            created_at=created_at,
            verified=verified,
        )

        org_profile.additional_properties = d
        return org_profile

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
