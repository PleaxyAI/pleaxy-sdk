from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.punchout_line_origin_kind import (
    PunchoutLineOriginKind,
    check_punchout_line_origin_kind,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.punchout_line_origin_classification import (
        PunchoutLineOriginClassification,
    )


T = TypeVar("T", bound="PunchoutLineOrigin")


@_attrs_define
class PunchoutLineOrigin:
    """
    Attributes:
        kind (Union[Unset, PunchoutLineOriginKind]):
        store_id (Union[Unset, str]):
        session_id (Union[Unset, str]):
        cart_line_no (Union[Unset, float]):
        supplier_part_id (Union[Unset, str]):
        supplier_part_auxiliary_id (Union[Unset, str]):
        manufacturer_part_id (Union[Unset, str]):
        manufacturer_name (Union[Unset, str]):
        classification (Union[Unset, PunchoutLineOriginClassification]):
        evidence_unit_price (Union[Unset, float]):
        evidence_quantity (Union[Unset, float]):
        edited (Union[Unset, bool]):
    """

    kind: Union[Unset, PunchoutLineOriginKind] = UNSET
    store_id: Union[Unset, str] = UNSET
    session_id: Union[Unset, str] = UNSET
    cart_line_no: Union[Unset, float] = UNSET
    supplier_part_id: Union[Unset, str] = UNSET
    supplier_part_auxiliary_id: Union[Unset, str] = UNSET
    manufacturer_part_id: Union[Unset, str] = UNSET
    manufacturer_name: Union[Unset, str] = UNSET
    classification: Union[Unset, "PunchoutLineOriginClassification"] = UNSET
    evidence_unit_price: Union[Unset, float] = UNSET
    evidence_quantity: Union[Unset, float] = UNSET
    edited: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        store_id = self.store_id

        session_id = self.session_id

        cart_line_no = self.cart_line_no

        supplier_part_id = self.supplier_part_id

        supplier_part_auxiliary_id = self.supplier_part_auxiliary_id

        manufacturer_part_id = self.manufacturer_part_id

        manufacturer_name = self.manufacturer_name

        classification: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.classification, Unset):
            classification = self.classification.to_dict()

        evidence_unit_price = self.evidence_unit_price

        evidence_quantity = self.evidence_quantity

        edited = self.edited

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if store_id is not UNSET:
            field_dict["storeId"] = store_id
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id
        if cart_line_no is not UNSET:
            field_dict["cartLineNo"] = cart_line_no
        if supplier_part_id is not UNSET:
            field_dict["supplierPartId"] = supplier_part_id
        if supplier_part_auxiliary_id is not UNSET:
            field_dict["supplierPartAuxiliaryId"] = supplier_part_auxiliary_id
        if manufacturer_part_id is not UNSET:
            field_dict["manufacturerPartId"] = manufacturer_part_id
        if manufacturer_name is not UNSET:
            field_dict["manufacturerName"] = manufacturer_name
        if classification is not UNSET:
            field_dict["classification"] = classification
        if evidence_unit_price is not UNSET:
            field_dict["evidenceUnitPrice"] = evidence_unit_price
        if evidence_quantity is not UNSET:
            field_dict["evidenceQuantity"] = evidence_quantity
        if edited is not UNSET:
            field_dict["edited"] = edited

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.punchout_line_origin_classification import (
            PunchoutLineOriginClassification,
        )

        d = src_dict.copy()
        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, PunchoutLineOriginKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_punchout_line_origin_kind(_kind)

        store_id = d.pop("storeId", UNSET)

        session_id = d.pop("sessionId", UNSET)

        cart_line_no = d.pop("cartLineNo", UNSET)

        supplier_part_id = d.pop("supplierPartId", UNSET)

        supplier_part_auxiliary_id = d.pop("supplierPartAuxiliaryId", UNSET)

        manufacturer_part_id = d.pop("manufacturerPartId", UNSET)

        manufacturer_name = d.pop("manufacturerName", UNSET)

        _classification = d.pop("classification", UNSET)
        classification: Union[Unset, PunchoutLineOriginClassification]
        if isinstance(_classification, Unset):
            classification = UNSET
        else:
            classification = PunchoutLineOriginClassification.from_dict(_classification)

        evidence_unit_price = d.pop("evidenceUnitPrice", UNSET)

        evidence_quantity = d.pop("evidenceQuantity", UNSET)

        edited = d.pop("edited", UNSET)

        punchout_line_origin = cls(
            kind=kind,
            store_id=store_id,
            session_id=session_id,
            cart_line_no=cart_line_no,
            supplier_part_id=supplier_part_id,
            supplier_part_auxiliary_id=supplier_part_auxiliary_id,
            manufacturer_part_id=manufacturer_part_id,
            manufacturer_name=manufacturer_name,
            classification=classification,
            evidence_unit_price=evidence_unit_price,
            evidence_quantity=evidence_quantity,
            edited=edited,
        )

        punchout_line_origin.additional_properties = d
        return punchout_line_origin

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
