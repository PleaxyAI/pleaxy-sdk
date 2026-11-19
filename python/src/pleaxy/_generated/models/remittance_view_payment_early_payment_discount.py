from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RemittanceViewPaymentEarlyPaymentDiscount")


@_attrs_define
class RemittanceViewPaymentEarlyPaymentDiscount:
    """
    Attributes:
        percent (Union[Unset, float]):
        amount (Union[Unset, float]):
    """

    percent: Union[Unset, float] = UNSET
    amount: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        percent = self.percent

        amount = self.amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if percent is not UNSET:
            field_dict["percent"] = percent
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        percent = d.pop("percent", UNSET)

        amount = d.pop("amount", UNSET)

        remittance_view_payment_early_payment_discount = cls(
            percent=percent,
            amount=amount,
        )

        remittance_view_payment_early_payment_discount.additional_properties = d
        return remittance_view_payment_early_payment_discount

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
