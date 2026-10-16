from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_invoices_item_supplier_credit_note_history_item_action import (
    ListInvoicesItemSupplierCreditNoteHistoryItemAction,
    check_list_invoices_item_supplier_credit_note_history_item_action,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListInvoicesItemSupplierCreditNoteHistoryItem")


@_attrs_define
class ListInvoicesItemSupplierCreditNoteHistoryItem:
    """
    Attributes:
        at (Union[Unset, str]):
        amount (Union[Unset, float]):
        invoice_id (Union[Unset, str]):
        action (Union[Unset, ListInvoicesItemSupplierCreditNoteHistoryItemAction]):
        export_id (Union[Unset, str]):
    """

    at: Union[Unset, str] = UNSET
    amount: Union[Unset, float] = UNSET
    invoice_id: Union[Unset, str] = UNSET
    action: Union[Unset, ListInvoicesItemSupplierCreditNoteHistoryItemAction] = UNSET
    export_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        at = self.at

        amount = self.amount

        invoice_id = self.invoice_id

        action: Union[Unset, str] = UNSET
        if not isinstance(self.action, Unset):
            action = self.action

        export_id = self.export_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if amount is not UNSET:
            field_dict["amount"] = amount
        if invoice_id is not UNSET:
            field_dict["invoiceId"] = invoice_id
        if action is not UNSET:
            field_dict["action"] = action
        if export_id is not UNSET:
            field_dict["exportId"] = export_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        at = d.pop("at", UNSET)

        amount = d.pop("amount", UNSET)

        invoice_id = d.pop("invoiceId", UNSET)

        _action = d.pop("action", UNSET)
        action: Union[Unset, ListInvoicesItemSupplierCreditNoteHistoryItemAction]
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = check_list_invoices_item_supplier_credit_note_history_item_action(
                _action
            )

        export_id = d.pop("exportId", UNSET)

        list_invoices_item_supplier_credit_note_history_item = cls(
            at=at,
            amount=amount,
            invoice_id=invoice_id,
            action=action,
            export_id=export_id,
        )

        list_invoices_item_supplier_credit_note_history_item.additional_properties = d
        return list_invoices_item_supplier_credit_note_history_item

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
