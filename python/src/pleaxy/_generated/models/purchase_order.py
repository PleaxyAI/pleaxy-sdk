from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.purchase_order_matching import (
    PurchaseOrderMatching,
    check_purchase_order_matching,
)
from ..models.purchase_order_matching_default import (
    PurchaseOrderMatchingDefault,
    check_purchase_order_matching_default,
)
from ..models.purchase_order_provider import (
    PurchaseOrderProvider,
    check_purchase_order_provider,
)
from ..models.purchase_order_receipt_state import (
    PurchaseOrderReceiptState,
    check_purchase_order_receipt_state,
)
from ..models.purchase_order_status import (
    PurchaseOrderStatus,
    check_purchase_order_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.approval_chain import ApprovalChain
    from ..models.budget_check import BudgetCheck
    from ..models.line_item import LineItem
    from ..models.payer_account_ref import PayerAccountRef
    from ..models.purchase_order_bill_to import PurchaseOrderBillTo
    from ..models.purchase_order_change_summary import PurchaseOrderChangeSummary
    from ..models.purchase_order_cost_center_change import PurchaseOrderCostCenterChange
    from ..models.purchase_order_matching_change import PurchaseOrderMatchingChange
    from ..models.purchase_order_prior_invoiced import PurchaseOrderPriorInvoiced
    from ..models.purchase_order_punchout import PurchaseOrderPunchout
    from ..models.purchase_order_quote_document import PurchaseOrderQuoteDocument
    from ..models.purchase_order_receipt_tolerance import PurchaseOrderReceiptTolerance
    from ..models.purchase_order_received_line import PurchaseOrderReceivedLine
    from ..models.purchase_order_ship_to import PurchaseOrderShipTo
    from ..models.purchase_order_supplier_email import PurchaseOrderSupplierEmail
    from ..models.purchase_order_supplier_invite import PurchaseOrderSupplierInvite
    from ..models.store_order import StoreOrder


T = TypeVar("T", bound="PurchaseOrder")


@_attrs_define
class PurchaseOrder:
    """
    Attributes:
        id (str):
        buyer_org_id (Union[Unset, str]):
        supplier_org_id (Union[Unset, str]):
        supplier (Union[Unset, str]):
        amount (Union[Unset, float]):
        currency (Union[Unset, str]):
        status (Union[Unset, PurchaseOrderStatus]):
        invoice_id (Union[Unset, str]):
        invoice_ids (Union[Unset, List[str]]):
        invoiced_amount (Union[Unset, float]):
        prior_invoiced (Union[Unset, PurchaseOrderPriorInvoiced]):
        rejected_invoice_count (Union[Unset, float]):
        last_rejected_invoice_id (Union[Unset, str]):
        last_replaced_invoice_id (Union[Unset, str]):
        provider (Union[Unset, PurchaseOrderProvider]):
        payer_accounts (Union[Unset, List['PayerAccountRef']]):
        bill_to (Union[Unset, str]):
        bill_to_party (Union[Unset, PurchaseOrderBillTo]):
        cost_center (Union[Unset, str]):
        cost_center_changes (Union[Unset, List['PurchaseOrderCostCenterChange']]):
        gl_code (Union[Unset, str]):
        submitted_at (Union[Unset, str]):
        budget_check (Union[Unset, BudgetCheck]):
        request_id (Union[Unset, str]):
        budget_owner (Union[Unset, str]):
        buyer_name (Union[Unset, str]):
        buyer_org_name (Union[Unset, str]):
        buyer_region_name (Union[Unset, str]):
        supplier_region_name (Union[Unset, str]):
        supplier_site (Union[Unset, str]):
        supplier_contact_email (Union[Unset, str]):
        supplier_invite (Union[Unset, PurchaseOrderSupplierInvite]):
        supplier_connection_id (Union[Unset, str]):
        notes (Union[Unset, str]):
        contract_id (Union[Unset, str]):
        supplier_email (Union[Unset, PurchaseOrderSupplierEmail]):
        mailbox_token (Union[Unset, str]):
        quote_document (Union[Unset, PurchaseOrderQuoteDocument]):
        sow_document (Union[Unset, PurchaseOrderQuoteDocument]):
        line_items (Union[Unset, List['LineItem']]):
        approval (Union[Unset, ApprovalChain]):
        approval_version (Union[Unset, float]):
        ever_spend_limit_gated (Union[Unset, bool]):
        spend_limit_gated_at (Union[Unset, str]):
        updated_by (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        version (Union[Unset, float]):
        last_change (Union[Unset, PurchaseOrderChangeSummary]):
        approval_amount (Union[Unset, float]):
        punchout (Union[Unset, PurchaseOrderPunchout]):
        store_id (Union[Unset, str]):
        delivery_address_id (Union[Unset, str]):
        ship_to (Union[Unset, PurchaseOrderShipTo]):
        store_order (Union[Unset, StoreOrder]):
        matching (Union[Unset, PurchaseOrderMatching]):
        matching_default (Union[Unset, PurchaseOrderMatchingDefault]):
        matching_changes (Union[Unset, List['PurchaseOrderMatchingChange']]):
        receiver_employee_key (Union[Unset, str]):
        receiver_name (Union[Unset, str]):
        received (Union[Unset, List['PurchaseOrderReceivedLine']]):
        received_pending (Union[Unset, List['PurchaseOrderReceivedLine']]):
        receipt_state (Union[Unset, PurchaseOrderReceiptState]):
        receipt_required (Union[Unset, bool]):
        ready_to_invoice (Union[Unset, float]):
        receipt_tolerance (Union[Unset, PurchaseOrderReceiptTolerance]):
        created_at (Union[Unset, str]):
    """

    id: str
    buyer_org_id: Union[Unset, str] = UNSET
    supplier_org_id: Union[Unset, str] = UNSET
    supplier: Union[Unset, str] = UNSET
    amount: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    status: Union[Unset, PurchaseOrderStatus] = UNSET
    invoice_id: Union[Unset, str] = UNSET
    invoice_ids: Union[Unset, List[str]] = UNSET
    invoiced_amount: Union[Unset, float] = UNSET
    prior_invoiced: Union[Unset, "PurchaseOrderPriorInvoiced"] = UNSET
    rejected_invoice_count: Union[Unset, float] = UNSET
    last_rejected_invoice_id: Union[Unset, str] = UNSET
    last_replaced_invoice_id: Union[Unset, str] = UNSET
    provider: Union[Unset, PurchaseOrderProvider] = UNSET
    payer_accounts: Union[Unset, List["PayerAccountRef"]] = UNSET
    bill_to: Union[Unset, str] = UNSET
    bill_to_party: Union[Unset, "PurchaseOrderBillTo"] = UNSET
    cost_center: Union[Unset, str] = UNSET
    cost_center_changes: Union[Unset, List["PurchaseOrderCostCenterChange"]] = UNSET
    gl_code: Union[Unset, str] = UNSET
    submitted_at: Union[Unset, str] = UNSET
    budget_check: Union[Unset, "BudgetCheck"] = UNSET
    request_id: Union[Unset, str] = UNSET
    budget_owner: Union[Unset, str] = UNSET
    buyer_name: Union[Unset, str] = UNSET
    buyer_org_name: Union[Unset, str] = UNSET
    buyer_region_name: Union[Unset, str] = UNSET
    supplier_region_name: Union[Unset, str] = UNSET
    supplier_site: Union[Unset, str] = UNSET
    supplier_contact_email: Union[Unset, str] = UNSET
    supplier_invite: Union[Unset, "PurchaseOrderSupplierInvite"] = UNSET
    supplier_connection_id: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    contract_id: Union[Unset, str] = UNSET
    supplier_email: Union[Unset, "PurchaseOrderSupplierEmail"] = UNSET
    mailbox_token: Union[Unset, str] = UNSET
    quote_document: Union[Unset, "PurchaseOrderQuoteDocument"] = UNSET
    sow_document: Union[Unset, "PurchaseOrderQuoteDocument"] = UNSET
    line_items: Union[Unset, List["LineItem"]] = UNSET
    approval: Union[Unset, "ApprovalChain"] = UNSET
    approval_version: Union[Unset, float] = UNSET
    ever_spend_limit_gated: Union[Unset, bool] = UNSET
    spend_limit_gated_at: Union[Unset, str] = UNSET
    updated_by: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    version: Union[Unset, float] = UNSET
    last_change: Union[Unset, "PurchaseOrderChangeSummary"] = UNSET
    approval_amount: Union[Unset, float] = UNSET
    punchout: Union[Unset, "PurchaseOrderPunchout"] = UNSET
    store_id: Union[Unset, str] = UNSET
    delivery_address_id: Union[Unset, str] = UNSET
    ship_to: Union[Unset, "PurchaseOrderShipTo"] = UNSET
    store_order: Union[Unset, "StoreOrder"] = UNSET
    matching: Union[Unset, PurchaseOrderMatching] = UNSET
    matching_default: Union[Unset, PurchaseOrderMatchingDefault] = UNSET
    matching_changes: Union[Unset, List["PurchaseOrderMatchingChange"]] = UNSET
    receiver_employee_key: Union[Unset, str] = UNSET
    receiver_name: Union[Unset, str] = UNSET
    received: Union[Unset, List["PurchaseOrderReceivedLine"]] = UNSET
    received_pending: Union[Unset, List["PurchaseOrderReceivedLine"]] = UNSET
    receipt_state: Union[Unset, PurchaseOrderReceiptState] = UNSET
    receipt_required: Union[Unset, bool] = UNSET
    ready_to_invoice: Union[Unset, float] = UNSET
    receipt_tolerance: Union[Unset, "PurchaseOrderReceiptTolerance"] = UNSET
    created_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        buyer_org_id = self.buyer_org_id

        supplier_org_id = self.supplier_org_id

        supplier = self.supplier

        amount = self.amount

        currency = self.currency

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        invoice_id = self.invoice_id

        invoice_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.invoice_ids, Unset):
            invoice_ids = self.invoice_ids

        invoiced_amount = self.invoiced_amount

        prior_invoiced: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.prior_invoiced, Unset):
            prior_invoiced = self.prior_invoiced.to_dict()

        rejected_invoice_count = self.rejected_invoice_count

        last_rejected_invoice_id = self.last_rejected_invoice_id

        last_replaced_invoice_id = self.last_replaced_invoice_id

        provider: Union[Unset, str] = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider

        payer_accounts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.payer_accounts, Unset):
            payer_accounts = []
            for payer_accounts_item_data in self.payer_accounts:
                payer_accounts_item = payer_accounts_item_data.to_dict()
                payer_accounts.append(payer_accounts_item)

        bill_to = self.bill_to

        bill_to_party: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bill_to_party, Unset):
            bill_to_party = self.bill_to_party.to_dict()

        cost_center = self.cost_center

        cost_center_changes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.cost_center_changes, Unset):
            cost_center_changes = []
            for cost_center_changes_item_data in self.cost_center_changes:
                cost_center_changes_item = cost_center_changes_item_data.to_dict()
                cost_center_changes.append(cost_center_changes_item)

        gl_code = self.gl_code

        submitted_at = self.submitted_at

        budget_check: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.budget_check, Unset):
            budget_check = self.budget_check.to_dict()

        request_id = self.request_id

        budget_owner = self.budget_owner

        buyer_name = self.buyer_name

        buyer_org_name = self.buyer_org_name

        buyer_region_name = self.buyer_region_name

        supplier_region_name = self.supplier_region_name

        supplier_site = self.supplier_site

        supplier_contact_email = self.supplier_contact_email

        supplier_invite: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.supplier_invite, Unset):
            supplier_invite = self.supplier_invite.to_dict()

        supplier_connection_id = self.supplier_connection_id

        notes = self.notes

        contract_id = self.contract_id

        supplier_email: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.supplier_email, Unset):
            supplier_email = self.supplier_email.to_dict()

        mailbox_token = self.mailbox_token

        quote_document: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.quote_document, Unset):
            quote_document = self.quote_document.to_dict()

        sow_document: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sow_document, Unset):
            sow_document = self.sow_document.to_dict()

        line_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.line_items, Unset):
            line_items = []
            for line_items_item_data in self.line_items:
                line_items_item = line_items_item_data.to_dict()
                line_items.append(line_items_item)

        approval: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.approval, Unset):
            approval = self.approval.to_dict()

        approval_version = self.approval_version

        ever_spend_limit_gated = self.ever_spend_limit_gated

        spend_limit_gated_at = self.spend_limit_gated_at

        updated_by = self.updated_by

        updated_at = self.updated_at

        version = self.version

        last_change: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.last_change, Unset):
            last_change = self.last_change.to_dict()

        approval_amount = self.approval_amount

        punchout: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.punchout, Unset):
            punchout = self.punchout.to_dict()

        store_id = self.store_id

        delivery_address_id = self.delivery_address_id

        ship_to: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ship_to, Unset):
            ship_to = self.ship_to.to_dict()

        store_order: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.store_order, Unset):
            store_order = self.store_order.to_dict()

        matching: Union[Unset, str] = UNSET
        if not isinstance(self.matching, Unset):
            matching = self.matching

        matching_default: Union[Unset, str] = UNSET
        if not isinstance(self.matching_default, Unset):
            matching_default = self.matching_default

        matching_changes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.matching_changes, Unset):
            matching_changes = []
            for matching_changes_item_data in self.matching_changes:
                matching_changes_item = matching_changes_item_data.to_dict()
                matching_changes.append(matching_changes_item)

        receiver_employee_key = self.receiver_employee_key

        receiver_name = self.receiver_name

        received: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.received, Unset):
            received = []
            for received_item_data in self.received:
                received_item = received_item_data.to_dict()
                received.append(received_item)

        received_pending: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.received_pending, Unset):
            received_pending = []
            for received_pending_item_data in self.received_pending:
                received_pending_item = received_pending_item_data.to_dict()
                received_pending.append(received_pending_item)

        receipt_state: Union[Unset, str] = UNSET
        if not isinstance(self.receipt_state, Unset):
            receipt_state = self.receipt_state

        receipt_required = self.receipt_required

        ready_to_invoice = self.ready_to_invoice

        receipt_tolerance: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.receipt_tolerance, Unset):
            receipt_tolerance = self.receipt_tolerance.to_dict()

        created_at = self.created_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if buyer_org_id is not UNSET:
            field_dict["buyerOrgId"] = buyer_org_id
        if supplier_org_id is not UNSET:
            field_dict["supplierOrgId"] = supplier_org_id
        if supplier is not UNSET:
            field_dict["supplier"] = supplier
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if status is not UNSET:
            field_dict["status"] = status
        if invoice_id is not UNSET:
            field_dict["invoiceId"] = invoice_id
        if invoice_ids is not UNSET:
            field_dict["invoiceIds"] = invoice_ids
        if invoiced_amount is not UNSET:
            field_dict["invoicedAmount"] = invoiced_amount
        if prior_invoiced is not UNSET:
            field_dict["priorInvoiced"] = prior_invoiced
        if rejected_invoice_count is not UNSET:
            field_dict["rejectedInvoiceCount"] = rejected_invoice_count
        if last_rejected_invoice_id is not UNSET:
            field_dict["lastRejectedInvoiceId"] = last_rejected_invoice_id
        if last_replaced_invoice_id is not UNSET:
            field_dict["lastReplacedInvoiceId"] = last_replaced_invoice_id
        if provider is not UNSET:
            field_dict["provider"] = provider
        if payer_accounts is not UNSET:
            field_dict["payerAccounts"] = payer_accounts
        if bill_to is not UNSET:
            field_dict["billTo"] = bill_to
        if bill_to_party is not UNSET:
            field_dict["billToParty"] = bill_to_party
        if cost_center is not UNSET:
            field_dict["costCenter"] = cost_center
        if cost_center_changes is not UNSET:
            field_dict["costCenterChanges"] = cost_center_changes
        if gl_code is not UNSET:
            field_dict["glCode"] = gl_code
        if submitted_at is not UNSET:
            field_dict["submittedAt"] = submitted_at
        if budget_check is not UNSET:
            field_dict["budgetCheck"] = budget_check
        if request_id is not UNSET:
            field_dict["requestId"] = request_id
        if budget_owner is not UNSET:
            field_dict["budgetOwner"] = budget_owner
        if buyer_name is not UNSET:
            field_dict["buyerName"] = buyer_name
        if buyer_org_name is not UNSET:
            field_dict["buyerOrgName"] = buyer_org_name
        if buyer_region_name is not UNSET:
            field_dict["buyerRegionName"] = buyer_region_name
        if supplier_region_name is not UNSET:
            field_dict["supplierRegionName"] = supplier_region_name
        if supplier_site is not UNSET:
            field_dict["supplierSite"] = supplier_site
        if supplier_contact_email is not UNSET:
            field_dict["supplierContactEmail"] = supplier_contact_email
        if supplier_invite is not UNSET:
            field_dict["supplierInvite"] = supplier_invite
        if supplier_connection_id is not UNSET:
            field_dict["supplierConnectionId"] = supplier_connection_id
        if notes is not UNSET:
            field_dict["notes"] = notes
        if contract_id is not UNSET:
            field_dict["contractId"] = contract_id
        if supplier_email is not UNSET:
            field_dict["supplierEmail"] = supplier_email
        if mailbox_token is not UNSET:
            field_dict["mailboxToken"] = mailbox_token
        if quote_document is not UNSET:
            field_dict["quoteDocument"] = quote_document
        if sow_document is not UNSET:
            field_dict["sowDocument"] = sow_document
        if line_items is not UNSET:
            field_dict["lineItems"] = line_items
        if approval is not UNSET:
            field_dict["approval"] = approval
        if approval_version is not UNSET:
            field_dict["approvalVersion"] = approval_version
        if ever_spend_limit_gated is not UNSET:
            field_dict["everSpendLimitGated"] = ever_spend_limit_gated
        if spend_limit_gated_at is not UNSET:
            field_dict["spendLimitGatedAt"] = spend_limit_gated_at
        if updated_by is not UNSET:
            field_dict["updatedBy"] = updated_by
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if version is not UNSET:
            field_dict["version"] = version
        if last_change is not UNSET:
            field_dict["lastChange"] = last_change
        if approval_amount is not UNSET:
            field_dict["approvalAmount"] = approval_amount
        if punchout is not UNSET:
            field_dict["punchout"] = punchout
        if store_id is not UNSET:
            field_dict["storeId"] = store_id
        if delivery_address_id is not UNSET:
            field_dict["deliveryAddressId"] = delivery_address_id
        if ship_to is not UNSET:
            field_dict["shipTo"] = ship_to
        if store_order is not UNSET:
            field_dict["storeOrder"] = store_order
        if matching is not UNSET:
            field_dict["matching"] = matching
        if matching_default is not UNSET:
            field_dict["matchingDefault"] = matching_default
        if matching_changes is not UNSET:
            field_dict["matchingChanges"] = matching_changes
        if receiver_employee_key is not UNSET:
            field_dict["receiverEmployeeKey"] = receiver_employee_key
        if receiver_name is not UNSET:
            field_dict["receiverName"] = receiver_name
        if received is not UNSET:
            field_dict["received"] = received
        if received_pending is not UNSET:
            field_dict["receivedPending"] = received_pending
        if receipt_state is not UNSET:
            field_dict["receiptState"] = receipt_state
        if receipt_required is not UNSET:
            field_dict["receiptRequired"] = receipt_required
        if ready_to_invoice is not UNSET:
            field_dict["readyToInvoice"] = ready_to_invoice
        if receipt_tolerance is not UNSET:
            field_dict["receiptTolerance"] = receipt_tolerance
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.approval_chain import ApprovalChain
        from ..models.budget_check import BudgetCheck
        from ..models.line_item import LineItem
        from ..models.payer_account_ref import PayerAccountRef
        from ..models.purchase_order_bill_to import PurchaseOrderBillTo
        from ..models.purchase_order_change_summary import PurchaseOrderChangeSummary
        from ..models.purchase_order_cost_center_change import (
            PurchaseOrderCostCenterChange,
        )
        from ..models.purchase_order_matching_change import PurchaseOrderMatchingChange
        from ..models.purchase_order_prior_invoiced import PurchaseOrderPriorInvoiced
        from ..models.purchase_order_punchout import PurchaseOrderPunchout
        from ..models.purchase_order_quote_document import PurchaseOrderQuoteDocument
        from ..models.purchase_order_receipt_tolerance import (
            PurchaseOrderReceiptTolerance,
        )
        from ..models.purchase_order_received_line import PurchaseOrderReceivedLine
        from ..models.purchase_order_ship_to import PurchaseOrderShipTo
        from ..models.purchase_order_supplier_email import PurchaseOrderSupplierEmail
        from ..models.purchase_order_supplier_invite import PurchaseOrderSupplierInvite
        from ..models.store_order import StoreOrder

        d = src_dict.copy()
        id = d.pop("id")

        buyer_org_id = d.pop("buyerOrgId", UNSET)

        supplier_org_id = d.pop("supplierOrgId", UNSET)

        supplier = d.pop("supplier", UNSET)

        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, PurchaseOrderStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_purchase_order_status(_status)

        invoice_id = d.pop("invoiceId", UNSET)

        invoice_ids = cast(List[str], d.pop("invoiceIds", UNSET))

        invoiced_amount = d.pop("invoicedAmount", UNSET)

        _prior_invoiced = d.pop("priorInvoiced", UNSET)
        prior_invoiced: Union[Unset, PurchaseOrderPriorInvoiced]
        if isinstance(_prior_invoiced, Unset):
            prior_invoiced = UNSET
        else:
            prior_invoiced = PurchaseOrderPriorInvoiced.from_dict(_prior_invoiced)

        rejected_invoice_count = d.pop("rejectedInvoiceCount", UNSET)

        last_rejected_invoice_id = d.pop("lastRejectedInvoiceId", UNSET)

        last_replaced_invoice_id = d.pop("lastReplacedInvoiceId", UNSET)

        _provider = d.pop("provider", UNSET)
        provider: Union[Unset, PurchaseOrderProvider]
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = check_purchase_order_provider(_provider)

        payer_accounts = []
        _payer_accounts = d.pop("payerAccounts", UNSET)
        for payer_accounts_item_data in _payer_accounts or []:
            payer_accounts_item = PayerAccountRef.from_dict(payer_accounts_item_data)

            payer_accounts.append(payer_accounts_item)

        bill_to = d.pop("billTo", UNSET)

        _bill_to_party = d.pop("billToParty", UNSET)
        bill_to_party: Union[Unset, PurchaseOrderBillTo]
        if isinstance(_bill_to_party, Unset):
            bill_to_party = UNSET
        else:
            bill_to_party = PurchaseOrderBillTo.from_dict(_bill_to_party)

        cost_center = d.pop("costCenter", UNSET)

        cost_center_changes = []
        _cost_center_changes = d.pop("costCenterChanges", UNSET)
        for cost_center_changes_item_data in _cost_center_changes or []:
            cost_center_changes_item = PurchaseOrderCostCenterChange.from_dict(
                cost_center_changes_item_data
            )

            cost_center_changes.append(cost_center_changes_item)

        gl_code = d.pop("glCode", UNSET)

        submitted_at = d.pop("submittedAt", UNSET)

        _budget_check = d.pop("budgetCheck", UNSET)
        budget_check: Union[Unset, BudgetCheck]
        if isinstance(_budget_check, Unset):
            budget_check = UNSET
        else:
            budget_check = BudgetCheck.from_dict(_budget_check)

        request_id = d.pop("requestId", UNSET)

        budget_owner = d.pop("budgetOwner", UNSET)

        buyer_name = d.pop("buyerName", UNSET)

        buyer_org_name = d.pop("buyerOrgName", UNSET)

        buyer_region_name = d.pop("buyerRegionName", UNSET)

        supplier_region_name = d.pop("supplierRegionName", UNSET)

        supplier_site = d.pop("supplierSite", UNSET)

        supplier_contact_email = d.pop("supplierContactEmail", UNSET)

        _supplier_invite = d.pop("supplierInvite", UNSET)
        supplier_invite: Union[Unset, PurchaseOrderSupplierInvite]
        if isinstance(_supplier_invite, Unset):
            supplier_invite = UNSET
        else:
            supplier_invite = PurchaseOrderSupplierInvite.from_dict(_supplier_invite)

        supplier_connection_id = d.pop("supplierConnectionId", UNSET)

        notes = d.pop("notes", UNSET)

        contract_id = d.pop("contractId", UNSET)

        _supplier_email = d.pop("supplierEmail", UNSET)
        supplier_email: Union[Unset, PurchaseOrderSupplierEmail]
        if isinstance(_supplier_email, Unset):
            supplier_email = UNSET
        else:
            supplier_email = PurchaseOrderSupplierEmail.from_dict(_supplier_email)

        mailbox_token = d.pop("mailboxToken", UNSET)

        _quote_document = d.pop("quoteDocument", UNSET)
        quote_document: Union[Unset, PurchaseOrderQuoteDocument]
        if isinstance(_quote_document, Unset):
            quote_document = UNSET
        else:
            quote_document = PurchaseOrderQuoteDocument.from_dict(_quote_document)

        _sow_document = d.pop("sowDocument", UNSET)
        sow_document: Union[Unset, PurchaseOrderQuoteDocument]
        if isinstance(_sow_document, Unset):
            sow_document = UNSET
        else:
            sow_document = PurchaseOrderQuoteDocument.from_dict(_sow_document)

        line_items = []
        _line_items = d.pop("lineItems", UNSET)
        for line_items_item_data in _line_items or []:
            line_items_item = LineItem.from_dict(line_items_item_data)

            line_items.append(line_items_item)

        _approval = d.pop("approval", UNSET)
        approval: Union[Unset, ApprovalChain]
        if isinstance(_approval, Unset):
            approval = UNSET
        else:
            approval = ApprovalChain.from_dict(_approval)

        approval_version = d.pop("approvalVersion", UNSET)

        ever_spend_limit_gated = d.pop("everSpendLimitGated", UNSET)

        spend_limit_gated_at = d.pop("spendLimitGatedAt", UNSET)

        updated_by = d.pop("updatedBy", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        version = d.pop("version", UNSET)

        _last_change = d.pop("lastChange", UNSET)
        last_change: Union[Unset, PurchaseOrderChangeSummary]
        if isinstance(_last_change, Unset):
            last_change = UNSET
        else:
            last_change = PurchaseOrderChangeSummary.from_dict(_last_change)

        approval_amount = d.pop("approvalAmount", UNSET)

        _punchout = d.pop("punchout", UNSET)
        punchout: Union[Unset, PurchaseOrderPunchout]
        if isinstance(_punchout, Unset):
            punchout = UNSET
        else:
            punchout = PurchaseOrderPunchout.from_dict(_punchout)

        store_id = d.pop("storeId", UNSET)

        delivery_address_id = d.pop("deliveryAddressId", UNSET)

        _ship_to = d.pop("shipTo", UNSET)
        ship_to: Union[Unset, PurchaseOrderShipTo]
        if isinstance(_ship_to, Unset):
            ship_to = UNSET
        else:
            ship_to = PurchaseOrderShipTo.from_dict(_ship_to)

        _store_order = d.pop("storeOrder", UNSET)
        store_order: Union[Unset, StoreOrder]
        if isinstance(_store_order, Unset):
            store_order = UNSET
        else:
            store_order = StoreOrder.from_dict(_store_order)

        _matching = d.pop("matching", UNSET)
        matching: Union[Unset, PurchaseOrderMatching]
        if isinstance(_matching, Unset):
            matching = UNSET
        else:
            matching = check_purchase_order_matching(_matching)

        _matching_default = d.pop("matchingDefault", UNSET)
        matching_default: Union[Unset, PurchaseOrderMatchingDefault]
        if isinstance(_matching_default, Unset):
            matching_default = UNSET
        else:
            matching_default = check_purchase_order_matching_default(_matching_default)

        matching_changes = []
        _matching_changes = d.pop("matchingChanges", UNSET)
        for matching_changes_item_data in _matching_changes or []:
            matching_changes_item = PurchaseOrderMatchingChange.from_dict(
                matching_changes_item_data
            )

            matching_changes.append(matching_changes_item)

        receiver_employee_key = d.pop("receiverEmployeeKey", UNSET)

        receiver_name = d.pop("receiverName", UNSET)

        received = []
        _received = d.pop("received", UNSET)
        for received_item_data in _received or []:
            received_item = PurchaseOrderReceivedLine.from_dict(received_item_data)

            received.append(received_item)

        received_pending = []
        _received_pending = d.pop("receivedPending", UNSET)
        for received_pending_item_data in _received_pending or []:
            received_pending_item = PurchaseOrderReceivedLine.from_dict(
                received_pending_item_data
            )

            received_pending.append(received_pending_item)

        _receipt_state = d.pop("receiptState", UNSET)
        receipt_state: Union[Unset, PurchaseOrderReceiptState]
        if isinstance(_receipt_state, Unset):
            receipt_state = UNSET
        else:
            receipt_state = check_purchase_order_receipt_state(_receipt_state)

        receipt_required = d.pop("receiptRequired", UNSET)

        ready_to_invoice = d.pop("readyToInvoice", UNSET)

        _receipt_tolerance = d.pop("receiptTolerance", UNSET)
        receipt_tolerance: Union[Unset, PurchaseOrderReceiptTolerance]
        if isinstance(_receipt_tolerance, Unset):
            receipt_tolerance = UNSET
        else:
            receipt_tolerance = PurchaseOrderReceiptTolerance.from_dict(
                _receipt_tolerance
            )

        created_at = d.pop("createdAt", UNSET)

        purchase_order = cls(
            id=id,
            buyer_org_id=buyer_org_id,
            supplier_org_id=supplier_org_id,
            supplier=supplier,
            amount=amount,
            currency=currency,
            status=status,
            invoice_id=invoice_id,
            invoice_ids=invoice_ids,
            invoiced_amount=invoiced_amount,
            prior_invoiced=prior_invoiced,
            rejected_invoice_count=rejected_invoice_count,
            last_rejected_invoice_id=last_rejected_invoice_id,
            last_replaced_invoice_id=last_replaced_invoice_id,
            provider=provider,
            payer_accounts=payer_accounts,
            bill_to=bill_to,
            bill_to_party=bill_to_party,
            cost_center=cost_center,
            cost_center_changes=cost_center_changes,
            gl_code=gl_code,
            submitted_at=submitted_at,
            budget_check=budget_check,
            request_id=request_id,
            budget_owner=budget_owner,
            buyer_name=buyer_name,
            buyer_org_name=buyer_org_name,
            buyer_region_name=buyer_region_name,
            supplier_region_name=supplier_region_name,
            supplier_site=supplier_site,
            supplier_contact_email=supplier_contact_email,
            supplier_invite=supplier_invite,
            supplier_connection_id=supplier_connection_id,
            notes=notes,
            contract_id=contract_id,
            supplier_email=supplier_email,
            mailbox_token=mailbox_token,
            quote_document=quote_document,
            sow_document=sow_document,
            line_items=line_items,
            approval=approval,
            approval_version=approval_version,
            ever_spend_limit_gated=ever_spend_limit_gated,
            spend_limit_gated_at=spend_limit_gated_at,
            updated_by=updated_by,
            updated_at=updated_at,
            version=version,
            last_change=last_change,
            approval_amount=approval_amount,
            punchout=punchout,
            store_id=store_id,
            delivery_address_id=delivery_address_id,
            ship_to=ship_to,
            store_order=store_order,
            matching=matching,
            matching_default=matching_default,
            matching_changes=matching_changes,
            receiver_employee_key=receiver_employee_key,
            receiver_name=receiver_name,
            received=received,
            received_pending=received_pending,
            receipt_state=receipt_state,
            receipt_required=receipt_required,
            ready_to_invoice=ready_to_invoice,
            receipt_tolerance=receipt_tolerance,
            created_at=created_at,
        )

        purchase_order.additional_properties = d
        return purchase_order

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
