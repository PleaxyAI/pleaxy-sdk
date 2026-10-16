from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.purchase_order_provider import (
    PurchaseOrderProvider,
    check_purchase_order_provider,
)
from ..models.purchase_order_status import (
    PurchaseOrderStatus,
    check_purchase_order_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.approval_chain import ApprovalChain
    from ..models.line_item import LineItem
    from ..models.payer_account_ref import PayerAccountRef
    from ..models.purchase_order_bill_to import PurchaseOrderBillTo
    from ..models.purchase_order_change_summary import PurchaseOrderChangeSummary
    from ..models.purchase_order_cost_center_change import PurchaseOrderCostCenterChange
    from ..models.purchase_order_prior_invoiced import PurchaseOrderPriorInvoiced
    from ..models.purchase_order_punchout import PurchaseOrderPunchout
    from ..models.purchase_order_quote_document import PurchaseOrderQuoteDocument
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
        quote_document (Union[Unset, PurchaseOrderQuoteDocument]):
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
    quote_document: Union[Unset, "PurchaseOrderQuoteDocument"] = UNSET
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

        quote_document: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.quote_document, Unset):
            quote_document = self.quote_document.to_dict()

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
        if quote_document is not UNSET:
            field_dict["quoteDocument"] = quote_document
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
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.approval_chain import ApprovalChain
        from ..models.line_item import LineItem
        from ..models.payer_account_ref import PayerAccountRef
        from ..models.purchase_order_bill_to import PurchaseOrderBillTo
        from ..models.purchase_order_change_summary import PurchaseOrderChangeSummary
        from ..models.purchase_order_cost_center_change import (
            PurchaseOrderCostCenterChange,
        )
        from ..models.purchase_order_prior_invoiced import PurchaseOrderPriorInvoiced
        from ..models.purchase_order_punchout import PurchaseOrderPunchout
        from ..models.purchase_order_quote_document import PurchaseOrderQuoteDocument
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

        _quote_document = d.pop("quoteDocument", UNSET)
        quote_document: Union[Unset, PurchaseOrderQuoteDocument]
        if isinstance(_quote_document, Unset):
            quote_document = UNSET
        else:
            quote_document = PurchaseOrderQuoteDocument.from_dict(_quote_document)

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
            quote_document=quote_document,
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
