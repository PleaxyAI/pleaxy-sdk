from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reconciliation_result_match_type import (
    ReconciliationResultMatchType,
    check_reconciliation_result_match_type,
)
from ..models.reconciliation_result_primary_failure import (
    ReconciliationResultPrimaryFailure,
    check_reconciliation_result_primary_failure,
)
from ..models.reconciliation_result_status import (
    ReconciliationResultStatus,
    check_reconciliation_result_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reconciliation_failure import ReconciliationFailure
    from ..models.reconciliation_result_checked_item import (
        ReconciliationResultCheckedItem,
    )
    from ..models.reconciliation_result_insights_item import (
        ReconciliationResultInsightsItem,
    )
    from ..models.reconciliation_result_records import ReconciliationResultRecords
    from ..models.reconciliation_result_tolerance import ReconciliationResultTolerance


T = TypeVar("T", bound="ReconciliationResult")


@_attrs_define
class ReconciliationResult:
    """
    Attributes:
        invoice_id (Union[Unset, str]):
        currency (Union[Unset, str]):
        amount (Union[Unset, str]):
        status (Union[Unset, ReconciliationResultStatus]):
        unverified_reason (Union[Unset, str]):
        resolved_by_person (Union[Unset, bool]):
        approval_status (Union[Unset, str]):
        paid (Union[Unset, bool]):
        match_type (Union[Unset, ReconciliationResultMatchType]):
        records (Union[Unset, ReconciliationResultRecords]):
        tolerance (Union[Unset, ReconciliationResultTolerance]):
        checked (Union[Unset, List['ReconciliationResultCheckedItem']]):
        failures (Union[Unset, List['ReconciliationFailure']]):
        primary_failure (Union[Unset, ReconciliationResultPrimaryFailure]):
        insights (Union[Unset, List['ReconciliationResultInsightsItem']]):
    """

    invoice_id: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    amount: Union[Unset, str] = UNSET
    status: Union[Unset, ReconciliationResultStatus] = UNSET
    unverified_reason: Union[Unset, str] = UNSET
    resolved_by_person: Union[Unset, bool] = UNSET
    approval_status: Union[Unset, str] = UNSET
    paid: Union[Unset, bool] = UNSET
    match_type: Union[Unset, ReconciliationResultMatchType] = UNSET
    records: Union[Unset, "ReconciliationResultRecords"] = UNSET
    tolerance: Union[Unset, "ReconciliationResultTolerance"] = UNSET
    checked: Union[Unset, List["ReconciliationResultCheckedItem"]] = UNSET
    failures: Union[Unset, List["ReconciliationFailure"]] = UNSET
    primary_failure: Union[Unset, ReconciliationResultPrimaryFailure] = UNSET
    insights: Union[Unset, List["ReconciliationResultInsightsItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoice_id = self.invoice_id

        currency = self.currency

        amount = self.amount

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        unverified_reason = self.unverified_reason

        resolved_by_person = self.resolved_by_person

        approval_status = self.approval_status

        paid = self.paid

        match_type: Union[Unset, str] = UNSET
        if not isinstance(self.match_type, Unset):
            match_type = self.match_type

        records: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.records, Unset):
            records = self.records.to_dict()

        tolerance: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tolerance, Unset):
            tolerance = self.tolerance.to_dict()

        checked: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.checked, Unset):
            checked = []
            for checked_item_data in self.checked:
                checked_item = checked_item_data.to_dict()
                checked.append(checked_item)

        failures: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.failures, Unset):
            failures = []
            for failures_item_data in self.failures:
                failures_item = failures_item_data.to_dict()
                failures.append(failures_item)

        primary_failure: Union[Unset, str] = UNSET
        if not isinstance(self.primary_failure, Unset):
            primary_failure = self.primary_failure

        insights: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.insights, Unset):
            insights = []
            for insights_item_data in self.insights:
                insights_item = insights_item_data.to_dict()
                insights.append(insights_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invoice_id is not UNSET:
            field_dict["invoice_id"] = invoice_id
        if currency is not UNSET:
            field_dict["currency"] = currency
        if amount is not UNSET:
            field_dict["amount"] = amount
        if status is not UNSET:
            field_dict["status"] = status
        if unverified_reason is not UNSET:
            field_dict["unverified_reason"] = unverified_reason
        if resolved_by_person is not UNSET:
            field_dict["resolved_by_person"] = resolved_by_person
        if approval_status is not UNSET:
            field_dict["approval_status"] = approval_status
        if paid is not UNSET:
            field_dict["paid"] = paid
        if match_type is not UNSET:
            field_dict["match_type"] = match_type
        if records is not UNSET:
            field_dict["records"] = records
        if tolerance is not UNSET:
            field_dict["tolerance"] = tolerance
        if checked is not UNSET:
            field_dict["checked"] = checked
        if failures is not UNSET:
            field_dict["failures"] = failures
        if primary_failure is not UNSET:
            field_dict["primary_failure"] = primary_failure
        if insights is not UNSET:
            field_dict["insights"] = insights

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reconciliation_failure import ReconciliationFailure
        from ..models.reconciliation_result_checked_item import (
            ReconciliationResultCheckedItem,
        )
        from ..models.reconciliation_result_insights_item import (
            ReconciliationResultInsightsItem,
        )
        from ..models.reconciliation_result_records import ReconciliationResultRecords
        from ..models.reconciliation_result_tolerance import (
            ReconciliationResultTolerance,
        )

        d = src_dict.copy()
        invoice_id = d.pop("invoice_id", UNSET)

        currency = d.pop("currency", UNSET)

        amount = d.pop("amount", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ReconciliationResultStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_reconciliation_result_status(_status)

        unverified_reason = d.pop("unverified_reason", UNSET)

        resolved_by_person = d.pop("resolved_by_person", UNSET)

        approval_status = d.pop("approval_status", UNSET)

        paid = d.pop("paid", UNSET)

        _match_type = d.pop("match_type", UNSET)
        match_type: Union[Unset, ReconciliationResultMatchType]
        if isinstance(_match_type, Unset):
            match_type = UNSET
        else:
            match_type = check_reconciliation_result_match_type(_match_type)

        _records = d.pop("records", UNSET)
        records: Union[Unset, ReconciliationResultRecords]
        if isinstance(_records, Unset):
            records = UNSET
        else:
            records = ReconciliationResultRecords.from_dict(_records)

        _tolerance = d.pop("tolerance", UNSET)
        tolerance: Union[Unset, ReconciliationResultTolerance]
        if isinstance(_tolerance, Unset):
            tolerance = UNSET
        else:
            tolerance = ReconciliationResultTolerance.from_dict(_tolerance)

        checked = []
        _checked = d.pop("checked", UNSET)
        for checked_item_data in _checked or []:
            checked_item = ReconciliationResultCheckedItem.from_dict(checked_item_data)

            checked.append(checked_item)

        failures = []
        _failures = d.pop("failures", UNSET)
        for failures_item_data in _failures or []:
            failures_item = ReconciliationFailure.from_dict(failures_item_data)

            failures.append(failures_item)

        _primary_failure = d.pop("primary_failure", UNSET)
        primary_failure: Union[Unset, ReconciliationResultPrimaryFailure]
        if isinstance(_primary_failure, Unset):
            primary_failure = UNSET
        else:
            primary_failure = check_reconciliation_result_primary_failure(
                _primary_failure
            )

        insights = []
        _insights = d.pop("insights", UNSET)
        for insights_item_data in _insights or []:
            insights_item = ReconciliationResultInsightsItem.from_dict(
                insights_item_data
            )

            insights.append(insights_item)

        reconciliation_result = cls(
            invoice_id=invoice_id,
            currency=currency,
            amount=amount,
            status=status,
            unverified_reason=unverified_reason,
            resolved_by_person=resolved_by_person,
            approval_status=approval_status,
            paid=paid,
            match_type=match_type,
            records=records,
            tolerance=tolerance,
            checked=checked,
            failures=failures,
            primary_failure=primary_failure,
            insights=insights,
        )

        reconciliation_result.additional_properties = d
        return reconciliation_result

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
