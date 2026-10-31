from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ai_uncovered_spend_invoicer import (
    AiUncoveredSpendInvoicer,
    check_ai_uncovered_spend_invoicer,
)
from ..models.ai_uncovered_spend_reason import (
    AiUncoveredSpendReason,
    check_ai_uncovered_spend_reason,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AiUncoveredSpend")


@_attrs_define
class AiUncoveredSpend:
    """
    Attributes:
        invoicer_id (Union[Unset, str]):
        invoicer (Union[Unset, AiUncoveredSpendInvoicer]):
        label (Union[Unset, str]):
        currency (Union[Unset, str]):
        month_to_date (Union[Unset, float]):
        forecast (Union[Unset, float]):
        covered (Union[Unset, float]):
        gap (Union[Unset, float]):
        reason (Union[Unset, AiUncoveredSpendReason]):
        po_ids (Union[Unset, List[str]]):
        draft_po_ids (Union[Unset, List[str]]):
        pending_po_ids (Union[Unset, List[str]]):
    """

    invoicer_id: Union[Unset, str] = UNSET
    invoicer: Union[Unset, AiUncoveredSpendInvoicer] = UNSET
    label: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    month_to_date: Union[Unset, float] = UNSET
    forecast: Union[Unset, float] = UNSET
    covered: Union[Unset, float] = UNSET
    gap: Union[Unset, float] = UNSET
    reason: Union[Unset, AiUncoveredSpendReason] = UNSET
    po_ids: Union[Unset, List[str]] = UNSET
    draft_po_ids: Union[Unset, List[str]] = UNSET
    pending_po_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoicer_id = self.invoicer_id

        invoicer: Union[Unset, str] = UNSET
        if not isinstance(self.invoicer, Unset):
            invoicer = self.invoicer

        label = self.label

        currency = self.currency

        month_to_date = self.month_to_date

        forecast = self.forecast

        covered = self.covered

        gap = self.gap

        reason: Union[Unset, str] = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason

        po_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.po_ids, Unset):
            po_ids = self.po_ids

        draft_po_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.draft_po_ids, Unset):
            draft_po_ids = self.draft_po_ids

        pending_po_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.pending_po_ids, Unset):
            pending_po_ids = self.pending_po_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invoicer_id is not UNSET:
            field_dict["invoicerId"] = invoicer_id
        if invoicer is not UNSET:
            field_dict["invoicer"] = invoicer
        if label is not UNSET:
            field_dict["label"] = label
        if currency is not UNSET:
            field_dict["currency"] = currency
        if month_to_date is not UNSET:
            field_dict["monthToDate"] = month_to_date
        if forecast is not UNSET:
            field_dict["forecast"] = forecast
        if covered is not UNSET:
            field_dict["covered"] = covered
        if gap is not UNSET:
            field_dict["gap"] = gap
        if reason is not UNSET:
            field_dict["reason"] = reason
        if po_ids is not UNSET:
            field_dict["poIds"] = po_ids
        if draft_po_ids is not UNSET:
            field_dict["draftPoIds"] = draft_po_ids
        if pending_po_ids is not UNSET:
            field_dict["pendingPoIds"] = pending_po_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        invoicer_id = d.pop("invoicerId", UNSET)

        _invoicer = d.pop("invoicer", UNSET)
        invoicer: Union[Unset, AiUncoveredSpendInvoicer]
        if isinstance(_invoicer, Unset):
            invoicer = UNSET
        else:
            invoicer = check_ai_uncovered_spend_invoicer(_invoicer)

        label = d.pop("label", UNSET)

        currency = d.pop("currency", UNSET)

        month_to_date = d.pop("monthToDate", UNSET)

        forecast = d.pop("forecast", UNSET)

        covered = d.pop("covered", UNSET)

        gap = d.pop("gap", UNSET)

        _reason = d.pop("reason", UNSET)
        reason: Union[Unset, AiUncoveredSpendReason]
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = check_ai_uncovered_spend_reason(_reason)

        po_ids = cast(List[str], d.pop("poIds", UNSET))

        draft_po_ids = cast(List[str], d.pop("draftPoIds", UNSET))

        pending_po_ids = cast(List[str], d.pop("pendingPoIds", UNSET))

        ai_uncovered_spend = cls(
            invoicer_id=invoicer_id,
            invoicer=invoicer,
            label=label,
            currency=currency,
            month_to_date=month_to_date,
            forecast=forecast,
            covered=covered,
            gap=gap,
            reason=reason,
            po_ids=po_ids,
            draft_po_ids=draft_po_ids,
            pending_po_ids=pending_po_ids,
        )

        ai_uncovered_spend.additional_properties = d
        return ai_uncovered_spend

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
