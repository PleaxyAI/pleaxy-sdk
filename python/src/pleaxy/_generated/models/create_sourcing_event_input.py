from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sourcing_line_input import SourcingLineInput


T = TypeVar("T", bound="CreateSourcingEventInput")


@_attrs_define
class CreateSourcingEventInput:
    """
    Attributes:
        from_request_id (Union[Unset, str]): An approved purchase request with no order: its lines, cost center, GL
            account, needed-by and files are copied, and it moves to `sourcing`.
        title (Union[Unset, str]): 1–200 characters. From a request: the request's title unless given.
        description (Union[Unset, str]): What the suppliers are asked for, up to 5,000 characters.
        currency (Union[Unset, str]): ISO 4217: the currency suppliers answer in. Default: the request's, else the
            workspace's.
        due_at (Union[Unset, str]): The answer deadline, an ISO timestamp; it must be in the future when the RFQ is
            sent. Default: 7 days from now.
        sealed (Union[Unset, bool]): Sealed (the default): until it closes, the buyer sees who answered and when, never
            prices or files.
        lines (Union[Unset, List['SourcingLineInput']]): From a request: the request's lines unless given.
        cost_center (Union[Unset, str]):
        gl_code (Union[Unset, str]):
    """

    from_request_id: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    due_at: Union[Unset, str] = UNSET
    sealed: Union[Unset, bool] = UNSET
    lines: Union[Unset, List["SourcingLineInput"]] = UNSET
    cost_center: Union[Unset, str] = UNSET
    gl_code: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from_request_id = self.from_request_id

        title = self.title

        description = self.description

        currency = self.currency

        due_at = self.due_at

        sealed = self.sealed

        lines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        cost_center = self.cost_center

        gl_code = self.gl_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_request_id is not UNSET:
            field_dict["fromRequestId"] = from_request_id
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if currency is not UNSET:
            field_dict["currency"] = currency
        if due_at is not UNSET:
            field_dict["dueAt"] = due_at
        if sealed is not UNSET:
            field_dict["sealed"] = sealed
        if lines is not UNSET:
            field_dict["lines"] = lines
        if cost_center is not UNSET:
            field_dict["costCenter"] = cost_center
        if gl_code is not UNSET:
            field_dict["glCode"] = gl_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sourcing_line_input import SourcingLineInput

        d = src_dict.copy()
        from_request_id = d.pop("fromRequestId", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        currency = d.pop("currency", UNSET)

        due_at = d.pop("dueAt", UNSET)

        sealed = d.pop("sealed", UNSET)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = SourcingLineInput.from_dict(lines_item_data)

            lines.append(lines_item)

        cost_center = d.pop("costCenter", UNSET)

        gl_code = d.pop("glCode", UNSET)

        create_sourcing_event_input = cls(
            from_request_id=from_request_id,
            title=title,
            description=description,
            currency=currency,
            due_at=due_at,
            sealed=sealed,
            lines=lines,
            cost_center=cost_center,
            gl_code=gl_code,
        )

        create_sourcing_event_input.additional_properties = d
        return create_sourcing_event_input

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
