from typing import Literal, Set, cast

ReceiptSource = Literal["api", "app", "assistant", "import", "supplier"]

RECEIPT_SOURCE_VALUES: Set[ReceiptSource] = {
    "api",
    "app",
    "assistant",
    "import",
    "supplier",
}


def check_receipt_source(value: str) -> ReceiptSource:
    if value in RECEIPT_SOURCE_VALUES:
        return cast(ReceiptSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECEIPT_SOURCE_VALUES!r}"
    )
