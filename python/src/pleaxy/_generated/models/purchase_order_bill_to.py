from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.purchase_order_bill_to_source import (
    PurchaseOrderBillToSource,
    check_purchase_order_bill_to_source,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.postal_address import PostalAddress


T = TypeVar("T", bound="PurchaseOrderBillTo")


@_attrs_define
class PurchaseOrderBillTo:
    """
    Attributes:
        source (Union[Unset, PurchaseOrderBillToSource]):
        company_name (Union[Unset, str]):
        address (Union[Unset, PostalAddress]):
        address_text (Union[Unset, str]):
        tax_id (Union[Unset, str]):
    """

    source: Union[Unset, PurchaseOrderBillToSource] = UNSET
    company_name: Union[Unset, str] = UNSET
    address: Union[Unset, "PostalAddress"] = UNSET
    address_text: Union[Unset, str] = UNSET
    tax_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source

        company_name = self.company_name

        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        address_text = self.address_text

        tax_id = self.tax_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source is not UNSET:
            field_dict["source"] = source
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if address is not UNSET:
            field_dict["address"] = address
        if address_text is not UNSET:
            field_dict["addressText"] = address_text
        if tax_id is not UNSET:
            field_dict["taxId"] = tax_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.postal_address import PostalAddress

        d = src_dict.copy()
        _source = d.pop("source", UNSET)
        source: Union[Unset, PurchaseOrderBillToSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = check_purchase_order_bill_to_source(_source)

        company_name = d.pop("companyName", UNSET)

        _address = d.pop("address", UNSET)
        address: Union[Unset, PostalAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = PostalAddress.from_dict(_address)

        address_text = d.pop("addressText", UNSET)

        tax_id = d.pop("taxId", UNSET)

        purchase_order_bill_to = cls(
            source=source,
            company_name=company_name,
            address=address,
            address_text=address_text,
            tax_id=tax_id,
        )

        purchase_order_bill_to.additional_properties = d
        return purchase_order_bill_to

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
