from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.purchase_order_supplier_view_provider import (
    PurchaseOrderSupplierViewProvider,
    check_purchase_order_supplier_view_provider,
)
from ..models.purchase_order_supplier_view_status import (
    PurchaseOrderSupplierViewStatus,
    check_purchase_order_supplier_view_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.line_item import LineItem
    from ..models.payer_account_ref import PayerAccountRef
    from ..models.purchase_order_supplier_view_quote_document import (
        PurchaseOrderSupplierViewQuoteDocument,
    )
    from ..models.supplier_approval_view import SupplierApprovalView


T = TypeVar("T", bound="PurchaseOrderSupplierView")


@_attrs_define
class PurchaseOrderSupplierView:
    """
    Attributes:
        id (str):
        supplier (Union[Unset, str]):
        provider (Union[Unset, PurchaseOrderSupplierViewProvider]):
        buyer_org_id (Union[Unset, str]):
        supplier_org_id (Union[Unset, str]):
        status (Union[Unset, PurchaseOrderSupplierViewStatus]):
        created_at (Union[Unset, str]):
        amount (Union[Unset, float]):
        currency (Union[Unset, str]):
        invoice_id (Union[Unset, str]):
        invoice_ids (Union[Unset, List[str]]):
        invoiced_amount (Union[Unset, float]):
        rejected_invoice_count (Union[Unset, float]):
        last_rejected_invoice_id (Union[Unset, str]):
        last_replaced_invoice_id (Union[Unset, str]):
        payer_accounts (Union[Unset, List['PayerAccountRef']]):
        bill_to (Union[Unset, str]):
        buyer_org_name (Union[Unset, str]):
        buyer_region_name (Union[Unset, str]):
        supplier_region_name (Union[Unset, str]):
        supplier_site (Union[Unset, str]):
        contract_id (Union[Unset, str]):
        line_items (Union[Unset, List['LineItem']]):
        version (Union[Unset, float]):
        approval (Union[Unset, SupplierApprovalView]):
        quote_document (Union[Unset, PurchaseOrderSupplierViewQuoteDocument]):
        buyer_workspace_id (Union[Unset, str]):
    """

    id: str
    supplier: Union[Unset, str] = UNSET
    provider: Union[Unset, PurchaseOrderSupplierViewProvider] = UNSET
    buyer_org_id: Union[Unset, str] = UNSET
    supplier_org_id: Union[Unset, str] = UNSET
    status: Union[Unset, PurchaseOrderSupplierViewStatus] = UNSET
    created_at: Union[Unset, str] = UNSET
    amount: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    invoice_id: Union[Unset, str] = UNSET
    invoice_ids: Union[Unset, List[str]] = UNSET
    invoiced_amount: Union[Unset, float] = UNSET
    rejected_invoice_count: Union[Unset, float] = UNSET
    last_rejected_invoice_id: Union[Unset, str] = UNSET
    last_replaced_invoice_id: Union[Unset, str] = UNSET
    payer_accounts: Union[Unset, List["PayerAccountRef"]] = UNSET
    bill_to: Union[Unset, str] = UNSET
    buyer_org_name: Union[Unset, str] = UNSET
    buyer_region_name: Union[Unset, str] = UNSET
    supplier_region_name: Union[Unset, str] = UNSET
    supplier_site: Union[Unset, str] = UNSET
    contract_id: Union[Unset, str] = UNSET
    line_items: Union[Unset, List["LineItem"]] = UNSET
    version: Union[Unset, float] = UNSET
    approval: Union[Unset, "SupplierApprovalView"] = UNSET
    quote_document: Union[Unset, "PurchaseOrderSupplierViewQuoteDocument"] = UNSET
    buyer_workspace_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        supplier = self.supplier

        provider: Union[Unset, str] = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider

        buyer_org_id = self.buyer_org_id

        supplier_org_id = self.supplier_org_id

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        created_at = self.created_at

        amount = self.amount

        currency = self.currency

        invoice_id = self.invoice_id

        invoice_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.invoice_ids, Unset):
            invoice_ids = self.invoice_ids

        invoiced_amount = self.invoiced_amount

        rejected_invoice_count = self.rejected_invoice_count

        last_rejected_invoice_id = self.last_rejected_invoice_id

        last_replaced_invoice_id = self.last_replaced_invoice_id

        payer_accounts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.payer_accounts, Unset):
            payer_accounts = []
            for payer_accounts_item_data in self.payer_accounts:
                payer_accounts_item = payer_accounts_item_data.to_dict()
                payer_accounts.append(payer_accounts_item)

        bill_to = self.bill_to

        buyer_org_name = self.buyer_org_name

        buyer_region_name = self.buyer_region_name

        supplier_region_name = self.supplier_region_name

        supplier_site = self.supplier_site

        contract_id = self.contract_id

        line_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.line_items, Unset):
            line_items = []
            for line_items_item_data in self.line_items:
                line_items_item = line_items_item_data.to_dict()
                line_items.append(line_items_item)

        version = self.version

        approval: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.approval, Unset):
            approval = self.approval.to_dict()

        quote_document: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.quote_document, Unset):
            quote_document = self.quote_document.to_dict()

        buyer_workspace_id = self.buyer_workspace_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if supplier is not UNSET:
            field_dict["supplier"] = supplier
        if provider is not UNSET:
            field_dict["provider"] = provider
        if buyer_org_id is not UNSET:
            field_dict["buyerOrgId"] = buyer_org_id
        if supplier_org_id is not UNSET:
            field_dict["supplierOrgId"] = supplier_org_id
        if status is not UNSET:
            field_dict["status"] = status
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if invoice_id is not UNSET:
            field_dict["invoiceId"] = invoice_id
        if invoice_ids is not UNSET:
            field_dict["invoiceIds"] = invoice_ids
        if invoiced_amount is not UNSET:
            field_dict["invoicedAmount"] = invoiced_amount
        if rejected_invoice_count is not UNSET:
            field_dict["rejectedInvoiceCount"] = rejected_invoice_count
        if last_rejected_invoice_id is not UNSET:
            field_dict["lastRejectedInvoiceId"] = last_rejected_invoice_id
        if last_replaced_invoice_id is not UNSET:
            field_dict["lastReplacedInvoiceId"] = last_replaced_invoice_id
        if payer_accounts is not UNSET:
            field_dict["payerAccounts"] = payer_accounts
        if bill_to is not UNSET:
            field_dict["billTo"] = bill_to
        if buyer_org_name is not UNSET:
            field_dict["buyerOrgName"] = buyer_org_name
        if buyer_region_name is not UNSET:
            field_dict["buyerRegionName"] = buyer_region_name
        if supplier_region_name is not UNSET:
            field_dict["supplierRegionName"] = supplier_region_name
        if supplier_site is not UNSET:
            field_dict["supplierSite"] = supplier_site
        if contract_id is not UNSET:
            field_dict["contractId"] = contract_id
        if line_items is not UNSET:
            field_dict["lineItems"] = line_items
        if version is not UNSET:
            field_dict["version"] = version
        if approval is not UNSET:
            field_dict["approval"] = approval
        if quote_document is not UNSET:
            field_dict["quoteDocument"] = quote_document
        if buyer_workspace_id is not UNSET:
            field_dict["buyerWorkspaceId"] = buyer_workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.line_item import LineItem
        from ..models.payer_account_ref import PayerAccountRef
        from ..models.purchase_order_supplier_view_quote_document import (
            PurchaseOrderSupplierViewQuoteDocument,
        )
        from ..models.supplier_approval_view import SupplierApprovalView

        d = src_dict.copy()
        id = d.pop("id")

        supplier = d.pop("supplier", UNSET)

        _provider = d.pop("provider", UNSET)
        provider: Union[Unset, PurchaseOrderSupplierViewProvider]
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = check_purchase_order_supplier_view_provider(_provider)

        buyer_org_id = d.pop("buyerOrgId", UNSET)

        supplier_org_id = d.pop("supplierOrgId", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, PurchaseOrderSupplierViewStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_purchase_order_supplier_view_status(_status)

        created_at = d.pop("createdAt", UNSET)

        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        invoice_id = d.pop("invoiceId", UNSET)

        invoice_ids = cast(List[str], d.pop("invoiceIds", UNSET))

        invoiced_amount = d.pop("invoicedAmount", UNSET)

        rejected_invoice_count = d.pop("rejectedInvoiceCount", UNSET)

        last_rejected_invoice_id = d.pop("lastRejectedInvoiceId", UNSET)

        last_replaced_invoice_id = d.pop("lastReplacedInvoiceId", UNSET)

        payer_accounts = []
        _payer_accounts = d.pop("payerAccounts", UNSET)
        for payer_accounts_item_data in _payer_accounts or []:
            payer_accounts_item = PayerAccountRef.from_dict(payer_accounts_item_data)

            payer_accounts.append(payer_accounts_item)

        bill_to = d.pop("billTo", UNSET)

        buyer_org_name = d.pop("buyerOrgName", UNSET)

        buyer_region_name = d.pop("buyerRegionName", UNSET)

        supplier_region_name = d.pop("supplierRegionName", UNSET)

        supplier_site = d.pop("supplierSite", UNSET)

        contract_id = d.pop("contractId", UNSET)

        line_items = []
        _line_items = d.pop("lineItems", UNSET)
        for line_items_item_data in _line_items or []:
            line_items_item = LineItem.from_dict(line_items_item_data)

            line_items.append(line_items_item)

        version = d.pop("version", UNSET)

        _approval = d.pop("approval", UNSET)
        approval: Union[Unset, SupplierApprovalView]
        if isinstance(_approval, Unset):
            approval = UNSET
        else:
            approval = SupplierApprovalView.from_dict(_approval)

        _quote_document = d.pop("quoteDocument", UNSET)
        quote_document: Union[Unset, PurchaseOrderSupplierViewQuoteDocument]
        if isinstance(_quote_document, Unset):
            quote_document = UNSET
        else:
            quote_document = PurchaseOrderSupplierViewQuoteDocument.from_dict(
                _quote_document
            )

        buyer_workspace_id = d.pop("buyerWorkspaceId", UNSET)

        purchase_order_supplier_view = cls(
            id=id,
            supplier=supplier,
            provider=provider,
            buyer_org_id=buyer_org_id,
            supplier_org_id=supplier_org_id,
            status=status,
            created_at=created_at,
            amount=amount,
            currency=currency,
            invoice_id=invoice_id,
            invoice_ids=invoice_ids,
            invoiced_amount=invoiced_amount,
            rejected_invoice_count=rejected_invoice_count,
            last_rejected_invoice_id=last_rejected_invoice_id,
            last_replaced_invoice_id=last_replaced_invoice_id,
            payer_accounts=payer_accounts,
            bill_to=bill_to,
            buyer_org_name=buyer_org_name,
            buyer_region_name=buyer_region_name,
            supplier_region_name=supplier_region_name,
            supplier_site=supplier_site,
            contract_id=contract_id,
            line_items=line_items,
            version=version,
            approval=approval,
            quote_document=quote_document,
            buyer_workspace_id=buyer_workspace_id,
        )

        purchase_order_supplier_view.additional_properties = d
        return purchase_order_supplier_view

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
