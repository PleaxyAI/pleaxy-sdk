from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.focus_export_summary_format import (
    FocusExportSummaryFormat,
    check_focus_export_summary_format,
)
from ..models.focus_export_summary_include import (
    FocusExportSummaryInclude,
    check_focus_export_summary_include,
)
from ..models.focus_export_summary_status import (
    FocusExportSummaryStatus,
    check_focus_export_summary_status,
)
from ..models.focus_export_summary_version import (
    FocusExportSummaryVersion,
    check_focus_export_summary_version,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="FocusExportSummary")


@_attrs_define
class FocusExportSummary:
    """
    Attributes:
        id (str):
        status (Union[Unset, FocusExportSummaryStatus]):
        created_at (Union[Unset, str]):
        version (Union[Unset, FocusExportSummaryVersion]):
        include (Union[Unset, FocusExportSummaryInclude]):
        from_ (Union[Unset, str]):
        to (Union[Unset, str]):
        format_ (Union[Unset, FocusExportSummaryFormat]):
        row_count (Union[Unset, float]):
        document_count (Union[Unset, float]):
        expires_at (Union[Unset, str]):
    """

    id: str
    status: Union[Unset, FocusExportSummaryStatus] = UNSET
    created_at: Union[Unset, str] = UNSET
    version: Union[Unset, FocusExportSummaryVersion] = UNSET
    include: Union[Unset, FocusExportSummaryInclude] = UNSET
    from_: Union[Unset, str] = UNSET
    to: Union[Unset, str] = UNSET
    format_: Union[Unset, FocusExportSummaryFormat] = UNSET
    row_count: Union[Unset, float] = UNSET
    document_count: Union[Unset, float] = UNSET
    expires_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        created_at = self.created_at

        version: Union[Unset, str] = UNSET
        if not isinstance(self.version, Unset):
            version = self.version

        include: Union[Unset, str] = UNSET
        if not isinstance(self.include, Unset):
            include = self.include

        from_ = self.from_

        to = self.to

        format_: Union[Unset, str] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_

        row_count = self.row_count

        document_count = self.document_count

        expires_at = self.expires_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if version is not UNSET:
            field_dict["version"] = version
        if include is not UNSET:
            field_dict["include"] = include
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if format_ is not UNSET:
            field_dict["format"] = format_
        if row_count is not UNSET:
            field_dict["rowCount"] = row_count
        if document_count is not UNSET:
            field_dict["documentCount"] = document_count
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        _status = d.pop("status", UNSET)
        status: Union[Unset, FocusExportSummaryStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_focus_export_summary_status(_status)

        created_at = d.pop("createdAt", UNSET)

        _version = d.pop("version", UNSET)
        version: Union[Unset, FocusExportSummaryVersion]
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = check_focus_export_summary_version(_version)

        _include = d.pop("include", UNSET)
        include: Union[Unset, FocusExportSummaryInclude]
        if isinstance(_include, Unset):
            include = UNSET
        else:
            include = check_focus_export_summary_include(_include)

        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, FocusExportSummaryFormat]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = check_focus_export_summary_format(_format_)

        row_count = d.pop("rowCount", UNSET)

        document_count = d.pop("documentCount", UNSET)

        expires_at = d.pop("expiresAt", UNSET)

        focus_export_summary = cls(
            id=id,
            status=status,
            created_at=created_at,
            version=version,
            include=include,
            from_=from_,
            to=to,
            format_=format_,
            row_count=row_count,
            document_count=document_count,
            expires_at=expires_at,
        )

        focus_export_summary.additional_properties = d
        return focus_export_summary

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
