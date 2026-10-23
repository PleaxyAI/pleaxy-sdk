from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.receipt_return_want import ReceiptReturnWant, check_receipt_return_want
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.receipt_attachment import ReceiptAttachment
    from ..models.receipt_line import ReceiptLine


T = TypeVar("T", bound="ReceiptReturn")


@_attrs_define
class ReceiptReturn:
    """
    Attributes:
        id (str):
        lines (Union[Unset, List['ReceiptLine']]):
        amount (Union[Unset, float]):
        returned_at (Union[Unset, str]):
        reason (Union[Unset, str]):
        want (Union[Unset, ReceiptReturnWant]):
        attachment (Union[Unset, ReceiptAttachment]):
        by (Union[Unset, str]):
        by_name (Union[Unset, str]):
        at (Union[Unset, str]):
    """

    id: str
    lines: Union[Unset, List["ReceiptLine"]] = UNSET
    amount: Union[Unset, float] = UNSET
    returned_at: Union[Unset, str] = UNSET
    reason: Union[Unset, str] = UNSET
    want: Union[Unset, ReceiptReturnWant] = UNSET
    attachment: Union[Unset, "ReceiptAttachment"] = UNSET
    by: Union[Unset, str] = UNSET
    by_name: Union[Unset, str] = UNSET
    at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        lines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        amount = self.amount

        returned_at = self.returned_at

        reason = self.reason

        want: Union[Unset, str] = UNSET
        if not isinstance(self.want, Unset):
            want = self.want

        attachment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachment, Unset):
            attachment = self.attachment.to_dict()

        by = self.by

        by_name = self.by_name

        at = self.at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if lines is not UNSET:
            field_dict["lines"] = lines
        if amount is not UNSET:
            field_dict["amount"] = amount
        if returned_at is not UNSET:
            field_dict["returnedAt"] = returned_at
        if reason is not UNSET:
            field_dict["reason"] = reason
        if want is not UNSET:
            field_dict["want"] = want
        if attachment is not UNSET:
            field_dict["attachment"] = attachment
        if by is not UNSET:
            field_dict["by"] = by
        if by_name is not UNSET:
            field_dict["byName"] = by_name
        if at is not UNSET:
            field_dict["at"] = at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.receipt_attachment import ReceiptAttachment
        from ..models.receipt_line import ReceiptLine

        d = src_dict.copy()
        id = d.pop("id")

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = ReceiptLine.from_dict(lines_item_data)

            lines.append(lines_item)

        amount = d.pop("amount", UNSET)

        returned_at = d.pop("returnedAt", UNSET)

        reason = d.pop("reason", UNSET)

        _want = d.pop("want", UNSET)
        want: Union[Unset, ReceiptReturnWant]
        if isinstance(_want, Unset):
            want = UNSET
        else:
            want = check_receipt_return_want(_want)

        _attachment = d.pop("attachment", UNSET)
        attachment: Union[Unset, ReceiptAttachment]
        if isinstance(_attachment, Unset):
            attachment = UNSET
        else:
            attachment = ReceiptAttachment.from_dict(_attachment)

        by = d.pop("by", UNSET)

        by_name = d.pop("byName", UNSET)

        at = d.pop("at", UNSET)

        receipt_return = cls(
            id=id,
            lines=lines,
            amount=amount,
            returned_at=returned_at,
            reason=reason,
            want=want,
            attachment=attachment,
            by=by,
            by_name=by_name,
            at=at,
        )

        receipt_return.additional_properties = d
        return receipt_return

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
