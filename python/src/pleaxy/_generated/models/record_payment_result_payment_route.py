from typing import Literal, Set, cast

RecordPaymentResultPaymentRoute = Literal["erp", "pleaxy"]

RECORD_PAYMENT_RESULT_PAYMENT_ROUTE_VALUES: Set[RecordPaymentResultPaymentRoute] = {
    "erp",
    "pleaxy",
}


def check_record_payment_result_payment_route(
    value: str,
) -> RecordPaymentResultPaymentRoute:
    if value in RECORD_PAYMENT_RESULT_PAYMENT_ROUTE_VALUES:
        return cast(RecordPaymentResultPaymentRoute, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECORD_PAYMENT_RESULT_PAYMENT_ROUTE_VALUES!r}"
    )
