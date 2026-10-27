from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.supplier_remittance_view_file import SupplierRemittanceViewFile


T = TypeVar("T", bound="SupplierRemittanceView")


@_attrs_define
class SupplierRemittanceView:
    """
    Attributes:
        id (str):
        note (Union[Unset, str]):
        sent_at (Union[Unset, str]):
        file (Union[Unset, SupplierRemittanceViewFile]):
    """

    id: str
    note: Union[Unset, str] = UNSET
    sent_at: Union[Unset, str] = UNSET
    file: Union[Unset, "SupplierRemittanceViewFile"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        note = self.note

        sent_at = self.sent_at

        file: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if note is not UNSET:
            field_dict["note"] = note
        if sent_at is not UNSET:
            field_dict["sentAt"] = sent_at
        if file is not UNSET:
            field_dict["file"] = file

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.supplier_remittance_view_file import SupplierRemittanceViewFile

        d = src_dict.copy()
        id = d.pop("id")

        note = d.pop("note", UNSET)

        sent_at = d.pop("sentAt", UNSET)

        _file = d.pop("file", UNSET)
        file: Union[Unset, SupplierRemittanceViewFile]
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = SupplierRemittanceViewFile.from_dict(_file)

        supplier_remittance_view = cls(
            id=id,
            note=note,
            sent_at=sent_at,
            file=file,
        )

        supplier_remittance_view.additional_properties = d
        return supplier_remittance_view

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
