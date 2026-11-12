from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Type,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sourcing_round_feedback_by_supplier_additional_property_type_0 import (
        SourcingRoundFeedbackBySupplierAdditionalPropertyType0,
    )
    from ..models.sourcing_round_feedback_by_supplier_additional_property_type_1 import (
        SourcingRoundFeedbackBySupplierAdditionalPropertyType1,
    )


T = TypeVar("T", bound="SourcingRoundFeedbackBySupplier")


@_attrs_define
class SourcingRoundFeedbackBySupplier:
    """ """

    additional_properties: Dict[
        str,
        Union[
            "SourcingRoundFeedbackBySupplierAdditionalPropertyType0",
            "SourcingRoundFeedbackBySupplierAdditionalPropertyType1",
        ],
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.sourcing_round_feedback_by_supplier_additional_property_type_0 import (
            SourcingRoundFeedbackBySupplierAdditionalPropertyType0,
        )

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, SourcingRoundFeedbackBySupplierAdditionalPropertyType0):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sourcing_round_feedback_by_supplier_additional_property_type_0 import (
            SourcingRoundFeedbackBySupplierAdditionalPropertyType0,
        )
        from ..models.sourcing_round_feedback_by_supplier_additional_property_type_1 import (
            SourcingRoundFeedbackBySupplierAdditionalPropertyType1,
        )

        d = src_dict.copy()
        sourcing_round_feedback_by_supplier = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(
                data: object,
            ) -> Union[
                "SourcingRoundFeedbackBySupplierAdditionalPropertyType0",
                "SourcingRoundFeedbackBySupplierAdditionalPropertyType1",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_0 = SourcingRoundFeedbackBySupplierAdditionalPropertyType0.from_dict(
                        data
                    )

                    return additional_property_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                additional_property_type_1 = (
                    SourcingRoundFeedbackBySupplierAdditionalPropertyType1.from_dict(
                        data
                    )
                )

                return additional_property_type_1

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        sourcing_round_feedback_by_supplier.additional_properties = (
            additional_properties
        )
        return sourcing_round_feedback_by_supplier

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> Union[
        "SourcingRoundFeedbackBySupplierAdditionalPropertyType0",
        "SourcingRoundFeedbackBySupplierAdditionalPropertyType1",
    ]:
        return self.additional_properties[key]

    def __setitem__(
        self,
        key: str,
        value: Union[
            "SourcingRoundFeedbackBySupplierAdditionalPropertyType0",
            "SourcingRoundFeedbackBySupplierAdditionalPropertyType1",
        ],
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
