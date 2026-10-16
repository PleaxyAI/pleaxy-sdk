from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validate_feed_invoice_result_credit_note_credit_note_reason import (
    ValidateFeedInvoiceResultCreditNoteCreditNoteReason,
    check_validate_feed_invoice_result_credit_note_credit_note_reason,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_adjustment import InvoiceAdjustment
    from ..models.invoice_line_item import InvoiceLineItem


T = TypeVar("T", bound="ValidateFeedInvoiceResultCreditNoteCreditNote")


@_attrs_define
class ValidateFeedInvoiceResultCreditNoteCreditNote:
    """
    Attributes:
        invoice_id (Union[Unset, str]):
        external_invoice_number (Union[Unset, str]):
        adjustments (Union[Unset, List['InvoiceAdjustment']]):
        line_items (Union[Unset, List['InvoiceLineItem']]):
        tax_amount (Union[Unset, float]):
        refunded (Union[Unset, float]):
        amount (Union[Unset, float]):
        corrects_billing (Union[Unset, bool]):
        external_credit_note_number (Union[Unset, str]):
        issue_date (Union[Unset, str]):
        currency (Union[Unset, str]):
        reason (Union[Unset, ValidateFeedInvoiceResultCreditNoteCreditNoteReason]):
    """

    invoice_id: Union[Unset, str] = UNSET
    external_invoice_number: Union[Unset, str] = UNSET
    adjustments: Union[Unset, List["InvoiceAdjustment"]] = UNSET
    line_items: Union[Unset, List["InvoiceLineItem"]] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    refunded: Union[Unset, float] = UNSET
    amount: Union[Unset, float] = UNSET
    corrects_billing: Union[Unset, bool] = UNSET
    external_credit_note_number: Union[Unset, str] = UNSET
    issue_date: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    reason: Union[Unset, ValidateFeedInvoiceResultCreditNoteCreditNoteReason] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoice_id = self.invoice_id

        external_invoice_number = self.external_invoice_number

        adjustments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.adjustments, Unset):
            adjustments = []
            for adjustments_item_data in self.adjustments:
                adjustments_item = adjustments_item_data.to_dict()
                adjustments.append(adjustments_item)

        line_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.line_items, Unset):
            line_items = []
            for line_items_item_data in self.line_items:
                line_items_item = line_items_item_data.to_dict()
                line_items.append(line_items_item)

        tax_amount = self.tax_amount

        refunded = self.refunded

        amount = self.amount

        corrects_billing = self.corrects_billing

        external_credit_note_number = self.external_credit_note_number

        issue_date = self.issue_date

        currency = self.currency

        reason: Union[Unset, str] = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invoice_id is not UNSET:
            field_dict["invoiceId"] = invoice_id
        if external_invoice_number is not UNSET:
            field_dict["externalInvoiceNumber"] = external_invoice_number
        if adjustments is not UNSET:
            field_dict["adjustments"] = adjustments
        if line_items is not UNSET:
            field_dict["lineItems"] = line_items
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount
        if refunded is not UNSET:
            field_dict["refunded"] = refunded
        if amount is not UNSET:
            field_dict["amount"] = amount
        if corrects_billing is not UNSET:
            field_dict["correctsBilling"] = corrects_billing
        if external_credit_note_number is not UNSET:
            field_dict["externalCreditNoteNumber"] = external_credit_note_number
        if issue_date is not UNSET:
            field_dict["issueDate"] = issue_date
        if currency is not UNSET:
            field_dict["currency"] = currency
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_adjustment import InvoiceAdjustment
        from ..models.invoice_line_item import InvoiceLineItem

        d = src_dict.copy()
        invoice_id = d.pop("invoiceId", UNSET)

        external_invoice_number = d.pop("externalInvoiceNumber", UNSET)

        adjustments = []
        _adjustments = d.pop("adjustments", UNSET)
        for adjustments_item_data in _adjustments or []:
            adjustments_item = InvoiceAdjustment.from_dict(adjustments_item_data)

            adjustments.append(adjustments_item)

        line_items = []
        _line_items = d.pop("lineItems", UNSET)
        for line_items_item_data in _line_items or []:
            line_items_item = InvoiceLineItem.from_dict(line_items_item_data)

            line_items.append(line_items_item)

        tax_amount = d.pop("taxAmount", UNSET)

        refunded = d.pop("refunded", UNSET)

        amount = d.pop("amount", UNSET)

        corrects_billing = d.pop("correctsBilling", UNSET)

        external_credit_note_number = d.pop("externalCreditNoteNumber", UNSET)

        issue_date = d.pop("issueDate", UNSET)

        currency = d.pop("currency", UNSET)

        _reason = d.pop("reason", UNSET)
        reason: Union[Unset, ValidateFeedInvoiceResultCreditNoteCreditNoteReason]
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = check_validate_feed_invoice_result_credit_note_credit_note_reason(
                _reason
            )

        validate_feed_invoice_result_credit_note_credit_note = cls(
            invoice_id=invoice_id,
            external_invoice_number=external_invoice_number,
            adjustments=adjustments,
            line_items=line_items,
            tax_amount=tax_amount,
            refunded=refunded,
            amount=amount,
            corrects_billing=corrects_billing,
            external_credit_note_number=external_credit_note_number,
            issue_date=issue_date,
            currency=currency,
            reason=reason,
        )

        validate_feed_invoice_result_credit_note_credit_note.additional_properties = d
        return validate_feed_invoice_result_credit_note_credit_note

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
