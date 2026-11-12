from typing import Literal, Set, cast

SourcingAttachmentSource = Literal["request", "upload"]

SOURCING_ATTACHMENT_SOURCE_VALUES: Set[SourcingAttachmentSource] = {
    "request",
    "upload",
}


def check_sourcing_attachment_source(value: str) -> SourcingAttachmentSource:
    if value in SOURCING_ATTACHMENT_SOURCE_VALUES:
        return cast(SourcingAttachmentSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SOURCING_ATTACHMENT_SOURCE_VALUES!r}"
    )
