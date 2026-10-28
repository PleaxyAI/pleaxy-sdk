from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.supplier_screening_status import (
    SupplierScreeningStatus,
    check_supplier_screening_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.screen_subject import ScreenSubject
    from ..models.screening_match import ScreeningMatch
    from ..models.supplier_screening_history_item import SupplierScreeningHistoryItem
    from ..models.supplier_screening_list_versions import SupplierScreeningListVersions


T = TypeVar("T", bound="SupplierScreening")


@_attrs_define
class SupplierScreening:
    """
    Attributes:
        connection_id (Union[Unset, str]):
        supplier_key (Union[Unset, str]):
        supplier_name (Union[Unset, str]):
        status (Union[Unset, SupplierScreeningStatus]):
        checked_at (Union[Unset, str]):
        list_versions (Union[Unset, SupplierScreeningListVersions]):
        subjects (Union[Unset, List['ScreenSubject']]):
        countries (Union[Unset, List[str]]):
        matches (Union[Unset, List['ScreeningMatch']]):
        history (Union[Unset, List['SupplierScreeningHistoryItem']]):
        version (Union[Unset, float]):
    """

    connection_id: Union[Unset, str] = UNSET
    supplier_key: Union[Unset, str] = UNSET
    supplier_name: Union[Unset, str] = UNSET
    status: Union[Unset, SupplierScreeningStatus] = UNSET
    checked_at: Union[Unset, str] = UNSET
    list_versions: Union[Unset, "SupplierScreeningListVersions"] = UNSET
    subjects: Union[Unset, List["ScreenSubject"]] = UNSET
    countries: Union[Unset, List[str]] = UNSET
    matches: Union[Unset, List["ScreeningMatch"]] = UNSET
    history: Union[Unset, List["SupplierScreeningHistoryItem"]] = UNSET
    version: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_id = self.connection_id

        supplier_key = self.supplier_key

        supplier_name = self.supplier_name

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        checked_at = self.checked_at

        list_versions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.list_versions, Unset):
            list_versions = self.list_versions.to_dict()

        subjects: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subjects, Unset):
            subjects = []
            for subjects_item_data in self.subjects:
                subjects_item = subjects_item_data.to_dict()
                subjects.append(subjects_item)

        countries: Union[Unset, List[str]] = UNSET
        if not isinstance(self.countries, Unset):
            countries = self.countries

        matches: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.matches, Unset):
            matches = []
            for matches_item_data in self.matches:
                matches_item = matches_item_data.to_dict()
                matches.append(matches_item)

        history: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.history, Unset):
            history = []
            for history_item_data in self.history:
                history_item = history_item_data.to_dict()
                history.append(history_item)

        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connection_id is not UNSET:
            field_dict["connectionId"] = connection_id
        if supplier_key is not UNSET:
            field_dict["supplierKey"] = supplier_key
        if supplier_name is not UNSET:
            field_dict["supplierName"] = supplier_name
        if status is not UNSET:
            field_dict["status"] = status
        if checked_at is not UNSET:
            field_dict["checkedAt"] = checked_at
        if list_versions is not UNSET:
            field_dict["listVersions"] = list_versions
        if subjects is not UNSET:
            field_dict["subjects"] = subjects
        if countries is not UNSET:
            field_dict["countries"] = countries
        if matches is not UNSET:
            field_dict["matches"] = matches
        if history is not UNSET:
            field_dict["history"] = history
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.screen_subject import ScreenSubject
        from ..models.screening_match import ScreeningMatch
        from ..models.supplier_screening_history_item import (
            SupplierScreeningHistoryItem,
        )
        from ..models.supplier_screening_list_versions import (
            SupplierScreeningListVersions,
        )

        d = src_dict.copy()
        connection_id = d.pop("connectionId", UNSET)

        supplier_key = d.pop("supplierKey", UNSET)

        supplier_name = d.pop("supplierName", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, SupplierScreeningStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_supplier_screening_status(_status)

        checked_at = d.pop("checkedAt", UNSET)

        _list_versions = d.pop("listVersions", UNSET)
        list_versions: Union[Unset, SupplierScreeningListVersions]
        if isinstance(_list_versions, Unset):
            list_versions = UNSET
        else:
            list_versions = SupplierScreeningListVersions.from_dict(_list_versions)

        subjects = []
        _subjects = d.pop("subjects", UNSET)
        for subjects_item_data in _subjects or []:
            subjects_item = ScreenSubject.from_dict(subjects_item_data)

            subjects.append(subjects_item)

        countries = cast(List[str], d.pop("countries", UNSET))

        matches = []
        _matches = d.pop("matches", UNSET)
        for matches_item_data in _matches or []:
            matches_item = ScreeningMatch.from_dict(matches_item_data)

            matches.append(matches_item)

        history = []
        _history = d.pop("history", UNSET)
        for history_item_data in _history or []:
            history_item = SupplierScreeningHistoryItem.from_dict(history_item_data)

            history.append(history_item)

        version = d.pop("version", UNSET)

        supplier_screening = cls(
            connection_id=connection_id,
            supplier_key=supplier_key,
            supplier_name=supplier_name,
            status=status,
            checked_at=checked_at,
            list_versions=list_versions,
            subjects=subjects,
            countries=countries,
            matches=matches,
            history=history,
            version=version,
        )

        supplier_screening.additional_properties = d
        return supplier_screening

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
