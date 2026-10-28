from typing import Literal, Set, cast

GetInvoiceBankAccountResultHold = Literal["differs_from_file", "first_payment"]

GET_INVOICE_BANK_ACCOUNT_RESULT_HOLD_VALUES: Set[GetInvoiceBankAccountResultHold] = {
    "differs_from_file",
    "first_payment",
}


def check_get_invoice_bank_account_result_hold(
    value: str,
) -> GetInvoiceBankAccountResultHold:
    if value in GET_INVOICE_BANK_ACCOUNT_RESULT_HOLD_VALUES:
        return cast(GetInvoiceBankAccountResultHold, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_BANK_ACCOUNT_RESULT_HOLD_VALUES!r}"
    )
