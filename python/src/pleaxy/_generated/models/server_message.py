from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_message_params import ServerMessageParams


T = TypeVar("T", bound="ServerMessage")


@_attrs_define
class ServerMessage:
    """
    Attributes:
        message_id (Union[Unset, str]):
        params (Union[Unset, ServerMessageParams]):
    """

    message_id: Union[Unset, str] = UNSET
    params: Union[Unset, "ServerMessageParams"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message_id = self.message_id

        params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.server_message_params import ServerMessageParams

        d = src_dict.copy()
        message_id = d.pop("messageId", UNSET)

        _params = d.pop("params", UNSET)
        params: Union[Unset, ServerMessageParams]
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = ServerMessageParams.from_dict(_params)

        server_message = cls(
            message_id=message_id,
            params=params,
        )

        server_message.additional_properties = d
        return server_message

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
