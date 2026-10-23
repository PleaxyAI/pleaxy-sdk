from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.record_payments_result_results_item_outcome import (
    RecordPaymentsResultResultsItemOutcome,
    check_record_payments_result_results_item_outcome,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_params import ErrorParams


T = TypeVar("T", bound="RecordPaymentsResultResultsItem")


@_attrs_define
class RecordPaymentsResultResultsItem:
    """
    Attributes:
        invoice_id (Union[Unset, str]):
        outcome (Union[Unset, RecordPaymentsResultResultsItemOutcome]):
        status (Union[Unset, float]):
        code (Union[Unset, str]):
        message (Union[Unset, str]):
        message_id (Union[Unset, str]):
        params (Union[Unset, ErrorParams]):
    """

    invoice_id: Union[Unset, str] = UNSET
    outcome: Union[Unset, RecordPaymentsResultResultsItemOutcome] = UNSET
    status: Union[Unset, float] = UNSET
    code: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    message_id: Union[Unset, str] = UNSET
    params: Union[Unset, "ErrorParams"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoice_id = self.invoice_id

        outcome: Union[Unset, str] = UNSET
        if not isinstance(self.outcome, Unset):
            outcome = self.outcome

        status = self.status

        code = self.code

        message = self.message

        message_id = self.message_id

        params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invoice_id is not UNSET:
            field_dict["invoiceId"] = invoice_id
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if status is not UNSET:
            field_dict["status"] = status
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.error_params import ErrorParams

        d = src_dict.copy()
        invoice_id = d.pop("invoiceId", UNSET)

        _outcome = d.pop("outcome", UNSET)
        outcome: Union[Unset, RecordPaymentsResultResultsItemOutcome]
        if isinstance(_outcome, Unset):
            outcome = UNSET
        else:
            outcome = check_record_payments_result_results_item_outcome(_outcome)

        status = d.pop("status", UNSET)

        code = d.pop("code", UNSET)

        message = d.pop("message", UNSET)

        message_id = d.pop("messageId", UNSET)

        _params = d.pop("params", UNSET)
        params: Union[Unset, ErrorParams]
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = ErrorParams.from_dict(_params)

        record_payments_result_results_item = cls(
            invoice_id=invoice_id,
            outcome=outcome,
            status=status,
            code=code,
            message=message,
            message_id=message_id,
            params=params,
        )

        record_payments_result_results_item.additional_properties = d
        return record_payments_result_results_item

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
