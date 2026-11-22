from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.spike_finding_type import SpikeFindingType, check_spike_finding_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.spike_finding_subject_type_0 import SpikeFindingSubjectType0
    from ..models.spike_finding_subject_type_1 import SpikeFindingSubjectType1
    from ..models.spike_finding_subject_type_2 import SpikeFindingSubjectType2
    from ..models.spike_finding_subject_type_3 import SpikeFindingSubjectType3


T = TypeVar("T", bound="SpikeFinding")


@_attrs_define
class SpikeFinding:
    """
    Attributes:
        type (Union[Unset, SpikeFindingType]):
        subject (Union['SpikeFindingSubjectType0', 'SpikeFindingSubjectType1', 'SpikeFindingSubjectType2',
            'SpikeFindingSubjectType3', Unset]):
        recent_from (Union[Unset, str]):
        recent_to (Union[Unset, str]):
        baseline_from (Union[Unset, str]):
        baseline_to (Union[Unset, str]):
        recent_per_day (Union[Unset, float]):
        baseline_per_day (Union[Unset, float]):
        rise_pct (Union[Unset, float]):
        excess (Union[Unset, float]):
    """

    type: Union[Unset, SpikeFindingType] = UNSET
    subject: Union[
        "SpikeFindingSubjectType0",
        "SpikeFindingSubjectType1",
        "SpikeFindingSubjectType2",
        "SpikeFindingSubjectType3",
        Unset,
    ] = UNSET
    recent_from: Union[Unset, str] = UNSET
    recent_to: Union[Unset, str] = UNSET
    baseline_from: Union[Unset, str] = UNSET
    baseline_to: Union[Unset, str] = UNSET
    recent_per_day: Union[Unset, float] = UNSET
    baseline_per_day: Union[Unset, float] = UNSET
    rise_pct: Union[Unset, float] = UNSET
    excess: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.spike_finding_subject_type_0 import SpikeFindingSubjectType0
        from ..models.spike_finding_subject_type_1 import SpikeFindingSubjectType1
        from ..models.spike_finding_subject_type_2 import SpikeFindingSubjectType2

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type

        subject: Union[Dict[str, Any], Unset]
        if isinstance(self.subject, Unset):
            subject = UNSET
        elif isinstance(self.subject, SpikeFindingSubjectType0):
            subject = self.subject.to_dict()
        elif isinstance(self.subject, SpikeFindingSubjectType1):
            subject = self.subject.to_dict()
        elif isinstance(self.subject, SpikeFindingSubjectType2):
            subject = self.subject.to_dict()
        else:
            subject = self.subject.to_dict()

        recent_from = self.recent_from

        recent_to = self.recent_to

        baseline_from = self.baseline_from

        baseline_to = self.baseline_to

        recent_per_day = self.recent_per_day

        baseline_per_day = self.baseline_per_day

        rise_pct = self.rise_pct

        excess = self.excess

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if subject is not UNSET:
            field_dict["subject"] = subject
        if recent_from is not UNSET:
            field_dict["recentFrom"] = recent_from
        if recent_to is not UNSET:
            field_dict["recentTo"] = recent_to
        if baseline_from is not UNSET:
            field_dict["baselineFrom"] = baseline_from
        if baseline_to is not UNSET:
            field_dict["baselineTo"] = baseline_to
        if recent_per_day is not UNSET:
            field_dict["recentPerDay"] = recent_per_day
        if baseline_per_day is not UNSET:
            field_dict["baselinePerDay"] = baseline_per_day
        if rise_pct is not UNSET:
            field_dict["risePct"] = rise_pct
        if excess is not UNSET:
            field_dict["excess"] = excess

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spike_finding_subject_type_0 import SpikeFindingSubjectType0
        from ..models.spike_finding_subject_type_1 import SpikeFindingSubjectType1
        from ..models.spike_finding_subject_type_2 import SpikeFindingSubjectType2
        from ..models.spike_finding_subject_type_3 import SpikeFindingSubjectType3

        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, SpikeFindingType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = check_spike_finding_type(_type)

        def _parse_subject(
            data: object,
        ) -> Union[
            "SpikeFindingSubjectType0",
            "SpikeFindingSubjectType1",
            "SpikeFindingSubjectType2",
            "SpikeFindingSubjectType3",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                subject_type_0 = SpikeFindingSubjectType0.from_dict(data)

                return subject_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                subject_type_1 = SpikeFindingSubjectType1.from_dict(data)

                return subject_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                subject_type_2 = SpikeFindingSubjectType2.from_dict(data)

                return subject_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            subject_type_3 = SpikeFindingSubjectType3.from_dict(data)

            return subject_type_3

        subject = _parse_subject(d.pop("subject", UNSET))

        recent_from = d.pop("recentFrom", UNSET)

        recent_to = d.pop("recentTo", UNSET)

        baseline_from = d.pop("baselineFrom", UNSET)

        baseline_to = d.pop("baselineTo", UNSET)

        recent_per_day = d.pop("recentPerDay", UNSET)

        baseline_per_day = d.pop("baselinePerDay", UNSET)

        rise_pct = d.pop("risePct", UNSET)

        excess = d.pop("excess", UNSET)

        spike_finding = cls(
            type=type,
            subject=subject,
            recent_from=recent_from,
            recent_to=recent_to,
            baseline_from=baseline_from,
            baseline_to=baseline_to,
            recent_per_day=recent_per_day,
            baseline_per_day=baseline_per_day,
            rise_pct=rise_pct,
            excess=excess,
        )

        spike_finding.additional_properties = d
        return spike_finding

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
