from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Type,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validate_feed_invoice_result_credit_note_document_type import (
    ValidateFeedInvoiceResultCreditNoteDocumentType,
    check_validate_feed_invoice_result_credit_note_document_type,
)
from ..models.validate_feed_invoice_result_credit_note_submitted_format import (
    ValidateFeedInvoiceResultCreditNoteSubmittedFormat,
    check_validate_feed_invoice_result_credit_note_submitted_format,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.validate_feed_invoice_result_credit_note_credit_note import (
        ValidateFeedInvoiceResultCreditNoteCreditNote,
    )
    from ..models.validate_feed_invoice_result_credit_note_replay_type_0 import (
        ValidateFeedInvoiceResultCreditNoteReplayType0,
    )
    from ..models.validate_feed_invoice_result_credit_note_warnings_item import (
        ValidateFeedInvoiceResultCreditNoteWarningsItem,
    )


T = TypeVar("T", bound="ValidateFeedInvoiceResultCreditNote")


@_attrs_define
class ValidateFeedInvoiceResultCreditNote:
    """
    Attributes:
        valid (Union[Unset, bool]):
        document_type (Union[Unset, ValidateFeedInvoiceResultCreditNoteDocumentType]):
        feed_enabled (Union[Unset, bool]):
        submitted_format (Union[Unset, ValidateFeedInvoiceResultCreditNoteSubmittedFormat]):
        credit_note (Union[Unset, ValidateFeedInvoiceResultCreditNoteCreditNote]):
        replay (Union['ValidateFeedInvoiceResultCreditNoteReplayType0', None, Unset]):
        warnings (Union[Unset, List['ValidateFeedInvoiceResultCreditNoteWarningsItem']]):
    """

    valid: Union[Unset, bool] = UNSET
    document_type: Union[Unset, ValidateFeedInvoiceResultCreditNoteDocumentType] = UNSET
    feed_enabled: Union[Unset, bool] = UNSET
    submitted_format: Union[
        Unset, ValidateFeedInvoiceResultCreditNoteSubmittedFormat
    ] = UNSET
    credit_note: Union[Unset, "ValidateFeedInvoiceResultCreditNoteCreditNote"] = UNSET
    replay: Union["ValidateFeedInvoiceResultCreditNoteReplayType0", None, Unset] = UNSET
    warnings: Union[Unset, List["ValidateFeedInvoiceResultCreditNoteWarningsItem"]] = (
        UNSET
    )
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.validate_feed_invoice_result_credit_note_replay_type_0 import (
            ValidateFeedInvoiceResultCreditNoteReplayType0,
        )

        valid = self.valid

        document_type: Union[Unset, str] = UNSET
        if not isinstance(self.document_type, Unset):
            document_type = self.document_type

        feed_enabled = self.feed_enabled

        submitted_format: Union[Unset, str] = UNSET
        if not isinstance(self.submitted_format, Unset):
            submitted_format = self.submitted_format

        credit_note: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credit_note, Unset):
            credit_note = self.credit_note.to_dict()

        replay: Union[Dict[str, Any], None, Unset]
        if isinstance(self.replay, Unset):
            replay = UNSET
        elif isinstance(self.replay, ValidateFeedInvoiceResultCreditNoteReplayType0):
            replay = self.replay.to_dict()
        else:
            replay = self.replay

        warnings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for warnings_item_data in self.warnings:
                warnings_item = warnings_item_data.to_dict()
                warnings.append(warnings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if valid is not UNSET:
            field_dict["valid"] = valid
        if document_type is not UNSET:
            field_dict["documentType"] = document_type
        if feed_enabled is not UNSET:
            field_dict["feedEnabled"] = feed_enabled
        if submitted_format is not UNSET:
            field_dict["submittedFormat"] = submitted_format
        if credit_note is not UNSET:
            field_dict["creditNote"] = credit_note
        if replay is not UNSET:
            field_dict["replay"] = replay
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.validate_feed_invoice_result_credit_note_credit_note import (
            ValidateFeedInvoiceResultCreditNoteCreditNote,
        )
        from ..models.validate_feed_invoice_result_credit_note_replay_type_0 import (
            ValidateFeedInvoiceResultCreditNoteReplayType0,
        )
        from ..models.validate_feed_invoice_result_credit_note_warnings_item import (
            ValidateFeedInvoiceResultCreditNoteWarningsItem,
        )

        d = src_dict.copy()
        valid = d.pop("valid", UNSET)

        _document_type = d.pop("documentType", UNSET)
        document_type: Union[Unset, ValidateFeedInvoiceResultCreditNoteDocumentType]
        if isinstance(_document_type, Unset):
            document_type = UNSET
        else:
            document_type = (
                check_validate_feed_invoice_result_credit_note_document_type(
                    _document_type
                )
            )

        feed_enabled = d.pop("feedEnabled", UNSET)

        _submitted_format = d.pop("submittedFormat", UNSET)
        submitted_format: Union[
            Unset, ValidateFeedInvoiceResultCreditNoteSubmittedFormat
        ]
        if isinstance(_submitted_format, Unset):
            submitted_format = UNSET
        else:
            submitted_format = (
                check_validate_feed_invoice_result_credit_note_submitted_format(
                    _submitted_format
                )
            )

        _credit_note = d.pop("creditNote", UNSET)
        credit_note: Union[Unset, ValidateFeedInvoiceResultCreditNoteCreditNote]
        if isinstance(_credit_note, Unset):
            credit_note = UNSET
        else:
            credit_note = ValidateFeedInvoiceResultCreditNoteCreditNote.from_dict(
                _credit_note
            )

        def _parse_replay(
            data: object,
        ) -> Union["ValidateFeedInvoiceResultCreditNoteReplayType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                replay_type_0 = (
                    ValidateFeedInvoiceResultCreditNoteReplayType0.from_dict(data)
                )

                return replay_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union["ValidateFeedInvoiceResultCreditNoteReplayType0", None, Unset],
                data,
            )

        replay = _parse_replay(d.pop("replay", UNSET))

        warnings = []
        _warnings = d.pop("warnings", UNSET)
        for warnings_item_data in _warnings or []:
            warnings_item = ValidateFeedInvoiceResultCreditNoteWarningsItem.from_dict(
                warnings_item_data
            )

            warnings.append(warnings_item)

        validate_feed_invoice_result_credit_note = cls(
            valid=valid,
            document_type=document_type,
            feed_enabled=feed_enabled,
            submitted_format=submitted_format,
            credit_note=credit_note,
            replay=replay,
            warnings=warnings,
        )

        validate_feed_invoice_result_credit_note.additional_properties = d
        return validate_feed_invoice_result_credit_note

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
