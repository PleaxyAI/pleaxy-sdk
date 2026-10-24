from typing import Literal, Set, cast

InboundEmailReasonCode = Literal[
    "autoReply",
    "dailyLimit",
    "notFulfillment",
    "otherOrder",
    "readingLimit",
    "refused",
    "unreadable",
]

INBOUND_EMAIL_REASON_CODE_VALUES: Set[InboundEmailReasonCode] = {
    "autoReply",
    "dailyLimit",
    "notFulfillment",
    "otherOrder",
    "readingLimit",
    "refused",
    "unreadable",
}


def check_inbound_email_reason_code(value: str) -> InboundEmailReasonCode:
    if value in INBOUND_EMAIL_REASON_CODE_VALUES:
        return cast(InboundEmailReasonCode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INBOUND_EMAIL_REASON_CODE_VALUES!r}"
    )
