from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_remittance_file import InvoiceRemittanceFile


T = TypeVar("T", bound="InvoiceRemittance")


@_attrs_define
class InvoiceRemittance:
    """
    Attributes:
        id (str):
        sent_at (Union[Unset, str]):
        sent_by (Union[Unset, str]):
        sent_by_name (Union[Unset, str]):
        note (Union[Unset, str]):
        file (Union[Unset, InvoiceRemittanceFile]):
    """

    id: str
    sent_at: Union[Unset, str] = UNSET
    sent_by: Union[Unset, str] = UNSET
    sent_by_name: Union[Unset, str] = UNSET
    note: Union[Unset, str] = UNSET
    file: Union[Unset, "InvoiceRemittanceFile"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        sent_at = self.sent_at

        sent_by = self.sent_by

        sent_by_name = self.sent_by_name

        note = self.note

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
        if sent_at is not UNSET:
            field_dict["sentAt"] = sent_at
        if sent_by is not UNSET:
            field_dict["sentBy"] = sent_by
        if sent_by_name is not UNSET:
            field_dict["sentByName"] = sent_by_name
        if note is not UNSET:
            field_dict["note"] = note
        if file is not UNSET:
            field_dict["file"] = file

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_remittance_file import InvoiceRemittanceFile

        d = src_dict.copy()
        id = d.pop("id")

        sent_at = d.pop("sentAt", UNSET)

        sent_by = d.pop("sentBy", UNSET)

        sent_by_name = d.pop("sentByName", UNSET)

        note = d.pop("note", UNSET)

        _file = d.pop("file", UNSET)
        file: Union[Unset, InvoiceRemittanceFile]
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = InvoiceRemittanceFile.from_dict(_file)

        invoice_remittance = cls(
            id=id,
            sent_at=sent_at,
            sent_by=sent_by,
            sent_by_name=sent_by_name,
            note=note,
            file=file,
        )

        invoice_remittance.additional_properties = d
        return invoice_remittance

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
