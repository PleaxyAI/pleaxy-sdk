from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.breakdown_entry_input import BreakdownEntryInput
    from ..models.create_manual_invoice_line_item_input import (
        CreateManualInvoiceLineItemInput,
    )
    from ..models.currency_amount_input import CurrencyAmountInput
    from ..models.invoice_adjustment_input import InvoiceAdjustmentInput
    from ..models.remittance_instructions_input import RemittanceInstructionsInput


T = TypeVar("T", bound="CreateFeedInvoiceInput")


@_attrs_define
class CreateFeedInvoiceInput:
    """
    Attributes:
        invoice_number (str): Unique per supplier within the buyer's workspace, case-insensitively
        invoice_date (str): YYYY-MM-DD - not in the future, not more than 365 days back
        line_items (List['CreateManualInvoiceLineItemInput']):
        po_id (Union[Unset, str]): An open PO between exactly this buyer and supplier
        due_in_days (Union[Unset, float]): 0–365, default 30
        adjustments (Union[Unset, List['InvoiceAdjustmentInput']]): Invoice-level discounts and charges, before tax. At
            most 20.
        source_import_id (Union[Unset, str]): Buyer only: the invoice import (POST .../invoice-imports) this invoice was
            recorded from. Its document is kept with the invoice when it is a PDF under 8 MB, and the import records the
            invoice.
        tax_amount (Union[Unset, float]): Total tax on the invoice, as stated by the supplier. It is included in the
            invoice total. Pleaxy doesn't calculate tax.
        tax_breakdown (Union[Unset, List['BreakdownEntryInput']]): Tax by type in the invoice's currency, e.g. IVA 21%
            and a percepción. Must sum to taxAmount, which is then required. At most 20.
        withholdings (Union[Unset, List['BreakdownEntryInput']]): Amounts the invoice withholds from its total, in the
            invoice's currency, e.g. ISR retenido 10%. Positive; they reduce what's owed, never the total. Less than the
            total in all. At most 20.
        payment_currency_amount (Union[Unset, CurrencyAmountInput]):
        tax_currency_amount (Union[Unset, CurrencyAmountInput]):
        currency (Union[Unset, str]): ISO 4217, case-insensitive. Optional; absent means the buyer region's currency.
            For a connected supplier the buyer region's currency is always the one stored, and any other is refused. For an
            off-platform supplier (no Pleaxy account) it is the currency the invoice is in.
        remittance_instructions (Union[Unset, RemittanceInstructionsInput]):
        pdf_base_64 (Union[Unset, str]): Base64-encoded PDF of the invoice
    """

    invoice_number: str
    invoice_date: str
    line_items: List["CreateManualInvoiceLineItemInput"]
    po_id: Union[Unset, str] = UNSET
    due_in_days: Union[Unset, float] = UNSET
    adjustments: Union[Unset, List["InvoiceAdjustmentInput"]] = UNSET
    source_import_id: Union[Unset, str] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    tax_breakdown: Union[Unset, List["BreakdownEntryInput"]] = UNSET
    withholdings: Union[Unset, List["BreakdownEntryInput"]] = UNSET
    payment_currency_amount: Union[Unset, "CurrencyAmountInput"] = UNSET
    tax_currency_amount: Union[Unset, "CurrencyAmountInput"] = UNSET
    currency: Union[Unset, str] = UNSET
    remittance_instructions: Union[Unset, "RemittanceInstructionsInput"] = UNSET
    pdf_base_64: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoice_number = self.invoice_number

        invoice_date = self.invoice_date

        line_items = []
        for line_items_item_data in self.line_items:
            line_items_item = line_items_item_data.to_dict()
            line_items.append(line_items_item)

        po_id = self.po_id

        due_in_days = self.due_in_days

        adjustments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.adjustments, Unset):
            adjustments = []
            for adjustments_item_data in self.adjustments:
                adjustments_item = adjustments_item_data.to_dict()
                adjustments.append(adjustments_item)

        source_import_id = self.source_import_id

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

        currency = self.currency

        remittance_instructions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.remittance_instructions, Unset):
            remittance_instructions = self.remittance_instructions.to_dict()

        pdf_base_64 = self.pdf_base_64

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invoiceNumber": invoice_number,
                "invoiceDate": invoice_date,
                "lineItems": line_items,
            }
        )
        if po_id is not UNSET:
            field_dict["poId"] = po_id
        if due_in_days is not UNSET:
            field_dict["dueInDays"] = due_in_days
        if adjustments is not UNSET:
            field_dict["adjustments"] = adjustments
        if source_import_id is not UNSET:
            field_dict["sourceImportId"] = source_import_id
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
        if currency is not UNSET:
            field_dict["currency"] = currency
        if remittance_instructions is not UNSET:
            field_dict["remittanceInstructions"] = remittance_instructions
        if pdf_base_64 is not UNSET:
            field_dict["pdfBase64"] = pdf_base_64

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.breakdown_entry_input import BreakdownEntryInput
        from ..models.create_manual_invoice_line_item_input import (
            CreateManualInvoiceLineItemInput,
        )
        from ..models.currency_amount_input import CurrencyAmountInput
        from ..models.invoice_adjustment_input import InvoiceAdjustmentInput
        from ..models.remittance_instructions_input import RemittanceInstructionsInput

        d = src_dict.copy()
        invoice_number = d.pop("invoiceNumber")

        invoice_date = d.pop("invoiceDate")

        line_items = []
        _line_items = d.pop("lineItems")
        for line_items_item_data in _line_items:
            line_items_item = CreateManualInvoiceLineItemInput.from_dict(
                line_items_item_data
            )

            line_items.append(line_items_item)

        po_id = d.pop("poId", UNSET)

        due_in_days = d.pop("dueInDays", UNSET)

        adjustments = []
        _adjustments = d.pop("adjustments", UNSET)
        for adjustments_item_data in _adjustments or []:
            adjustments_item = InvoiceAdjustmentInput.from_dict(adjustments_item_data)

            adjustments.append(adjustments_item)

        source_import_id = d.pop("sourceImportId", UNSET)

        tax_amount = d.pop("taxAmount", UNSET)

        tax_breakdown = []
        _tax_breakdown = d.pop("taxBreakdown", UNSET)
        for tax_breakdown_item_data in _tax_breakdown or []:
            tax_breakdown_item = BreakdownEntryInput.from_dict(tax_breakdown_item_data)

            tax_breakdown.append(tax_breakdown_item)

        withholdings = []
        _withholdings = d.pop("withholdings", UNSET)
        for withholdings_item_data in _withholdings or []:
            withholdings_item = BreakdownEntryInput.from_dict(withholdings_item_data)

            withholdings.append(withholdings_item)

        _payment_currency_amount = d.pop("paymentCurrencyAmount", UNSET)
        payment_currency_amount: Union[Unset, CurrencyAmountInput]
        if isinstance(_payment_currency_amount, Unset):
            payment_currency_amount = UNSET
        else:
            payment_currency_amount = CurrencyAmountInput.from_dict(
                _payment_currency_amount
            )

        _tax_currency_amount = d.pop("taxCurrencyAmount", UNSET)
        tax_currency_amount: Union[Unset, CurrencyAmountInput]
        if isinstance(_tax_currency_amount, Unset):
            tax_currency_amount = UNSET
        else:
            tax_currency_amount = CurrencyAmountInput.from_dict(_tax_currency_amount)

        currency = d.pop("currency", UNSET)

        _remittance_instructions = d.pop("remittanceInstructions", UNSET)
        remittance_instructions: Union[Unset, RemittanceInstructionsInput]
        if isinstance(_remittance_instructions, Unset):
            remittance_instructions = UNSET
        else:
            remittance_instructions = RemittanceInstructionsInput.from_dict(
                _remittance_instructions
            )

        pdf_base_64 = d.pop("pdfBase64", UNSET)

        create_feed_invoice_input = cls(
            invoice_number=invoice_number,
            invoice_date=invoice_date,
            line_items=line_items,
            po_id=po_id,
            due_in_days=due_in_days,
            adjustments=adjustments,
            source_import_id=source_import_id,
            tax_amount=tax_amount,
            tax_breakdown=tax_breakdown,
            withholdings=withholdings,
            payment_currency_amount=payment_currency_amount,
            tax_currency_amount=tax_currency_amount,
            currency=currency,
            remittance_instructions=remittance_instructions,
            pdf_base_64=pdf_base_64,
        )

        create_feed_invoice_input.additional_properties = d
        return create_feed_invoice_input

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
