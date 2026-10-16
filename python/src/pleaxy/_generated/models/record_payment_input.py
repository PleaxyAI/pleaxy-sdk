from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.record_payment_input_method import (
    RecordPaymentInputMethod,
    check_record_payment_input_method,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.breakdown_entry_input import BreakdownEntryInput
    from ..models.send_remittance_input import SendRemittanceInput


T = TypeVar("T", bound="RecordPaymentInput")


@_attrs_define
class RecordPaymentInput:
    """
    Attributes:
        method (RecordPaymentInputMethod):
        payment_date (str):
        reference (str):
        amount (Union[Unset, float]):
        currency (Union[Unset, str]):
        rate (Union[Unset, float]):
        rate_date (Union[Unset, str]):
        withholdings (Union[Unset, List['BreakdownEntryInput']]):
        remittance (Union[Unset, SendRemittanceInput]):
        confirm_replaced (Union[Unset, bool]):
    """

    method: RecordPaymentInputMethod
    payment_date: str
    reference: str
    amount: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    rate: Union[Unset, float] = UNSET
    rate_date: Union[Unset, str] = UNSET
    withholdings: Union[Unset, List["BreakdownEntryInput"]] = UNSET
    remittance: Union[Unset, "SendRemittanceInput"] = UNSET
    confirm_replaced: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        method: str = self.method

        payment_date = self.payment_date

        reference = self.reference

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

        remittance: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.remittance, Unset):
            remittance = self.remittance.to_dict()

        confirm_replaced = self.confirm_replaced

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method": method,
                "paymentDate": payment_date,
                "reference": reference,
            }
        )
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
        if remittance is not UNSET:
            field_dict["remittance"] = remittance
        if confirm_replaced is not UNSET:
            field_dict["confirmReplaced"] = confirm_replaced

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.breakdown_entry_input import BreakdownEntryInput
        from ..models.send_remittance_input import SendRemittanceInput

        d = src_dict.copy()
        method = check_record_payment_input_method(d.pop("method"))

        payment_date = d.pop("paymentDate")

        reference = d.pop("reference")

        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        rate = d.pop("rate", UNSET)

        rate_date = d.pop("rateDate", UNSET)

        withholdings = []
        _withholdings = d.pop("withholdings", UNSET)
        for withholdings_item_data in _withholdings or []:
            withholdings_item = BreakdownEntryInput.from_dict(withholdings_item_data)

            withholdings.append(withholdings_item)

        _remittance = d.pop("remittance", UNSET)
        remittance: Union[Unset, SendRemittanceInput]
        if isinstance(_remittance, Unset):
            remittance = UNSET
        else:
            remittance = SendRemittanceInput.from_dict(_remittance)

        confirm_replaced = d.pop("confirmReplaced", UNSET)

        record_payment_input = cls(
            method=method,
            payment_date=payment_date,
            reference=reference,
            amount=amount,
            currency=currency,
            rate=rate,
            rate_date=rate_date,
            withholdings=withholdings,
            remittance=remittance,
            confirm_replaced=confirm_replaced,
        )

        record_payment_input.additional_properties = d
        return record_payment_input

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
