from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.postal_address_input import PostalAddressInput


T = TypeVar("T", bound="BillToPartyInput")


@_attrs_define
class BillToPartyInput:
    """
    Attributes:
        address (PostalAddressInput):
        company_name (Union[Unset, str]): The company the supplier invoices. Defaults to the buyer's company name.
        tax_id (Union[Unset, str]): That company's tax id (VAT number, CUIT, EIN...). None when left out.
    """

    address: "PostalAddressInput"
    company_name: Union[Unset, str] = UNSET
    tax_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address = self.address.to_dict()

        company_name = self.company_name

        tax_id = self.tax_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "address": address,
            }
        )
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if tax_id is not UNSET:
            field_dict["taxId"] = tax_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.postal_address_input import PostalAddressInput

        d = src_dict.copy()
        address = PostalAddressInput.from_dict(d.pop("address"))

        company_name = d.pop("companyName", UNSET)

        tax_id = d.pop("taxId", UNSET)

        bill_to_party_input = cls(
            address=address,
            company_name=company_name,
            tax_id=tax_id,
        )

        bill_to_party_input.additional_properties = d
        return bill_to_party_input

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
