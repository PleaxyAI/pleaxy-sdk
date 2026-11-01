from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_focus_source_period_result_version import (
    GetFocusSourcePeriodResultVersion,
    check_get_focus_source_period_result_version,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.focus_cost_center_total import FocusCostCenterTotal
    from ..models.focus_invoice_total import FocusInvoiceTotal
    from ..models.get_focus_source_period_result_issuers import (
        GetFocusSourcePeriodResultIssuers,
    )
    from ..models.get_focus_source_period_result_totals import (
        GetFocusSourcePeriodResultTotals,
    )


T = TypeVar("T", bound="GetFocusSourcePeriodResult")


@_attrs_define
class GetFocusSourcePeriodResult:
    """
    Attributes:
        invoices (Union[Unset, List['FocusInvoiceTotal']]):
        cost_centers (Union[Unset, List['FocusCostCenterTotal']]):
        source_id (Union[Unset, str]):
        period (Union[Unset, str]):
        rows (Union[Unset, float]):
        totals (Union[Unset, GetFocusSourcePeriodResultTotals]):
        issuers (Union[Unset, GetFocusSourcePeriodResultIssuers]):
        version (Union[Unset, GetFocusSourcePeriodResultVersion]):
        as_of (Union[Unset, str]):
    """

    invoices: Union[Unset, List["FocusInvoiceTotal"]] = UNSET
    cost_centers: Union[Unset, List["FocusCostCenterTotal"]] = UNSET
    source_id: Union[Unset, str] = UNSET
    period: Union[Unset, str] = UNSET
    rows: Union[Unset, float] = UNSET
    totals: Union[Unset, "GetFocusSourcePeriodResultTotals"] = UNSET
    issuers: Union[Unset, "GetFocusSourcePeriodResultIssuers"] = UNSET
    version: Union[Unset, GetFocusSourcePeriodResultVersion] = UNSET
    as_of: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoices: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.invoices, Unset):
            invoices = []
            for invoices_item_data in self.invoices:
                invoices_item = invoices_item_data.to_dict()
                invoices.append(invoices_item)

        cost_centers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.cost_centers, Unset):
            cost_centers = []
            for cost_centers_item_data in self.cost_centers:
                cost_centers_item = cost_centers_item_data.to_dict()
                cost_centers.append(cost_centers_item)

        source_id = self.source_id

        period = self.period

        rows = self.rows

        totals: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.totals, Unset):
            totals = self.totals.to_dict()

        issuers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.issuers, Unset):
            issuers = self.issuers.to_dict()

        version: Union[Unset, str] = UNSET
        if not isinstance(self.version, Unset):
            version = self.version

        as_of = self.as_of

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invoices is not UNSET:
            field_dict["invoices"] = invoices
        if cost_centers is not UNSET:
            field_dict["costCenters"] = cost_centers
        if source_id is not UNSET:
            field_dict["sourceId"] = source_id
        if period is not UNSET:
            field_dict["period"] = period
        if rows is not UNSET:
            field_dict["rows"] = rows
        if totals is not UNSET:
            field_dict["totals"] = totals
        if issuers is not UNSET:
            field_dict["issuers"] = issuers
        if version is not UNSET:
            field_dict["version"] = version
        if as_of is not UNSET:
            field_dict["asOf"] = as_of

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.focus_cost_center_total import FocusCostCenterTotal
        from ..models.focus_invoice_total import FocusInvoiceTotal
        from ..models.get_focus_source_period_result_issuers import (
            GetFocusSourcePeriodResultIssuers,
        )
        from ..models.get_focus_source_period_result_totals import (
            GetFocusSourcePeriodResultTotals,
        )

        d = src_dict.copy()
        invoices = []
        _invoices = d.pop("invoices", UNSET)
        for invoices_item_data in _invoices or []:
            invoices_item = FocusInvoiceTotal.from_dict(invoices_item_data)

            invoices.append(invoices_item)

        cost_centers = []
        _cost_centers = d.pop("costCenters", UNSET)
        for cost_centers_item_data in _cost_centers or []:
            cost_centers_item = FocusCostCenterTotal.from_dict(cost_centers_item_data)

            cost_centers.append(cost_centers_item)

        source_id = d.pop("sourceId", UNSET)

        period = d.pop("period", UNSET)

        rows = d.pop("rows", UNSET)

        _totals = d.pop("totals", UNSET)
        totals: Union[Unset, GetFocusSourcePeriodResultTotals]
        if isinstance(_totals, Unset):
            totals = UNSET
        else:
            totals = GetFocusSourcePeriodResultTotals.from_dict(_totals)

        _issuers = d.pop("issuers", UNSET)
        issuers: Union[Unset, GetFocusSourcePeriodResultIssuers]
        if isinstance(_issuers, Unset):
            issuers = UNSET
        else:
            issuers = GetFocusSourcePeriodResultIssuers.from_dict(_issuers)

        _version = d.pop("version", UNSET)
        version: Union[Unset, GetFocusSourcePeriodResultVersion]
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = check_get_focus_source_period_result_version(_version)

        as_of = d.pop("asOf", UNSET)

        get_focus_source_period_result = cls(
            invoices=invoices,
            cost_centers=cost_centers,
            source_id=source_id,
            period=period,
            rows=rows,
            totals=totals,
            issuers=issuers,
            version=version,
            as_of=as_of,
        )

        get_focus_source_period_result.additional_properties = d
        return get_focus_source_period_result

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
