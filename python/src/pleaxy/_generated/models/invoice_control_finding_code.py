from typing import Literal, Set, cast

InvoiceControlFindingCode = Literal[
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

INVOICE_CONTROL_FINDING_CODE_VALUES: Set[InvoiceControlFindingCode] = {
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


def check_invoice_control_finding_code(value: str) -> InvoiceControlFindingCode:
    if value in INVOICE_CONTROL_FINDING_CODE_VALUES:
        return cast(InvoiceControlFindingCode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_CONTROL_FINDING_CODE_VALUES!r}"
    )
