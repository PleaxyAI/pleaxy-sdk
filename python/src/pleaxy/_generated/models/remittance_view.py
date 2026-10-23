from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.remittance_view_status import (
    RemittanceViewStatus,
    check_remittance_view_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.remittance_view_amount_due import RemittanceViewAmountDue
    from ..models.remittance_view_payment import RemittanceViewPayment
    from ..models.remittance_view_remittances_item import RemittanceViewRemittancesItem


T = TypeVar("T", bound="RemittanceView")


@_attrs_define
class RemittanceView:
    """
    Attributes:
        invoice_id (Union[Unset, str]):
        invoice_number (Union[Unset, str]):
        buyer_workspace_id (Union[Unset, str]):
        purchase_order_id (Union[Unset, str]):
        status (Union[Unset, RemittanceViewStatus]):
        failed_at (Union[Unset, str]):
        paid (Union[Unset, bool]):
        paid_at (Union[Unset, str]):
        amount_due (Union[Unset, RemittanceViewAmountDue]):
        payment (Union[Unset, RemittanceViewPayment]):
        remittances (Union[Unset, List['RemittanceViewRemittancesItem']]):
    """

    invoice_id: Union[Unset, str] = UNSET
    invoice_number: Union[Unset, str] = UNSET
    buyer_workspace_id: Union[Unset, str] = UNSET
    purchase_order_id: Union[Unset, str] = UNSET
    status: Union[Unset, RemittanceViewStatus] = UNSET
    failed_at: Union[Unset, str] = UNSET
    paid: Union[Unset, bool] = UNSET
    paid_at: Union[Unset, str] = UNSET
    amount_due: Union[Unset, "RemittanceViewAmountDue"] = UNSET
    payment: Union[Unset, "RemittanceViewPayment"] = UNSET
    remittances: Union[Unset, List["RemittanceViewRemittancesItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoice_id = self.invoice_id

        invoice_number = self.invoice_number

        buyer_workspace_id = self.buyer_workspace_id

        purchase_order_id = self.purchase_order_id

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        failed_at = self.failed_at

        paid = self.paid

        paid_at = self.paid_at

        amount_due: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.amount_due, Unset):
            amount_due = self.amount_due.to_dict()

        payment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment, Unset):
            payment = self.payment.to_dict()

        remittances: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.remittances, Unset):
            remittances = []
            for remittances_item_data in self.remittances:
                remittances_item = remittances_item_data.to_dict()
                remittances.append(remittances_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invoice_id is not UNSET:
            field_dict["invoiceId"] = invoice_id
        if invoice_number is not UNSET:
            field_dict["invoiceNumber"] = invoice_number
        if buyer_workspace_id is not UNSET:
            field_dict["buyerWorkspaceId"] = buyer_workspace_id
        if purchase_order_id is not UNSET:
            field_dict["purchaseOrderId"] = purchase_order_id
        if status is not UNSET:
            field_dict["status"] = status
        if failed_at is not UNSET:
            field_dict["failedAt"] = failed_at
        if paid is not UNSET:
            field_dict["paid"] = paid
        if paid_at is not UNSET:
            field_dict["paidAt"] = paid_at
        if amount_due is not UNSET:
            field_dict["amountDue"] = amount_due
        if payment is not UNSET:
            field_dict["payment"] = payment
        if remittances is not UNSET:
            field_dict["remittances"] = remittances

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.remittance_view_amount_due import RemittanceViewAmountDue
        from ..models.remittance_view_payment import RemittanceViewPayment
        from ..models.remittance_view_remittances_item import (
            RemittanceViewRemittancesItem,
        )

        d = src_dict.copy()
        invoice_id = d.pop("invoiceId", UNSET)

        invoice_number = d.pop("invoiceNumber", UNSET)

        buyer_workspace_id = d.pop("buyerWorkspaceId", UNSET)

        purchase_order_id = d.pop("purchaseOrderId", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, RemittanceViewStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_remittance_view_status(_status)

        failed_at = d.pop("failedAt", UNSET)

        paid = d.pop("paid", UNSET)

        paid_at = d.pop("paidAt", UNSET)

        _amount_due = d.pop("amountDue", UNSET)
        amount_due: Union[Unset, RemittanceViewAmountDue]
        if isinstance(_amount_due, Unset):
            amount_due = UNSET
        else:
            amount_due = RemittanceViewAmountDue.from_dict(_amount_due)

        _payment = d.pop("payment", UNSET)
        payment: Union[Unset, RemittanceViewPayment]
        if isinstance(_payment, Unset):
            payment = UNSET
        else:
            payment = RemittanceViewPayment.from_dict(_payment)

        remittances = []
        _remittances = d.pop("remittances", UNSET)
        for remittances_item_data in _remittances or []:
            remittances_item = RemittanceViewRemittancesItem.from_dict(
                remittances_item_data
            )

            remittances.append(remittances_item)

        remittance_view = cls(
            invoice_id=invoice_id,
            invoice_number=invoice_number,
            buyer_workspace_id=buyer_workspace_id,
            purchase_order_id=purchase_order_id,
            status=status,
            failed_at=failed_at,
            paid=paid,
            paid_at=paid_at,
            amount_due=amount_due,
            payment=payment,
            remittances=remittances,
        )

        remittance_view.additional_properties = d
        return remittance_view

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
