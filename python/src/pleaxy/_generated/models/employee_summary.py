from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EmployeeSummary")


@_attrs_define
class EmployeeSummary:
    """
    Attributes:
        key (Union[Unset, str]):
        name (Union[Unset, str]):
        email (Union[Unset, str]):
        title (Union[Unset, str]):
        can_approve_purchase_orders (Union[Unset, bool]):
        can_approve_invoices (Union[Unset, bool]):
    """

    key: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    can_approve_purchase_orders: Union[Unset, bool] = UNSET
    can_approve_invoices: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key

        name = self.name

        email = self.email

        title = self.title

        can_approve_purchase_orders = self.can_approve_purchase_orders

        can_approve_invoices = self.can_approve_invoices

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email
        if title is not UNSET:
            field_dict["title"] = title
        if can_approve_purchase_orders is not UNSET:
            field_dict["canApprovePurchaseOrders"] = can_approve_purchase_orders
        if can_approve_invoices is not UNSET:
            field_dict["canApproveInvoices"] = can_approve_invoices

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key = d.pop("key", UNSET)

        name = d.pop("name", UNSET)

        email = d.pop("email", UNSET)

        title = d.pop("title", UNSET)

        can_approve_purchase_orders = d.pop("canApprovePurchaseOrders", UNSET)

        can_approve_invoices = d.pop("canApproveInvoices", UNSET)

        employee_summary = cls(
            key=key,
            name=name,
            email=email,
            title=title,
            can_approve_purchase_orders=can_approve_purchase_orders,
            can_approve_invoices=can_approve_invoices,
        )

        employee_summary.additional_properties = d
        return employee_summary

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
