from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.approval_fx_source import ApprovalFxSource, check_approval_fx_source
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.approval_fx_supplier_stated import ApprovalFxSupplierStated


T = TypeVar("T", bound="ApprovalFx")


@_attrs_define
class ApprovalFx:
    """
    Attributes:
        from_ (Union[Unset, str]):
        to (Union[Unset, str]):
        rate (Union[Unset, float]):
        source (Union[Unset, ApprovalFxSource]):
        as_of (Union[Unset, str]):
        control_amount (Union[Unset, float]):
        supplier_stated (Union[Unset, ApprovalFxSupplierStated]):
    """

    from_: Union[Unset, str] = UNSET
    to: Union[Unset, str] = UNSET
    rate: Union[Unset, float] = UNSET
    source: Union[Unset, ApprovalFxSource] = UNSET
    as_of: Union[Unset, str] = UNSET
    control_amount: Union[Unset, float] = UNSET
    supplier_stated: Union[Unset, "ApprovalFxSupplierStated"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from_ = self.from_

        to = self.to

        rate = self.rate

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source

        as_of = self.as_of

        control_amount = self.control_amount

        supplier_stated: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.supplier_stated, Unset):
            supplier_stated = self.supplier_stated.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if rate is not UNSET:
            field_dict["rate"] = rate
        if source is not UNSET:
            field_dict["source"] = source
        if as_of is not UNSET:
            field_dict["asOf"] = as_of
        if control_amount is not UNSET:
            field_dict["controlAmount"] = control_amount
        if supplier_stated is not UNSET:
            field_dict["supplierStated"] = supplier_stated

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.approval_fx_supplier_stated import ApprovalFxSupplierStated

        d = src_dict.copy()
        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        rate = d.pop("rate", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, ApprovalFxSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = check_approval_fx_source(_source)

        as_of = d.pop("asOf", UNSET)

        control_amount = d.pop("controlAmount", UNSET)

        _supplier_stated = d.pop("supplierStated", UNSET)
        supplier_stated: Union[Unset, ApprovalFxSupplierStated]
        if isinstance(_supplier_stated, Unset):
            supplier_stated = UNSET
        else:
            supplier_stated = ApprovalFxSupplierStated.from_dict(_supplier_stated)

        approval_fx = cls(
            from_=from_,
            to=to,
            rate=rate,
            source=source,
            as_of=as_of,
            control_amount=control_amount,
            supplier_stated=supplier_stated,
        )

        approval_fx.additional_properties = d
        return approval_fx

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
