from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.buyer_sourcing_event_view_status import (
    BuyerSourcingEventViewStatus,
    check_buyer_sourcing_event_view_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.buyer_sourcing_event_view_scoring import BuyerSourcingEventViewScoring
    from ..models.buyer_sourcing_invitee_view import BuyerSourcingInviteeView
    from ..models.buyer_sourcing_question_view import BuyerSourcingQuestionView
    from ..models.buyer_sourcing_response_view import BuyerSourcingResponseView
    from ..models.sourcing_activity import SourcingActivity
    from ..models.sourcing_answer_counts import SourcingAnswerCounts
    from ..models.sourcing_assistant_read import SourcingAssistantRead
    from ..models.sourcing_attachment import SourcingAttachment
    from ..models.sourcing_award import SourcingAward
    from ..models.sourcing_criterion import SourcingCriterion
    from ..models.sourcing_line import SourcingLine
    from ..models.sourcing_manual_points import SourcingManualPoints
    from ..models.sourcing_questionnaire import SourcingQuestionnaire
    from ..models.sourcing_round import SourcingRound


T = TypeVar("T", bound="BuyerSourcingEventView")


@_attrs_define
class BuyerSourcingEventView:
    """
    Attributes:
        id (str):
        title (Union[Unset, str]):
        description (Union[Unset, str]):
        status (Union[Unset, BuyerSourcingEventViewStatus]):
        currency (Union[Unset, str]):
        due_at (Union[Unset, str]):
        sealed (Union[Unset, bool]):
        sealed_now (Union[Unset, bool]):
        lines (Union[Unset, List['SourcingLine']]):
        attachments (Union[Unset, List['SourcingAttachment']]):
        from_request_id (Union[Unset, str]):
        cost_center (Union[Unset, str]):
        gl_code (Union[Unset, str]):
        award (Union[Unset, SourcingAward]):
        awards (Union[Unset, List['SourcingAward']]):
        questionnaire (Union[Unset, SourcingQuestionnaire]):
        scoring (Union[Unset, BuyerSourcingEventViewScoring]):
        manual_points (Union[Unset, SourcingManualPoints]):
        assistant_read (Union[Unset, SourcingAssistantRead]):
        round_ (Union[Unset, float]):
        rounds (Union[Unset, List['SourcingRound']]):
        criteria (Union[Unset, List['SourcingCriterion']]):
        evaluators (Union[Unset, List[str]]):
        created_by (Union[Unset, str]):
        created_by_name (Union[Unset, str]):
        created_at (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        published_at (Union[Unset, str]):
        closed_at (Union[Unset, str]):
        canceled_at (Union[Unset, str]):
        version (Union[Unset, float]):
        invitees (Union[Unset, List['BuyerSourcingInviteeView']]):
        answers (Union[Unset, SourcingAnswerCounts]):
        responses (Union[Unset, List['BuyerSourcingResponseView']]):
        questions (Union[Unset, List['BuyerSourcingQuestionView']]):
        activity (Union[Unset, List['SourcingActivity']]):
    """

    id: str
    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    status: Union[Unset, BuyerSourcingEventViewStatus] = UNSET
    currency: Union[Unset, str] = UNSET
    due_at: Union[Unset, str] = UNSET
    sealed: Union[Unset, bool] = UNSET
    sealed_now: Union[Unset, bool] = UNSET
    lines: Union[Unset, List["SourcingLine"]] = UNSET
    attachments: Union[Unset, List["SourcingAttachment"]] = UNSET
    from_request_id: Union[Unset, str] = UNSET
    cost_center: Union[Unset, str] = UNSET
    gl_code: Union[Unset, str] = UNSET
    award: Union[Unset, "SourcingAward"] = UNSET
    awards: Union[Unset, List["SourcingAward"]] = UNSET
    questionnaire: Union[Unset, "SourcingQuestionnaire"] = UNSET
    scoring: Union[Unset, "BuyerSourcingEventViewScoring"] = UNSET
    manual_points: Union[Unset, "SourcingManualPoints"] = UNSET
    assistant_read: Union[Unset, "SourcingAssistantRead"] = UNSET
    round_: Union[Unset, float] = UNSET
    rounds: Union[Unset, List["SourcingRound"]] = UNSET
    criteria: Union[Unset, List["SourcingCriterion"]] = UNSET
    evaluators: Union[Unset, List[str]] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_by_name: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    published_at: Union[Unset, str] = UNSET
    closed_at: Union[Unset, str] = UNSET
    canceled_at: Union[Unset, str] = UNSET
    version: Union[Unset, float] = UNSET
    invitees: Union[Unset, List["BuyerSourcingInviteeView"]] = UNSET
    answers: Union[Unset, "SourcingAnswerCounts"] = UNSET
    responses: Union[Unset, List["BuyerSourcingResponseView"]] = UNSET
    questions: Union[Unset, List["BuyerSourcingQuestionView"]] = UNSET
    activity: Union[Unset, List["SourcingActivity"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        title = self.title

        description = self.description

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        currency = self.currency

        due_at = self.due_at

        sealed = self.sealed

        sealed_now = self.sealed_now

        lines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        attachments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)

        from_request_id = self.from_request_id

        cost_center = self.cost_center

        gl_code = self.gl_code

        award: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.award, Unset):
            award = self.award.to_dict()

        awards: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.awards, Unset):
            awards = []
            for awards_item_data in self.awards:
                awards_item = awards_item_data.to_dict()
                awards.append(awards_item)

        questionnaire: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.questionnaire, Unset):
            questionnaire = self.questionnaire.to_dict()

        scoring: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.scoring, Unset):
            scoring = self.scoring.to_dict()

        manual_points: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.manual_points, Unset):
            manual_points = self.manual_points.to_dict()

        assistant_read: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.assistant_read, Unset):
            assistant_read = self.assistant_read.to_dict()

        round_ = self.round_

        rounds: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rounds, Unset):
            rounds = []
            for rounds_item_data in self.rounds:
                rounds_item = rounds_item_data.to_dict()
                rounds.append(rounds_item)

        criteria: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.criteria, Unset):
            criteria = []
            for criteria_item_data in self.criteria:
                criteria_item = criteria_item_data.to_dict()
                criteria.append(criteria_item)

        evaluators: Union[Unset, List[str]] = UNSET
        if not isinstance(self.evaluators, Unset):
            evaluators = self.evaluators

        created_by = self.created_by

        created_by_name = self.created_by_name

        created_at = self.created_at

        updated_at = self.updated_at

        published_at = self.published_at

        closed_at = self.closed_at

        canceled_at = self.canceled_at

        version = self.version

        invitees: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.invitees, Unset):
            invitees = []
            for invitees_item_data in self.invitees:
                invitees_item = invitees_item_data.to_dict()
                invitees.append(invitees_item)

        answers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.answers, Unset):
            answers = self.answers.to_dict()

        responses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.responses, Unset):
            responses = []
            for responses_item_data in self.responses:
                responses_item = responses_item_data.to_dict()
                responses.append(responses_item)

        questions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.questions, Unset):
            questions = []
            for questions_item_data in self.questions:
                questions_item = questions_item_data.to_dict()
                questions.append(questions_item)

        activity: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.activity, Unset):
            activity = []
            for activity_item_data in self.activity:
                activity_item = activity_item_data.to_dict()
                activity.append(activity_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
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
        if lines is not UNSET:
            field_dict["lines"] = lines
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if from_request_id is not UNSET:
            field_dict["fromRequestId"] = from_request_id
        if cost_center is not UNSET:
            field_dict["costCenter"] = cost_center
        if gl_code is not UNSET:
            field_dict["glCode"] = gl_code
        if award is not UNSET:
            field_dict["award"] = award
        if awards is not UNSET:
            field_dict["awards"] = awards
        if questionnaire is not UNSET:
            field_dict["questionnaire"] = questionnaire
        if scoring is not UNSET:
            field_dict["scoring"] = scoring
        if manual_points is not UNSET:
            field_dict["manualPoints"] = manual_points
        if assistant_read is not UNSET:
            field_dict["assistantRead"] = assistant_read
        if round_ is not UNSET:
            field_dict["round"] = round_
        if rounds is not UNSET:
            field_dict["rounds"] = rounds
        if criteria is not UNSET:
            field_dict["criteria"] = criteria
        if evaluators is not UNSET:
            field_dict["evaluators"] = evaluators
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_by_name is not UNSET:
            field_dict["createdByName"] = created_by_name
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if published_at is not UNSET:
            field_dict["publishedAt"] = published_at
        if closed_at is not UNSET:
            field_dict["closedAt"] = closed_at
        if canceled_at is not UNSET:
            field_dict["canceledAt"] = canceled_at
        if version is not UNSET:
            field_dict["version"] = version
        if invitees is not UNSET:
            field_dict["invitees"] = invitees
        if answers is not UNSET:
            field_dict["answers"] = answers
        if responses is not UNSET:
            field_dict["responses"] = responses
        if questions is not UNSET:
            field_dict["questions"] = questions
        if activity is not UNSET:
            field_dict["activity"] = activity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.buyer_sourcing_event_view_scoring import (
            BuyerSourcingEventViewScoring,
        )
        from ..models.buyer_sourcing_invitee_view import BuyerSourcingInviteeView
        from ..models.buyer_sourcing_question_view import BuyerSourcingQuestionView
        from ..models.buyer_sourcing_response_view import BuyerSourcingResponseView
        from ..models.sourcing_activity import SourcingActivity
        from ..models.sourcing_answer_counts import SourcingAnswerCounts
        from ..models.sourcing_assistant_read import SourcingAssistantRead
        from ..models.sourcing_attachment import SourcingAttachment
        from ..models.sourcing_award import SourcingAward
        from ..models.sourcing_criterion import SourcingCriterion
        from ..models.sourcing_line import SourcingLine
        from ..models.sourcing_manual_points import SourcingManualPoints
        from ..models.sourcing_questionnaire import SourcingQuestionnaire
        from ..models.sourcing_round import SourcingRound

        d = src_dict.copy()
        id = d.pop("id")

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, BuyerSourcingEventViewStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_buyer_sourcing_event_view_status(_status)

        currency = d.pop("currency", UNSET)

        due_at = d.pop("dueAt", UNSET)

        sealed = d.pop("sealed", UNSET)

        sealed_now = d.pop("sealedNow", UNSET)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = SourcingLine.from_dict(lines_item_data)

            lines.append(lines_item)

        attachments = []
        _attachments = d.pop("attachments", UNSET)
        for attachments_item_data in _attachments or []:
            attachments_item = SourcingAttachment.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        from_request_id = d.pop("fromRequestId", UNSET)

        cost_center = d.pop("costCenter", UNSET)

        gl_code = d.pop("glCode", UNSET)

        _award = d.pop("award", UNSET)
        award: Union[Unset, SourcingAward]
        if isinstance(_award, Unset):
            award = UNSET
        else:
            award = SourcingAward.from_dict(_award)

        awards = []
        _awards = d.pop("awards", UNSET)
        for awards_item_data in _awards or []:
            awards_item = SourcingAward.from_dict(awards_item_data)

            awards.append(awards_item)

        _questionnaire = d.pop("questionnaire", UNSET)
        questionnaire: Union[Unset, SourcingQuestionnaire]
        if isinstance(_questionnaire, Unset):
            questionnaire = UNSET
        else:
            questionnaire = SourcingQuestionnaire.from_dict(_questionnaire)

        _scoring = d.pop("scoring", UNSET)
        scoring: Union[Unset, BuyerSourcingEventViewScoring]
        if isinstance(_scoring, Unset):
            scoring = UNSET
        else:
            scoring = BuyerSourcingEventViewScoring.from_dict(_scoring)

        _manual_points = d.pop("manualPoints", UNSET)
        manual_points: Union[Unset, SourcingManualPoints]
        if isinstance(_manual_points, Unset):
            manual_points = UNSET
        else:
            manual_points = SourcingManualPoints.from_dict(_manual_points)

        _assistant_read = d.pop("assistantRead", UNSET)
        assistant_read: Union[Unset, SourcingAssistantRead]
        if isinstance(_assistant_read, Unset):
            assistant_read = UNSET
        else:
            assistant_read = SourcingAssistantRead.from_dict(_assistant_read)

        round_ = d.pop("round", UNSET)

        rounds = []
        _rounds = d.pop("rounds", UNSET)
        for rounds_item_data in _rounds or []:
            rounds_item = SourcingRound.from_dict(rounds_item_data)

            rounds.append(rounds_item)

        criteria = []
        _criteria = d.pop("criteria", UNSET)
        for criteria_item_data in _criteria or []:
            criteria_item = SourcingCriterion.from_dict(criteria_item_data)

            criteria.append(criteria_item)

        evaluators = cast(List[str], d.pop("evaluators", UNSET))

        created_by = d.pop("createdBy", UNSET)

        created_by_name = d.pop("createdByName", UNSET)

        created_at = d.pop("createdAt", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        published_at = d.pop("publishedAt", UNSET)

        closed_at = d.pop("closedAt", UNSET)

        canceled_at = d.pop("canceledAt", UNSET)

        version = d.pop("version", UNSET)

        invitees = []
        _invitees = d.pop("invitees", UNSET)
        for invitees_item_data in _invitees or []:
            invitees_item = BuyerSourcingInviteeView.from_dict(invitees_item_data)

            invitees.append(invitees_item)

        _answers = d.pop("answers", UNSET)
        answers: Union[Unset, SourcingAnswerCounts]
        if isinstance(_answers, Unset):
            answers = UNSET
        else:
            answers = SourcingAnswerCounts.from_dict(_answers)

        responses = []
        _responses = d.pop("responses", UNSET)
        for responses_item_data in _responses or []:
            responses_item = BuyerSourcingResponseView.from_dict(responses_item_data)

            responses.append(responses_item)

        questions = []
        _questions = d.pop("questions", UNSET)
        for questions_item_data in _questions or []:
            questions_item = BuyerSourcingQuestionView.from_dict(questions_item_data)

            questions.append(questions_item)

        activity = []
        _activity = d.pop("activity", UNSET)
        for activity_item_data in _activity or []:
            activity_item = SourcingActivity.from_dict(activity_item_data)

            activity.append(activity_item)

        buyer_sourcing_event_view = cls(
            id=id,
            title=title,
            description=description,
            status=status,
            currency=currency,
            due_at=due_at,
            sealed=sealed,
            sealed_now=sealed_now,
            lines=lines,
            attachments=attachments,
            from_request_id=from_request_id,
            cost_center=cost_center,
            gl_code=gl_code,
            award=award,
            awards=awards,
            questionnaire=questionnaire,
            scoring=scoring,
            manual_points=manual_points,
            assistant_read=assistant_read,
            round_=round_,
            rounds=rounds,
            criteria=criteria,
            evaluators=evaluators,
            created_by=created_by,
            created_by_name=created_by_name,
            created_at=created_at,
            updated_at=updated_at,
            published_at=published_at,
            closed_at=closed_at,
            canceled_at=canceled_at,
            version=version,
            invitees=invitees,
            answers=answers,
            responses=responses,
            questions=questions,
            activity=activity,
        )

        buyer_sourcing_event_view.additional_properties = d
        return buyer_sourcing_event_view

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
