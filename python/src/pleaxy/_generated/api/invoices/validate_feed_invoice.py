from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_feed_invoice_input import CreateFeedInvoiceInput
from ...models.feed_validation_result import FeedValidationResult
from ...types import Response


def _get_kwargs(
    connection_id: str,
    *,
    body: CreateFeedInvoiceInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/invoices/connections/{connection_id}/validate".format(
            connection_id=connection_id,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[FeedValidationResult]:
    if response.status_code == 200:
        response_200 = FeedValidationResult.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[FeedValidationResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    connection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateFeedInvoiceInput,
) -> Response[FeedValidationResult]:
    """[Supplier] Check an invoice document against one connected buyer exactly as SubmitFeedInvoice would,
    writing nothing: no invoice, no number reservation, no notification. Same key, scope, formats and
    refusals; the buyer's switch is reported (feedEnabled) instead of enforced; 200 test calls per
    connection per day.

    Args:
        connection_id (str):
        body (CreateFeedInvoiceInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FeedValidationResult]
    """

    kwargs = _get_kwargs(
        connection_id=connection_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    connection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateFeedInvoiceInput,
) -> Optional[FeedValidationResult]:
    """[Supplier] Check an invoice document against one connected buyer exactly as SubmitFeedInvoice would,
    writing nothing: no invoice, no number reservation, no notification. Same key, scope, formats and
    refusals; the buyer's switch is reported (feedEnabled) instead of enforced; 200 test calls per
    connection per day.

    Args:
        connection_id (str):
        body (CreateFeedInvoiceInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FeedValidationResult
    """

    return sync_detailed(
        connection_id=connection_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    connection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateFeedInvoiceInput,
) -> Response[FeedValidationResult]:
    """[Supplier] Check an invoice document against one connected buyer exactly as SubmitFeedInvoice would,
    writing nothing: no invoice, no number reservation, no notification. Same key, scope, formats and
    refusals; the buyer's switch is reported (feedEnabled) instead of enforced; 200 test calls per
    connection per day.

    Args:
        connection_id (str):
        body (CreateFeedInvoiceInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FeedValidationResult]
    """

    kwargs = _get_kwargs(
        connection_id=connection_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    connection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateFeedInvoiceInput,
) -> Optional[FeedValidationResult]:
    """[Supplier] Check an invoice document against one connected buyer exactly as SubmitFeedInvoice would,
    writing nothing: no invoice, no number reservation, no notification. Same key, scope, formats and
    refusals; the buyer's switch is reported (feedEnabled) instead of enforced; 200 test calls per
    connection per day.

    Args:
        connection_id (str):
        body (CreateFeedInvoiceInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FeedValidationResult
    """

    return (
        await asyncio_detailed(
            connection_id=connection_id,
            client=client,
            body=body,
        )
    ).parsed
