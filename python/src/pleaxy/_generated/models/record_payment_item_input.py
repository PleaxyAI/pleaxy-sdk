from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.record_payment_item_input_method import (
    RecordPaymentItemInputMethod,
    check_record_payment_item_input_method,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.breakdown_entry_input import BreakdownEntryInput


T = TypeVar("T", bound="RecordPaymentItemInput")


@_attrs_define
class RecordPaymentItemInput:
    """
    Attributes:
        invoice_id (str):
        method (RecordPaymentItemInputMethod):
        payment_date (str):
        reference (str):
        note (Union[Unset, str]):
        amount (Union[Unset, float]):
        currency (Union[Unset, str]):
        rate (Union[Unset, float]):
        rate_date (Union[Unset, str]):
        withholdings (Union[Unset, List['BreakdownEntryInput']]):
        confirm_replaced (Union[Unset, bool]):
    """

    invoice_id: str
    method: RecordPaymentItemInputMethod
    payment_date: str
    reference: str
    note: Union[Unset, str] = UNSET
    amount: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    rate: Union[Unset, float] = UNSET
    rate_date: Union[Unset, str] = UNSET
    withholdings: Union[Unset, List["BreakdownEntryInput"]] = UNSET
    confirm_replaced: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoice_id = self.invoice_id

        method: str = self.method

        payment_date = self.payment_date

        reference = self.reference

        note = self.note

        amount = self.amount

        currency = self.currency

        rate = self.rate

        rate_date = self.rate_date

        withholdings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.withholdings, Unset):
            withholdings = []
            for withholdings_item_data in self.withholdings:
                withholdings_item = withholdings_item_data.to_dict()
                withholdings.append(withholdings_item)

        confirm_replaced = self.confirm_replaced

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invoiceId": invoice_id,
                "method": method,
                "paymentDate": payment_date,
                "reference": reference,
            }
        )
        if note is not UNSET:
            field_dict["note"] = note
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if rate is not UNSET:
            field_dict["rate"] = rate
        if rate_date is not UNSET:
            field_dict["rateDate"] = rate_date
        if withholdings is not UNSET:
            field_dict["withholdings"] = withholdings
        if confirm_replaced is not UNSET:
            field_dict["confirmReplaced"] = confirm_replaced

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.breakdown_entry_input import BreakdownEntryInput

        d = src_dict.copy()
        invoice_id = d.pop("invoiceId")

        method = check_record_payment_item_input_method(d.pop("method"))

        payment_date = d.pop("paymentDate")

        reference = d.pop("reference")

        note = d.pop("note", UNSET)

        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        rate = d.pop("rate", UNSET)

        rate_date = d.pop("rateDate", UNSET)

        withholdings = []
        _withholdings = d.pop("withholdings", UNSET)
        for withholdings_item_data in _withholdings or []:
            withholdings_item = BreakdownEntryInput.from_dict(withholdings_item_data)

            withholdings.append(withholdings_item)

        confirm_replaced = d.pop("confirmReplaced", UNSET)

        record_payment_item_input = cls(
            invoice_id=invoice_id,
            method=method,
            payment_date=payment_date,
            reference=reference,
            note=note,
            amount=amount,
            currency=currency,
            rate=rate,
            rate_date=rate_date,
            withholdings=withholdings,
            confirm_replaced=confirm_replaced,
        )

        record_payment_item_input.additional_properties = d
        return record_payment_item_input

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
