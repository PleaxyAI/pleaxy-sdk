from typing import Literal, Set, cast

FeedAttemptFormat = Literal[
    "cii", "cxml", "facturae", "fatturapa", "json", "nfe", "nfse", "ubl"
]

FEED_ATTEMPT_FORMAT_VALUES: Set[FeedAttemptFormat] = {
    "cii",
    "cxml",
    "facturae",
    "fatturapa",
    "json",
    "nfe",
    "nfse",
    "ubl",
}


def check_feed_attempt_format(value: str) -> FeedAttemptFormat:
    if value in FEED_ATTEMPT_FORMAT_VALUES:
        return cast(FeedAttemptFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FEED_ATTEMPT_FORMAT_VALUES!r}"
    )
