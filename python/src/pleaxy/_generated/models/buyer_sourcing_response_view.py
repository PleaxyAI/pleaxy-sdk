from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.buyer_sourcing_response_view_answered_via import (
    BuyerSourcingResponseViewAnsweredVia,
    check_buyer_sourcing_response_view_answered_via,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sourcing_attachment import SourcingAttachment
    from ..models.sourcing_question_answer import SourcingQuestionAnswer
    from ..models.sourcing_response_line import SourcingResponseLine


T = TypeVar("T", bound="BuyerSourcingResponseView")


@_attrs_define
class BuyerSourcingResponseView:
    """
    Attributes:
        supplier_key (Union[Unset, str]):
        supplier_name (Union[Unset, str]):
        lines (Union[Unset, List['SourcingResponseLine']]):
        valid_until (Union[Unset, str]):
        payment_terms_days (Union[Unset, float]):
        reference (Union[Unset, str]):
        note (Union[Unset, str]):
        attachments (Union[Unset, List['SourcingAttachment']]):
        quote_import_id (Union[Unset, str]):
        submitted_at (Union[Unset, str]):
        version (Union[Unset, float]):
        total (Union[None, Unset, float]):
        answers (Union[Unset, List['SourcingQuestionAnswer']]):
        answered_via (Union[Unset, BuyerSourcingResponseViewAnsweredVia]):
        answered_by_email (Union[Unset, str]):
        carried_from (Union[Unset, float]):
    """

    supplier_key: Union[Unset, str] = UNSET
    supplier_name: Union[Unset, str] = UNSET
    lines: Union[Unset, List["SourcingResponseLine"]] = UNSET
    valid_until: Union[Unset, str] = UNSET
    payment_terms_days: Union[Unset, float] = UNSET
    reference: Union[Unset, str] = UNSET
    note: Union[Unset, str] = UNSET
    attachments: Union[Unset, List["SourcingAttachment"]] = UNSET
    quote_import_id: Union[Unset, str] = UNSET
    submitted_at: Union[Unset, str] = UNSET
    version: Union[Unset, float] = UNSET
    total: Union[None, Unset, float] = UNSET
    answers: Union[Unset, List["SourcingQuestionAnswer"]] = UNSET
    answered_via: Union[Unset, BuyerSourcingResponseViewAnsweredVia] = UNSET
    answered_by_email: Union[Unset, str] = UNSET
    carried_from: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        supplier_key = self.supplier_key

        supplier_name = self.supplier_name

        lines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        valid_until = self.valid_until

        payment_terms_days = self.payment_terms_days

        reference = self.reference

        note = self.note

        attachments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)

        quote_import_id = self.quote_import_id

        submitted_at = self.submitted_at

        version = self.version

        total: Union[None, Unset, float]
        if isinstance(self.total, Unset):
            total = UNSET
        else:
            total = self.total

        answers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.answers, Unset):
            answers = []
            for answers_item_data in self.answers:
                answers_item = answers_item_data.to_dict()
                answers.append(answers_item)

        answered_via: Union[Unset, str] = UNSET
        if not isinstance(self.answered_via, Unset):
            answered_via = self.answered_via

        answered_by_email = self.answered_by_email

        carried_from = self.carried_from

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if supplier_key is not UNSET:
            field_dict["supplierKey"] = supplier_key
        if supplier_name is not UNSET:
            field_dict["supplierName"] = supplier_name
        if lines is not UNSET:
            field_dict["lines"] = lines
        if valid_until is not UNSET:
            field_dict["validUntil"] = valid_until
        if payment_terms_days is not UNSET:
            field_dict["paymentTermsDays"] = payment_terms_days
        if reference is not UNSET:
            field_dict["reference"] = reference
        if note is not UNSET:
            field_dict["note"] = note
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if quote_import_id is not UNSET:
            field_dict["quoteImportId"] = quote_import_id
        if submitted_at is not UNSET:
            field_dict["submittedAt"] = submitted_at
        if version is not UNSET:
            field_dict["version"] = version
        if total is not UNSET:
            field_dict["total"] = total
        if answers is not UNSET:
            field_dict["answers"] = answers
        if answered_via is not UNSET:
            field_dict["answeredVia"] = answered_via
        if answered_by_email is not UNSET:
            field_dict["answeredByEmail"] = answered_by_email
        if carried_from is not UNSET:
            field_dict["carriedFrom"] = carried_from

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sourcing_attachment import SourcingAttachment
        from ..models.sourcing_question_answer import SourcingQuestionAnswer
        from ..models.sourcing_response_line import SourcingResponseLine

        d = src_dict.copy()
        supplier_key = d.pop("supplierKey", UNSET)

        supplier_name = d.pop("supplierName", UNSET)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = SourcingResponseLine.from_dict(lines_item_data)

            lines.append(lines_item)

        valid_until = d.pop("validUntil", UNSET)

        payment_terms_days = d.pop("paymentTermsDays", UNSET)

        reference = d.pop("reference", UNSET)

        note = d.pop("note", UNSET)

        attachments = []
        _attachments = d.pop("attachments", UNSET)
        for attachments_item_data in _attachments or []:
            attachments_item = SourcingAttachment.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        quote_import_id = d.pop("quoteImportId", UNSET)

        submitted_at = d.pop("submittedAt", UNSET)

        version = d.pop("version", UNSET)

        def _parse_total(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        total = _parse_total(d.pop("total", UNSET))

        answers = []
        _answers = d.pop("answers", UNSET)
        for answers_item_data in _answers or []:
            answers_item = SourcingQuestionAnswer.from_dict(answers_item_data)

            answers.append(answers_item)

        _answered_via = d.pop("answeredVia", UNSET)
        answered_via: Union[Unset, BuyerSourcingResponseViewAnsweredVia]
        if isinstance(_answered_via, Unset):
            answered_via = UNSET
        else:
            answered_via = check_buyer_sourcing_response_view_answered_via(
                _answered_via
            )

        answered_by_email = d.pop("answeredByEmail", UNSET)

        carried_from = d.pop("carriedFrom", UNSET)

        buyer_sourcing_response_view = cls(
            supplier_key=supplier_key,
            supplier_name=supplier_name,
            lines=lines,
            valid_until=valid_until,
            payment_terms_days=payment_terms_days,
            reference=reference,
            note=note,
            attachments=attachments,
            quote_import_id=quote_import_id,
            submitted_at=submitted_at,
            version=version,
            total=total,
            answers=answers,
            answered_via=answered_via,
            answered_by_email=answered_by_email,
            carried_from=carried_from,
        )

        buyer_sourcing_response_view.additional_properties = d
        return buyer_sourcing_response_view

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
