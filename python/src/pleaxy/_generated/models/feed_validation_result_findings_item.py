from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.feed_validation_result_findings_item_code import (
    FeedValidationResultFindingsItemCode,
    check_feed_validation_result_findings_item_code,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="FeedValidationResultFindingsItem")


@_attrs_define
class FeedValidationResultFindingsItem:
    """
    Attributes:
        contract_id (Union[Unset, str]):
        code (Union[Unset, FeedValidationResultFindingsItemCode]):
        message (Union[Unset, str]):
        invoice_line (Union[Unset, float]):
        po_line_no (Union[Unset, float]):
    """

    contract_id: Union[Unset, str] = UNSET
    code: Union[Unset, FeedValidationResultFindingsItemCode] = UNSET
    message: Union[Unset, str] = UNSET
    invoice_line: Union[Unset, float] = UNSET
    po_line_no: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contract_id = self.contract_id

        code: Union[Unset, str] = UNSET
        if not isinstance(self.code, Unset):
            code = self.code

        message = self.message

        invoice_line = self.invoice_line

        po_line_no = self.po_line_no

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contract_id is not UNSET:
            field_dict["contractId"] = contract_id
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message
        if invoice_line is not UNSET:
            field_dict["invoiceLine"] = invoice_line
        if po_line_no is not UNSET:
            field_dict["poLineNo"] = po_line_no

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        contract_id = d.pop("contractId", UNSET)

        _code = d.pop("code", UNSET)
        code: Union[Unset, FeedValidationResultFindingsItemCode]
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = check_feed_validation_result_findings_item_code(_code)

        message = d.pop("message", UNSET)

        invoice_line = d.pop("invoiceLine", UNSET)

        po_line_no = d.pop("poLineNo", UNSET)

        feed_validation_result_findings_item = cls(
            contract_id=contract_id,
            code=code,
            message=message,
            invoice_line=invoice_line,
            po_line_no=po_line_no,
        )

        feed_validation_result_findings_item.additional_properties = d
        return feed_validation_result_findings_item

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
