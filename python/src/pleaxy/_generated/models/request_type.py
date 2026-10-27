from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.questionnaire_field_def import QuestionnaireFieldDef
    from ..models.request_type_defaults import RequestTypeDefaults


T = TypeVar("T", bound="RequestType")


@_attrs_define
class RequestType:
    """
    Attributes:
        id (str):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        active (Union[Unset, bool]):
        order (Union[Unset, float]):
        defaults (Union[Unset, RequestTypeDefaults]):
        fields (Union[Unset, List['QuestionnaireFieldDef']]):
        version (Union[Unset, float]):
        used_at (Union[Unset, str]):
        created_at (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        updated_by (Union[Unset, str]):
    """

    id: str
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    active: Union[Unset, bool] = UNSET
    order: Union[Unset, float] = UNSET
    defaults: Union[Unset, "RequestTypeDefaults"] = UNSET
    fields: Union[Unset, List["QuestionnaireFieldDef"]] = UNSET
    version: Union[Unset, float] = UNSET
    used_at: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    updated_by: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        active = self.active

        order = self.order

        defaults: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.defaults, Unset):
            defaults = self.defaults.to_dict()

        fields: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)

        version = self.version

        used_at = self.used_at

        created_at = self.created_at

        updated_at = self.updated_at

        updated_by = self.updated_by

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if active is not UNSET:
            field_dict["active"] = active
        if order is not UNSET:
            field_dict["order"] = order
        if defaults is not UNSET:
            field_dict["defaults"] = defaults
        if fields is not UNSET:
            field_dict["fields"] = fields
        if version is not UNSET:
            field_dict["version"] = version
        if used_at is not UNSET:
            field_dict["usedAt"] = used_at
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if updated_by is not UNSET:
            field_dict["updatedBy"] = updated_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.questionnaire_field_def import QuestionnaireFieldDef
        from ..models.request_type_defaults import RequestTypeDefaults

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        active = d.pop("active", UNSET)

        order = d.pop("order", UNSET)

        _defaults = d.pop("defaults", UNSET)
        defaults: Union[Unset, RequestTypeDefaults]
        if isinstance(_defaults, Unset):
            defaults = UNSET
        else:
            defaults = RequestTypeDefaults.from_dict(_defaults)

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = QuestionnaireFieldDef.from_dict(fields_item_data)

            fields.append(fields_item)

        version = d.pop("version", UNSET)

        used_at = d.pop("usedAt", UNSET)

        created_at = d.pop("createdAt", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        updated_by = d.pop("updatedBy", UNSET)

        request_type = cls(
            id=id,
            name=name,
            description=description,
            active=active,
            order=order,
            defaults=defaults,
            fields=fields,
            version=version,
            used_at=used_at,
            created_at=created_at,
            updated_at=updated_at,
            updated_by=updated_by,
        )

        request_type.additional_properties = d
        return request_type

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
