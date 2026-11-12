from typing import Literal, Set, cast

SourcingRoundFeedbackBySupplierAdditionalPropertyType1Kind = Literal["gap"]

SOURCING_ROUND_FEEDBACK_BY_SUPPLIER_ADDITIONAL_PROPERTY_TYPE_1_KIND_VALUES: Set[
    SourcingRoundFeedbackBySupplierAdditionalPropertyType1Kind
] = {
    "gap",
}


def check_sourcing_round_feedback_by_supplier_additional_property_type_1_kind(
    value: str,
) -> SourcingRoundFeedbackBySupplierAdditionalPropertyType1Kind:
    if (
        value
        in SOURCING_ROUND_FEEDBACK_BY_SUPPLIER_ADDITIONAL_PROPERTY_TYPE_1_KIND_VALUES
    ):
        return cast(SourcingRoundFeedbackBySupplierAdditionalPropertyType1Kind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SOURCING_ROUND_FEEDBACK_BY_SUPPLIER_ADDITIONAL_PROPERTY_TYPE_1_KIND_VALUES!r}"
    )
