from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.purchase_order_change_summary_outcome import (
    PurchaseOrderChangeSummaryOutcome,
    check_purchase_order_change_summary_outcome,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PurchaseOrderChangeSummary")


@_attrs_define
class PurchaseOrderChangeSummary:
    """
    Attributes:
        version (Union[Unset, float]):
        at (Union[Unset, str]):
        by (Union[Unset, str]):
        by_name (Union[Unset, str]):
        amount_from (Union[Unset, float]):
        amount_to (Union[Unset, float]):
        currency (Union[Unset, str]):
        lines_added (Union[Unset, float]):
        lines_removed (Union[Unset, float]):
        lines_changed (Union[Unset, float]):
        outcome (Union[Unset, PurchaseOrderChangeSummaryOutcome]):
    """

    version: Union[Unset, float] = UNSET
    at: Union[Unset, str] = UNSET
    by: Union[Unset, str] = UNSET
    by_name: Union[Unset, str] = UNSET
    amount_from: Union[Unset, float] = UNSET
    amount_to: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    lines_added: Union[Unset, float] = UNSET
    lines_removed: Union[Unset, float] = UNSET
    lines_changed: Union[Unset, float] = UNSET
    outcome: Union[Unset, PurchaseOrderChangeSummaryOutcome] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        version = self.version

        at = self.at

        by = self.by

        by_name = self.by_name

        amount_from = self.amount_from

        amount_to = self.amount_to

        currency = self.currency

        lines_added = self.lines_added

        lines_removed = self.lines_removed

        lines_changed = self.lines_changed

        outcome: Union[Unset, str] = UNSET
        if not isinstance(self.outcome, Unset):
            outcome = self.outcome

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version
        if at is not UNSET:
            field_dict["at"] = at
        if by is not UNSET:
            field_dict["by"] = by
        if by_name is not UNSET:
            field_dict["byName"] = by_name
        if amount_from is not UNSET:
            field_dict["amountFrom"] = amount_from
        if amount_to is not UNSET:
            field_dict["amountTo"] = amount_to
        if currency is not UNSET:
            field_dict["currency"] = currency
        if lines_added is not UNSET:
            field_dict["linesAdded"] = lines_added
        if lines_removed is not UNSET:
            field_dict["linesRemoved"] = lines_removed
        if lines_changed is not UNSET:
            field_dict["linesChanged"] = lines_changed
        if outcome is not UNSET:
            field_dict["outcome"] = outcome

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        version = d.pop("version", UNSET)

        at = d.pop("at", UNSET)

        by = d.pop("by", UNSET)

        by_name = d.pop("byName", UNSET)

        amount_from = d.pop("amountFrom", UNSET)

        amount_to = d.pop("amountTo", UNSET)

        currency = d.pop("currency", UNSET)

        lines_added = d.pop("linesAdded", UNSET)

        lines_removed = d.pop("linesRemoved", UNSET)

        lines_changed = d.pop("linesChanged", UNSET)

        _outcome = d.pop("outcome", UNSET)
        outcome: Union[Unset, PurchaseOrderChangeSummaryOutcome]
        if isinstance(_outcome, Unset):
            outcome = UNSET
        else:
            outcome = check_purchase_order_change_summary_outcome(_outcome)

        purchase_order_change_summary = cls(
            version=version,
            at=at,
            by=by,
            by_name=by_name,
            amount_from=amount_from,
            amount_to=amount_to,
            currency=currency,
            lines_added=lines_added,
            lines_removed=lines_removed,
            lines_changed=lines_changed,
            outcome=outcome,
        )

        purchase_order_change_summary.additional_properties = d
        return purchase_order_change_summary

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
