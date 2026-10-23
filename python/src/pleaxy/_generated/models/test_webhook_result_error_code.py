from typing import Literal, Set, cast

TestWebhookResultErrorCode = Literal[
    "blocked_address",
    "endpoint_off",
    "failed",
    "http_status",
    "redirect",
    "timeout",
    "too_large",
    "unreachable",
]

TEST_WEBHOOK_RESULT_ERROR_CODE_VALUES: Set[TestWebhookResultErrorCode] = {
    "blocked_address",
    "endpoint_off",
    "failed",
    "http_status",
    "redirect",
    "timeout",
    "too_large",
    "unreachable",
}


def check_test_webhook_result_error_code(value: str) -> TestWebhookResultErrorCode:
    if value in TEST_WEBHOOK_RESULT_ERROR_CODE_VALUES:
        return cast(TestWebhookResultErrorCode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TEST_WEBHOOK_RESULT_ERROR_CODE_VALUES!r}"
    )
