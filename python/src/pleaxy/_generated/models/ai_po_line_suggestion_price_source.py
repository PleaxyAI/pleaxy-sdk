from typing import Literal, Set, cast

AiPoLineSuggestionPriceSource = Literal["billed", "contract", "list"]

AI_PO_LINE_SUGGESTION_PRICE_SOURCE_VALUES: Set[AiPoLineSuggestionPriceSource] = {
    "billed",
    "contract",
    "list",
}


def check_ai_po_line_suggestion_price_source(
    value: str,
) -> AiPoLineSuggestionPriceSource:
    if value in AI_PO_LINE_SUGGESTION_PRICE_SOURCE_VALUES:
        return cast(AiPoLineSuggestionPriceSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_PO_LINE_SUGGESTION_PRICE_SOURCE_VALUES!r}"
    )
