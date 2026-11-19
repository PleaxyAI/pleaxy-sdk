from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudUsageLine")


@_attrs_define
class CloudUsageLine:
    """
    Attributes:
        service (Union[Unset, str]):
        sku (Union[Unset, str]):
        project (Union[Unset, str]):
        amount (Union[Unset, float]):
    """

    service: Union[Unset, str] = UNSET
    sku: Union[Unset, str] = UNSET
    project: Union[Unset, str] = UNSET
    amount: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service = self.service

        sku = self.sku

        project = self.project

        amount = self.amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service is not UNSET:
            field_dict["service"] = service
        if sku is not UNSET:
            field_dict["sku"] = sku
        if project is not UNSET:
            field_dict["project"] = project
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        service = d.pop("service", UNSET)

        sku = d.pop("sku", UNSET)

        project = d.pop("project", UNSET)

        amount = d.pop("amount", UNSET)

        cloud_usage_line = cls(
            service=service,
            sku=sku,
            project=project,
            amount=amount,
        )

        cloud_usage_line.additional_properties = d
        return cloud_usage_line

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
