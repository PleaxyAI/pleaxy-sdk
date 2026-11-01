from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FocusCostCenterTotal")


@_attrs_define
class FocusCostCenterTotal:
    """
    Attributes:
        cost_center (Union[Unset, str]):
        service_category (Union[Unset, str]):
        currency (Union[Unset, str]):
        amount (Union[Unset, float]):
    """

    cost_center: Union[Unset, str] = UNSET
    service_category: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    amount: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cost_center = self.cost_center

        service_category = self.service_category

        currency = self.currency

        amount = self.amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cost_center is not UNSET:
            field_dict["costCenter"] = cost_center
        if service_category is not UNSET:
            field_dict["serviceCategory"] = service_category
        if currency is not UNSET:
            field_dict["currency"] = currency
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cost_center = d.pop("costCenter", UNSET)

        service_category = d.pop("serviceCategory", UNSET)

        currency = d.pop("currency", UNSET)

        amount = d.pop("amount", UNSET)

        focus_cost_center_total = cls(
            cost_center=cost_center,
            service_category=service_category,
            currency=currency,
            amount=amount,
        )

        focus_cost_center_total.additional_properties = d
        return focus_cost_center_total

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
