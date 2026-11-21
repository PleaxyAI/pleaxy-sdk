from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.early_payment_discount_taken_source import (
    EarlyPaymentDiscountTakenSource,
    check_early_payment_discount_taken_source,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EarlyPaymentDiscountTaken")


@_attrs_define
class EarlyPaymentDiscountTaken:
    """
    Attributes:
        percent (Union[Unset, float]):
        amount (Union[Unset, float]):
        deadline (Union[Unset, str]):
        source (Union[Unset, EarlyPaymentDiscountTakenSource]):
    """

    percent: Union[Unset, float] = UNSET
    amount: Union[Unset, float] = UNSET
    deadline: Union[Unset, str] = UNSET
    source: Union[Unset, EarlyPaymentDiscountTakenSource] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        percent = self.percent

        amount = self.amount

        deadline = self.deadline

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if percent is not UNSET:
            field_dict["percent"] = percent
        if amount is not UNSET:
            field_dict["amount"] = amount
        if deadline is not UNSET:
            field_dict["deadline"] = deadline
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        percent = d.pop("percent", UNSET)

        amount = d.pop("amount", UNSET)

        deadline = d.pop("deadline", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, EarlyPaymentDiscountTakenSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = check_early_payment_discount_taken_source(_source)

        early_payment_discount_taken = cls(
            percent=percent,
            amount=amount,
            deadline=deadline,
            source=source,
        )

        early_payment_discount_taken.additional_properties = d
        return early_payment_discount_taken

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
