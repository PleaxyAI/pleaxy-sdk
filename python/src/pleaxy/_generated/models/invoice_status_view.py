from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_status_view_cxml_status import (
    InvoiceStatusViewCxmlStatus,
    check_invoice_status_view_cxml_status,
)
from ..models.invoice_status_view_document_type import (
    InvoiceStatusViewDocumentType,
    check_invoice_status_view_document_type,
)
from ..models.invoice_status_view_query_reason import (
    InvoiceStatusViewQueryReason,
    check_invoice_status_view_query_reason,
)
from ..models.invoice_status_view_response_code import (
    InvoiceStatusViewResponseCode,
    check_invoice_status_view_response_code,
)
from ..models.invoice_status_view_status import (
    InvoiceStatusViewStatus,
    check_invoice_status_view_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_status_view_amount_due import InvoiceStatusViewAmountDue
    from ..models.invoice_status_view_rejection import InvoiceStatusViewRejection
    from ..models.invoice_status_view_total import InvoiceStatusViewTotal


T = TypeVar("T", bound="InvoiceStatusView")


@_attrs_define
class InvoiceStatusView:
    """
    Attributes:
        invoice_id (Union[Unset, str]):
        invoice_number (Union[Unset, str]):
        document_type (Union[Unset, InvoiceStatusViewDocumentType]):
        buyer_workspace_id (Union[Unset, str]):
        purchase_order_id (Union[Unset, str]):
        status (Union[Unset, InvoiceStatusViewStatus]):
        response_code (Union[Unset, InvoiceStatusViewResponseCode]):
        cxml_status (Union[Unset, InvoiceStatusViewCxmlStatus]):
        query_reason (Union[Unset, InvoiceStatusViewQueryReason]):
        rejection (Union[Unset, InvoiceStatusViewRejection]):
        replaced_by_invoice_ids (Union[Unset, List[str]]):
        issue_date (Union[Unset, str]):
        received_at (Union[Unset, str]):
        due_date (Union[Unset, str]):
        total (Union[Unset, InvoiceStatusViewTotal]):
        amount_due (Union[Unset, InvoiceStatusViewAmountDue]):
        paid (Union[Unset, bool]):
        paid_at (Union[Unset, str]):
    """

    invoice_id: Union[Unset, str] = UNSET
    invoice_number: Union[Unset, str] = UNSET
    document_type: Union[Unset, InvoiceStatusViewDocumentType] = UNSET
    buyer_workspace_id: Union[Unset, str] = UNSET
    purchase_order_id: Union[Unset, str] = UNSET
    status: Union[Unset, InvoiceStatusViewStatus] = UNSET
    response_code: Union[Unset, InvoiceStatusViewResponseCode] = UNSET
    cxml_status: Union[Unset, InvoiceStatusViewCxmlStatus] = UNSET
    query_reason: Union[Unset, InvoiceStatusViewQueryReason] = UNSET
    rejection: Union[Unset, "InvoiceStatusViewRejection"] = UNSET
    replaced_by_invoice_ids: Union[Unset, List[str]] = UNSET
    issue_date: Union[Unset, str] = UNSET
    received_at: Union[Unset, str] = UNSET
    due_date: Union[Unset, str] = UNSET
    total: Union[Unset, "InvoiceStatusViewTotal"] = UNSET
    amount_due: Union[Unset, "InvoiceStatusViewAmountDue"] = UNSET
    paid: Union[Unset, bool] = UNSET
    paid_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoice_id = self.invoice_id

        invoice_number = self.invoice_number

        document_type: Union[Unset, str] = UNSET
        if not isinstance(self.document_type, Unset):
            document_type = self.document_type

        buyer_workspace_id = self.buyer_workspace_id

        purchase_order_id = self.purchase_order_id

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        response_code: Union[Unset, str] = UNSET
        if not isinstance(self.response_code, Unset):
            response_code = self.response_code

        cxml_status: Union[Unset, str] = UNSET
        if not isinstance(self.cxml_status, Unset):
            cxml_status = self.cxml_status

        query_reason: Union[Unset, str] = UNSET
        if not isinstance(self.query_reason, Unset):
            query_reason = self.query_reason

        rejection: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rejection, Unset):
            rejection = self.rejection.to_dict()

        replaced_by_invoice_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.replaced_by_invoice_ids, Unset):
            replaced_by_invoice_ids = self.replaced_by_invoice_ids

        issue_date = self.issue_date

        received_at = self.received_at

        due_date = self.due_date

        total: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.total, Unset):
            total = self.total.to_dict()

        amount_due: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.amount_due, Unset):
            amount_due = self.amount_due.to_dict()

        paid = self.paid

        paid_at = self.paid_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invoice_id is not UNSET:
            field_dict["invoiceId"] = invoice_id
        if invoice_number is not UNSET:
            field_dict["invoiceNumber"] = invoice_number
        if document_type is not UNSET:
            field_dict["documentType"] = document_type
        if buyer_workspace_id is not UNSET:
            field_dict["buyerWorkspaceId"] = buyer_workspace_id
        if purchase_order_id is not UNSET:
            field_dict["purchaseOrderId"] = purchase_order_id
        if status is not UNSET:
            field_dict["status"] = status
        if response_code is not UNSET:
            field_dict["responseCode"] = response_code
        if cxml_status is not UNSET:
            field_dict["cxmlStatus"] = cxml_status
        if query_reason is not UNSET:
            field_dict["queryReason"] = query_reason
        if rejection is not UNSET:
            field_dict["rejection"] = rejection
        if replaced_by_invoice_ids is not UNSET:
            field_dict["replacedByInvoiceIds"] = replaced_by_invoice_ids
        if issue_date is not UNSET:
            field_dict["issueDate"] = issue_date
        if received_at is not UNSET:
            field_dict["receivedAt"] = received_at
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if total is not UNSET:
            field_dict["total"] = total
        if amount_due is not UNSET:
            field_dict["amountDue"] = amount_due
        if paid is not UNSET:
            field_dict["paid"] = paid
        if paid_at is not UNSET:
            field_dict["paidAt"] = paid_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_status_view_amount_due import InvoiceStatusViewAmountDue
        from ..models.invoice_status_view_rejection import InvoiceStatusViewRejection
        from ..models.invoice_status_view_total import InvoiceStatusViewTotal

        d = src_dict.copy()
        invoice_id = d.pop("invoiceId", UNSET)

        invoice_number = d.pop("invoiceNumber", UNSET)

        _document_type = d.pop("documentType", UNSET)
        document_type: Union[Unset, InvoiceStatusViewDocumentType]
        if isinstance(_document_type, Unset):
            document_type = UNSET
        else:
            document_type = check_invoice_status_view_document_type(_document_type)

        buyer_workspace_id = d.pop("buyerWorkspaceId", UNSET)

        purchase_order_id = d.pop("purchaseOrderId", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, InvoiceStatusViewStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_invoice_status_view_status(_status)

        _response_code = d.pop("responseCode", UNSET)
        response_code: Union[Unset, InvoiceStatusViewResponseCode]
        if isinstance(_response_code, Unset):
            response_code = UNSET
        else:
            response_code = check_invoice_status_view_response_code(_response_code)

        _cxml_status = d.pop("cxmlStatus", UNSET)
        cxml_status: Union[Unset, InvoiceStatusViewCxmlStatus]
        if isinstance(_cxml_status, Unset):
            cxml_status = UNSET
        else:
            cxml_status = check_invoice_status_view_cxml_status(_cxml_status)

        _query_reason = d.pop("queryReason", UNSET)
        query_reason: Union[Unset, InvoiceStatusViewQueryReason]
        if isinstance(_query_reason, Unset):
            query_reason = UNSET
        else:
            query_reason = check_invoice_status_view_query_reason(_query_reason)

        _rejection = d.pop("rejection", UNSET)
        rejection: Union[Unset, InvoiceStatusViewRejection]
        if isinstance(_rejection, Unset):
            rejection = UNSET
        else:
            rejection = InvoiceStatusViewRejection.from_dict(_rejection)

        replaced_by_invoice_ids = cast(List[str], d.pop("replacedByInvoiceIds", UNSET))

        issue_date = d.pop("issueDate", UNSET)

        received_at = d.pop("receivedAt", UNSET)

        due_date = d.pop("dueDate", UNSET)

        _total = d.pop("total", UNSET)
        total: Union[Unset, InvoiceStatusViewTotal]
        if isinstance(_total, Unset):
            total = UNSET
        else:
            total = InvoiceStatusViewTotal.from_dict(_total)

        _amount_due = d.pop("amountDue", UNSET)
        amount_due: Union[Unset, InvoiceStatusViewAmountDue]
        if isinstance(_amount_due, Unset):
            amount_due = UNSET
        else:
            amount_due = InvoiceStatusViewAmountDue.from_dict(_amount_due)

        paid = d.pop("paid", UNSET)

        paid_at = d.pop("paidAt", UNSET)

        invoice_status_view = cls(
            invoice_id=invoice_id,
            invoice_number=invoice_number,
            document_type=document_type,
            buyer_workspace_id=buyer_workspace_id,
            purchase_order_id=purchase_order_id,
            status=status,
            response_code=response_code,
            cxml_status=cxml_status,
            query_reason=query_reason,
            rejection=rejection,
            replaced_by_invoice_ids=replaced_by_invoice_ids,
            issue_date=issue_date,
            received_at=received_at,
            due_date=due_date,
            total=total,
            amount_due=amount_due,
            paid=paid,
            paid_at=paid_at,
        )

        invoice_status_view.additional_properties = d
        return invoice_status_view

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
