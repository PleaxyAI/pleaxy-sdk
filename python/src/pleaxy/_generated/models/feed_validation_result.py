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

from ..models.feed_validation_result_match_status_on_submit import (
    FeedValidationResultMatchStatusOnSubmit,
    check_feed_validation_result_match_status_on_submit,
)
from ..models.feed_validation_result_submitted_format import (
    FeedValidationResultSubmittedFormat,
    check_feed_validation_result_submitted_format,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feed_validation_result_findings_item import (
        FeedValidationResultFindingsItem,
    )
    from ..models.feed_validation_result_invoice import FeedValidationResultInvoice
    from ..models.feed_validation_result_replay_type_0 import (
        FeedValidationResultReplayType0,
    )
    from ..models.feed_validation_warning import FeedValidationWarning


T = TypeVar("T", bound="FeedValidationResult")


@_attrs_define
class FeedValidationResult:
    """
    Attributes:
        valid (Union[Unset, bool]):
        feed_enabled (Union[Unset, bool]):
        submitted_format (Union[Unset, FeedValidationResultSubmittedFormat]):
        invoice (Union[Unset, FeedValidationResultInvoice]):
        match_status_on_submit (Union[Unset, FeedValidationResultMatchStatusOnSubmit]):
        findings (Union[Unset, List['FeedValidationResultFindingsItem']]):
        replay (Union['FeedValidationResultReplayType0', None, Unset]):
        warnings (Union[Unset, List['FeedValidationWarning']]):
    """

    valid: Union[Unset, bool] = UNSET
    feed_enabled: Union[Unset, bool] = UNSET
    submitted_format: Union[Unset, FeedValidationResultSubmittedFormat] = UNSET
    invoice: Union[Unset, "FeedValidationResultInvoice"] = UNSET
    match_status_on_submit: Union[Unset, FeedValidationResultMatchStatusOnSubmit] = (
        UNSET
    )
    findings: Union[Unset, List["FeedValidationResultFindingsItem"]] = UNSET
    replay: Union["FeedValidationResultReplayType0", None, Unset] = UNSET
    warnings: Union[Unset, List["FeedValidationWarning"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.feed_validation_result_replay_type_0 import (
            FeedValidationResultReplayType0,
        )

        valid = self.valid

        feed_enabled = self.feed_enabled

        submitted_format: Union[Unset, str] = UNSET
        if not isinstance(self.submitted_format, Unset):
            submitted_format = self.submitted_format

        invoice: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.invoice, Unset):
            invoice = self.invoice.to_dict()

        match_status_on_submit: Union[Unset, str] = UNSET
        if not isinstance(self.match_status_on_submit, Unset):
            match_status_on_submit = self.match_status_on_submit

        findings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.findings, Unset):
            findings = []
            for findings_item_data in self.findings:
                findings_item = findings_item_data.to_dict()
                findings.append(findings_item)

        replay: Union[Dict[str, Any], None, Unset]
        if isinstance(self.replay, Unset):
            replay = UNSET
        elif isinstance(self.replay, FeedValidationResultReplayType0):
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
        if feed_enabled is not UNSET:
            field_dict["feedEnabled"] = feed_enabled
        if submitted_format is not UNSET:
            field_dict["submittedFormat"] = submitted_format
        if invoice is not UNSET:
            field_dict["invoice"] = invoice
        if match_status_on_submit is not UNSET:
            field_dict["matchStatusOnSubmit"] = match_status_on_submit
        if findings is not UNSET:
            field_dict["findings"] = findings
        if replay is not UNSET:
            field_dict["replay"] = replay
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.feed_validation_result_findings_item import (
            FeedValidationResultFindingsItem,
        )
        from ..models.feed_validation_result_invoice import FeedValidationResultInvoice
        from ..models.feed_validation_result_replay_type_0 import (
            FeedValidationResultReplayType0,
        )
        from ..models.feed_validation_warning import FeedValidationWarning

        d = src_dict.copy()
        valid = d.pop("valid", UNSET)

        feed_enabled = d.pop("feedEnabled", UNSET)

        _submitted_format = d.pop("submittedFormat", UNSET)
        submitted_format: Union[Unset, FeedValidationResultSubmittedFormat]
        if isinstance(_submitted_format, Unset):
            submitted_format = UNSET
        else:
            submitted_format = check_feed_validation_result_submitted_format(
                _submitted_format
            )

        _invoice = d.pop("invoice", UNSET)
        invoice: Union[Unset, FeedValidationResultInvoice]
        if isinstance(_invoice, Unset):
            invoice = UNSET
        else:
            invoice = FeedValidationResultInvoice.from_dict(_invoice)

        _match_status_on_submit = d.pop("matchStatusOnSubmit", UNSET)
        match_status_on_submit: Union[Unset, FeedValidationResultMatchStatusOnSubmit]
        if isinstance(_match_status_on_submit, Unset):
            match_status_on_submit = UNSET
        else:
            match_status_on_submit = (
                check_feed_validation_result_match_status_on_submit(
                    _match_status_on_submit
                )
            )

        findings = []
        _findings = d.pop("findings", UNSET)
        for findings_item_data in _findings or []:
            findings_item = FeedValidationResultFindingsItem.from_dict(
                findings_item_data
            )

            findings.append(findings_item)

        def _parse_replay(
            data: object,
        ) -> Union["FeedValidationResultReplayType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                replay_type_0 = FeedValidationResultReplayType0.from_dict(data)

                return replay_type_0
            except:  # noqa: E722
                pass
            return cast(Union["FeedValidationResultReplayType0", None, Unset], data)

        replay = _parse_replay(d.pop("replay", UNSET))

        warnings = []
        _warnings = d.pop("warnings", UNSET)
        for warnings_item_data in _warnings or []:
            warnings_item = FeedValidationWarning.from_dict(warnings_item_data)

            warnings.append(warnings_item)

        feed_validation_result = cls(
            valid=valid,
            feed_enabled=feed_enabled,
            submitted_format=submitted_format,
            invoice=invoice,
            match_status_on_submit=match_status_on_submit,
            findings=findings,
            replay=replay,
            warnings=warnings,
        )

        feed_validation_result.additional_properties = d
        return feed_validation_result

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
