from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.remittance_file_input import RemittanceFileInput


T = TypeVar("T", bound="SendRemittanceInput")


@_attrs_define
class SendRemittanceInput:
    """
    Attributes:
        note (Union[Unset, str]):
        file (Union[Unset, RemittanceFileInput]):
    """

    note: Union[Unset, str] = UNSET
    file: Union[Unset, "RemittanceFileInput"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        note = self.note

        file: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if note is not UNSET:
            field_dict["note"] = note
        if file is not UNSET:
            field_dict["file"] = file

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.remittance_file_input import RemittanceFileInput

        d = src_dict.copy()
        note = d.pop("note", UNSET)

        _file = d.pop("file", UNSET)
        file: Union[Unset, RemittanceFileInput]
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = RemittanceFileInput.from_dict(_file)

        send_remittance_input = cls(
            note=note,
            file=file,
        )

        send_remittance_input.additional_properties = d
        return send_remittance_input

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
