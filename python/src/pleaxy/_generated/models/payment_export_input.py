from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PaymentExportInput")


@_attrs_define
class PaymentExportInput:
    """
    Attributes:
        invoice_ids (Union[Unset, List[str]]):
        confirm_replaced (Union[Unset, bool]):
    """

    invoice_ids: Union[Unset, List[str]] = UNSET
    confirm_replaced: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoice_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.invoice_ids, Unset):
            invoice_ids = self.invoice_ids

        confirm_replaced = self.confirm_replaced

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invoice_ids is not UNSET:
            field_dict["invoiceIds"] = invoice_ids
        if confirm_replaced is not UNSET:
            field_dict["confirmReplaced"] = confirm_replaced

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        invoice_ids = cast(List[str], d.pop("invoiceIds", UNSET))

        confirm_replaced = d.pop("confirmReplaced", UNSET)

        payment_export_input = cls(
            invoice_ids=invoice_ids,
            confirm_replaced=confirm_replaced,
        )

        payment_export_input.additional_properties = d
        return payment_export_input

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
