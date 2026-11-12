from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_credit_note_input_reason import (
    CreateCreditNoteInputReason,
    check_create_credit_note_input_reason,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.breakdown_entry_input import BreakdownEntryInput
    from ..models.create_manual_invoice_line_item_input import (
        CreateManualInvoiceLineItemInput,
    )


T = TypeVar("T", bound="CreateCreditNoteInput")


@_attrs_define
class CreateCreditNoteInput:
    """
    Attributes:
        external_credit_note_number (str): The supplier's own number for it: unique per supplier within the buyer, case-
            insensitively.
        issue_date (str): YYYY-MM-DD - not in the future, not more than 365 days back
        reason (CreateCreditNoteInputReason): returned_goods and price_adjustment give PO balance back once accepted;
            service_credit and rebate don't.
        line_items (List['CreateManualInvoiceLineItemInput']): What is credited, before tax. 1–200 lines.
        invoice_id (Union[Unset, str]): The invoice it corrects. Its buyer, supplier, currency, PO and PO line are the
            credit note's. Give this or connectionId.
        connection_id (Union[Unset, str]): The counterparty it's for, when it corrects no one invoice - see GET
            .../invoices/counterparties.
        corrects_billing (Union[Unset, bool]): Reason "other" only: it corrects what was billed, so it gives PO balance
            back too.
        note (Union[Unset, str]): 1–1000 characters, e.g. the return's RMA number.
        currency (Union[Unset, str]): ISO 4217. Required without invoiceId; with one, it must be the invoice's.
        tax_amount (Union[Unset, float]): The tax credited, included in the credit note's total.
        tax_breakdown (Union[Unset, List['BreakdownEntryInput']]): Tax by type, summing to taxAmount. At most 20.
        pdf_base_64 (Union[Unset, str]): Base64-encoded PDF of the credit note as issued, kept with it. Up to 8 MB.
        source_import_id (Union[Unset, str]): Buyer only: the invoice import (POST .../invoice-imports) this credit note
            was recorded from - the supplier's credit note document Pleaxy read. Its document is kept with the credit note
            when it is a PDF under 8 MB, and the import records the credit note.
    """

    external_credit_note_number: str
    issue_date: str
    reason: CreateCreditNoteInputReason
    line_items: List["CreateManualInvoiceLineItemInput"]
    invoice_id: Union[Unset, str] = UNSET
    connection_id: Union[Unset, str] = UNSET
    corrects_billing: Union[Unset, bool] = UNSET
    note: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    tax_breakdown: Union[Unset, List["BreakdownEntryInput"]] = UNSET
    pdf_base_64: Union[Unset, str] = UNSET
    source_import_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        external_credit_note_number = self.external_credit_note_number

        issue_date = self.issue_date

        reason: str = self.reason

        line_items = []
        for line_items_item_data in self.line_items:
            line_items_item = line_items_item_data.to_dict()
            line_items.append(line_items_item)

        invoice_id = self.invoice_id

        connection_id = self.connection_id

        corrects_billing = self.corrects_billing

        note = self.note

        currency = self.currency

        tax_amount = self.tax_amount

        tax_breakdown: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tax_breakdown, Unset):
            tax_breakdown = []
            for tax_breakdown_item_data in self.tax_breakdown:
                tax_breakdown_item = tax_breakdown_item_data.to_dict()
                tax_breakdown.append(tax_breakdown_item)

        pdf_base_64 = self.pdf_base_64

        source_import_id = self.source_import_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "externalCreditNoteNumber": external_credit_note_number,
                "issueDate": issue_date,
                "reason": reason,
                "lineItems": line_items,
            }
        )
        if invoice_id is not UNSET:
            field_dict["invoiceId"] = invoice_id
        if connection_id is not UNSET:
            field_dict["connectionId"] = connection_id
        if corrects_billing is not UNSET:
            field_dict["correctsBilling"] = corrects_billing
        if note is not UNSET:
            field_dict["note"] = note
        if currency is not UNSET:
            field_dict["currency"] = currency
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount
        if tax_breakdown is not UNSET:
            field_dict["taxBreakdown"] = tax_breakdown
        if pdf_base_64 is not UNSET:
            field_dict["pdfBase64"] = pdf_base_64
        if source_import_id is not UNSET:
            field_dict["sourceImportId"] = source_import_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.breakdown_entry_input import BreakdownEntryInput
        from ..models.create_manual_invoice_line_item_input import (
            CreateManualInvoiceLineItemInput,
        )

        d = src_dict.copy()
        external_credit_note_number = d.pop("externalCreditNoteNumber")

        issue_date = d.pop("issueDate")

        reason = check_create_credit_note_input_reason(d.pop("reason"))

        line_items = []
        _line_items = d.pop("lineItems")
        for line_items_item_data in _line_items:
            line_items_item = CreateManualInvoiceLineItemInput.from_dict(
                line_items_item_data
            )

            line_items.append(line_items_item)

        invoice_id = d.pop("invoiceId", UNSET)

        connection_id = d.pop("connectionId", UNSET)

        corrects_billing = d.pop("correctsBilling", UNSET)

        note = d.pop("note", UNSET)

        currency = d.pop("currency", UNSET)

        tax_amount = d.pop("taxAmount", UNSET)

        tax_breakdown = []
        _tax_breakdown = d.pop("taxBreakdown", UNSET)
        for tax_breakdown_item_data in _tax_breakdown or []:
            tax_breakdown_item = BreakdownEntryInput.from_dict(tax_breakdown_item_data)

            tax_breakdown.append(tax_breakdown_item)

        pdf_base_64 = d.pop("pdfBase64", UNSET)

        source_import_id = d.pop("sourceImportId", UNSET)

        create_credit_note_input = cls(
            external_credit_note_number=external_credit_note_number,
            issue_date=issue_date,
            reason=reason,
            line_items=line_items,
            invoice_id=invoice_id,
            connection_id=connection_id,
            corrects_billing=corrects_billing,
            note=note,
            currency=currency,
            tax_amount=tax_amount,
            tax_breakdown=tax_breakdown,
            pdf_base_64=pdf_base_64,
            source_import_id=source_import_id,
        )

        create_credit_note_input.additional_properties = d
        return create_credit_note_input

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
