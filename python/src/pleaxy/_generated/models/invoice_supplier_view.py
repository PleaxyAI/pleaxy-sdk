from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Type,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_supplier_view_due_date_source import (
    InvoiceSupplierViewDueDateSource,
    check_invoice_supplier_view_due_date_source,
)
from ..models.invoice_supplier_view_entered_by import (
    InvoiceSupplierViewEnteredBy,
    check_invoice_supplier_view_entered_by,
)
from ..models.invoice_supplier_view_match_status import (
    InvoiceSupplierViewMatchStatus,
    check_invoice_supplier_view_match_status,
)
from ..models.invoice_supplier_view_source import (
    InvoiceSupplierViewSource,
    check_invoice_supplier_view_source,
)
from ..models.invoice_supplier_view_submitted_format import (
    InvoiceSupplierViewSubmittedFormat,
    check_invoice_supplier_view_submitted_format,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_adjustment import InvoiceAdjustment
    from ..models.invoice_base_currency_amount import InvoiceBaseCurrencyAmount
    from ..models.invoice_breakdown_entry import InvoiceBreakdownEntry
    from ..models.invoice_currency_amount import InvoiceCurrencyAmount
    from ..models.invoice_line_item import InvoiceLineItem
    from ..models.invoice_rejection import InvoiceRejection
    from ..models.invoice_source_document import InvoiceSourceDocument
    from ..models.invoice_supplier_view_party_details import (
        InvoiceSupplierViewPartyDetails,
    )
    from ..models.invoice_supplier_view_payment_type_0 import (
        InvoiceSupplierViewPaymentType0,
    )
    from ..models.invoice_supplier_view_payment_type_1 import (
        InvoiceSupplierViewPaymentType1,
    )
    from ..models.invoice_supplier_view_withdrawn_payment_type_0 import (
        InvoiceSupplierViewWithdrawnPaymentType0,
    )
    from ..models.invoice_supplier_view_withdrawn_payment_type_1 import (
        InvoiceSupplierViewWithdrawnPaymentType1,
    )
    from ..models.late_fee_terms import LateFeeTerms
    from ..models.remittance_instructions import RemittanceInstructions
    from ..models.supplier_approval_view import SupplierApprovalView


T = TypeVar("T", bound="InvoiceSupplierView")


@_attrs_define
class InvoiceSupplierView:
    """
    Attributes:
        id (str):
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
        party_details (Union[Unset, InvoiceSupplierViewPartyDetails]):
        match_status (Union[Unset, InvoiceSupplierViewMatchStatus]):
        paid (Union[Unset, bool]):
        due_in_days (Union[Unset, float]):
        due_date (Union[Unset, str]):
        paid_at (Union[Unset, str]):
        due_date_source (Union[Unset, InvoiceSupplierViewDueDateSource]):
        last_reminded_at (Union[Unset, str]):
        rejection (Union[Unset, InvoiceRejection]):
        replaces_invoice_id (Union[Unset, str]):
        source (Union[Unset, InvoiceSupplierViewSource]):
        entered_by (Union[Unset, InvoiceSupplierViewEnteredBy]):
        invoice_date (Union[Unset, str]):
        submitted_format (Union[Unset, InvoiceSupplierViewSubmittedFormat]):
        external_invoice_number (Union[Unset, str]):
        adjustments (Union[Unset, List['InvoiceAdjustment']]):
        tax_amount (Union[Unset, float]):
        tax_breakdown (Union[Unset, List['InvoiceBreakdownEntry']]):
        withholdings (Union[Unset, List['InvoiceBreakdownEntry']]):
        payment_currency_amount (Union[Unset, InvoiceCurrencyAmount]):
        tax_currency_amount (Union[Unset, InvoiceCurrencyAmount]):
        remittance_instructions (Union[Unset, RemittanceInstructions]):
        source_document (Union[Unset, InvoiceSourceDocument]):
        has_original_pdf (Union[Unset, bool]):
        base_currency_amount (Union[Unset, InvoiceBaseCurrencyAmount]):
        approval (Union[Unset, SupplierApprovalView]):
        payment (Union['InvoiceSupplierViewPaymentType0', 'InvoiceSupplierViewPaymentType1', Unset]):
        withdrawn_payment (Union['InvoiceSupplierViewWithdrawnPaymentType0', 'InvoiceSupplierViewWithdrawnPaymentType1',
            Unset]):
        buyer_workspace_id (Union[Unset, str]):
        next_reminder_at (Union[Unset, str]):
    """

    id: str
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
    party_details: Union[Unset, "InvoiceSupplierViewPartyDetails"] = UNSET
    match_status: Union[Unset, InvoiceSupplierViewMatchStatus] = UNSET
    paid: Union[Unset, bool] = UNSET
    due_in_days: Union[Unset, float] = UNSET
    due_date: Union[Unset, str] = UNSET
    paid_at: Union[Unset, str] = UNSET
    due_date_source: Union[Unset, InvoiceSupplierViewDueDateSource] = UNSET
    last_reminded_at: Union[Unset, str] = UNSET
    rejection: Union[Unset, "InvoiceRejection"] = UNSET
    replaces_invoice_id: Union[Unset, str] = UNSET
    source: Union[Unset, InvoiceSupplierViewSource] = UNSET
    entered_by: Union[Unset, InvoiceSupplierViewEnteredBy] = UNSET
    invoice_date: Union[Unset, str] = UNSET
    submitted_format: Union[Unset, InvoiceSupplierViewSubmittedFormat] = UNSET
    external_invoice_number: Union[Unset, str] = UNSET
    adjustments: Union[Unset, List["InvoiceAdjustment"]] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    tax_breakdown: Union[Unset, List["InvoiceBreakdownEntry"]] = UNSET
    withholdings: Union[Unset, List["InvoiceBreakdownEntry"]] = UNSET
    payment_currency_amount: Union[Unset, "InvoiceCurrencyAmount"] = UNSET
    tax_currency_amount: Union[Unset, "InvoiceCurrencyAmount"] = UNSET
    remittance_instructions: Union[Unset, "RemittanceInstructions"] = UNSET
    source_document: Union[Unset, "InvoiceSourceDocument"] = UNSET
    has_original_pdf: Union[Unset, bool] = UNSET
    base_currency_amount: Union[Unset, "InvoiceBaseCurrencyAmount"] = UNSET
    approval: Union[Unset, "SupplierApprovalView"] = UNSET
    payment: Union[
        "InvoiceSupplierViewPaymentType0", "InvoiceSupplierViewPaymentType1", Unset
    ] = UNSET
    withdrawn_payment: Union[
        "InvoiceSupplierViewWithdrawnPaymentType0",
        "InvoiceSupplierViewWithdrawnPaymentType1",
        Unset,
    ] = UNSET
    buyer_workspace_id: Union[Unset, str] = UNSET
    next_reminder_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.invoice_supplier_view_payment_type_0 import (
            InvoiceSupplierViewPaymentType0,
        )
        from ..models.invoice_supplier_view_withdrawn_payment_type_0 import (
            InvoiceSupplierViewWithdrawnPaymentType0,
        )

        id = self.id

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

        party_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.party_details, Unset):
            party_details = self.party_details.to_dict()

        match_status: Union[Unset, str] = UNSET
        if not isinstance(self.match_status, Unset):
            match_status = self.match_status

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

        payment_currency_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_currency_amount, Unset):
            payment_currency_amount = self.payment_currency_amount.to_dict()

        tax_currency_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_currency_amount, Unset):
            tax_currency_amount = self.tax_currency_amount.to_dict()

        remittance_instructions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.remittance_instructions, Unset):
            remittance_instructions = self.remittance_instructions.to_dict()

        source_document: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.source_document, Unset):
            source_document = self.source_document.to_dict()

        has_original_pdf = self.has_original_pdf

        base_currency_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.base_currency_amount, Unset):
            base_currency_amount = self.base_currency_amount.to_dict()

        approval: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.approval, Unset):
            approval = self.approval.to_dict()

        payment: Union[Dict[str, Any], Unset]
        if isinstance(self.payment, Unset):
            payment = UNSET
        elif isinstance(self.payment, InvoiceSupplierViewPaymentType0):
            payment = self.payment.to_dict()
        else:
            payment = self.payment.to_dict()

        withdrawn_payment: Union[Dict[str, Any], Unset]
        if isinstance(self.withdrawn_payment, Unset):
            withdrawn_payment = UNSET
        elif isinstance(
            self.withdrawn_payment, InvoiceSupplierViewWithdrawnPaymentType0
        ):
            withdrawn_payment = self.withdrawn_payment.to_dict()
        else:
            withdrawn_payment = self.withdrawn_payment.to_dict()

        buyer_workspace_id = self.buyer_workspace_id

        next_reminder_at = self.next_reminder_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
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
        if party_details is not UNSET:
            field_dict["partyDetails"] = party_details
        if match_status is not UNSET:
            field_dict["matchStatus"] = match_status
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
        if payment_currency_amount is not UNSET:
            field_dict["paymentCurrencyAmount"] = payment_currency_amount
        if tax_currency_amount is not UNSET:
            field_dict["taxCurrencyAmount"] = tax_currency_amount
        if remittance_instructions is not UNSET:
            field_dict["remittanceInstructions"] = remittance_instructions
        if source_document is not UNSET:
            field_dict["sourceDocument"] = source_document
        if has_original_pdf is not UNSET:
            field_dict["hasOriginalPdf"] = has_original_pdf
        if base_currency_amount is not UNSET:
            field_dict["baseCurrencyAmount"] = base_currency_amount
        if approval is not UNSET:
            field_dict["approval"] = approval
        if payment is not UNSET:
            field_dict["payment"] = payment
        if withdrawn_payment is not UNSET:
            field_dict["withdrawnPayment"] = withdrawn_payment
        if buyer_workspace_id is not UNSET:
            field_dict["buyerWorkspaceId"] = buyer_workspace_id
        if next_reminder_at is not UNSET:
            field_dict["nextReminderAt"] = next_reminder_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_adjustment import InvoiceAdjustment
        from ..models.invoice_base_currency_amount import InvoiceBaseCurrencyAmount
        from ..models.invoice_breakdown_entry import InvoiceBreakdownEntry
        from ..models.invoice_currency_amount import InvoiceCurrencyAmount
        from ..models.invoice_line_item import InvoiceLineItem
        from ..models.invoice_rejection import InvoiceRejection
        from ..models.invoice_source_document import InvoiceSourceDocument
        from ..models.invoice_supplier_view_party_details import (
            InvoiceSupplierViewPartyDetails,
        )
        from ..models.invoice_supplier_view_payment_type_0 import (
            InvoiceSupplierViewPaymentType0,
        )
        from ..models.invoice_supplier_view_payment_type_1 import (
            InvoiceSupplierViewPaymentType1,
        )
        from ..models.invoice_supplier_view_withdrawn_payment_type_0 import (
            InvoiceSupplierViewWithdrawnPaymentType0,
        )
        from ..models.invoice_supplier_view_withdrawn_payment_type_1 import (
            InvoiceSupplierViewWithdrawnPaymentType1,
        )
        from ..models.late_fee_terms import LateFeeTerms
        from ..models.remittance_instructions import RemittanceInstructions
        from ..models.supplier_approval_view import SupplierApprovalView

        d = src_dict.copy()
        id = d.pop("id")

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

        _party_details = d.pop("partyDetails", UNSET)
        party_details: Union[Unset, InvoiceSupplierViewPartyDetails]
        if isinstance(_party_details, Unset):
            party_details = UNSET
        else:
            party_details = InvoiceSupplierViewPartyDetails.from_dict(_party_details)

        _match_status = d.pop("matchStatus", UNSET)
        match_status: Union[Unset, InvoiceSupplierViewMatchStatus]
        if isinstance(_match_status, Unset):
            match_status = UNSET
        else:
            match_status = check_invoice_supplier_view_match_status(_match_status)

        paid = d.pop("paid", UNSET)

        due_in_days = d.pop("dueInDays", UNSET)

        due_date = d.pop("dueDate", UNSET)

        paid_at = d.pop("paidAt", UNSET)

        _due_date_source = d.pop("dueDateSource", UNSET)
        due_date_source: Union[Unset, InvoiceSupplierViewDueDateSource]
        if isinstance(_due_date_source, Unset):
            due_date_source = UNSET
        else:
            due_date_source = check_invoice_supplier_view_due_date_source(
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

        _source = d.pop("source", UNSET)
        source: Union[Unset, InvoiceSupplierViewSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = check_invoice_supplier_view_source(_source)

        _entered_by = d.pop("enteredBy", UNSET)
        entered_by: Union[Unset, InvoiceSupplierViewEnteredBy]
        if isinstance(_entered_by, Unset):
            entered_by = UNSET
        else:
            entered_by = check_invoice_supplier_view_entered_by(_entered_by)

        invoice_date = d.pop("invoiceDate", UNSET)

        _submitted_format = d.pop("submittedFormat", UNSET)
        submitted_format: Union[Unset, InvoiceSupplierViewSubmittedFormat]
        if isinstance(_submitted_format, Unset):
            submitted_format = UNSET
        else:
            submitted_format = check_invoice_supplier_view_submitted_format(
                _submitted_format
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

        _source_document = d.pop("sourceDocument", UNSET)
        source_document: Union[Unset, InvoiceSourceDocument]
        if isinstance(_source_document, Unset):
            source_document = UNSET
        else:
            source_document = InvoiceSourceDocument.from_dict(_source_document)

        has_original_pdf = d.pop("hasOriginalPdf", UNSET)

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
            "InvoiceSupplierViewPaymentType0", "InvoiceSupplierViewPaymentType1", Unset
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payment_type_0 = InvoiceSupplierViewPaymentType0.from_dict(data)

                return payment_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            payment_type_1 = InvoiceSupplierViewPaymentType1.from_dict(data)

            return payment_type_1

        payment = _parse_payment(d.pop("payment", UNSET))

        def _parse_withdrawn_payment(
            data: object,
        ) -> Union[
            "InvoiceSupplierViewWithdrawnPaymentType0",
            "InvoiceSupplierViewWithdrawnPaymentType1",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                withdrawn_payment_type_0 = (
                    InvoiceSupplierViewWithdrawnPaymentType0.from_dict(data)
                )

                return withdrawn_payment_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            withdrawn_payment_type_1 = (
                InvoiceSupplierViewWithdrawnPaymentType1.from_dict(data)
            )

            return withdrawn_payment_type_1

        withdrawn_payment = _parse_withdrawn_payment(d.pop("withdrawnPayment", UNSET))

        buyer_workspace_id = d.pop("buyerWorkspaceId", UNSET)

        next_reminder_at = d.pop("nextReminderAt", UNSET)

        invoice_supplier_view = cls(
            id=id,
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
            party_details=party_details,
            match_status=match_status,
            paid=paid,
            due_in_days=due_in_days,
            due_date=due_date,
            paid_at=paid_at,
            due_date_source=due_date_source,
            last_reminded_at=last_reminded_at,
            rejection=rejection,
            replaces_invoice_id=replaces_invoice_id,
            source=source,
            entered_by=entered_by,
            invoice_date=invoice_date,
            submitted_format=submitted_format,
            external_invoice_number=external_invoice_number,
            adjustments=adjustments,
            tax_amount=tax_amount,
            tax_breakdown=tax_breakdown,
            withholdings=withholdings,
            payment_currency_amount=payment_currency_amount,
            tax_currency_amount=tax_currency_amount,
            remittance_instructions=remittance_instructions,
            source_document=source_document,
            has_original_pdf=has_original_pdf,
            base_currency_amount=base_currency_amount,
            approval=approval,
            payment=payment,
            withdrawn_payment=withdrawn_payment,
            buyer_workspace_id=buyer_workspace_id,
            next_reminder_at=next_reminder_at,
        )

        invoice_supplier_view.additional_properties = d
        return invoice_supplier_view

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
