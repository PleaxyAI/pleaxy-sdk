from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="CreateInvoiceResultBuyerInvoiceReceiptToleranceAppliedLinesItem"
)


@_attrs_define
class CreateInvoiceResultBuyerInvoiceReceiptToleranceAppliedLinesItem:
    """
    Attributes:
        po_line_no (Union[Unset, float]):
        over (Union[Unset, float]):
    """

    po_line_no: Union[Unset, float] = UNSET
    over: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        po_line_no = self.po_line_no

        over = self.over

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if po_line_no is not UNSET:
            field_dict["poLineNo"] = po_line_no
        if over is not UNSET:
            field_dict["over"] = over

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        po_line_no = d.pop("poLineNo", UNSET)

        over = d.pop("over", UNSET)

        create_invoice_result_buyer_invoice_receipt_tolerance_applied_lines_item = cls(
            po_line_no=po_line_no,
            over=over,
        )

        create_invoice_result_buyer_invoice_receipt_tolerance_applied_lines_item.additional_properties = d
        return create_invoice_result_buyer_invoice_receipt_tolerance_applied_lines_item

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
