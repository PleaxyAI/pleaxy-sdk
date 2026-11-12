from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.buyer_sourcing_event_summary_status import (
    BuyerSourcingEventSummaryStatus,
    check_buyer_sourcing_event_summary_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.buyer_sourcing_event_summary_award import (
        BuyerSourcingEventSummaryAward,
    )
    from ..models.buyer_sourcing_event_summary_awards_item import (
        BuyerSourcingEventSummaryAwardsItem,
    )
    from ..models.sourcing_answer_counts import SourcingAnswerCounts


T = TypeVar("T", bound="BuyerSourcingEventSummary")


@_attrs_define
class BuyerSourcingEventSummary:
    """
    Attributes:
        id (str):
        title (Union[Unset, str]):
        status (Union[Unset, BuyerSourcingEventSummaryStatus]):
        currency (Union[Unset, str]):
        due_at (Union[Unset, str]):
        sealed (Union[Unset, bool]):
        sealed_now (Union[Unset, bool]):
        answers (Union[Unset, SourcingAnswerCounts]):
        line_count (Union[Unset, float]):
        lowest_total (Union[None, Unset, float]):
        from_request_id (Union[Unset, str]):
        award (Union[Unset, BuyerSourcingEventSummaryAward]):
        awards (Union[Unset, List['BuyerSourcingEventSummaryAwardsItem']]):
        created_at (Union[Unset, str]):
        updated_at (Union[Unset, str]):
    """

    id: str
    title: Union[Unset, str] = UNSET
    status: Union[Unset, BuyerSourcingEventSummaryStatus] = UNSET
    currency: Union[Unset, str] = UNSET
    due_at: Union[Unset, str] = UNSET
    sealed: Union[Unset, bool] = UNSET
    sealed_now: Union[Unset, bool] = UNSET
    answers: Union[Unset, "SourcingAnswerCounts"] = UNSET
    line_count: Union[Unset, float] = UNSET
    lowest_total: Union[None, Unset, float] = UNSET
    from_request_id: Union[Unset, str] = UNSET
    award: Union[Unset, "BuyerSourcingEventSummaryAward"] = UNSET
    awards: Union[Unset, List["BuyerSourcingEventSummaryAwardsItem"]] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        title = self.title

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        currency = self.currency

        due_at = self.due_at

        sealed = self.sealed

        sealed_now = self.sealed_now

        answers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.answers, Unset):
            answers = self.answers.to_dict()

        line_count = self.line_count

        lowest_total: Union[None, Unset, float]
        if isinstance(self.lowest_total, Unset):
            lowest_total = UNSET
        else:
            lowest_total = self.lowest_total

        from_request_id = self.from_request_id

        award: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.award, Unset):
            award = self.award.to_dict()

        awards: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.awards, Unset):
            awards = []
            for awards_item_data in self.awards:
                awards_item = awards_item_data.to_dict()
                awards.append(awards_item)

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if status is not UNSET:
            field_dict["status"] = status
        if currency is not UNSET:
            field_dict["currency"] = currency
        if due_at is not UNSET:
            field_dict["dueAt"] = due_at
        if sealed is not UNSET:
            field_dict["sealed"] = sealed
        if sealed_now is not UNSET:
            field_dict["sealedNow"] = sealed_now
        if answers is not UNSET:
            field_dict["answers"] = answers
        if line_count is not UNSET:
            field_dict["lineCount"] = line_count
        if lowest_total is not UNSET:
            field_dict["lowestTotal"] = lowest_total
        if from_request_id is not UNSET:
            field_dict["fromRequestId"] = from_request_id
        if award is not UNSET:
            field_dict["award"] = award
        if awards is not UNSET:
            field_dict["awards"] = awards
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.buyer_sourcing_event_summary_award import (
            BuyerSourcingEventSummaryAward,
        )
        from ..models.buyer_sourcing_event_summary_awards_item import (
            BuyerSourcingEventSummaryAwardsItem,
        )
        from ..models.sourcing_answer_counts import SourcingAnswerCounts

        d = src_dict.copy()
        id = d.pop("id")

        title = d.pop("title", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, BuyerSourcingEventSummaryStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_buyer_sourcing_event_summary_status(_status)

        currency = d.pop("currency", UNSET)

        due_at = d.pop("dueAt", UNSET)

        sealed = d.pop("sealed", UNSET)

        sealed_now = d.pop("sealedNow", UNSET)

        _answers = d.pop("answers", UNSET)
        answers: Union[Unset, SourcingAnswerCounts]
        if isinstance(_answers, Unset):
            answers = UNSET
        else:
            answers = SourcingAnswerCounts.from_dict(_answers)

        line_count = d.pop("lineCount", UNSET)

        def _parse_lowest_total(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        lowest_total = _parse_lowest_total(d.pop("lowestTotal", UNSET))

        from_request_id = d.pop("fromRequestId", UNSET)

        _award = d.pop("award", UNSET)
        award: Union[Unset, BuyerSourcingEventSummaryAward]
        if isinstance(_award, Unset):
            award = UNSET
        else:
            award = BuyerSourcingEventSummaryAward.from_dict(_award)

        awards = []
        _awards = d.pop("awards", UNSET)
        for awards_item_data in _awards or []:
            awards_item = BuyerSourcingEventSummaryAwardsItem.from_dict(
                awards_item_data
            )

            awards.append(awards_item)

        created_at = d.pop("createdAt", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        buyer_sourcing_event_summary = cls(
            id=id,
            title=title,
            status=status,
            currency=currency,
            due_at=due_at,
            sealed=sealed,
            sealed_now=sealed_now,
            answers=answers,
            line_count=line_count,
            lowest_total=lowest_total,
            from_request_id=from_request_id,
            award=award,
            awards=awards,
            created_at=created_at,
            updated_at=updated_at,
        )

        buyer_sourcing_event_summary.additional_properties = d
        return buyer_sourcing_event_summary

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
