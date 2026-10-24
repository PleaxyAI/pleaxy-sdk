from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.inbound_email_draft_confirmation_operation import (
    InboundEmailDraftConfirmationOperation,
    check_inbound_email_draft_confirmation_operation,
)
from ..models.inbound_email_draft_confirmation_type import (
    InboundEmailDraftConfirmationType,
    check_inbound_email_draft_confirmation_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inbound_email_draft_confirmation_lines_item import (
        InboundEmailDraftConfirmationLinesItem,
    )


T = TypeVar("T", bound="InboundEmailDraftConfirmation")


@_attrs_define
class InboundEmailDraftConfirmation:
    """
    Attributes:
        type (Union[Unset, InboundEmailDraftConfirmationType]):
        confirm_id (Union[Unset, str]):
        operation (Union[Unset, InboundEmailDraftConfirmationOperation]):
        delivery_date (Union[Unset, str]):
        note (Union[Unset, str]):
        lines (Union[Unset, List['InboundEmailDraftConfirmationLinesItem']]):
    """

    type: Union[Unset, InboundEmailDraftConfirmationType] = UNSET
    confirm_id: Union[Unset, str] = UNSET
    operation: Union[Unset, InboundEmailDraftConfirmationOperation] = UNSET
    delivery_date: Union[Unset, str] = UNSET
    note: Union[Unset, str] = UNSET
    lines: Union[Unset, List["InboundEmailDraftConfirmationLinesItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type

        confirm_id = self.confirm_id

        operation: Union[Unset, str] = UNSET
        if not isinstance(self.operation, Unset):
            operation = self.operation

        delivery_date = self.delivery_date

        note = self.note

        lines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if confirm_id is not UNSET:
            field_dict["confirmId"] = confirm_id
        if operation is not UNSET:
            field_dict["operation"] = operation
        if delivery_date is not UNSET:
            field_dict["deliveryDate"] = delivery_date
        if note is not UNSET:
            field_dict["note"] = note
        if lines is not UNSET:
            field_dict["lines"] = lines

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.inbound_email_draft_confirmation_lines_item import (
            InboundEmailDraftConfirmationLinesItem,
        )

        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, InboundEmailDraftConfirmationType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = check_inbound_email_draft_confirmation_type(_type)

        confirm_id = d.pop("confirmId", UNSET)

        _operation = d.pop("operation", UNSET)
        operation: Union[Unset, InboundEmailDraftConfirmationOperation]
        if isinstance(_operation, Unset):
            operation = UNSET
        else:
            operation = check_inbound_email_draft_confirmation_operation(_operation)

        delivery_date = d.pop("deliveryDate", UNSET)

        note = d.pop("note", UNSET)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = InboundEmailDraftConfirmationLinesItem.from_dict(
                lines_item_data
            )

            lines.append(lines_item)

        inbound_email_draft_confirmation = cls(
            type=type,
            confirm_id=confirm_id,
            operation=operation,
            delivery_date=delivery_date,
            note=note,
            lines=lines,
        )

        inbound_email_draft_confirmation.additional_properties = d
        return inbound_email_draft_confirmation

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
