from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pace_finding_last_month_source import (
    PaceFindingLastMonthSource,
    check_pace_finding_last_month_source,
)
from ..models.pace_finding_type import PaceFindingType, check_pace_finding_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pace_finding_subject_type_0 import PaceFindingSubjectType0
    from ..models.pace_finding_subject_type_1 import PaceFindingSubjectType1
    from ..models.pace_finding_subject_type_2 import PaceFindingSubjectType2
    from ..models.pace_finding_subject_type_3 import PaceFindingSubjectType3


T = TypeVar("T", bound="PaceFinding")


@_attrs_define
class PaceFinding:
    """
    Attributes:
        type (Union[Unset, PaceFindingType]):
        subject (Union['PaceFindingSubjectType0', 'PaceFindingSubjectType1', 'PaceFindingSubjectType2',
            'PaceFindingSubjectType3', Unset]):
        month_to_date (Union[Unset, float]):
        as_of (Union[Unset, str]):
        projected (Union[Unset, float]):
        last_month (Union[Unset, float]):
        last_month_source (Union[Unset, PaceFindingLastMonthSource]):
        rise_pct (Union[Unset, float]):
        excess (Union[Unset, float]):
    """

    type: Union[Unset, PaceFindingType] = UNSET
    subject: Union[
        "PaceFindingSubjectType0",
        "PaceFindingSubjectType1",
        "PaceFindingSubjectType2",
        "PaceFindingSubjectType3",
        Unset,
    ] = UNSET
    month_to_date: Union[Unset, float] = UNSET
    as_of: Union[Unset, str] = UNSET
    projected: Union[Unset, float] = UNSET
    last_month: Union[Unset, float] = UNSET
    last_month_source: Union[Unset, PaceFindingLastMonthSource] = UNSET
    rise_pct: Union[Unset, float] = UNSET
    excess: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.pace_finding_subject_type_0 import PaceFindingSubjectType0
        from ..models.pace_finding_subject_type_1 import PaceFindingSubjectType1
        from ..models.pace_finding_subject_type_2 import PaceFindingSubjectType2

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type

        subject: Union[Dict[str, Any], Unset]
        if isinstance(self.subject, Unset):
            subject = UNSET
        elif isinstance(self.subject, PaceFindingSubjectType0):
            subject = self.subject.to_dict()
        elif isinstance(self.subject, PaceFindingSubjectType1):
            subject = self.subject.to_dict()
        elif isinstance(self.subject, PaceFindingSubjectType2):
            subject = self.subject.to_dict()
        else:
            subject = self.subject.to_dict()

        month_to_date = self.month_to_date

        as_of = self.as_of

        projected = self.projected

        last_month = self.last_month

        last_month_source: Union[Unset, str] = UNSET
        if not isinstance(self.last_month_source, Unset):
            last_month_source = self.last_month_source

        rise_pct = self.rise_pct

        excess = self.excess

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if subject is not UNSET:
            field_dict["subject"] = subject
        if month_to_date is not UNSET:
            field_dict["monthToDate"] = month_to_date
        if as_of is not UNSET:
            field_dict["asOf"] = as_of
        if projected is not UNSET:
            field_dict["projected"] = projected
        if last_month is not UNSET:
            field_dict["lastMonth"] = last_month
        if last_month_source is not UNSET:
            field_dict["lastMonthSource"] = last_month_source
        if rise_pct is not UNSET:
            field_dict["risePct"] = rise_pct
        if excess is not UNSET:
            field_dict["excess"] = excess

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pace_finding_subject_type_0 import PaceFindingSubjectType0
        from ..models.pace_finding_subject_type_1 import PaceFindingSubjectType1
        from ..models.pace_finding_subject_type_2 import PaceFindingSubjectType2
        from ..models.pace_finding_subject_type_3 import PaceFindingSubjectType3

        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, PaceFindingType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = check_pace_finding_type(_type)

        def _parse_subject(
            data: object,
        ) -> Union[
            "PaceFindingSubjectType0",
            "PaceFindingSubjectType1",
            "PaceFindingSubjectType2",
            "PaceFindingSubjectType3",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                subject_type_0 = PaceFindingSubjectType0.from_dict(data)

                return subject_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                subject_type_1 = PaceFindingSubjectType1.from_dict(data)

                return subject_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                subject_type_2 = PaceFindingSubjectType2.from_dict(data)

                return subject_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            subject_type_3 = PaceFindingSubjectType3.from_dict(data)

            return subject_type_3

        subject = _parse_subject(d.pop("subject", UNSET))

        month_to_date = d.pop("monthToDate", UNSET)

        as_of = d.pop("asOf", UNSET)

        projected = d.pop("projected", UNSET)

        last_month = d.pop("lastMonth", UNSET)

        _last_month_source = d.pop("lastMonthSource", UNSET)
        last_month_source: Union[Unset, PaceFindingLastMonthSource]
        if isinstance(_last_month_source, Unset):
            last_month_source = UNSET
        else:
            last_month_source = check_pace_finding_last_month_source(_last_month_source)

        rise_pct = d.pop("risePct", UNSET)

        excess = d.pop("excess", UNSET)

        pace_finding = cls(
            type=type,
            subject=subject,
            month_to_date=month_to_date,
            as_of=as_of,
            projected=projected,
            last_month=last_month,
            last_month_source=last_month_source,
            rise_pct=rise_pct,
            excess=excess,
        )

        pace_finding.additional_properties = d
        return pace_finding

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
