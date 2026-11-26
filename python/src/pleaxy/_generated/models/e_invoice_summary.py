from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_invoice_summary_container import (
    EInvoiceSummaryContainer,
    check_e_invoice_summary_container,
)
from ..models.e_invoice_summary_profile import (
    EInvoiceSummaryProfile,
    check_e_invoice_summary_profile,
)
from ..models.e_invoice_summary_rule_sets_item import (
    EInvoiceSummaryRuleSetsItem,
    check_e_invoice_summary_rule_sets_item,
)
from ..models.e_invoice_summary_syntax import (
    EInvoiceSummarySyntax,
    check_e_invoice_summary_syntax,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.e_invoice_summary_archive import EInvoiceSummaryArchive
    from ..models.e_invoice_summary_findings_item import EInvoiceSummaryFindingsItem


T = TypeVar("T", bound="EInvoiceSummary")


@_attrs_define
class EInvoiceSummary:
    """
    Attributes:
        syntax (Union[Unset, EInvoiceSummarySyntax]):
        profile (Union[Unset, EInvoiceSummaryProfile]):
        specification_id (Union[Unset, str]):
        profile_version (Union[Unset, str]):
        rule_sets (Union[Unset, List[EInvoiceSummaryRuleSetsItem]]):
        findings (Union[Unset, List['EInvoiceSummaryFindingsItem']]):
        findings_truncated (Union[Unset, bool]):
        container (Union[Unset, EInvoiceSummaryContainer]):
        embedded_filename (Union[Unset, str]):
        archive (Union[Unset, EInvoiceSummaryArchive]):
    """

    syntax: Union[Unset, EInvoiceSummarySyntax] = UNSET
    profile: Union[Unset, EInvoiceSummaryProfile] = UNSET
    specification_id: Union[Unset, str] = UNSET
    profile_version: Union[Unset, str] = UNSET
    rule_sets: Union[Unset, List[EInvoiceSummaryRuleSetsItem]] = UNSET
    findings: Union[Unset, List["EInvoiceSummaryFindingsItem"]] = UNSET
    findings_truncated: Union[Unset, bool] = UNSET
    container: Union[Unset, EInvoiceSummaryContainer] = UNSET
    embedded_filename: Union[Unset, str] = UNSET
    archive: Union[Unset, "EInvoiceSummaryArchive"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        syntax: Union[Unset, str] = UNSET
        if not isinstance(self.syntax, Unset):
            syntax = self.syntax

        profile: Union[Unset, str] = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile

        specification_id = self.specification_id

        profile_version = self.profile_version

        rule_sets: Union[Unset, List[str]] = UNSET
        if not isinstance(self.rule_sets, Unset):
            rule_sets = []
            for rule_sets_item_data in self.rule_sets:
                rule_sets_item: str = rule_sets_item_data
                rule_sets.append(rule_sets_item)

        findings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.findings, Unset):
            findings = []
            for findings_item_data in self.findings:
                findings_item = findings_item_data.to_dict()
                findings.append(findings_item)

        findings_truncated = self.findings_truncated

        container: Union[Unset, str] = UNSET
        if not isinstance(self.container, Unset):
            container = self.container

        embedded_filename = self.embedded_filename

        archive: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.archive, Unset):
            archive = self.archive.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if syntax is not UNSET:
            field_dict["syntax"] = syntax
        if profile is not UNSET:
            field_dict["profile"] = profile
        if specification_id is not UNSET:
            field_dict["specificationId"] = specification_id
        if profile_version is not UNSET:
            field_dict["profileVersion"] = profile_version
        if rule_sets is not UNSET:
            field_dict["ruleSets"] = rule_sets
        if findings is not UNSET:
            field_dict["findings"] = findings
        if findings_truncated is not UNSET:
            field_dict["findingsTruncated"] = findings_truncated
        if container is not UNSET:
            field_dict["container"] = container
        if embedded_filename is not UNSET:
            field_dict["embeddedFilename"] = embedded_filename
        if archive is not UNSET:
            field_dict["archive"] = archive

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.e_invoice_summary_archive import EInvoiceSummaryArchive
        from ..models.e_invoice_summary_findings_item import EInvoiceSummaryFindingsItem

        d = src_dict.copy()
        _syntax = d.pop("syntax", UNSET)
        syntax: Union[Unset, EInvoiceSummarySyntax]
        if isinstance(_syntax, Unset):
            syntax = UNSET
        else:
            syntax = check_e_invoice_summary_syntax(_syntax)

        _profile = d.pop("profile", UNSET)
        profile: Union[Unset, EInvoiceSummaryProfile]
        if isinstance(_profile, Unset):
            profile = UNSET
        else:
            profile = check_e_invoice_summary_profile(_profile)

        specification_id = d.pop("specificationId", UNSET)

        profile_version = d.pop("profileVersion", UNSET)

        rule_sets = []
        _rule_sets = d.pop("ruleSets", UNSET)
        for rule_sets_item_data in _rule_sets or []:
            rule_sets_item = check_e_invoice_summary_rule_sets_item(rule_sets_item_data)

            rule_sets.append(rule_sets_item)

        findings = []
        _findings = d.pop("findings", UNSET)
        for findings_item_data in _findings or []:
            findings_item = EInvoiceSummaryFindingsItem.from_dict(findings_item_data)

            findings.append(findings_item)

        findings_truncated = d.pop("findingsTruncated", UNSET)

        _container = d.pop("container", UNSET)
        container: Union[Unset, EInvoiceSummaryContainer]
        if isinstance(_container, Unset):
            container = UNSET
        else:
            container = check_e_invoice_summary_container(_container)

        embedded_filename = d.pop("embeddedFilename", UNSET)

        _archive = d.pop("archive", UNSET)
        archive: Union[Unset, EInvoiceSummaryArchive]
        if isinstance(_archive, Unset):
            archive = UNSET
        else:
            archive = EInvoiceSummaryArchive.from_dict(_archive)

        e_invoice_summary = cls(
            syntax=syntax,
            profile=profile,
            specification_id=specification_id,
            profile_version=profile_version,
            rule_sets=rule_sets,
            findings=findings,
            findings_truncated=findings_truncated,
            container=container,
            embedded_filename=embedded_filename,
            archive=archive,
        )

        e_invoice_summary.additional_properties = d
        return e_invoice_summary

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
