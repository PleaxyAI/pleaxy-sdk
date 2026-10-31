from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ai_draft_orders_result import AiDraftOrdersResult
from ...models.draft_ai_orders_input import DraftAiOrdersInput
from ...types import Response


def _get_kwargs(
    *,
    body: DraftAiOrdersInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/ai-spend/draft-orders",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AiDraftOrdersResult]:
    if response.status_code == 200:
        response_200 = AiDraftOrdersResult.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AiDraftOrdersResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: DraftAiOrdersInput,
) -> Response[AiDraftOrdersResult]:
    """[Buyer] Drafts an order for each invoicer named, for the period (default this month): one line per
    model and meter of last month's usage at the contract rate (else the list price), each quantity the
    forecast from this month so far, scaled to the gap when open orders already cover part of it. With
    scope account, a cloud account from accounts gets one amount line instead (everything the account
    bills, up to the gap, to the month's end). Returns the drafts and, for an invoicer with nothing to
    base an order on or no supplier on the list, why it was skipped. Drafts go through the usual
    approval when submitted. 'create' on purchase orders.

    Args:
        body (DraftAiOrdersInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AiDraftOrdersResult]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: DraftAiOrdersInput,
) -> Optional[AiDraftOrdersResult]:
    """[Buyer] Drafts an order for each invoicer named, for the period (default this month): one line per
    model and meter of last month's usage at the contract rate (else the list price), each quantity the
    forecast from this month so far, scaled to the gap when open orders already cover part of it. With
    scope account, a cloud account from accounts gets one amount line instead (everything the account
    bills, up to the gap, to the month's end). Returns the drafts and, for an invoicer with nothing to
    base an order on or no supplier on the list, why it was skipped. Drafts go through the usual
    approval when submitted. 'create' on purchase orders.

    Args:
        body (DraftAiOrdersInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AiDraftOrdersResult
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: DraftAiOrdersInput,
) -> Response[AiDraftOrdersResult]:
    """[Buyer] Drafts an order for each invoicer named, for the period (default this month): one line per
    model and meter of last month's usage at the contract rate (else the list price), each quantity the
    forecast from this month so far, scaled to the gap when open orders already cover part of it. With
    scope account, a cloud account from accounts gets one amount line instead (everything the account
    bills, up to the gap, to the month's end). Returns the drafts and, for an invoicer with nothing to
    base an order on or no supplier on the list, why it was skipped. Drafts go through the usual
    approval when submitted. 'create' on purchase orders.

    Args:
        body (DraftAiOrdersInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AiDraftOrdersResult]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: DraftAiOrdersInput,
) -> Optional[AiDraftOrdersResult]:
    """[Buyer] Drafts an order for each invoicer named, for the period (default this month): one line per
    model and meter of last month's usage at the contract rate (else the list price), each quantity the
    forecast from this month so far, scaled to the gap when open orders already cover part of it. With
    scope account, a cloud account from accounts gets one amount line instead (everything the account
    bills, up to the gap, to the month's end). Returns the drafts and, for an invoicer with nothing to
    base an order on or no supplier on the list, why it was skipped. Drafts go through the usual
    approval when submitted. 'create' on purchase orders.

    Args:
        body (DraftAiOrdersInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AiDraftOrdersResult
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
