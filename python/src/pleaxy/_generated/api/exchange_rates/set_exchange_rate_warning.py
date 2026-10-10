from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.set_exchange_rate_warning_result import SetExchangeRateWarningResult
from ...models.set_warning_pct_input import SetWarningPctInput
from ...types import Response


def _get_kwargs(
    *,
    body: SetWarningPctInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/exchange-rates",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SetExchangeRateWarningResult]:
    if response.status_code == 200:
        response_200 = SetExchangeRateWarningResult.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SetExchangeRateWarningResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SetWarningPctInput,
) -> Response[SetExchangeRateWarningResult]:
    """[Buyer] Set how far (percent, 0–100) an invoice's stated rate may be from the reference rate before
    the invoice is flagged. Default 5. Administrators only, signed-in session only.

    Args:
        body (SetWarningPctInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SetExchangeRateWarningResult]
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
    body: SetWarningPctInput,
) -> Optional[SetExchangeRateWarningResult]:
    """[Buyer] Set how far (percent, 0–100) an invoice's stated rate may be from the reference rate before
    the invoice is flagged. Default 5. Administrators only, signed-in session only.

    Args:
        body (SetWarningPctInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SetExchangeRateWarningResult
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SetWarningPctInput,
) -> Response[SetExchangeRateWarningResult]:
    """[Buyer] Set how far (percent, 0–100) an invoice's stated rate may be from the reference rate before
    the invoice is flagged. Default 5. Administrators only, signed-in session only.

    Args:
        body (SetWarningPctInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SetExchangeRateWarningResult]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SetWarningPctInput,
) -> Optional[SetExchangeRateWarningResult]:
    """[Buyer] Set how far (percent, 0–100) an invoice's stated rate may be from the reference rate before
    the invoice is flagged. Default 5. Administrators only, signed-in session only.

    Args:
        body (SetWarningPctInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SetExchangeRateWarningResult
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
