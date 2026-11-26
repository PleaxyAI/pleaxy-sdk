from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReconciliationResultToleranceReceipt")


@_attrs_define
class ReconciliationResultToleranceReceipt:
    """
    Attributes:
        percent (Union[Unset, float]):
        max_amount (Union[Unset, str]):
    """

    percent: Union[Unset, float] = UNSET
    max_amount: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        percent = self.percent

        max_amount = self.max_amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if percent is not UNSET:
            field_dict["percent"] = percent
        if max_amount is not UNSET:
            field_dict["max_amount"] = max_amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        percent = d.pop("percent", UNSET)

        max_amount = d.pop("max_amount", UNSET)

        reconciliation_result_tolerance_receipt = cls(
            percent=percent,
            max_amount=max_amount,
        )

        reconciliation_result_tolerance_receipt.additional_properties = d
        return reconciliation_result_tolerance_receipt

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
