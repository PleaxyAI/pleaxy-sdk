from typing import Literal, Set, cast

FeedValidationResultFindingsItemCode = Literal[
    "contract_cap_exceeded",
    "contract_check_failed",
    "contract_max_unit_price_exceeded",
    "contract_not_active",
    "contract_outside_term",
    "contract_rate_exceeded",
    "po_balance_exceeded",
    "po_line_amount_exceeded",
    "po_line_missing",
    "po_line_price_exceeded",
    "po_line_qty_exceeded",
    "po_line_unassigned",
    "receipt_amount_exceeded",
    "receipt_missing",
    "receipt_qty_exceeded",
]

FEED_VALIDATION_RESULT_FINDINGS_ITEM_CODE_VALUES: Set[
    FeedValidationResultFindingsItemCode
] = {
    "contract_cap_exceeded",
    "contract_check_failed",
    "contract_max_unit_price_exceeded",
    "contract_not_active",
    "contract_outside_term",
    "contract_rate_exceeded",
    "po_balance_exceeded",
    "po_line_amount_exceeded",
    "po_line_missing",
    "po_line_price_exceeded",
    "po_line_qty_exceeded",
    "po_line_unassigned",
    "receipt_amount_exceeded",
    "receipt_missing",
    "receipt_qty_exceeded",
}


def check_feed_validation_result_findings_item_code(
    value: str,
) -> FeedValidationResultFindingsItemCode:
    if value in FEED_VALIDATION_RESULT_FINDINGS_ITEM_CODE_VALUES:
        return cast(FeedValidationResultFindingsItemCode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FEED_VALIDATION_RESULT_FINDINGS_ITEM_CODE_VALUES!r}"
    )
