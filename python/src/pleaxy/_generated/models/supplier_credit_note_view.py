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

from ..models.supplier_credit_note_view_cloud_provider import (
    SupplierCreditNoteViewCloudProvider,
    check_supplier_credit_note_view_cloud_provider,
)
from ..models.supplier_credit_note_view_entered_by import (
    SupplierCreditNoteViewEnteredBy,
    check_supplier_credit_note_view_entered_by,
)
from ..models.supplier_credit_note_view_reason import (
    SupplierCreditNoteViewReason,
    check_supplier_credit_note_view_reason,
)
from ..models.supplier_credit_note_view_source import (
    SupplierCreditNoteViewSource,
    check_supplier_credit_note_view_source,
)
from ..models.supplier_credit_note_view_status import (
    SupplierCreditNoteViewStatus,
    check_supplier_credit_note_view_status,
)
from ..models.supplier_credit_note_view_submitted_format import (
    SupplierCreditNoteViewSubmittedFormat,
    check_supplier_credit_note_view_submitted_format,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credit_note_application import CreditNoteApplication
    from ..models.invoice_adjustment import InvoiceAdjustment
    from ..models.invoice_breakdown_entry import InvoiceBreakdownEntry
    from ..models.invoice_line_item import InvoiceLineItem
    from ..models.supplier_credit_note_view_exports_item import (
        SupplierCreditNoteViewExportsItem,
    )
    from ..models.supplier_credit_note_view_history_item import (
        SupplierCreditNoteViewHistoryItem,
    )
    from ..models.supplier_credit_note_view_po_effect_type_0 import (
        SupplierCreditNoteViewPoEffectType0,
    )
    from ..models.supplier_credit_note_view_po_effect_type_1 import (
        SupplierCreditNoteViewPoEffectType1,
    )
    from ..models.supplier_credit_note_view_rejection import (
        SupplierCreditNoteViewRejection,
    )


T = TypeVar("T", bound="SupplierCreditNoteView")


@_attrs_define
class SupplierCreditNoteView:
    """
    Attributes:
        id (str):
        supplier (Union[Unset, str]):
        buyer_org_id (Union[Unset, str]):
        supplier_org_id (Union[Unset, str]):
        status (Union[Unset, SupplierCreditNoteViewStatus]):
        created_at (Union[Unset, str]):
        cloud_provider (Union[Unset, SupplierCreditNoteViewCloudProvider]):
        amount (Union[Unset, float]):
        supplier_connection_id (Union[Unset, str]):
        currency (Union[Unset, str]):
        invoice_id (Union[Unset, str]):
        buyer_org_name (Union[Unset, str]):
        line_items (Union[Unset, List['InvoiceLineItem']]):
        version (Union[Unset, float]):
        po (Union[Unset, str]):
        po_line_no (Union[Unset, float]):
        source (Union[Unset, SupplierCreditNoteViewSource]):
        entered_by (Union[Unset, SupplierCreditNoteViewEnteredBy]):
        submitted_format (Union[Unset, SupplierCreditNoteViewSubmittedFormat]):
        external_invoice_number (Union[Unset, str]):
        adjustments (Union[Unset, List['InvoiceAdjustment']]):
        tax_amount (Union[Unset, float]):
        tax_breakdown (Union[Unset, List['InvoiceBreakdownEntry']]):
        note (Union[Unset, str]):
        external_credit_note_number (Union[Unset, str]):
        issue_date (Union[Unset, str]):
        reason (Union[Unset, SupplierCreditNoteViewReason]):
        corrects_billing (Union[Unset, bool]):
        refunded (Union[Unset, float]):
        accepted_at (Union[Unset, str]):
        auto_accepted (Union[Unset, bool]):
        po_effect (Union['SupplierCreditNoteViewPoEffectType0', 'SupplierCreditNoteViewPoEffectType1', Unset]):
        applications (Union[Unset, List['CreditNoteApplication']]):
        exports (Union[Unset, List['SupplierCreditNoteViewExportsItem']]):
        remaining (Union[Unset, float]):
        has_pdf (Union[Unset, bool]):
        buyer_workspace_id (Union[Unset, str]):
        history (Union[Unset, List['SupplierCreditNoteViewHistoryItem']]):
        rejection (Union[Unset, SupplierCreditNoteViewRejection]):
    """

    id: str
    supplier: Union[Unset, str] = UNSET
    buyer_org_id: Union[Unset, str] = UNSET
    supplier_org_id: Union[Unset, str] = UNSET
    status: Union[Unset, SupplierCreditNoteViewStatus] = UNSET
    created_at: Union[Unset, str] = UNSET
    cloud_provider: Union[Unset, SupplierCreditNoteViewCloudProvider] = UNSET
    amount: Union[Unset, float] = UNSET
    supplier_connection_id: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    invoice_id: Union[Unset, str] = UNSET
    buyer_org_name: Union[Unset, str] = UNSET
    line_items: Union[Unset, List["InvoiceLineItem"]] = UNSET
    version: Union[Unset, float] = UNSET
    po: Union[Unset, str] = UNSET
    po_line_no: Union[Unset, float] = UNSET
    source: Union[Unset, SupplierCreditNoteViewSource] = UNSET
    entered_by: Union[Unset, SupplierCreditNoteViewEnteredBy] = UNSET
    submitted_format: Union[Unset, SupplierCreditNoteViewSubmittedFormat] = UNSET
    external_invoice_number: Union[Unset, str] = UNSET
    adjustments: Union[Unset, List["InvoiceAdjustment"]] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    tax_breakdown: Union[Unset, List["InvoiceBreakdownEntry"]] = UNSET
    note: Union[Unset, str] = UNSET
    external_credit_note_number: Union[Unset, str] = UNSET
    issue_date: Union[Unset, str] = UNSET
    reason: Union[Unset, SupplierCreditNoteViewReason] = UNSET
    corrects_billing: Union[Unset, bool] = UNSET
    refunded: Union[Unset, float] = UNSET
    accepted_at: Union[Unset, str] = UNSET
    auto_accepted: Union[Unset, bool] = UNSET
    po_effect: Union[
        "SupplierCreditNoteViewPoEffectType0",
        "SupplierCreditNoteViewPoEffectType1",
        Unset,
    ] = UNSET
    applications: Union[Unset, List["CreditNoteApplication"]] = UNSET
    exports: Union[Unset, List["SupplierCreditNoteViewExportsItem"]] = UNSET
    remaining: Union[Unset, float] = UNSET
    has_pdf: Union[Unset, bool] = UNSET
    buyer_workspace_id: Union[Unset, str] = UNSET
    history: Union[Unset, List["SupplierCreditNoteViewHistoryItem"]] = UNSET
    rejection: Union[Unset, "SupplierCreditNoteViewRejection"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.supplier_credit_note_view_po_effect_type_0 import (
            SupplierCreditNoteViewPoEffectType0,
        )

        id = self.id

        supplier = self.supplier

        buyer_org_id = self.buyer_org_id

        supplier_org_id = self.supplier_org_id

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        created_at = self.created_at

        cloud_provider: Union[Unset, str] = UNSET
        if not isinstance(self.cloud_provider, Unset):
            cloud_provider = self.cloud_provider

        amount = self.amount

        supplier_connection_id = self.supplier_connection_id

        currency = self.currency

        invoice_id = self.invoice_id

        buyer_org_name = self.buyer_org_name

        line_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.line_items, Unset):
            line_items = []
            for line_items_item_data in self.line_items:
                line_items_item = line_items_item_data.to_dict()
                line_items.append(line_items_item)

        version = self.version

        po = self.po

        po_line_no = self.po_line_no

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source

        entered_by: Union[Unset, str] = UNSET
        if not isinstance(self.entered_by, Unset):
            entered_by = self.entered_by

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

        note = self.note

        external_credit_note_number = self.external_credit_note_number

        issue_date = self.issue_date

        reason: Union[Unset, str] = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason

        corrects_billing = self.corrects_billing

        refunded = self.refunded

        accepted_at = self.accepted_at

        auto_accepted = self.auto_accepted

        po_effect: Union[Dict[str, Any], Unset]
        if isinstance(self.po_effect, Unset):
            po_effect = UNSET
        elif isinstance(self.po_effect, SupplierCreditNoteViewPoEffectType0):
            po_effect = self.po_effect.to_dict()
        else:
            po_effect = self.po_effect.to_dict()

        applications: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.applications, Unset):
            applications = []
            for applications_item_data in self.applications:
                applications_item = applications_item_data.to_dict()
                applications.append(applications_item)

        exports: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.exports, Unset):
            exports = []
            for exports_item_data in self.exports:
                exports_item = exports_item_data.to_dict()
                exports.append(exports_item)

        remaining = self.remaining

        has_pdf = self.has_pdf

        buyer_workspace_id = self.buyer_workspace_id

        history: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.history, Unset):
            history = []
            for history_item_data in self.history:
                history_item = history_item_data.to_dict()
                history.append(history_item)

        rejection: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rejection, Unset):
            rejection = self.rejection.to_dict()

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
        if status is not UNSET:
            field_dict["status"] = status
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if cloud_provider is not UNSET:
            field_dict["cloudProvider"] = cloud_provider
        if amount is not UNSET:
            field_dict["amount"] = amount
        if supplier_connection_id is not UNSET:
            field_dict["supplierConnectionId"] = supplier_connection_id
        if currency is not UNSET:
            field_dict["currency"] = currency
        if invoice_id is not UNSET:
            field_dict["invoiceId"] = invoice_id
        if buyer_org_name is not UNSET:
            field_dict["buyerOrgName"] = buyer_org_name
        if line_items is not UNSET:
            field_dict["lineItems"] = line_items
        if version is not UNSET:
            field_dict["version"] = version
        if po is not UNSET:
            field_dict["po"] = po
        if po_line_no is not UNSET:
            field_dict["poLineNo"] = po_line_no
        if source is not UNSET:
            field_dict["source"] = source
        if entered_by is not UNSET:
            field_dict["enteredBy"] = entered_by
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
        if note is not UNSET:
            field_dict["note"] = note
        if external_credit_note_number is not UNSET:
            field_dict["externalCreditNoteNumber"] = external_credit_note_number
        if issue_date is not UNSET:
            field_dict["issueDate"] = issue_date
        if reason is not UNSET:
            field_dict["reason"] = reason
        if corrects_billing is not UNSET:
            field_dict["correctsBilling"] = corrects_billing
        if refunded is not UNSET:
            field_dict["refunded"] = refunded
        if accepted_at is not UNSET:
            field_dict["acceptedAt"] = accepted_at
        if auto_accepted is not UNSET:
            field_dict["autoAccepted"] = auto_accepted
        if po_effect is not UNSET:
            field_dict["poEffect"] = po_effect
        if applications is not UNSET:
            field_dict["applications"] = applications
        if exports is not UNSET:
            field_dict["exports"] = exports
        if remaining is not UNSET:
            field_dict["remaining"] = remaining
        if has_pdf is not UNSET:
            field_dict["hasPdf"] = has_pdf
        if buyer_workspace_id is not UNSET:
            field_dict["buyerWorkspaceId"] = buyer_workspace_id
        if history is not UNSET:
            field_dict["history"] = history
        if rejection is not UNSET:
            field_dict["rejection"] = rejection

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.credit_note_application import CreditNoteApplication
        from ..models.invoice_adjustment import InvoiceAdjustment
        from ..models.invoice_breakdown_entry import InvoiceBreakdownEntry
        from ..models.invoice_line_item import InvoiceLineItem
        from ..models.supplier_credit_note_view_exports_item import (
            SupplierCreditNoteViewExportsItem,
        )
        from ..models.supplier_credit_note_view_history_item import (
            SupplierCreditNoteViewHistoryItem,
        )
        from ..models.supplier_credit_note_view_po_effect_type_0 import (
            SupplierCreditNoteViewPoEffectType0,
        )
        from ..models.supplier_credit_note_view_po_effect_type_1 import (
            SupplierCreditNoteViewPoEffectType1,
        )
        from ..models.supplier_credit_note_view_rejection import (
            SupplierCreditNoteViewRejection,
        )

        d = src_dict.copy()
        id = d.pop("id")

        supplier = d.pop("supplier", UNSET)

        buyer_org_id = d.pop("buyerOrgId", UNSET)

        supplier_org_id = d.pop("supplierOrgId", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, SupplierCreditNoteViewStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_supplier_credit_note_view_status(_status)

        created_at = d.pop("createdAt", UNSET)

        _cloud_provider = d.pop("cloudProvider", UNSET)
        cloud_provider: Union[Unset, SupplierCreditNoteViewCloudProvider]
        if isinstance(_cloud_provider, Unset):
            cloud_provider = UNSET
        else:
            cloud_provider = check_supplier_credit_note_view_cloud_provider(
                _cloud_provider
            )

        amount = d.pop("amount", UNSET)

        supplier_connection_id = d.pop("supplierConnectionId", UNSET)

        currency = d.pop("currency", UNSET)

        invoice_id = d.pop("invoiceId", UNSET)

        buyer_org_name = d.pop("buyerOrgName", UNSET)

        line_items = []
        _line_items = d.pop("lineItems", UNSET)
        for line_items_item_data in _line_items or []:
            line_items_item = InvoiceLineItem.from_dict(line_items_item_data)

            line_items.append(line_items_item)

        version = d.pop("version", UNSET)

        po = d.pop("po", UNSET)

        po_line_no = d.pop("poLineNo", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, SupplierCreditNoteViewSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = check_supplier_credit_note_view_source(_source)

        _entered_by = d.pop("enteredBy", UNSET)
        entered_by: Union[Unset, SupplierCreditNoteViewEnteredBy]
        if isinstance(_entered_by, Unset):
            entered_by = UNSET
        else:
            entered_by = check_supplier_credit_note_view_entered_by(_entered_by)

        _submitted_format = d.pop("submittedFormat", UNSET)
        submitted_format: Union[Unset, SupplierCreditNoteViewSubmittedFormat]
        if isinstance(_submitted_format, Unset):
            submitted_format = UNSET
        else:
            submitted_format = check_supplier_credit_note_view_submitted_format(
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

        note = d.pop("note", UNSET)

        external_credit_note_number = d.pop("externalCreditNoteNumber", UNSET)

        issue_date = d.pop("issueDate", UNSET)

        _reason = d.pop("reason", UNSET)
        reason: Union[Unset, SupplierCreditNoteViewReason]
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = check_supplier_credit_note_view_reason(_reason)

        corrects_billing = d.pop("correctsBilling", UNSET)

        refunded = d.pop("refunded", UNSET)

        accepted_at = d.pop("acceptedAt", UNSET)

        auto_accepted = d.pop("autoAccepted", UNSET)

        def _parse_po_effect(
            data: object,
        ) -> Union[
            "SupplierCreditNoteViewPoEffectType0",
            "SupplierCreditNoteViewPoEffectType1",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                po_effect_type_0 = SupplierCreditNoteViewPoEffectType0.from_dict(data)

                return po_effect_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            po_effect_type_1 = SupplierCreditNoteViewPoEffectType1.from_dict(data)

            return po_effect_type_1

        po_effect = _parse_po_effect(d.pop("poEffect", UNSET))

        applications = []
        _applications = d.pop("applications", UNSET)
        for applications_item_data in _applications or []:
            applications_item = CreditNoteApplication.from_dict(applications_item_data)

            applications.append(applications_item)

        exports = []
        _exports = d.pop("exports", UNSET)
        for exports_item_data in _exports or []:
            exports_item = SupplierCreditNoteViewExportsItem.from_dict(
                exports_item_data
            )

            exports.append(exports_item)

        remaining = d.pop("remaining", UNSET)

        has_pdf = d.pop("hasPdf", UNSET)

        buyer_workspace_id = d.pop("buyerWorkspaceId", UNSET)

        history = []
        _history = d.pop("history", UNSET)
        for history_item_data in _history or []:
            history_item = SupplierCreditNoteViewHistoryItem.from_dict(
                history_item_data
            )

            history.append(history_item)

        _rejection = d.pop("rejection", UNSET)
        rejection: Union[Unset, SupplierCreditNoteViewRejection]
        if isinstance(_rejection, Unset):
            rejection = UNSET
        else:
            rejection = SupplierCreditNoteViewRejection.from_dict(_rejection)

        supplier_credit_note_view = cls(
            id=id,
            supplier=supplier,
            buyer_org_id=buyer_org_id,
            supplier_org_id=supplier_org_id,
            status=status,
            created_at=created_at,
            cloud_provider=cloud_provider,
            amount=amount,
            supplier_connection_id=supplier_connection_id,
            currency=currency,
            invoice_id=invoice_id,
            buyer_org_name=buyer_org_name,
            line_items=line_items,
            version=version,
            po=po,
            po_line_no=po_line_no,
            source=source,
            entered_by=entered_by,
            submitted_format=submitted_format,
            external_invoice_number=external_invoice_number,
            adjustments=adjustments,
            tax_amount=tax_amount,
            tax_breakdown=tax_breakdown,
            note=note,
            external_credit_note_number=external_credit_note_number,
            issue_date=issue_date,
            reason=reason,
            corrects_billing=corrects_billing,
            refunded=refunded,
            accepted_at=accepted_at,
            auto_accepted=auto_accepted,
            po_effect=po_effect,
            applications=applications,
            exports=exports,
            remaining=remaining,
            has_pdf=has_pdf,
            buyer_workspace_id=buyer_workspace_id,
            history=history,
            rejection=rejection,
        )

        supplier_credit_note_view.additional_properties = d
        return supplier_credit_note_view

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
