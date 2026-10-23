from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.store_order_confirmation_lines_item_status import (
    StoreOrderConfirmationLinesItemStatus,
    check_store_order_confirmation_lines_item_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="StoreOrderConfirmationLinesItem")


@_attrs_define
class StoreOrderConfirmationLinesItem:
    """
    Attributes:
        line_no (Union[Unset, float]):
        status (Union[Unset, StoreOrderConfirmationLinesItemStatus]):
        quantity (Union[Unset, float]):
        reason (Union[Unset, str]):
    """

    line_no: Union[Unset, float] = UNSET
    status: Union[Unset, StoreOrderConfirmationLinesItemStatus] = UNSET
    quantity: Union[Unset, float] = UNSET
    reason: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        line_no = self.line_no

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        quantity = self.quantity

        reason = self.reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if line_no is not UNSET:
            field_dict["lineNo"] = line_no
        if status is not UNSET:
            field_dict["status"] = status
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        line_no = d.pop("lineNo", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, StoreOrderConfirmationLinesItemStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_store_order_confirmation_lines_item_status(_status)

        quantity = d.pop("quantity", UNSET)

        reason = d.pop("reason", UNSET)

        store_order_confirmation_lines_item = cls(
            line_no=line_no,
            status=status,
            quantity=quantity,
            reason=reason,
        )

        store_order_confirmation_lines_item.additional_properties = d
        return store_order_confirmation_lines_item

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
