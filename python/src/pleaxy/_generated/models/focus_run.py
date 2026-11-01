from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.focus_run_status import FocusRunStatus, check_focus_run_status
from ..models.focus_run_trigger import FocusRunTrigger, check_focus_run_trigger
from ..models.focus_run_version import FocusRunVersion, check_focus_run_version
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.focus_run_failure import FocusRunFailure
    from ..models.focus_run_skipped_by_reason import FocusRunSkippedByReason


T = TypeVar("T", bound="FocusRun")


@_attrs_define
class FocusRun:
    """
    Attributes:
        run_id (Union[Unset, str]):
        started_at (Union[Unset, str]):
        finished_at (Union[Unset, str]):
        status (Union[Unset, FocusRunStatus]):
        trigger (Union[Unset, FocusRunTrigger]):
        periods (Union[Unset, List[str]]):
        files (Union[Unset, float]):
        rows (Union[Unset, float]):
        skipped (Union[Unset, float]):
        skipped_by_reason (Union[Unset, FocusRunSkippedByReason]):
        version (Union[Unset, FocusRunVersion]):
        ignored_files (Union[Unset, float]):
        failure (Union[Unset, FocusRunFailure]):
    """

    run_id: Union[Unset, str] = UNSET
    started_at: Union[Unset, str] = UNSET
    finished_at: Union[Unset, str] = UNSET
    status: Union[Unset, FocusRunStatus] = UNSET
    trigger: Union[Unset, FocusRunTrigger] = UNSET
    periods: Union[Unset, List[str]] = UNSET
    files: Union[Unset, float] = UNSET
    rows: Union[Unset, float] = UNSET
    skipped: Union[Unset, float] = UNSET
    skipped_by_reason: Union[Unset, "FocusRunSkippedByReason"] = UNSET
    version: Union[Unset, FocusRunVersion] = UNSET
    ignored_files: Union[Unset, float] = UNSET
    failure: Union[Unset, "FocusRunFailure"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        run_id = self.run_id

        started_at = self.started_at

        finished_at = self.finished_at

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        trigger: Union[Unset, str] = UNSET
        if not isinstance(self.trigger, Unset):
            trigger = self.trigger

        periods: Union[Unset, List[str]] = UNSET
        if not isinstance(self.periods, Unset):
            periods = self.periods

        files = self.files

        rows = self.rows

        skipped = self.skipped

        skipped_by_reason: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.skipped_by_reason, Unset):
            skipped_by_reason = self.skipped_by_reason.to_dict()

        version: Union[Unset, str] = UNSET
        if not isinstance(self.version, Unset):
            version = self.version

        ignored_files = self.ignored_files

        failure: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.failure, Unset):
            failure = self.failure.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if run_id is not UNSET:
            field_dict["runId"] = run_id
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if finished_at is not UNSET:
            field_dict["finishedAt"] = finished_at
        if status is not UNSET:
            field_dict["status"] = status
        if trigger is not UNSET:
            field_dict["trigger"] = trigger
        if periods is not UNSET:
            field_dict["periods"] = periods
        if files is not UNSET:
            field_dict["files"] = files
        if rows is not UNSET:
            field_dict["rows"] = rows
        if skipped is not UNSET:
            field_dict["skipped"] = skipped
        if skipped_by_reason is not UNSET:
            field_dict["skippedByReason"] = skipped_by_reason
        if version is not UNSET:
            field_dict["version"] = version
        if ignored_files is not UNSET:
            field_dict["ignoredFiles"] = ignored_files
        if failure is not UNSET:
            field_dict["failure"] = failure

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.focus_run_failure import FocusRunFailure
        from ..models.focus_run_skipped_by_reason import FocusRunSkippedByReason

        d = src_dict.copy()
        run_id = d.pop("runId", UNSET)

        started_at = d.pop("startedAt", UNSET)

        finished_at = d.pop("finishedAt", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, FocusRunStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_focus_run_status(_status)

        _trigger = d.pop("trigger", UNSET)
        trigger: Union[Unset, FocusRunTrigger]
        if isinstance(_trigger, Unset):
            trigger = UNSET
        else:
            trigger = check_focus_run_trigger(_trigger)

        periods = cast(List[str], d.pop("periods", UNSET))

        files = d.pop("files", UNSET)

        rows = d.pop("rows", UNSET)

        skipped = d.pop("skipped", UNSET)

        _skipped_by_reason = d.pop("skippedByReason", UNSET)
        skipped_by_reason: Union[Unset, FocusRunSkippedByReason]
        if isinstance(_skipped_by_reason, Unset):
            skipped_by_reason = UNSET
        else:
            skipped_by_reason = FocusRunSkippedByReason.from_dict(_skipped_by_reason)

        _version = d.pop("version", UNSET)
        version: Union[Unset, FocusRunVersion]
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = check_focus_run_version(_version)

        ignored_files = d.pop("ignoredFiles", UNSET)

        _failure = d.pop("failure", UNSET)
        failure: Union[Unset, FocusRunFailure]
        if isinstance(_failure, Unset):
            failure = UNSET
        else:
            failure = FocusRunFailure.from_dict(_failure)

        focus_run = cls(
            run_id=run_id,
            started_at=started_at,
            finished_at=finished_at,
            status=status,
            trigger=trigger,
            periods=periods,
            files=files,
            rows=rows,
            skipped=skipped,
            skipped_by_reason=skipped_by_reason,
            version=version,
            ignored_files=ignored_files,
            failure=failure,
        )

        focus_run.additional_properties = d
        return focus_run

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
