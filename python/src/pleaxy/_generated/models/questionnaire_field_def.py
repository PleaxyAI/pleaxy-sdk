from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.questionnaire_field_def_doc_type import (
    QuestionnaireFieldDefDocType,
    check_questionnaire_field_def_doc_type,
)
from ..models.questionnaire_field_def_kind import (
    QuestionnaireFieldDefKind,
    check_questionnaire_field_def_kind,
)
from ..models.questionnaire_field_def_type import (
    QuestionnaireFieldDefType,
    check_questionnaire_field_def_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.question_condition import QuestionCondition
    from ..models.question_option import QuestionOption


T = TypeVar("T", bound="QuestionnaireFieldDef")


@_attrs_define
class QuestionnaireFieldDef:
    """
    Attributes:
        id (str):
        kind (Union[Unset, QuestionnaireFieldDefKind]):
        doc_type (Union[Unset, QuestionnaireFieldDefDocType]):
        label (Union[Unset, str]):
        required (Union[Unset, bool]):
        help_text (Union[Unset, str]):
        type (Union[Unset, QuestionnaireFieldDefType]):
        options (Union[Unset, List['QuestionOption']]):
        show_if (Union[Unset, QuestionCondition]):
        section (Union[Unset, str]):
        flag_if (Union[Unset, List[str]]):
    """

    id: str
    kind: Union[Unset, QuestionnaireFieldDefKind] = UNSET
    doc_type: Union[Unset, QuestionnaireFieldDefDocType] = UNSET
    label: Union[Unset, str] = UNSET
    required: Union[Unset, bool] = UNSET
    help_text: Union[Unset, str] = UNSET
    type: Union[Unset, QuestionnaireFieldDefType] = UNSET
    options: Union[Unset, List["QuestionOption"]] = UNSET
    show_if: Union[Unset, "QuestionCondition"] = UNSET
    section: Union[Unset, str] = UNSET
    flag_if: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        doc_type: Union[Unset, str] = UNSET
        if not isinstance(self.doc_type, Unset):
            doc_type = self.doc_type

        label = self.label

        required = self.required

        help_text = self.help_text

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type

        options: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        show_if: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.show_if, Unset):
            show_if = self.show_if.to_dict()

        section = self.section

        flag_if: Union[Unset, List[str]] = UNSET
        if not isinstance(self.flag_if, Unset):
            flag_if = self.flag_if

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if doc_type is not UNSET:
            field_dict["docType"] = doc_type
        if label is not UNSET:
            field_dict["label"] = label
        if required is not UNSET:
            field_dict["required"] = required
        if help_text is not UNSET:
            field_dict["helpText"] = help_text
        if type is not UNSET:
            field_dict["type"] = type
        if options is not UNSET:
            field_dict["options"] = options
        if show_if is not UNSET:
            field_dict["showIf"] = show_if
        if section is not UNSET:
            field_dict["section"] = section
        if flag_if is not UNSET:
            field_dict["flagIf"] = flag_if

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.question_condition import QuestionCondition
        from ..models.question_option import QuestionOption

        d = src_dict.copy()
        id = d.pop("id")

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, QuestionnaireFieldDefKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_questionnaire_field_def_kind(_kind)

        _doc_type = d.pop("docType", UNSET)
        doc_type: Union[Unset, QuestionnaireFieldDefDocType]
        if isinstance(_doc_type, Unset):
            doc_type = UNSET
        else:
            doc_type = check_questionnaire_field_def_doc_type(_doc_type)

        label = d.pop("label", UNSET)

        required = d.pop("required", UNSET)

        help_text = d.pop("helpText", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, QuestionnaireFieldDefType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = check_questionnaire_field_def_type(_type)

        options = []
        _options = d.pop("options", UNSET)
        for options_item_data in _options or []:
            options_item = QuestionOption.from_dict(options_item_data)

            options.append(options_item)

        _show_if = d.pop("showIf", UNSET)
        show_if: Union[Unset, QuestionCondition]
        if isinstance(_show_if, Unset):
            show_if = UNSET
        else:
            show_if = QuestionCondition.from_dict(_show_if)

        section = d.pop("section", UNSET)

        flag_if = cast(List[str], d.pop("flagIf", UNSET))

        questionnaire_field_def = cls(
            id=id,
            kind=kind,
            doc_type=doc_type,
            label=label,
            required=required,
            help_text=help_text,
            type=type,
            options=options,
            show_if=show_if,
            section=section,
            flag_if=flag_if,
        )

        questionnaire_field_def.additional_properties = d
        return questionnaire_field_def

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
