from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.purchase_request_status import (
    PurchaseRequestStatus,
    check_purchase_request_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.approval_chain import ApprovalChain
    from ..models.budget_check import BudgetCheck
    from ..models.purchase_order_quote_document import PurchaseOrderQuoteDocument
    from ..models.purchase_request_line import PurchaseRequestLine
    from ..models.purchase_request_supplier import PurchaseRequestSupplier


T = TypeVar("T", bound="PurchaseRequest")


@_attrs_define
class PurchaseRequest:
    """
    Attributes:
        id (str):
        title (Union[Unset, str]):
        description (Union[Unset, str]):
        requester_employee_key (Union[Unset, str]):
        requester_name (Union[Unset, str]):
        cost_center (Union[Unset, str]):
        gl_code (Union[Unset, str]):
        supplier (Union[Unset, PurchaseRequestSupplier]):
        line_items (Union[Unset, List['PurchaseRequestLine']]):
        amount (Union[Unset, float]):
        currency (Union[Unset, str]):
        needed_by (Union[Unset, str]):
        quote_document (Union[Unset, PurchaseOrderQuoteDocument]):
        notes (Union[Unset, str]):
        status (Union[Unset, PurchaseRequestStatus]):
        approval (Union[Unset, ApprovalChain]):
        approval_version (Union[Unset, float]):
        budget_check (Union[Unset, BudgetCheck]):
        po_id (Union[Unset, str]):
        rejection_reason (Union[Unset, str]):
        created_at (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        submitted_at (Union[Unset, str]):
        decided_at (Union[Unset, str]):
        canceled_at (Union[Unset, str]):
        canceled_by (Union[Unset, str]):
    """

    id: str
    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    requester_employee_key: Union[Unset, str] = UNSET
    requester_name: Union[Unset, str] = UNSET
    cost_center: Union[Unset, str] = UNSET
    gl_code: Union[Unset, str] = UNSET
    supplier: Union[Unset, "PurchaseRequestSupplier"] = UNSET
    line_items: Union[Unset, List["PurchaseRequestLine"]] = UNSET
    amount: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    needed_by: Union[Unset, str] = UNSET
    quote_document: Union[Unset, "PurchaseOrderQuoteDocument"] = UNSET
    notes: Union[Unset, str] = UNSET
    status: Union[Unset, PurchaseRequestStatus] = UNSET
    approval: Union[Unset, "ApprovalChain"] = UNSET
    approval_version: Union[Unset, float] = UNSET
    budget_check: Union[Unset, "BudgetCheck"] = UNSET
    po_id: Union[Unset, str] = UNSET
    rejection_reason: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    submitted_at: Union[Unset, str] = UNSET
    decided_at: Union[Unset, str] = UNSET
    canceled_at: Union[Unset, str] = UNSET
    canceled_by: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        title = self.title

        description = self.description

        requester_employee_key = self.requester_employee_key

        requester_name = self.requester_name

        cost_center = self.cost_center

        gl_code = self.gl_code

        supplier: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.supplier, Unset):
            supplier = self.supplier.to_dict()

        line_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.line_items, Unset):
            line_items = []
            for line_items_item_data in self.line_items:
                line_items_item = line_items_item_data.to_dict()
                line_items.append(line_items_item)

        amount = self.amount

        currency = self.currency

        needed_by = self.needed_by

        quote_document: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.quote_document, Unset):
            quote_document = self.quote_document.to_dict()

        notes = self.notes

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        approval: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.approval, Unset):
            approval = self.approval.to_dict()

        approval_version = self.approval_version

        budget_check: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.budget_check, Unset):
            budget_check = self.budget_check.to_dict()

        po_id = self.po_id

        rejection_reason = self.rejection_reason

        created_at = self.created_at

        updated_at = self.updated_at

        submitted_at = self.submitted_at

        decided_at = self.decided_at

        canceled_at = self.canceled_at

        canceled_by = self.canceled_by

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if requester_employee_key is not UNSET:
            field_dict["requesterEmployeeKey"] = requester_employee_key
        if requester_name is not UNSET:
            field_dict["requesterName"] = requester_name
        if cost_center is not UNSET:
            field_dict["costCenter"] = cost_center
        if gl_code is not UNSET:
            field_dict["glCode"] = gl_code
        if supplier is not UNSET:
            field_dict["supplier"] = supplier
        if line_items is not UNSET:
            field_dict["lineItems"] = line_items
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if needed_by is not UNSET:
            field_dict["neededBy"] = needed_by
        if quote_document is not UNSET:
            field_dict["quoteDocument"] = quote_document
        if notes is not UNSET:
            field_dict["notes"] = notes
        if status is not UNSET:
            field_dict["status"] = status
        if approval is not UNSET:
            field_dict["approval"] = approval
        if approval_version is not UNSET:
            field_dict["approvalVersion"] = approval_version
        if budget_check is not UNSET:
            field_dict["budgetCheck"] = budget_check
        if po_id is not UNSET:
            field_dict["poId"] = po_id
        if rejection_reason is not UNSET:
            field_dict["rejectionReason"] = rejection_reason
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if submitted_at is not UNSET:
            field_dict["submittedAt"] = submitted_at
        if decided_at is not UNSET:
            field_dict["decidedAt"] = decided_at
        if canceled_at is not UNSET:
            field_dict["canceledAt"] = canceled_at
        if canceled_by is not UNSET:
            field_dict["canceledBy"] = canceled_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.approval_chain import ApprovalChain
        from ..models.budget_check import BudgetCheck
        from ..models.purchase_order_quote_document import PurchaseOrderQuoteDocument
        from ..models.purchase_request_line import PurchaseRequestLine
        from ..models.purchase_request_supplier import PurchaseRequestSupplier

        d = src_dict.copy()
        id = d.pop("id")

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        requester_employee_key = d.pop("requesterEmployeeKey", UNSET)

        requester_name = d.pop("requesterName", UNSET)

        cost_center = d.pop("costCenter", UNSET)

        gl_code = d.pop("glCode", UNSET)

        _supplier = d.pop("supplier", UNSET)
        supplier: Union[Unset, PurchaseRequestSupplier]
        if isinstance(_supplier, Unset):
            supplier = UNSET
        else:
            supplier = PurchaseRequestSupplier.from_dict(_supplier)

        line_items = []
        _line_items = d.pop("lineItems", UNSET)
        for line_items_item_data in _line_items or []:
            line_items_item = PurchaseRequestLine.from_dict(line_items_item_data)

            line_items.append(line_items_item)

        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        needed_by = d.pop("neededBy", UNSET)

        _quote_document = d.pop("quoteDocument", UNSET)
        quote_document: Union[Unset, PurchaseOrderQuoteDocument]
        if isinstance(_quote_document, Unset):
            quote_document = UNSET
        else:
            quote_document = PurchaseOrderQuoteDocument.from_dict(_quote_document)

        notes = d.pop("notes", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, PurchaseRequestStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_purchase_request_status(_status)

        _approval = d.pop("approval", UNSET)
        approval: Union[Unset, ApprovalChain]
        if isinstance(_approval, Unset):
            approval = UNSET
        else:
            approval = ApprovalChain.from_dict(_approval)

        approval_version = d.pop("approvalVersion", UNSET)

        _budget_check = d.pop("budgetCheck", UNSET)
        budget_check: Union[Unset, BudgetCheck]
        if isinstance(_budget_check, Unset):
            budget_check = UNSET
        else:
            budget_check = BudgetCheck.from_dict(_budget_check)

        po_id = d.pop("poId", UNSET)

        rejection_reason = d.pop("rejectionReason", UNSET)

        created_at = d.pop("createdAt", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        submitted_at = d.pop("submittedAt", UNSET)

        decided_at = d.pop("decidedAt", UNSET)

        canceled_at = d.pop("canceledAt", UNSET)

        canceled_by = d.pop("canceledBy", UNSET)

        purchase_request = cls(
            id=id,
            title=title,
            description=description,
            requester_employee_key=requester_employee_key,
            requester_name=requester_name,
            cost_center=cost_center,
            gl_code=gl_code,
            supplier=supplier,
            line_items=line_items,
            amount=amount,
            currency=currency,
            needed_by=needed_by,
            quote_document=quote_document,
            notes=notes,
            status=status,
            approval=approval,
            approval_version=approval_version,
            budget_check=budget_check,
            po_id=po_id,
            rejection_reason=rejection_reason,
            created_at=created_at,
            updated_at=updated_at,
            submitted_at=submitted_at,
            decided_at=decided_at,
            canceled_at=canceled_at,
            canceled_by=canceled_by,
        )

        purchase_request.additional_properties = d
        return purchase_request

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
