from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Type,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_invoice_result_supplier_invoice_document_type import (
    GetInvoiceResultSupplierInvoiceDocumentType,
    check_get_invoice_result_supplier_invoice_document_type,
)
from ..models.get_invoice_result_supplier_invoice_due_date_source import (
    GetInvoiceResultSupplierInvoiceDueDateSource,
    check_get_invoice_result_supplier_invoice_due_date_source,
)
from ..models.get_invoice_result_supplier_invoice_entered_by import (
    GetInvoiceResultSupplierInvoiceEnteredBy,
    check_get_invoice_result_supplier_invoice_entered_by,
)
from ..models.get_invoice_result_supplier_invoice_invoice_kind import (
    GetInvoiceResultSupplierInvoiceInvoiceKind,
    check_get_invoice_result_supplier_invoice_invoice_kind,
)
from ..models.get_invoice_result_supplier_invoice_match_status import (
    GetInvoiceResultSupplierInvoiceMatchStatus,
    check_get_invoice_result_supplier_invoice_match_status,
)
from ..models.get_invoice_result_supplier_invoice_payment_route import (
    GetInvoiceResultSupplierInvoicePaymentRoute,
    check_get_invoice_result_supplier_invoice_payment_route,
)
from ..models.get_invoice_result_supplier_invoice_source import (
    GetInvoiceResultSupplierInvoiceSource,
    check_get_invoice_result_supplier_invoice_source,
)
from ..models.get_invoice_result_supplier_invoice_submitted_format import (
    GetInvoiceResultSupplierInvoiceSubmittedFormat,
    check_get_invoice_result_supplier_invoice_submitted_format,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_invoice_result_supplier_invoice_party_details import (
        GetInvoiceResultSupplierInvoicePartyDetails,
    )
    from ..models.get_invoice_result_supplier_invoice_payment_type_0 import (
        GetInvoiceResultSupplierInvoicePaymentType0,
    )
    from ..models.get_invoice_result_supplier_invoice_payment_type_1 import (
        GetInvoiceResultSupplierInvoicePaymentType1,
    )
    from ..models.get_invoice_result_supplier_invoice_withdrawn_payment_type_0 import (
        GetInvoiceResultSupplierInvoiceWithdrawnPaymentType0,
    )
    from ..models.get_invoice_result_supplier_invoice_withdrawn_payment_type_1 import (
        GetInvoiceResultSupplierInvoiceWithdrawnPaymentType1,
    )
    from ..models.invoice_adjustment import InvoiceAdjustment
    from ..models.invoice_base_currency_amount import InvoiceBaseCurrencyAmount
    from ..models.invoice_breakdown_entry import InvoiceBreakdownEntry
    from ..models.invoice_credit_application import InvoiceCreditApplication
    from ..models.invoice_currency_amount import InvoiceCurrencyAmount
    from ..models.invoice_deduction import InvoiceDeduction
    from ..models.invoice_duplicate_ref import InvoiceDuplicateRef
    from ..models.invoice_line_item import InvoiceLineItem
    from ..models.invoice_rejection import InvoiceRejection
    from ..models.invoice_replacement_check import InvoiceReplacementCheck
    from ..models.invoice_source_document import InvoiceSourceDocument
    from ..models.late_fee_terms import LateFeeTerms
    from ..models.no_po_comparison import NoPoComparison
    from ..models.remittance_instructions import RemittanceInstructions
    from ..models.supplier_approval_view import SupplierApprovalView
    from ..models.supplier_bank_details_confirmation_view import (
        SupplierBankDetailsConfirmationView,
    )
    from ..models.supplier_payment_problem_view import SupplierPaymentProblemView
    from ..models.supplier_remittance_view import SupplierRemittanceView
    from ..models.supplier_settlement_view import SupplierSettlementView
    from ..models.uncredited_original import UncreditedOriginal


T = TypeVar("T", bound="GetInvoiceResultSupplierInvoice")


@_attrs_define
class GetInvoiceResultSupplierInvoice:
    """
    Attributes:
        id (str):
        replacement (Union[Unset, InvoiceReplacementCheck]):
        uncredited_originals (Union[Unset, List['UncreditedOriginal']]):
        supplier (Union[Unset, str]):
        buyer_org_id (Union[Unset, str]):
        supplier_org_id (Union[Unset, str]):
        created_at (Union[Unset, str]):
        late_fee_terms (Union[Unset, LateFeeTerms]):
        amount (Union[Unset, float]):
        supplier_connection_id (Union[Unset, str]):
        currency (Union[Unset, str]):
        buyer_org_name (Union[Unset, str]):
        buyer_region_name (Union[Unset, str]):
        supplier_region_name (Union[Unset, str]):
        contract_id (Union[Unset, str]):
        line_items (Union[Unset, List['InvoiceLineItem']]):
        po (Union[Unset, str]):
        po_line_no (Union[Unset, float]):
        bills_no_po_line (Union[Unset, bool]):
        party_details (Union[Unset, GetInvoiceResultSupplierInvoicePartyDetails]):
        match_status (Union[Unset, GetInvoiceResultSupplierInvoiceMatchStatus]):
        no_po_comparison (Union[Unset, NoPoComparison]):
        payment_route (Union[Unset, GetInvoiceResultSupplierInvoicePaymentRoute]):
        paid (Union[Unset, bool]):
        due_in_days (Union[Unset, float]):
        due_date (Union[Unset, str]):
        paid_at (Union[Unset, str]):
        due_date_source (Union[Unset, GetInvoiceResultSupplierInvoiceDueDateSource]):
        last_reminded_at (Union[Unset, str]):
        rejection (Union[Unset, InvoiceRejection]):
        replaces_invoice_id (Union[Unset, str]):
        replaces_invoice_ids (Union[Unset, List[str]]):
        replaced_by_invoice_ids (Union[Unset, List[str]]):
        possible_duplicates (Union[Unset, List['InvoiceDuplicateRef']]):
        duplicates_checked (Union[Unset, bool]):
        has_lookup_rows (Union[Unset, bool]):
        source (Union[Unset, GetInvoiceResultSupplierInvoiceSource]):
        entered_by (Union[Unset, GetInvoiceResultSupplierInvoiceEnteredBy]):
        invoice_date (Union[Unset, str]):
        submitted_format (Union[Unset, GetInvoiceResultSupplierInvoiceSubmittedFormat]):
        external_invoice_number (Union[Unset, str]):
        adjustments (Union[Unset, List['InvoiceAdjustment']]):
        tax_amount (Union[Unset, float]):
        tax_breakdown (Union[Unset, List['InvoiceBreakdownEntry']]):
        withholdings (Union[Unset, List['InvoiceBreakdownEntry']]):
        document_type (Union[Unset, GetInvoiceResultSupplierInvoiceDocumentType]):
        amends_invoice_id (Union[Unset, str]):
        amends_external_invoice_number (Union[Unset, str]):
        debit_note_ids (Union[Unset, List[str]]):
        invoice_kind (Union[Unset, GetInvoiceResultSupplierInvoiceInvoiceKind]):
        deductions (Union[Unset, List['InvoiceDeduction']]):
        credit_applications (Union[Unset, List['InvoiceCreditApplication']]):
        credit_note_ids (Union[Unset, List[str]]):
        credit_version (Union[Unset, float]):
        payment_currency_amount (Union[Unset, InvoiceCurrencyAmount]):
        tax_currency_amount (Union[Unset, InvoiceCurrencyAmount]):
        remittance_instructions (Union[Unset, RemittanceInstructions]):
        bank_lane (Union[Unset, str]):
        source_document (Union[Unset, InvoiceSourceDocument]):
        has_original_pdf (Union[Unset, bool]):
        settlement (Union[Unset, SupplierSettlementView]):
        payment_problem (Union[Unset, SupplierPaymentProblemView]):
        bank_details_confirmation (Union[Unset, SupplierBankDetailsConfirmationView]):
        base_currency_amount (Union[Unset, InvoiceBaseCurrencyAmount]):
        approval (Union[Unset, SupplierApprovalView]):
        payment (Union['GetInvoiceResultSupplierInvoicePaymentType0', 'GetInvoiceResultSupplierInvoicePaymentType1',
            Unset]):
        withdrawn_payment (Union['GetInvoiceResultSupplierInvoiceWithdrawnPaymentType0',
            'GetInvoiceResultSupplierInvoiceWithdrawnPaymentType1', Unset]):
        remittances (Union[Unset, List['SupplierRemittanceView']]):
        buyer_workspace_id (Union[Unset, str]):
        next_reminder_at (Union[Unset, str]):
    """

    id: str
    replacement: Union[Unset, "InvoiceReplacementCheck"] = UNSET
    uncredited_originals: Union[Unset, List["UncreditedOriginal"]] = UNSET
    supplier: Union[Unset, str] = UNSET
    buyer_org_id: Union[Unset, str] = UNSET
    supplier_org_id: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    late_fee_terms: Union[Unset, "LateFeeTerms"] = UNSET
    amount: Union[Unset, float] = UNSET
    supplier_connection_id: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    buyer_org_name: Union[Unset, str] = UNSET
    buyer_region_name: Union[Unset, str] = UNSET
    supplier_region_name: Union[Unset, str] = UNSET
    contract_id: Union[Unset, str] = UNSET
    line_items: Union[Unset, List["InvoiceLineItem"]] = UNSET
    po: Union[Unset, str] = UNSET
    po_line_no: Union[Unset, float] = UNSET
    bills_no_po_line: Union[Unset, bool] = UNSET
    party_details: Union[Unset, "GetInvoiceResultSupplierInvoicePartyDetails"] = UNSET
    match_status: Union[Unset, GetInvoiceResultSupplierInvoiceMatchStatus] = UNSET
    no_po_comparison: Union[Unset, "NoPoComparison"] = UNSET
    payment_route: Union[Unset, GetInvoiceResultSupplierInvoicePaymentRoute] = UNSET
    paid: Union[Unset, bool] = UNSET
    due_in_days: Union[Unset, float] = UNSET
    due_date: Union[Unset, str] = UNSET
    paid_at: Union[Unset, str] = UNSET
    due_date_source: Union[Unset, GetInvoiceResultSupplierInvoiceDueDateSource] = UNSET
    last_reminded_at: Union[Unset, str] = UNSET
    rejection: Union[Unset, "InvoiceRejection"] = UNSET
    replaces_invoice_id: Union[Unset, str] = UNSET
    replaces_invoice_ids: Union[Unset, List[str]] = UNSET
    replaced_by_invoice_ids: Union[Unset, List[str]] = UNSET
    possible_duplicates: Union[Unset, List["InvoiceDuplicateRef"]] = UNSET
    duplicates_checked: Union[Unset, bool] = UNSET
    has_lookup_rows: Union[Unset, bool] = UNSET
    source: Union[Unset, GetInvoiceResultSupplierInvoiceSource] = UNSET
    entered_by: Union[Unset, GetInvoiceResultSupplierInvoiceEnteredBy] = UNSET
    invoice_date: Union[Unset, str] = UNSET
    submitted_format: Union[Unset, GetInvoiceResultSupplierInvoiceSubmittedFormat] = (
        UNSET
    )
    external_invoice_number: Union[Unset, str] = UNSET
    adjustments: Union[Unset, List["InvoiceAdjustment"]] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    tax_breakdown: Union[Unset, List["InvoiceBreakdownEntry"]] = UNSET
    withholdings: Union[Unset, List["InvoiceBreakdownEntry"]] = UNSET
    document_type: Union[Unset, GetInvoiceResultSupplierInvoiceDocumentType] = UNSET
    amends_invoice_id: Union[Unset, str] = UNSET
    amends_external_invoice_number: Union[Unset, str] = UNSET
    debit_note_ids: Union[Unset, List[str]] = UNSET
    invoice_kind: Union[Unset, GetInvoiceResultSupplierInvoiceInvoiceKind] = UNSET
    deductions: Union[Unset, List["InvoiceDeduction"]] = UNSET
    credit_applications: Union[Unset, List["InvoiceCreditApplication"]] = UNSET
    credit_note_ids: Union[Unset, List[str]] = UNSET
    credit_version: Union[Unset, float] = UNSET
    payment_currency_amount: Union[Unset, "InvoiceCurrencyAmount"] = UNSET
    tax_currency_amount: Union[Unset, "InvoiceCurrencyAmount"] = UNSET
    remittance_instructions: Union[Unset, "RemittanceInstructions"] = UNSET
    bank_lane: Union[Unset, str] = UNSET
    source_document: Union[Unset, "InvoiceSourceDocument"] = UNSET
    has_original_pdf: Union[Unset, bool] = UNSET
    settlement: Union[Unset, "SupplierSettlementView"] = UNSET
    payment_problem: Union[Unset, "SupplierPaymentProblemView"] = UNSET
    bank_details_confirmation: Union[Unset, "SupplierBankDetailsConfirmationView"] = (
        UNSET
    )
    base_currency_amount: Union[Unset, "InvoiceBaseCurrencyAmount"] = UNSET
    approval: Union[Unset, "SupplierApprovalView"] = UNSET
    payment: Union[
        "GetInvoiceResultSupplierInvoicePaymentType0",
        "GetInvoiceResultSupplierInvoicePaymentType1",
        Unset,
    ] = UNSET
    withdrawn_payment: Union[
        "GetInvoiceResultSupplierInvoiceWithdrawnPaymentType0",
        "GetInvoiceResultSupplierInvoiceWithdrawnPaymentType1",
        Unset,
    ] = UNSET
    remittances: Union[Unset, List["SupplierRemittanceView"]] = UNSET
    buyer_workspace_id: Union[Unset, str] = UNSET
    next_reminder_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.get_invoice_result_supplier_invoice_payment_type_0 import (
            GetInvoiceResultSupplierInvoicePaymentType0,
        )
        from ..models.get_invoice_result_supplier_invoice_withdrawn_payment_type_0 import (
            GetInvoiceResultSupplierInvoiceWithdrawnPaymentType0,
        )

        id = self.id

        replacement: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.replacement, Unset):
            replacement = self.replacement.to_dict()

        uncredited_originals: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.uncredited_originals, Unset):
            uncredited_originals = []
            for uncredited_originals_item_data in self.uncredited_originals:
                uncredited_originals_item = uncredited_originals_item_data.to_dict()
                uncredited_originals.append(uncredited_originals_item)

        supplier = self.supplier

        buyer_org_id = self.buyer_org_id

        supplier_org_id = self.supplier_org_id

        created_at = self.created_at

        late_fee_terms: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.late_fee_terms, Unset):
            late_fee_terms = self.late_fee_terms.to_dict()

        amount = self.amount

        supplier_connection_id = self.supplier_connection_id

        currency = self.currency

        buyer_org_name = self.buyer_org_name

        buyer_region_name = self.buyer_region_name

        supplier_region_name = self.supplier_region_name

        contract_id = self.contract_id

        line_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.line_items, Unset):
            line_items = []
            for line_items_item_data in self.line_items:
                line_items_item = line_items_item_data.to_dict()
                line_items.append(line_items_item)

        po = self.po

        po_line_no = self.po_line_no

        bills_no_po_line = self.bills_no_po_line

        party_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.party_details, Unset):
            party_details = self.party_details.to_dict()

        match_status: Union[Unset, str] = UNSET
        if not isinstance(self.match_status, Unset):
            match_status = self.match_status

        no_po_comparison: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.no_po_comparison, Unset):
            no_po_comparison = self.no_po_comparison.to_dict()

        payment_route: Union[Unset, str] = UNSET
        if not isinstance(self.payment_route, Unset):
            payment_route = self.payment_route

        paid = self.paid

        due_in_days = self.due_in_days

        due_date = self.due_date

        paid_at = self.paid_at

        due_date_source: Union[Unset, str] = UNSET
        if not isinstance(self.due_date_source, Unset):
            due_date_source = self.due_date_source

        last_reminded_at = self.last_reminded_at

        rejection: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rejection, Unset):
            rejection = self.rejection.to_dict()

        replaces_invoice_id = self.replaces_invoice_id

        replaces_invoice_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.replaces_invoice_ids, Unset):
            replaces_invoice_ids = self.replaces_invoice_ids

        replaced_by_invoice_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.replaced_by_invoice_ids, Unset):
            replaced_by_invoice_ids = self.replaced_by_invoice_ids

        possible_duplicates: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.possible_duplicates, Unset):
            possible_duplicates = []
            for possible_duplicates_item_data in self.possible_duplicates:
                possible_duplicates_item = possible_duplicates_item_data.to_dict()
                possible_duplicates.append(possible_duplicates_item)

        duplicates_checked = self.duplicates_checked

        has_lookup_rows = self.has_lookup_rows

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source

        entered_by: Union[Unset, str] = UNSET
        if not isinstance(self.entered_by, Unset):
            entered_by = self.entered_by

        invoice_date = self.invoice_date

        submitted_format: Union[Unset, str] = UNSET
        if not isinstance(self.submitted_format, Unset):
            submitted_format = self.submitted_format

        external_invoice_number = self.external_invoice_number

        adjustments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.adjustments, Unset):
            adjustments = []
            for adjustments_item_data in self.adjustments:
                adjustments_item = adjustments_item_data.to_dict()
                adjustments.append(adjustments_item)

        tax_amount = self.tax_amount

        tax_breakdown: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tax_breakdown, Unset):
            tax_breakdown = []
            for tax_breakdown_item_data in self.tax_breakdown:
                tax_breakdown_item = tax_breakdown_item_data.to_dict()
                tax_breakdown.append(tax_breakdown_item)

        withholdings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.withholdings, Unset):
            withholdings = []
            for withholdings_item_data in self.withholdings:
                withholdings_item = withholdings_item_data.to_dict()
                withholdings.append(withholdings_item)

        document_type: Union[Unset, str] = UNSET
        if not isinstance(self.document_type, Unset):
            document_type = self.document_type

        amends_invoice_id = self.amends_invoice_id

        amends_external_invoice_number = self.amends_external_invoice_number

        debit_note_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.debit_note_ids, Unset):
            debit_note_ids = self.debit_note_ids

        invoice_kind: Union[Unset, str] = UNSET
        if not isinstance(self.invoice_kind, Unset):
            invoice_kind = self.invoice_kind

        deductions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.deductions, Unset):
            deductions = []
            for deductions_item_data in self.deductions:
                deductions_item = deductions_item_data.to_dict()
                deductions.append(deductions_item)

        credit_applications: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.credit_applications, Unset):
            credit_applications = []
            for credit_applications_item_data in self.credit_applications:
                credit_applications_item = credit_applications_item_data.to_dict()
                credit_applications.append(credit_applications_item)

        credit_note_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.credit_note_ids, Unset):
            credit_note_ids = self.credit_note_ids

        credit_version = self.credit_version

        payment_currency_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_currency_amount, Unset):
            payment_currency_amount = self.payment_currency_amount.to_dict()

        tax_currency_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_currency_amount, Unset):
            tax_currency_amount = self.tax_currency_amount.to_dict()

        remittance_instructions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.remittance_instructions, Unset):
            remittance_instructions = self.remittance_instructions.to_dict()

        bank_lane = self.bank_lane

        source_document: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.source_document, Unset):
            source_document = self.source_document.to_dict()

        has_original_pdf = self.has_original_pdf

        settlement: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.settlement, Unset):
            settlement = self.settlement.to_dict()

        payment_problem: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_problem, Unset):
            payment_problem = self.payment_problem.to_dict()

        bank_details_confirmation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bank_details_confirmation, Unset):
            bank_details_confirmation = self.bank_details_confirmation.to_dict()

        base_currency_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.base_currency_amount, Unset):
            base_currency_amount = self.base_currency_amount.to_dict()

        approval: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.approval, Unset):
            approval = self.approval.to_dict()

        payment: Union[Dict[str, Any], Unset]
        if isinstance(self.payment, Unset):
            payment = UNSET
        elif isinstance(self.payment, GetInvoiceResultSupplierInvoicePaymentType0):
            payment = self.payment.to_dict()
        else:
            payment = self.payment.to_dict()

        withdrawn_payment: Union[Dict[str, Any], Unset]
        if isinstance(self.withdrawn_payment, Unset):
            withdrawn_payment = UNSET
        elif isinstance(
            self.withdrawn_payment, GetInvoiceResultSupplierInvoiceWithdrawnPaymentType0
        ):
            withdrawn_payment = self.withdrawn_payment.to_dict()
        else:
            withdrawn_payment = self.withdrawn_payment.to_dict()

        remittances: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.remittances, Unset):
            remittances = []
            for remittances_item_data in self.remittances:
                remittances_item = remittances_item_data.to_dict()
                remittances.append(remittances_item)

        buyer_workspace_id = self.buyer_workspace_id

        next_reminder_at = self.next_reminder_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if replacement is not UNSET:
            field_dict["replacement"] = replacement
        if uncredited_originals is not UNSET:
            field_dict["uncreditedOriginals"] = uncredited_originals
        if supplier is not UNSET:
            field_dict["supplier"] = supplier
        if buyer_org_id is not UNSET:
            field_dict["buyerOrgId"] = buyer_org_id
        if supplier_org_id is not UNSET:
            field_dict["supplierOrgId"] = supplier_org_id
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if late_fee_terms is not UNSET:
            field_dict["lateFeeTerms"] = late_fee_terms
        if amount is not UNSET:
            field_dict["amount"] = amount
        if supplier_connection_id is not UNSET:
            field_dict["supplierConnectionId"] = supplier_connection_id
        if currency is not UNSET:
            field_dict["currency"] = currency
        if buyer_org_name is not UNSET:
            field_dict["buyerOrgName"] = buyer_org_name
        if buyer_region_name is not UNSET:
            field_dict["buyerRegionName"] = buyer_region_name
        if supplier_region_name is not UNSET:
            field_dict["supplierRegionName"] = supplier_region_name
        if contract_id is not UNSET:
            field_dict["contractId"] = contract_id
        if line_items is not UNSET:
            field_dict["lineItems"] = line_items
        if po is not UNSET:
            field_dict["po"] = po
        if po_line_no is not UNSET:
            field_dict["poLineNo"] = po_line_no
        if bills_no_po_line is not UNSET:
            field_dict["billsNoPoLine"] = bills_no_po_line
        if party_details is not UNSET:
            field_dict["partyDetails"] = party_details
        if match_status is not UNSET:
            field_dict["matchStatus"] = match_status
        if no_po_comparison is not UNSET:
            field_dict["noPoComparison"] = no_po_comparison
        if payment_route is not UNSET:
            field_dict["paymentRoute"] = payment_route
        if paid is not UNSET:
            field_dict["paid"] = paid
        if due_in_days is not UNSET:
            field_dict["dueInDays"] = due_in_days
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if paid_at is not UNSET:
            field_dict["paidAt"] = paid_at
        if due_date_source is not UNSET:
            field_dict["dueDateSource"] = due_date_source
        if last_reminded_at is not UNSET:
            field_dict["lastRemindedAt"] = last_reminded_at
        if rejection is not UNSET:
            field_dict["rejection"] = rejection
        if replaces_invoice_id is not UNSET:
            field_dict["replacesInvoiceId"] = replaces_invoice_id
        if replaces_invoice_ids is not UNSET:
            field_dict["replacesInvoiceIds"] = replaces_invoice_ids
        if replaced_by_invoice_ids is not UNSET:
            field_dict["replacedByInvoiceIds"] = replaced_by_invoice_ids
        if possible_duplicates is not UNSET:
            field_dict["possibleDuplicates"] = possible_duplicates
        if duplicates_checked is not UNSET:
            field_dict["duplicatesChecked"] = duplicates_checked
        if has_lookup_rows is not UNSET:
            field_dict["hasLookupRows"] = has_lookup_rows
        if source is not UNSET:
            field_dict["source"] = source
        if entered_by is not UNSET:
            field_dict["enteredBy"] = entered_by
        if invoice_date is not UNSET:
            field_dict["invoiceDate"] = invoice_date
        if submitted_format is not UNSET:
            field_dict["submittedFormat"] = submitted_format
        if external_invoice_number is not UNSET:
            field_dict["externalInvoiceNumber"] = external_invoice_number
        if adjustments is not UNSET:
            field_dict["adjustments"] = adjustments
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount
        if tax_breakdown is not UNSET:
            field_dict["taxBreakdown"] = tax_breakdown
        if withholdings is not UNSET:
            field_dict["withholdings"] = withholdings
        if document_type is not UNSET:
            field_dict["documentType"] = document_type
        if amends_invoice_id is not UNSET:
            field_dict["amendsInvoiceId"] = amends_invoice_id
        if amends_external_invoice_number is not UNSET:
            field_dict["amendsExternalInvoiceNumber"] = amends_external_invoice_number
        if debit_note_ids is not UNSET:
            field_dict["debitNoteIds"] = debit_note_ids
        if invoice_kind is not UNSET:
            field_dict["invoiceKind"] = invoice_kind
        if deductions is not UNSET:
            field_dict["deductions"] = deductions
        if credit_applications is not UNSET:
            field_dict["creditApplications"] = credit_applications
        if credit_note_ids is not UNSET:
            field_dict["creditNoteIds"] = credit_note_ids
        if credit_version is not UNSET:
            field_dict["creditVersion"] = credit_version
        if payment_currency_amount is not UNSET:
            field_dict["paymentCurrencyAmount"] = payment_currency_amount
        if tax_currency_amount is not UNSET:
            field_dict["taxCurrencyAmount"] = tax_currency_amount
        if remittance_instructions is not UNSET:
            field_dict["remittanceInstructions"] = remittance_instructions
        if bank_lane is not UNSET:
            field_dict["bankLane"] = bank_lane
        if source_document is not UNSET:
            field_dict["sourceDocument"] = source_document
        if has_original_pdf is not UNSET:
            field_dict["hasOriginalPdf"] = has_original_pdf
        if settlement is not UNSET:
            field_dict["settlement"] = settlement
        if payment_problem is not UNSET:
            field_dict["paymentProblem"] = payment_problem
        if bank_details_confirmation is not UNSET:
            field_dict["bankDetailsConfirmation"] = bank_details_confirmation
        if base_currency_amount is not UNSET:
            field_dict["baseCurrencyAmount"] = base_currency_amount
        if approval is not UNSET:
            field_dict["approval"] = approval
        if payment is not UNSET:
            field_dict["payment"] = payment
        if withdrawn_payment is not UNSET:
            field_dict["withdrawnPayment"] = withdrawn_payment
        if remittances is not UNSET:
            field_dict["remittances"] = remittances
        if buyer_workspace_id is not UNSET:
            field_dict["buyerWorkspaceId"] = buyer_workspace_id
        if next_reminder_at is not UNSET:
            field_dict["nextReminderAt"] = next_reminder_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_invoice_result_supplier_invoice_party_details import (
            GetInvoiceResultSupplierInvoicePartyDetails,
        )
        from ..models.get_invoice_result_supplier_invoice_payment_type_0 import (
            GetInvoiceResultSupplierInvoicePaymentType0,
        )
        from ..models.get_invoice_result_supplier_invoice_payment_type_1 import (
            GetInvoiceResultSupplierInvoicePaymentType1,
        )
        from ..models.get_invoice_result_supplier_invoice_withdrawn_payment_type_0 import (
            GetInvoiceResultSupplierInvoiceWithdrawnPaymentType0,
        )
        from ..models.get_invoice_result_supplier_invoice_withdrawn_payment_type_1 import (
            GetInvoiceResultSupplierInvoiceWithdrawnPaymentType1,
        )
        from ..models.invoice_adjustment import InvoiceAdjustment
        from ..models.invoice_base_currency_amount import InvoiceBaseCurrencyAmount
        from ..models.invoice_breakdown_entry import InvoiceBreakdownEntry
        from ..models.invoice_credit_application import InvoiceCreditApplication
        from ..models.invoice_currency_amount import InvoiceCurrencyAmount
        from ..models.invoice_deduction import InvoiceDeduction
        from ..models.invoice_duplicate_ref import InvoiceDuplicateRef
        from ..models.invoice_line_item import InvoiceLineItem
        from ..models.invoice_rejection import InvoiceRejection
        from ..models.invoice_replacement_check import InvoiceReplacementCheck
        from ..models.invoice_source_document import InvoiceSourceDocument
        from ..models.late_fee_terms import LateFeeTerms
        from ..models.no_po_comparison import NoPoComparison
        from ..models.remittance_instructions import RemittanceInstructions
        from ..models.supplier_approval_view import SupplierApprovalView
        from ..models.supplier_bank_details_confirmation_view import (
            SupplierBankDetailsConfirmationView,
        )
        from ..models.supplier_payment_problem_view import SupplierPaymentProblemView
        from ..models.supplier_remittance_view import SupplierRemittanceView
        from ..models.supplier_settlement_view import SupplierSettlementView
        from ..models.uncredited_original import UncreditedOriginal

        d = src_dict.copy()
        id = d.pop("id")

        _replacement = d.pop("replacement", UNSET)
        replacement: Union[Unset, InvoiceReplacementCheck]
        if isinstance(_replacement, Unset):
            replacement = UNSET
        else:
            replacement = InvoiceReplacementCheck.from_dict(_replacement)

        uncredited_originals = []
        _uncredited_originals = d.pop("uncreditedOriginals", UNSET)
        for uncredited_originals_item_data in _uncredited_originals or []:
            uncredited_originals_item = UncreditedOriginal.from_dict(
                uncredited_originals_item_data
            )

            uncredited_originals.append(uncredited_originals_item)

        supplier = d.pop("supplier", UNSET)

        buyer_org_id = d.pop("buyerOrgId", UNSET)

        supplier_org_id = d.pop("supplierOrgId", UNSET)

        created_at = d.pop("createdAt", UNSET)

        _late_fee_terms = d.pop("lateFeeTerms", UNSET)
        late_fee_terms: Union[Unset, LateFeeTerms]
        if isinstance(_late_fee_terms, Unset):
            late_fee_terms = UNSET
        else:
            late_fee_terms = LateFeeTerms.from_dict(_late_fee_terms)

        amount = d.pop("amount", UNSET)

        supplier_connection_id = d.pop("supplierConnectionId", UNSET)

        currency = d.pop("currency", UNSET)

        buyer_org_name = d.pop("buyerOrgName", UNSET)

        buyer_region_name = d.pop("buyerRegionName", UNSET)

        supplier_region_name = d.pop("supplierRegionName", UNSET)

        contract_id = d.pop("contractId", UNSET)

        line_items = []
        _line_items = d.pop("lineItems", UNSET)
        for line_items_item_data in _line_items or []:
            line_items_item = InvoiceLineItem.from_dict(line_items_item_data)

            line_items.append(line_items_item)

        po = d.pop("po", UNSET)

        po_line_no = d.pop("poLineNo", UNSET)

        bills_no_po_line = d.pop("billsNoPoLine", UNSET)

        _party_details = d.pop("partyDetails", UNSET)
        party_details: Union[Unset, GetInvoiceResultSupplierInvoicePartyDetails]
        if isinstance(_party_details, Unset):
            party_details = UNSET
        else:
            party_details = GetInvoiceResultSupplierInvoicePartyDetails.from_dict(
                _party_details
            )

        _match_status = d.pop("matchStatus", UNSET)
        match_status: Union[Unset, GetInvoiceResultSupplierInvoiceMatchStatus]
        if isinstance(_match_status, Unset):
            match_status = UNSET
        else:
            match_status = check_get_invoice_result_supplier_invoice_match_status(
                _match_status
            )

        _no_po_comparison = d.pop("noPoComparison", UNSET)
        no_po_comparison: Union[Unset, NoPoComparison]
        if isinstance(_no_po_comparison, Unset):
            no_po_comparison = UNSET
        else:
            no_po_comparison = NoPoComparison.from_dict(_no_po_comparison)

        _payment_route = d.pop("paymentRoute", UNSET)
        payment_route: Union[Unset, GetInvoiceResultSupplierInvoicePaymentRoute]
        if isinstance(_payment_route, Unset):
            payment_route = UNSET
        else:
            payment_route = check_get_invoice_result_supplier_invoice_payment_route(
                _payment_route
            )

        paid = d.pop("paid", UNSET)

        due_in_days = d.pop("dueInDays", UNSET)

        due_date = d.pop("dueDate", UNSET)

        paid_at = d.pop("paidAt", UNSET)

        _due_date_source = d.pop("dueDateSource", UNSET)
        due_date_source: Union[Unset, GetInvoiceResultSupplierInvoiceDueDateSource]
        if isinstance(_due_date_source, Unset):
            due_date_source = UNSET
        else:
            due_date_source = check_get_invoice_result_supplier_invoice_due_date_source(
                _due_date_source
            )

        last_reminded_at = d.pop("lastRemindedAt", UNSET)

        _rejection = d.pop("rejection", UNSET)
        rejection: Union[Unset, InvoiceRejection]
        if isinstance(_rejection, Unset):
            rejection = UNSET
        else:
            rejection = InvoiceRejection.from_dict(_rejection)

        replaces_invoice_id = d.pop("replacesInvoiceId", UNSET)

        replaces_invoice_ids = cast(List[str], d.pop("replacesInvoiceIds", UNSET))

        replaced_by_invoice_ids = cast(List[str], d.pop("replacedByInvoiceIds", UNSET))

        possible_duplicates = []
        _possible_duplicates = d.pop("possibleDuplicates", UNSET)
        for possible_duplicates_item_data in _possible_duplicates or []:
            possible_duplicates_item = InvoiceDuplicateRef.from_dict(
                possible_duplicates_item_data
            )

            possible_duplicates.append(possible_duplicates_item)

        duplicates_checked = d.pop("duplicatesChecked", UNSET)

        has_lookup_rows = d.pop("hasLookupRows", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, GetInvoiceResultSupplierInvoiceSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = check_get_invoice_result_supplier_invoice_source(_source)

        _entered_by = d.pop("enteredBy", UNSET)
        entered_by: Union[Unset, GetInvoiceResultSupplierInvoiceEnteredBy]
        if isinstance(_entered_by, Unset):
            entered_by = UNSET
        else:
            entered_by = check_get_invoice_result_supplier_invoice_entered_by(
                _entered_by
            )

        invoice_date = d.pop("invoiceDate", UNSET)

        _submitted_format = d.pop("submittedFormat", UNSET)
        submitted_format: Union[Unset, GetInvoiceResultSupplierInvoiceSubmittedFormat]
        if isinstance(_submitted_format, Unset):
            submitted_format = UNSET
        else:
            submitted_format = (
                check_get_invoice_result_supplier_invoice_submitted_format(
                    _submitted_format
                )
            )

        external_invoice_number = d.pop("externalInvoiceNumber", UNSET)

        adjustments = []
        _adjustments = d.pop("adjustments", UNSET)
        for adjustments_item_data in _adjustments or []:
            adjustments_item = InvoiceAdjustment.from_dict(adjustments_item_data)

            adjustments.append(adjustments_item)

        tax_amount = d.pop("taxAmount", UNSET)

        tax_breakdown = []
        _tax_breakdown = d.pop("taxBreakdown", UNSET)
        for tax_breakdown_item_data in _tax_breakdown or []:
            tax_breakdown_item = InvoiceBreakdownEntry.from_dict(
                tax_breakdown_item_data
            )

            tax_breakdown.append(tax_breakdown_item)

        withholdings = []
        _withholdings = d.pop("withholdings", UNSET)
        for withholdings_item_data in _withholdings or []:
            withholdings_item = InvoiceBreakdownEntry.from_dict(withholdings_item_data)

            withholdings.append(withholdings_item)

        _document_type = d.pop("documentType", UNSET)
        document_type: Union[Unset, GetInvoiceResultSupplierInvoiceDocumentType]
        if isinstance(_document_type, Unset):
            document_type = UNSET
        else:
            document_type = check_get_invoice_result_supplier_invoice_document_type(
                _document_type
            )

        amends_invoice_id = d.pop("amendsInvoiceId", UNSET)

        amends_external_invoice_number = d.pop("amendsExternalInvoiceNumber", UNSET)

        debit_note_ids = cast(List[str], d.pop("debitNoteIds", UNSET))

        _invoice_kind = d.pop("invoiceKind", UNSET)
        invoice_kind: Union[Unset, GetInvoiceResultSupplierInvoiceInvoiceKind]
        if isinstance(_invoice_kind, Unset):
            invoice_kind = UNSET
        else:
            invoice_kind = check_get_invoice_result_supplier_invoice_invoice_kind(
                _invoice_kind
            )

        deductions = []
        _deductions = d.pop("deductions", UNSET)
        for deductions_item_data in _deductions or []:
            deductions_item = InvoiceDeduction.from_dict(deductions_item_data)

            deductions.append(deductions_item)

        credit_applications = []
        _credit_applications = d.pop("creditApplications", UNSET)
        for credit_applications_item_data in _credit_applications or []:
            credit_applications_item = InvoiceCreditApplication.from_dict(
                credit_applications_item_data
            )

            credit_applications.append(credit_applications_item)

        credit_note_ids = cast(List[str], d.pop("creditNoteIds", UNSET))

        credit_version = d.pop("creditVersion", UNSET)

        _payment_currency_amount = d.pop("paymentCurrencyAmount", UNSET)
        payment_currency_amount: Union[Unset, InvoiceCurrencyAmount]
        if isinstance(_payment_currency_amount, Unset):
            payment_currency_amount = UNSET
        else:
            payment_currency_amount = InvoiceCurrencyAmount.from_dict(
                _payment_currency_amount
            )

        _tax_currency_amount = d.pop("taxCurrencyAmount", UNSET)
        tax_currency_amount: Union[Unset, InvoiceCurrencyAmount]
        if isinstance(_tax_currency_amount, Unset):
            tax_currency_amount = UNSET
        else:
            tax_currency_amount = InvoiceCurrencyAmount.from_dict(_tax_currency_amount)

        _remittance_instructions = d.pop("remittanceInstructions", UNSET)
        remittance_instructions: Union[Unset, RemittanceInstructions]
        if isinstance(_remittance_instructions, Unset):
            remittance_instructions = UNSET
        else:
            remittance_instructions = RemittanceInstructions.from_dict(
                _remittance_instructions
            )

        bank_lane = d.pop("bankLane", UNSET)

        _source_document = d.pop("sourceDocument", UNSET)
        source_document: Union[Unset, InvoiceSourceDocument]
        if isinstance(_source_document, Unset):
            source_document = UNSET
        else:
            source_document = InvoiceSourceDocument.from_dict(_source_document)

        has_original_pdf = d.pop("hasOriginalPdf", UNSET)

        _settlement = d.pop("settlement", UNSET)
        settlement: Union[Unset, SupplierSettlementView]
        if isinstance(_settlement, Unset):
            settlement = UNSET
        else:
            settlement = SupplierSettlementView.from_dict(_settlement)

        _payment_problem = d.pop("paymentProblem", UNSET)
        payment_problem: Union[Unset, SupplierPaymentProblemView]
        if isinstance(_payment_problem, Unset):
            payment_problem = UNSET
        else:
            payment_problem = SupplierPaymentProblemView.from_dict(_payment_problem)

        _bank_details_confirmation = d.pop("bankDetailsConfirmation", UNSET)
        bank_details_confirmation: Union[Unset, SupplierBankDetailsConfirmationView]
        if isinstance(_bank_details_confirmation, Unset):
            bank_details_confirmation = UNSET
        else:
            bank_details_confirmation = SupplierBankDetailsConfirmationView.from_dict(
                _bank_details_confirmation
            )

        _base_currency_amount = d.pop("baseCurrencyAmount", UNSET)
        base_currency_amount: Union[Unset, InvoiceBaseCurrencyAmount]
        if isinstance(_base_currency_amount, Unset):
            base_currency_amount = UNSET
        else:
            base_currency_amount = InvoiceBaseCurrencyAmount.from_dict(
                _base_currency_amount
            )

        _approval = d.pop("approval", UNSET)
        approval: Union[Unset, SupplierApprovalView]
        if isinstance(_approval, Unset):
            approval = UNSET
        else:
            approval = SupplierApprovalView.from_dict(_approval)

        def _parse_payment(
            data: object,
        ) -> Union[
            "GetInvoiceResultSupplierInvoicePaymentType0",
            "GetInvoiceResultSupplierInvoicePaymentType1",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payment_type_0 = GetInvoiceResultSupplierInvoicePaymentType0.from_dict(
                    data
                )

                return payment_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            payment_type_1 = GetInvoiceResultSupplierInvoicePaymentType1.from_dict(data)

            return payment_type_1

        payment = _parse_payment(d.pop("payment", UNSET))

        def _parse_withdrawn_payment(
            data: object,
        ) -> Union[
            "GetInvoiceResultSupplierInvoiceWithdrawnPaymentType0",
            "GetInvoiceResultSupplierInvoiceWithdrawnPaymentType1",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                withdrawn_payment_type_0 = (
                    GetInvoiceResultSupplierInvoiceWithdrawnPaymentType0.from_dict(data)
                )

                return withdrawn_payment_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            withdrawn_payment_type_1 = (
                GetInvoiceResultSupplierInvoiceWithdrawnPaymentType1.from_dict(data)
            )

            return withdrawn_payment_type_1

        withdrawn_payment = _parse_withdrawn_payment(d.pop("withdrawnPayment", UNSET))

        remittances = []
        _remittances = d.pop("remittances", UNSET)
        for remittances_item_data in _remittances or []:
            remittances_item = SupplierRemittanceView.from_dict(remittances_item_data)

            remittances.append(remittances_item)

        buyer_workspace_id = d.pop("buyerWorkspaceId", UNSET)

        next_reminder_at = d.pop("nextReminderAt", UNSET)

        get_invoice_result_supplier_invoice = cls(
            id=id,
            replacement=replacement,
            uncredited_originals=uncredited_originals,
            supplier=supplier,
            buyer_org_id=buyer_org_id,
            supplier_org_id=supplier_org_id,
            created_at=created_at,
            late_fee_terms=late_fee_terms,
            amount=amount,
            supplier_connection_id=supplier_connection_id,
            currency=currency,
            buyer_org_name=buyer_org_name,
            buyer_region_name=buyer_region_name,
            supplier_region_name=supplier_region_name,
            contract_id=contract_id,
            line_items=line_items,
            po=po,
            po_line_no=po_line_no,
            bills_no_po_line=bills_no_po_line,
            party_details=party_details,
            match_status=match_status,
            no_po_comparison=no_po_comparison,
            payment_route=payment_route,
            paid=paid,
            due_in_days=due_in_days,
            due_date=due_date,
            paid_at=paid_at,
            due_date_source=due_date_source,
            last_reminded_at=last_reminded_at,
            rejection=rejection,
            replaces_invoice_id=replaces_invoice_id,
            replaces_invoice_ids=replaces_invoice_ids,
            replaced_by_invoice_ids=replaced_by_invoice_ids,
            possible_duplicates=possible_duplicates,
            duplicates_checked=duplicates_checked,
            has_lookup_rows=has_lookup_rows,
            source=source,
            entered_by=entered_by,
            invoice_date=invoice_date,
            submitted_format=submitted_format,
            external_invoice_number=external_invoice_number,
            adjustments=adjustments,
            tax_amount=tax_amount,
            tax_breakdown=tax_breakdown,
            withholdings=withholdings,
            document_type=document_type,
            amends_invoice_id=amends_invoice_id,
            amends_external_invoice_number=amends_external_invoice_number,
            debit_note_ids=debit_note_ids,
            invoice_kind=invoice_kind,
            deductions=deductions,
            credit_applications=credit_applications,
            credit_note_ids=credit_note_ids,
            credit_version=credit_version,
            payment_currency_amount=payment_currency_amount,
            tax_currency_amount=tax_currency_amount,
            remittance_instructions=remittance_instructions,
            bank_lane=bank_lane,
            source_document=source_document,
            has_original_pdf=has_original_pdf,
            settlement=settlement,
            payment_problem=payment_problem,
            bank_details_confirmation=bank_details_confirmation,
            base_currency_amount=base_currency_amount,
            approval=approval,
            payment=payment,
            withdrawn_payment=withdrawn_payment,
            remittances=remittances,
            buyer_workspace_id=buyer_workspace_id,
            next_reminder_at=next_reminder_at,
        )

        get_invoice_result_supplier_invoice.additional_properties = d
        return get_invoice_result_supplier_invoice

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
