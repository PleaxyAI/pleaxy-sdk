from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.questionnaire_field_def import QuestionnaireFieldDef


T = TypeVar("T", bound="SourcingQuestionnaire")


@_attrs_define
class SourcingQuestionnaire:
    """
    Attributes:
        template_id (Union[Unset, str]):
        version (Union[Unset, float]):
        name (Union[Unset, str]):
        fields (Union[Unset, List['QuestionnaireFieldDef']]):
    """

    template_id: Union[Unset, str] = UNSET
    version: Union[Unset, float] = UNSET
    name: Union[Unset, str] = UNSET
    fields: Union[Unset, List["QuestionnaireFieldDef"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        template_id = self.template_id

        version = self.version

        name = self.name

        fields: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if template_id is not UNSET:
            field_dict["templateId"] = template_id
        if version is not UNSET:
            field_dict["version"] = version
        if name is not UNSET:
            field_dict["name"] = name
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.questionnaire_field_def import QuestionnaireFieldDef

        d = src_dict.copy()
        template_id = d.pop("templateId", UNSET)

        version = d.pop("version", UNSET)

        name = d.pop("name", UNSET)

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = QuestionnaireFieldDef.from_dict(fields_item_data)

            fields.append(fields_item)

        sourcing_questionnaire = cls(
            template_id=template_id,
            version=version,
            name=name,
            fields=fields,
        )

        sourcing_questionnaire.additional_properties = d
        return sourcing_questionnaire

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
