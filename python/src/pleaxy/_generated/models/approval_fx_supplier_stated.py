from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApprovalFxSupplierStated")


@_attrs_define
class ApprovalFxSupplierStated:
    """
    Attributes:
        amount (Union[Unset, float]):
        rate_source (Union[Unset, str]):
        rate_date (Union[Unset, str]):
    """

    amount: Union[Unset, float] = UNSET
    rate_source: Union[Unset, str] = UNSET
    rate_date: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount

        rate_source = self.rate_source

        rate_date = self.rate_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if rate_source is not UNSET:
            field_dict["rateSource"] = rate_source
        if rate_date is not UNSET:
            field_dict["rateDate"] = rate_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amount = d.pop("amount", UNSET)

        rate_source = d.pop("rateSource", UNSET)

        rate_date = d.pop("rateDate", UNSET)

        approval_fx_supplier_stated = cls(
            amount=amount,
            rate_source=rate_source,
            rate_date=rate_date,
        )

        approval_fx_supplier_stated.additional_properties = d
        return approval_fx_supplier_stated

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
