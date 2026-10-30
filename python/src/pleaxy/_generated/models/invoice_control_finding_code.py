from typing import Literal, Set, cast

InvoiceControlFindingCode = Literal[
    "ai_batch_discount_missing",
    "ai_cache_discount_missing",
    "ai_capacity_underused",
    "ai_commitment_exceeded",
    "ai_double_billed",
    "ai_price_cut_not_applied",
    "ai_rate_above_contract",
    "ai_rate_above_list",
    "ai_tokens_mismatch",
    "commitment_shortfall_overbilled",
    "contract_cap_exceeded",
    "contract_check_failed",
    "contract_discount_missing",
    "contract_max_unit_price_exceeded",
    "contract_not_active",
    "contract_outside_term",
    "contract_rate_exceeded",
    "fixed_discount_missing",
    "po_balance_exceeded",
    "po_line_amount_exceeded",
    "po_line_missing",
    "po_line_price_exceeded",
    "po_line_qty_exceeded",
    "po_line_unassigned",
    "receipt_amount_exceeded",
    "receipt_missing",
    "receipt_qty_exceeded",
    "tier_price_exceeded",
    "usage_grew",
]

INVOICE_CONTROL_FINDING_CODE_VALUES: Set[InvoiceControlFindingCode] = {
    "ai_batch_discount_missing",
    "ai_cache_discount_missing",
    "ai_capacity_underused",
    "ai_commitment_exceeded",
    "ai_double_billed",
    "ai_price_cut_not_applied",
    "ai_rate_above_contract",
    "ai_rate_above_list",
    "ai_tokens_mismatch",
    "commitment_shortfall_overbilled",
    "contract_cap_exceeded",
    "contract_check_failed",
    "contract_discount_missing",
    "contract_max_unit_price_exceeded",
    "contract_not_active",
    "contract_outside_term",
    "contract_rate_exceeded",
    "fixed_discount_missing",
    "po_balance_exceeded",
    "po_line_amount_exceeded",
    "po_line_missing",
    "po_line_price_exceeded",
    "po_line_qty_exceeded",
    "po_line_unassigned",
    "receipt_amount_exceeded",
    "receipt_missing",
    "receipt_qty_exceeded",
    "tier_price_exceeded",
    "usage_grew",
}


def check_invoice_control_finding_code(value: str) -> InvoiceControlFindingCode:
    if value in INVOICE_CONTROL_FINDING_CODE_VALUES:
        return cast(InvoiceControlFindingCode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_CONTROL_FINDING_CODE_VALUES!r}"
    )
