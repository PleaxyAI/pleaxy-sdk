from typing import Literal, Set, cast

SourcingRoundFeedbackBySupplierAdditionalPropertyType0Kind = Literal["rank"]

SOURCING_ROUND_FEEDBACK_BY_SUPPLIER_ADDITIONAL_PROPERTY_TYPE_0_KIND_VALUES: Set[
    SourcingRoundFeedbackBySupplierAdditionalPropertyType0Kind
] = {
    "rank",
}


def check_sourcing_round_feedback_by_supplier_additional_property_type_0_kind(
    value: str,
) -> SourcingRoundFeedbackBySupplierAdditionalPropertyType0Kind:
    if (
        value
        in SOURCING_ROUND_FEEDBACK_BY_SUPPLIER_ADDITIONAL_PROPERTY_TYPE_0_KIND_VALUES
    ):
        return cast(SourcingRoundFeedbackBySupplierAdditionalPropertyType0Kind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SOURCING_ROUND_FEEDBACK_BY_SUPPLIER_ADDITIONAL_PROPERTY_TYPE_0_KIND_VALUES!r}"
    )
