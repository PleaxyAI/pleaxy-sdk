from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_payment_record_method import (
    InvoicePaymentRecordMethod,
    check_invoice_payment_record_method,
)
from ..models.invoice_payment_record_status import (
    InvoicePaymentRecordStatus,
    check_invoice_payment_record_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_breakdown_entry import InvoiceBreakdownEntry
    from ..models.invoice_payment_record_paid_amount import (
        InvoicePaymentRecordPaidAmount,
    )
    from ..models.invoice_stripe_payment import InvoiceStripePayment


T = TypeVar("T", bound="InvoicePaymentRecord")


@_attrs_define
class InvoicePaymentRecord:
    """
    Attributes:
        status (Union[Unset, InvoicePaymentRecordStatus]):
        stripe (Union[Unset, InvoiceStripePayment]):
        export_id (Union[Unset, str]):
        exported_at (Union[Unset, str]):
        exported_by (Union[Unset, str]):
        exported_by_name (Union[Unset, str]):
        method (Union[Unset, InvoicePaymentRecordMethod]):
        payment_date (Union[Unset, str]):
        reference (Union[Unset, str]):
        recorded_at (Union[Unset, str]):
        recorded_by (Union[Unset, str]):
        recorded_by_name (Union[Unset, str]):
        advice_version (Union[Unset, float]):
        paid_amount (Union[Unset, InvoicePaymentRecordPaidAmount]):
        withholdings (Union[Unset, List['InvoiceBreakdownEntry']]):
    """

    status: Union[Unset, InvoicePaymentRecordStatus] = UNSET
    stripe: Union[Unset, "InvoiceStripePayment"] = UNSET
    export_id: Union[Unset, str] = UNSET
    exported_at: Union[Unset, str] = UNSET
    exported_by: Union[Unset, str] = UNSET
    exported_by_name: Union[Unset, str] = UNSET
    method: Union[Unset, InvoicePaymentRecordMethod] = UNSET
    payment_date: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    recorded_at: Union[Unset, str] = UNSET
    recorded_by: Union[Unset, str] = UNSET
    recorded_by_name: Union[Unset, str] = UNSET
    advice_version: Union[Unset, float] = UNSET
    paid_amount: Union[Unset, "InvoicePaymentRecordPaidAmount"] = UNSET
    withholdings: Union[Unset, List["InvoiceBreakdownEntry"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        stripe: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stripe, Unset):
            stripe = self.stripe.to_dict()

        export_id = self.export_id

        exported_at = self.exported_at

        exported_by = self.exported_by

        exported_by_name = self.exported_by_name

        method: Union[Unset, str] = UNSET
        if not isinstance(self.method, Unset):
            method = self.method

        payment_date = self.payment_date

        reference = self.reference

        recorded_at = self.recorded_at

        recorded_by = self.recorded_by

        recorded_by_name = self.recorded_by_name

        advice_version = self.advice_version

        paid_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.paid_amount, Unset):
            paid_amount = self.paid_amount.to_dict()

        withholdings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.withholdings, Unset):
            withholdings = []
            for withholdings_item_data in self.withholdings:
                withholdings_item = withholdings_item_data.to_dict()
                withholdings.append(withholdings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if stripe is not UNSET:
            field_dict["stripe"] = stripe
        if export_id is not UNSET:
            field_dict["exportId"] = export_id
        if exported_at is not UNSET:
            field_dict["exportedAt"] = exported_at
        if exported_by is not UNSET:
            field_dict["exportedBy"] = exported_by
        if exported_by_name is not UNSET:
            field_dict["exportedByName"] = exported_by_name
        if method is not UNSET:
            field_dict["method"] = method
        if payment_date is not UNSET:
            field_dict["paymentDate"] = payment_date
        if reference is not UNSET:
            field_dict["reference"] = reference
        if recorded_at is not UNSET:
            field_dict["recordedAt"] = recorded_at
        if recorded_by is not UNSET:
            field_dict["recordedBy"] = recorded_by
        if recorded_by_name is not UNSET:
            field_dict["recordedByName"] = recorded_by_name
        if advice_version is not UNSET:
            field_dict["adviceVersion"] = advice_version
        if paid_amount is not UNSET:
            field_dict["paidAmount"] = paid_amount
        if withholdings is not UNSET:
            field_dict["withholdings"] = withholdings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_breakdown_entry import InvoiceBreakdownEntry
        from ..models.invoice_payment_record_paid_amount import (
            InvoicePaymentRecordPaidAmount,
        )
        from ..models.invoice_stripe_payment import InvoiceStripePayment

        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, InvoicePaymentRecordStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_invoice_payment_record_status(_status)

        _stripe = d.pop("stripe", UNSET)
        stripe: Union[Unset, InvoiceStripePayment]
        if isinstance(_stripe, Unset):
            stripe = UNSET
        else:
            stripe = InvoiceStripePayment.from_dict(_stripe)

        export_id = d.pop("exportId", UNSET)

        exported_at = d.pop("exportedAt", UNSET)

        exported_by = d.pop("exportedBy", UNSET)

        exported_by_name = d.pop("exportedByName", UNSET)

        _method = d.pop("method", UNSET)
        method: Union[Unset, InvoicePaymentRecordMethod]
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = check_invoice_payment_record_method(_method)

        payment_date = d.pop("paymentDate", UNSET)

        reference = d.pop("reference", UNSET)

        recorded_at = d.pop("recordedAt", UNSET)

        recorded_by = d.pop("recordedBy", UNSET)

        recorded_by_name = d.pop("recordedByName", UNSET)

        advice_version = d.pop("adviceVersion", UNSET)

        _paid_amount = d.pop("paidAmount", UNSET)
        paid_amount: Union[Unset, InvoicePaymentRecordPaidAmount]
        if isinstance(_paid_amount, Unset):
            paid_amount = UNSET
        else:
            paid_amount = InvoicePaymentRecordPaidAmount.from_dict(_paid_amount)

        withholdings = []
        _withholdings = d.pop("withholdings", UNSET)
        for withholdings_item_data in _withholdings or []:
            withholdings_item = InvoiceBreakdownEntry.from_dict(withholdings_item_data)

            withholdings.append(withholdings_item)

        invoice_payment_record = cls(
            status=status,
            stripe=stripe,
            export_id=export_id,
            exported_at=exported_at,
            exported_by=exported_by,
            exported_by_name=exported_by_name,
            method=method,
            payment_date=payment_date,
            reference=reference,
            recorded_at=recorded_at,
            recorded_by=recorded_by,
            recorded_by_name=recorded_by_name,
            advice_version=advice_version,
            paid_amount=paid_amount,
            withholdings=withholdings,
        )

        invoice_payment_record.additional_properties = d
        return invoice_payment_record

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
