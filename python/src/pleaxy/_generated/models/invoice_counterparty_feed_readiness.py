from typing import Literal, Set, cast

InvoiceCounterpartyFeedReadiness = Literal[
    "live", "no_key", "not_connected", "off", "tested", "untested"
]

INVOICE_COUNTERPARTY_FEED_READINESS_VALUES: Set[InvoiceCounterpartyFeedReadiness] = {
    "live",
    "no_key",
    "not_connected",
    "off",
    "tested",
    "untested",
}


def check_invoice_counterparty_feed_readiness(
    value: str,
) -> InvoiceCounterpartyFeedReadiness:
    if value in INVOICE_COUNTERPARTY_FEED_READINESS_VALUES:
        return cast(InvoiceCounterpartyFeedReadiness, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_COUNTERPARTY_FEED_READINESS_VALUES!r}"
    )
