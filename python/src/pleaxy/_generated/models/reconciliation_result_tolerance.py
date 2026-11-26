from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reconciliation_result_tolerance_receipt import (
        ReconciliationResultToleranceReceipt,
    )


T = TypeVar("T", bound="ReconciliationResultTolerance")


@_attrs_define
class ReconciliationResultTolerance:
    """
    Attributes:
        percent (Union[Unset, float]):
        receipt (Union[Unset, ReconciliationResultToleranceReceipt]):
    """

    percent: Union[Unset, float] = UNSET
    receipt: Union[Unset, "ReconciliationResultToleranceReceipt"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        percent = self.percent

        receipt: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.receipt, Unset):
            receipt = self.receipt.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if percent is not UNSET:
            field_dict["percent"] = percent
        if receipt is not UNSET:
            field_dict["receipt"] = receipt

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reconciliation_result_tolerance_receipt import (
            ReconciliationResultToleranceReceipt,
        )

        d = src_dict.copy()
        percent = d.pop("percent", UNSET)

        _receipt = d.pop("receipt", UNSET)
        receipt: Union[Unset, ReconciliationResultToleranceReceipt]
        if isinstance(_receipt, Unset):
            receipt = UNSET
        else:
            receipt = ReconciliationResultToleranceReceipt.from_dict(_receipt)

        reconciliation_result_tolerance = cls(
            percent=percent,
            receipt=receipt,
        )

        reconciliation_result_tolerance.additional_properties = d
        return reconciliation_result_tolerance

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
