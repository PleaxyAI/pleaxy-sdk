from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sourcing_comparison_field_scoring import (
    SourcingComparisonFieldScoring,
    check_sourcing_comparison_field_scoring,
)
from ..models.sourcing_comparison_field_type import (
    SourcingComparisonFieldType,
    check_sourcing_comparison_field_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.question_option import QuestionOption
    from ..models.sourcing_comparison_answer import SourcingComparisonAnswer
    from ..models.sourcing_comparison_field_option_points import (
        SourcingComparisonFieldOptionPoints,
    )


T = TypeVar("T", bound="SourcingComparisonField")


@_attrs_define
class SourcingComparisonField:
    """
    Attributes:
        field_id (Union[Unset, str]):
        label (Union[Unset, str]):
        type (Union[Unset, SourcingComparisonFieldType]):
        section (Union[Unset, str]):
        options (Union[Unset, List['QuestionOption']]):
        weight (Union[Unset, float]):
        scoring (Union[Unset, SourcingComparisonFieldScoring]):
        option_points (Union[Unset, SourcingComparisonFieldOptionPoints]):
        answers (Union[Unset, List['SourcingComparisonAnswer']]):
    """

    field_id: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    type: Union[Unset, SourcingComparisonFieldType] = UNSET
    section: Union[Unset, str] = UNSET
    options: Union[Unset, List["QuestionOption"]] = UNSET
    weight: Union[Unset, float] = UNSET
    scoring: Union[Unset, SourcingComparisonFieldScoring] = UNSET
    option_points: Union[Unset, "SourcingComparisonFieldOptionPoints"] = UNSET
    answers: Union[Unset, List["SourcingComparisonAnswer"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_id = self.field_id

        label = self.label

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type

        section = self.section

        options: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        weight = self.weight

        scoring: Union[Unset, str] = UNSET
        if not isinstance(self.scoring, Unset):
            scoring = self.scoring

        option_points: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.option_points, Unset):
            option_points = self.option_points.to_dict()

        answers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.answers, Unset):
            answers = []
            for answers_item_data in self.answers:
                answers_item = answers_item_data.to_dict()
                answers.append(answers_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_id is not UNSET:
            field_dict["fieldId"] = field_id
        if label is not UNSET:
            field_dict["label"] = label
        if type is not UNSET:
            field_dict["type"] = type
        if section is not UNSET:
            field_dict["section"] = section
        if options is not UNSET:
            field_dict["options"] = options
        if weight is not UNSET:
            field_dict["weight"] = weight
        if scoring is not UNSET:
            field_dict["scoring"] = scoring
        if option_points is not UNSET:
            field_dict["optionPoints"] = option_points
        if answers is not UNSET:
            field_dict["answers"] = answers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.question_option import QuestionOption
        from ..models.sourcing_comparison_answer import SourcingComparisonAnswer
        from ..models.sourcing_comparison_field_option_points import (
            SourcingComparisonFieldOptionPoints,
        )

        d = src_dict.copy()
        field_id = d.pop("fieldId", UNSET)

        label = d.pop("label", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, SourcingComparisonFieldType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = check_sourcing_comparison_field_type(_type)

        section = d.pop("section", UNSET)

        options = []
        _options = d.pop("options", UNSET)
        for options_item_data in _options or []:
            options_item = QuestionOption.from_dict(options_item_data)

            options.append(options_item)

        weight = d.pop("weight", UNSET)

        _scoring = d.pop("scoring", UNSET)
        scoring: Union[Unset, SourcingComparisonFieldScoring]
        if isinstance(_scoring, Unset):
            scoring = UNSET
        else:
            scoring = check_sourcing_comparison_field_scoring(_scoring)

        _option_points = d.pop("optionPoints", UNSET)
        option_points: Union[Unset, SourcingComparisonFieldOptionPoints]
        if isinstance(_option_points, Unset):
            option_points = UNSET
        else:
            option_points = SourcingComparisonFieldOptionPoints.from_dict(
                _option_points
            )

        answers = []
        _answers = d.pop("answers", UNSET)
        for answers_item_data in _answers or []:
            answers_item = SourcingComparisonAnswer.from_dict(answers_item_data)

            answers.append(answers_item)

        sourcing_comparison_field = cls(
            field_id=field_id,
            label=label,
            type=type,
            section=section,
            options=options,
            weight=weight,
            scoring=scoring,
            option_points=option_points,
            answers=answers,
        )

        sourcing_comparison_field.additional_properties = d
        return sourcing_comparison_field

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
