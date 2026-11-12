from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Type,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sourcing_comparison_status import (
    SourcingComparisonStatus,
    check_sourcing_comparison_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sourcing_comparison_declined_item import (
        SourcingComparisonDeclinedItem,
    )
    from ..models.sourcing_comparison_evaluation import SourcingComparisonEvaluation
    from ..models.sourcing_comparison_line import SourcingComparisonLine
    from ..models.sourcing_comparison_lowest_total_type_0 import (
        SourcingComparisonLowestTotalType0,
    )
    from ..models.sourcing_comparison_no_answer_item import (
        SourcingComparisonNoAnswerItem,
    )
    from ..models.sourcing_comparison_questionnaire import (
        SourcingComparisonQuestionnaire,
    )
    from ..models.sourcing_comparison_responder import SourcingComparisonResponder
    from ..models.sourcing_criterion import SourcingCriterion


T = TypeVar("T", bound="SourcingComparison")


@_attrs_define
class SourcingComparison:
    """
    Attributes:
        rfq_id (Union[Unset, str]):
        status (Union[Unset, SourcingComparisonStatus]):
        currency (Union[Unset, str]):
        today (Union[Unset, str]):
        lines (Union[Unset, List['SourcingComparisonLine']]):
        responders (Union[Unset, List['SourcingComparisonResponder']]):
        lowest_total (Union['SourcingComparisonLowestTotalType0', None, Unset]):
        declined (Union[Unset, List['SourcingComparisonDeclinedItem']]):
        no_answer (Union[Unset, List['SourcingComparisonNoAnswerItem']]):
        questionnaire (Union[Unset, SourcingComparisonQuestionnaire]):
        round_ (Union[Unset, float]):
        rounds (Union[Unset, float]):
        criteria (Union[Unset, List['SourcingCriterion']]):
        evaluation (Union[Unset, SourcingComparisonEvaluation]):
    """

    rfq_id: Union[Unset, str] = UNSET
    status: Union[Unset, SourcingComparisonStatus] = UNSET
    currency: Union[Unset, str] = UNSET
    today: Union[Unset, str] = UNSET
    lines: Union[Unset, List["SourcingComparisonLine"]] = UNSET
    responders: Union[Unset, List["SourcingComparisonResponder"]] = UNSET
    lowest_total: Union["SourcingComparisonLowestTotalType0", None, Unset] = UNSET
    declined: Union[Unset, List["SourcingComparisonDeclinedItem"]] = UNSET
    no_answer: Union[Unset, List["SourcingComparisonNoAnswerItem"]] = UNSET
    questionnaire: Union[Unset, "SourcingComparisonQuestionnaire"] = UNSET
    round_: Union[Unset, float] = UNSET
    rounds: Union[Unset, float] = UNSET
    criteria: Union[Unset, List["SourcingCriterion"]] = UNSET
    evaluation: Union[Unset, "SourcingComparisonEvaluation"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.sourcing_comparison_lowest_total_type_0 import (
            SourcingComparisonLowestTotalType0,
        )

        rfq_id = self.rfq_id

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        currency = self.currency

        today = self.today

        lines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        responders: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.responders, Unset):
            responders = []
            for responders_item_data in self.responders:
                responders_item = responders_item_data.to_dict()
                responders.append(responders_item)

        lowest_total: Union[Dict[str, Any], None, Unset]
        if isinstance(self.lowest_total, Unset):
            lowest_total = UNSET
        elif isinstance(self.lowest_total, SourcingComparisonLowestTotalType0):
            lowest_total = self.lowest_total.to_dict()
        else:
            lowest_total = self.lowest_total

        declined: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.declined, Unset):
            declined = []
            for declined_item_data in self.declined:
                declined_item = declined_item_data.to_dict()
                declined.append(declined_item)

        no_answer: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.no_answer, Unset):
            no_answer = []
            for no_answer_item_data in self.no_answer:
                no_answer_item = no_answer_item_data.to_dict()
                no_answer.append(no_answer_item)

        questionnaire: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.questionnaire, Unset):
            questionnaire = self.questionnaire.to_dict()

        round_ = self.round_

        rounds = self.rounds

        criteria: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.criteria, Unset):
            criteria = []
            for criteria_item_data in self.criteria:
                criteria_item = criteria_item_data.to_dict()
                criteria.append(criteria_item)

        evaluation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.evaluation, Unset):
            evaluation = self.evaluation.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rfq_id is not UNSET:
            field_dict["rfqId"] = rfq_id
        if status is not UNSET:
            field_dict["status"] = status
        if currency is not UNSET:
            field_dict["currency"] = currency
        if today is not UNSET:
            field_dict["today"] = today
        if lines is not UNSET:
            field_dict["lines"] = lines
        if responders is not UNSET:
            field_dict["responders"] = responders
        if lowest_total is not UNSET:
            field_dict["lowestTotal"] = lowest_total
        if declined is not UNSET:
            field_dict["declined"] = declined
        if no_answer is not UNSET:
            field_dict["noAnswer"] = no_answer
        if questionnaire is not UNSET:
            field_dict["questionnaire"] = questionnaire
        if round_ is not UNSET:
            field_dict["round"] = round_
        if rounds is not UNSET:
            field_dict["rounds"] = rounds
        if criteria is not UNSET:
            field_dict["criteria"] = criteria
        if evaluation is not UNSET:
            field_dict["evaluation"] = evaluation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sourcing_comparison_declined_item import (
            SourcingComparisonDeclinedItem,
        )
        from ..models.sourcing_comparison_evaluation import SourcingComparisonEvaluation
        from ..models.sourcing_comparison_line import SourcingComparisonLine
        from ..models.sourcing_comparison_lowest_total_type_0 import (
            SourcingComparisonLowestTotalType0,
        )
        from ..models.sourcing_comparison_no_answer_item import (
            SourcingComparisonNoAnswerItem,
        )
        from ..models.sourcing_comparison_questionnaire import (
            SourcingComparisonQuestionnaire,
        )
        from ..models.sourcing_comparison_responder import SourcingComparisonResponder
        from ..models.sourcing_criterion import SourcingCriterion

        d = src_dict.copy()
        rfq_id = d.pop("rfqId", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, SourcingComparisonStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_sourcing_comparison_status(_status)

        currency = d.pop("currency", UNSET)

        today = d.pop("today", UNSET)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = SourcingComparisonLine.from_dict(lines_item_data)

            lines.append(lines_item)

        responders = []
        _responders = d.pop("responders", UNSET)
        for responders_item_data in _responders or []:
            responders_item = SourcingComparisonResponder.from_dict(
                responders_item_data
            )

            responders.append(responders_item)

        def _parse_lowest_total(
            data: object,
        ) -> Union["SourcingComparisonLowestTotalType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                lowest_total_type_0 = SourcingComparisonLowestTotalType0.from_dict(data)

                return lowest_total_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SourcingComparisonLowestTotalType0", None, Unset], data)

        lowest_total = _parse_lowest_total(d.pop("lowestTotal", UNSET))

        declined = []
        _declined = d.pop("declined", UNSET)
        for declined_item_data in _declined or []:
            declined_item = SourcingComparisonDeclinedItem.from_dict(declined_item_data)

            declined.append(declined_item)

        no_answer = []
        _no_answer = d.pop("noAnswer", UNSET)
        for no_answer_item_data in _no_answer or []:
            no_answer_item = SourcingComparisonNoAnswerItem.from_dict(
                no_answer_item_data
            )

            no_answer.append(no_answer_item)

        _questionnaire = d.pop("questionnaire", UNSET)
        questionnaire: Union[Unset, SourcingComparisonQuestionnaire]
        if isinstance(_questionnaire, Unset):
            questionnaire = UNSET
        else:
            questionnaire = SourcingComparisonQuestionnaire.from_dict(_questionnaire)

        round_ = d.pop("round", UNSET)

        rounds = d.pop("rounds", UNSET)

        criteria = []
        _criteria = d.pop("criteria", UNSET)
        for criteria_item_data in _criteria or []:
            criteria_item = SourcingCriterion.from_dict(criteria_item_data)

            criteria.append(criteria_item)

        _evaluation = d.pop("evaluation", UNSET)
        evaluation: Union[Unset, SourcingComparisonEvaluation]
        if isinstance(_evaluation, Unset):
            evaluation = UNSET
        else:
            evaluation = SourcingComparisonEvaluation.from_dict(_evaluation)

        sourcing_comparison = cls(
            rfq_id=rfq_id,
            status=status,
            currency=currency,
            today=today,
            lines=lines,
            responders=responders,
            lowest_total=lowest_total,
            declined=declined,
            no_answer=no_answer,
            questionnaire=questionnaire,
            round_=round_,
            rounds=rounds,
            criteria=criteria,
            evaluation=evaluation,
        )

        sourcing_comparison.additional_properties = d
        return sourcing_comparison

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
