from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_purchase_order_input_provider import (
    CreatePurchaseOrderInputProvider,
    check_create_purchase_order_input_provider,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bill_to_party_input import BillToPartyInput
    from ..models.line_item_input import LineItemInput
    from ..models.payer_account_ref_input import PayerAccountRefInput


T = TypeVar("T", bound="CreatePurchaseOrderInput")


@_attrs_define
class CreatePurchaseOrderInput:
    """
    Attributes:
        supplier (str): Supplier / counterparty name
        line_items (List['LineItemInput']):
        po_number (Union[Unset, str]): Custom PO number to use as this PO's id instead of an auto-generated one (e.g.
            'PO-2026-0042'). Must be unique within the region.
        supplier_region_id (Union[Unset, str]): regionId of the onboarded supplier org this PO is issued to, if known.
            The buyer must hold an approved SupplierConnection to this supplier; the server rejects a region it isn't
            connected to. Links the PO to that org's real supplier workspace instead of just its free-text `supplier` name -
            see WorkspacesService.getSupplierWorkspace.
        currency (Union[Unset, str]): ISO 4217: the currency the order is priced in. To a supplier with an account
            (supplierRegionId), one its region prices in, its main currency by default (400 PO_CURRENCY_NOT_OFFERED
            otherwise). To a cloud provider or a supplier not on Pleaxy yet, any code; by default that supplier's "Bills in"
            currency, else your workspace's. An order in a currency other than your workspace's goes through every approval
            step and is never auto-approved.
        provider (Union[Unset, CreatePurchaseOrderInputProvider]):
        payer_accounts (Union[Unset, List['PayerAccountRefInput']]): Only with `provider`: this region's cloud
            connections of that provider the PO applies to, by `id`. A connection still being set up is refused. The PO
            stores each connection's own label and detail; any sent here are ignored.
        bill_to_party (Union[Unset, BillToPartyInput]):
        bill_to (Union[Unset, str]): Use `billToParty`. A one-line bill-to address for the buyer's company, kept as
            typed; ignored when `billToParty` is sent.
        cost_center (Union[Unset, str]):
        budget_owner (Union[Unset, str]):
        buyer_name (Union[Unset, str]):
        supplier_site (Union[Unset, str]):
        supplier_contact_email (Union[Unset, str]): Only for a supplier not on Pleaxy (no supplierRegionId or provider):
            their contact email. When the PO is sent (now, or when a draft is submitted), Pleaxy invites them - or links the
            supplier this workspace already has.
        notes (Union[Unset, str]):
        contract_id (Union[Unset, str]): One of this workspace's contracts this order falls under: active, and with the
            order's supplier (400 otherwise). Optional. Invoices against the order are checked against it.
        quote_import_id (Union[Unset, str]): The quote import (POST .../quote-imports) holding the supplier's quote this
            order is raised from. Its upload must have finished. Optional.
        draft (Union[Unset, bool]): Save as a draft instead of submitting for approval. Submit it later with
            SubmitPurchaseOrderDraft.
    """

    supplier: str
    line_items: List["LineItemInput"]
    po_number: Union[Unset, str] = UNSET
    supplier_region_id: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    provider: Union[Unset, CreatePurchaseOrderInputProvider] = UNSET
    payer_accounts: Union[Unset, List["PayerAccountRefInput"]] = UNSET
    bill_to_party: Union[Unset, "BillToPartyInput"] = UNSET
    bill_to: Union[Unset, str] = UNSET
    cost_center: Union[Unset, str] = UNSET
    budget_owner: Union[Unset, str] = UNSET
    buyer_name: Union[Unset, str] = UNSET
    supplier_site: Union[Unset, str] = UNSET
    supplier_contact_email: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    contract_id: Union[Unset, str] = UNSET
    quote_import_id: Union[Unset, str] = UNSET
    draft: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        supplier = self.supplier

        line_items = []
        for line_items_item_data in self.line_items:
            line_items_item = line_items_item_data.to_dict()
            line_items.append(line_items_item)

        po_number = self.po_number

        supplier_region_id = self.supplier_region_id

        currency = self.currency

        provider: Union[Unset, str] = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider

        payer_accounts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.payer_accounts, Unset):
            payer_accounts = []
            for payer_accounts_item_data in self.payer_accounts:
                payer_accounts_item = payer_accounts_item_data.to_dict()
                payer_accounts.append(payer_accounts_item)

        bill_to_party: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bill_to_party, Unset):
            bill_to_party = self.bill_to_party.to_dict()

        bill_to = self.bill_to

        cost_center = self.cost_center

        budget_owner = self.budget_owner

        buyer_name = self.buyer_name

        supplier_site = self.supplier_site

        supplier_contact_email = self.supplier_contact_email

        notes = self.notes

        contract_id = self.contract_id

        quote_import_id = self.quote_import_id

        draft = self.draft

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "supplier": supplier,
                "lineItems": line_items,
            }
        )
        if po_number is not UNSET:
            field_dict["poNumber"] = po_number
        if supplier_region_id is not UNSET:
            field_dict["supplierRegionId"] = supplier_region_id
        if currency is not UNSET:
            field_dict["currency"] = currency
        if provider is not UNSET:
            field_dict["provider"] = provider
        if payer_accounts is not UNSET:
            field_dict["payerAccounts"] = payer_accounts
        if bill_to_party is not UNSET:
            field_dict["billToParty"] = bill_to_party
        if bill_to is not UNSET:
            field_dict["billTo"] = bill_to
        if cost_center is not UNSET:
            field_dict["costCenter"] = cost_center
        if budget_owner is not UNSET:
            field_dict["budgetOwner"] = budget_owner
        if buyer_name is not UNSET:
            field_dict["buyerName"] = buyer_name
        if supplier_site is not UNSET:
            field_dict["supplierSite"] = supplier_site
        if supplier_contact_email is not UNSET:
            field_dict["supplierContactEmail"] = supplier_contact_email
        if notes is not UNSET:
            field_dict["notes"] = notes
        if contract_id is not UNSET:
            field_dict["contractId"] = contract_id
        if quote_import_id is not UNSET:
            field_dict["quoteImportId"] = quote_import_id
        if draft is not UNSET:
            field_dict["draft"] = draft

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bill_to_party_input import BillToPartyInput
        from ..models.line_item_input import LineItemInput
        from ..models.payer_account_ref_input import PayerAccountRefInput

        d = src_dict.copy()
        supplier = d.pop("supplier")

        line_items = []
        _line_items = d.pop("lineItems")
        for line_items_item_data in _line_items:
            line_items_item = LineItemInput.from_dict(line_items_item_data)

            line_items.append(line_items_item)

        po_number = d.pop("poNumber", UNSET)

        supplier_region_id = d.pop("supplierRegionId", UNSET)

        currency = d.pop("currency", UNSET)

        _provider = d.pop("provider", UNSET)
        provider: Union[Unset, CreatePurchaseOrderInputProvider]
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = check_create_purchase_order_input_provider(_provider)

        payer_accounts = []
        _payer_accounts = d.pop("payerAccounts", UNSET)
        for payer_accounts_item_data in _payer_accounts or []:
            payer_accounts_item = PayerAccountRefInput.from_dict(
                payer_accounts_item_data
            )

            payer_accounts.append(payer_accounts_item)

        _bill_to_party = d.pop("billToParty", UNSET)
        bill_to_party: Union[Unset, BillToPartyInput]
        if isinstance(_bill_to_party, Unset):
            bill_to_party = UNSET
        else:
            bill_to_party = BillToPartyInput.from_dict(_bill_to_party)

        bill_to = d.pop("billTo", UNSET)

        cost_center = d.pop("costCenter", UNSET)

        budget_owner = d.pop("budgetOwner", UNSET)

        buyer_name = d.pop("buyerName", UNSET)

        supplier_site = d.pop("supplierSite", UNSET)

        supplier_contact_email = d.pop("supplierContactEmail", UNSET)

        notes = d.pop("notes", UNSET)

        contract_id = d.pop("contractId", UNSET)

        quote_import_id = d.pop("quoteImportId", UNSET)

        draft = d.pop("draft", UNSET)

        create_purchase_order_input = cls(
            supplier=supplier,
            line_items=line_items,
            po_number=po_number,
            supplier_region_id=supplier_region_id,
            currency=currency,
            provider=provider,
            payer_accounts=payer_accounts,
            bill_to_party=bill_to_party,
            bill_to=bill_to,
            cost_center=cost_center,
            budget_owner=budget_owner,
            buyer_name=buyer_name,
            supplier_site=supplier_site,
            supplier_contact_email=supplier_contact_email,
            notes=notes,
            contract_id=contract_id,
            quote_import_id=quote_import_id,
            draft=draft,
        )

        create_purchase_order_input.additional_properties = d
        return create_purchase_order_input

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
