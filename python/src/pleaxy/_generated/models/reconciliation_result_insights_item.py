from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReconciliationResultInsightsItem")


@_attrs_define
class ReconciliationResultInsightsItem:
    """
    Attributes:
        code (Union[Unset, str]):
        invoice_line (Union[Unset, float]):
        order_line (Union[Unset, float]):
    """

    code: Union[Unset, str] = UNSET
    invoice_line: Union[Unset, float] = UNSET
    order_line: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code

        invoice_line = self.invoice_line

        order_line = self.order_line

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if invoice_line is not UNSET:
            field_dict["invoice_line"] = invoice_line
        if order_line is not UNSET:
            field_dict["order_line"] = order_line

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code", UNSET)

        invoice_line = d.pop("invoice_line", UNSET)

        order_line = d.pop("order_line", UNSET)

        reconciliation_result_insights_item = cls(
            code=code,
            invoice_line=invoice_line,
            order_line=order_line,
        )

        reconciliation_result_insights_item.additional_properties = d
        return reconciliation_result_insights_item

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
