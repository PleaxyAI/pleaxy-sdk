from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bank_check_method import BankCheckMethod, check_bank_check_method
from ..types import UNSET, Unset

T = TypeVar("T", bound="BankCheck")


@_attrs_define
class BankCheck:
    """
    Attributes:
        method (Union[Unset, BankCheckMethod]):
        detail (Union[Unset, str]):
        note (Union[Unset, str]):
    """

    method: Union[Unset, BankCheckMethod] = UNSET
    detail: Union[Unset, str] = UNSET
    note: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        method: Union[Unset, str] = UNSET
        if not isinstance(self.method, Unset):
            method = self.method

        detail = self.detail

        note = self.note

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if method is not UNSET:
            field_dict["method"] = method
        if detail is not UNSET:
            field_dict["detail"] = detail
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _method = d.pop("method", UNSET)
        method: Union[Unset, BankCheckMethod]
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = check_bank_check_method(_method)

        detail = d.pop("detail", UNSET)

        note = d.pop("note", UNSET)

        bank_check = cls(
            method=method,
            detail=detail,
            note=note,
        )

        bank_check.additional_properties = d
        return bank_check

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
