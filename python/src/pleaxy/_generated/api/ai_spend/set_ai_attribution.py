from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ai_attribution_response import AiAttributionResponse
from ...models.set_ai_attribution_input import SetAiAttributionInput
from ...types import Response


def _get_kwargs(
    *,
    body: SetAiAttributionInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/ai-spend/attribution",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AiAttributionResponse]:
    if response.status_code == 200:
        response_200 = AiAttributionResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AiAttributionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SetAiAttributionInput,
) -> Response[AiAttributionResponse]:
    """[Buyer] Replaces every attribution rule, in order, from the version read (409 when someone saved
    since). A tag or label rule needs its key; the cost center must be one of the workspace's. An AWS
    tag or Google Cloud label rule makes the next sync split that account's AI lines by it. 'edit' on
    purchase orders.

    Args:
        body (SetAiAttributionInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AiAttributionResponse]
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
    body: SetAiAttributionInput,
) -> Optional[AiAttributionResponse]:
    """[Buyer] Replaces every attribution rule, in order, from the version read (409 when someone saved
    since). A tag or label rule needs its key; the cost center must be one of the workspace's. An AWS
    tag or Google Cloud label rule makes the next sync split that account's AI lines by it. 'edit' on
    purchase orders.

    Args:
        body (SetAiAttributionInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AiAttributionResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SetAiAttributionInput,
) -> Response[AiAttributionResponse]:
    """[Buyer] Replaces every attribution rule, in order, from the version read (409 when someone saved
    since). A tag or label rule needs its key; the cost center must be one of the workspace's. An AWS
    tag or Google Cloud label rule makes the next sync split that account's AI lines by it. 'edit' on
    purchase orders.

    Args:
        body (SetAiAttributionInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AiAttributionResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SetAiAttributionInput,
) -> Optional[AiAttributionResponse]:
    """[Buyer] Replaces every attribution rule, in order, from the version read (409 when someone saved
    since). A tag or label rule needs its key; the cost center must be one of the workspace's. An AWS
    tag or Google Cloud label rule makes the next sync split that account's AI lines by it. 'edit' on
    purchase orders.

    Args:
        body (SetAiAttributionInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AiAttributionResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
