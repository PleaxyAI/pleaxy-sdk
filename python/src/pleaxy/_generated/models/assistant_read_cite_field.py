from typing import Literal, Set, cast

AssistantReadCiteField = Literal[
    "declined",
    "evaluation",
    "leadTime",
    "neededBy",
    "paymentTerms",
    "risk",
    "score",
    "total",
    "unitPrice",
    "validUntil",
    "weighted",
]

ASSISTANT_READ_CITE_FIELD_VALUES: Set[AssistantReadCiteField] = {
    "declined",
    "evaluation",
    "leadTime",
    "neededBy",
    "paymentTerms",
    "risk",
    "score",
    "total",
    "unitPrice",
    "validUntil",
    "weighted",
}


def check_assistant_read_cite_field(value: str) -> AssistantReadCiteField:
    if value in ASSISTANT_READ_CITE_FIELD_VALUES:
        return cast(AssistantReadCiteField, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ASSISTANT_READ_CITE_FIELD_VALUES!r}"
    )
