from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_invoice_result_buyer_invoice_receipt_tolerance_applied_lines_item import (
        GetInvoiceResultBuyerInvoiceReceiptToleranceAppliedLinesItem,
    )


T = TypeVar("T", bound="GetInvoiceResultBuyerInvoiceReceiptToleranceApplied")


@_attrs_define
class GetInvoiceResultBuyerInvoiceReceiptToleranceApplied:
    """
    Attributes:
        over (Union[Unset, float]):
        received (Union[Unset, float]):
        percent (Union[Unset, float]):
        max_amount (Union[Unset, float]):
        lines (Union[Unset, List['GetInvoiceResultBuyerInvoiceReceiptToleranceAppliedLinesItem']]):
        at (Union[Unset, str]):
    """

    over: Union[Unset, float] = UNSET
    received: Union[Unset, float] = UNSET
    percent: Union[Unset, float] = UNSET
    max_amount: Union[Unset, float] = UNSET
    lines: Union[
        Unset, List["GetInvoiceResultBuyerInvoiceReceiptToleranceAppliedLinesItem"]
    ] = UNSET
    at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        over = self.over

        received = self.received

        percent = self.percent

        max_amount = self.max_amount

        lines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        at = self.at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if over is not UNSET:
            field_dict["over"] = over
        if received is not UNSET:
            field_dict["received"] = received
        if percent is not UNSET:
            field_dict["percent"] = percent
        if max_amount is not UNSET:
            field_dict["maxAmount"] = max_amount
        if lines is not UNSET:
            field_dict["lines"] = lines
        if at is not UNSET:
            field_dict["at"] = at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_invoice_result_buyer_invoice_receipt_tolerance_applied_lines_item import (
            GetInvoiceResultBuyerInvoiceReceiptToleranceAppliedLinesItem,
        )

        d = src_dict.copy()
        over = d.pop("over", UNSET)

        received = d.pop("received", UNSET)

        percent = d.pop("percent", UNSET)

        max_amount = d.pop("maxAmount", UNSET)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = (
                GetInvoiceResultBuyerInvoiceReceiptToleranceAppliedLinesItem.from_dict(
                    lines_item_data
                )
            )

            lines.append(lines_item)

        at = d.pop("at", UNSET)

        get_invoice_result_buyer_invoice_receipt_tolerance_applied = cls(
            over=over,
            received=received,
            percent=percent,
            max_amount=max_amount,
            lines=lines,
            at=at,
        )

        get_invoice_result_buyer_invoice_receipt_tolerance_applied.additional_properties = d
        return get_invoice_result_buyer_invoice_receipt_tolerance_applied

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
