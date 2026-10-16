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

if TYPE_CHECKING:
    from ..models.server_message import ServerMessage


T = TypeVar("T", bound="ServerMessageParams")


@_attrs_define
class ServerMessageParams:
    """ """

    additional_properties: Dict[str, Union["ServerMessage", bool, float, str]] = (
        _attrs_field(init=False, factory=dict)
    )

    def to_dict(self) -> Dict[str, Any]:
        from ..models.server_message import ServerMessage

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, ServerMessage):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.server_message import ServerMessage

        d = src_dict.copy()
        server_message_params = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(
                data: object,
            ) -> Union["ServerMessage", bool, float, str]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_3 = ServerMessage.from_dict(data)

                    return additional_property_type_3
                except:  # noqa: E722
                    pass
                return cast(Union["ServerMessage", bool, float, str], data)

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        server_message_params.additional_properties = additional_properties
        return server_message_params

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Union["ServerMessage", bool, float, str]:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: Union["ServerMessage", bool, float, str]
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
