from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.convert_purchase_request_input import ConvertPurchaseRequestInput
from ...models.convert_purchase_request_result import ConvertPurchaseRequestResult
from ...types import Response


def _get_kwargs(
    request_id: str,
    *,
    body: ConvertPurchaseRequestInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/purchase-requests/{request_id}/convert".format(
            request_id=request_id,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ConvertPurchaseRequestResult]:
    if response.status_code == 201:
        response_201 = ConvertPurchaseRequestResult.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ConvertPurchaseRequestResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    request_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ConvertPurchaseRequestInput,
) -> Response[ConvertPurchaseRequestResult]:
    """[Buyer] Order an approved request: a purchase order from its lines, supplier, cost center, GL
    account and quote, each overridable. Within what was approved it keeps the request's approval.

    Args:
        request_id (str):
        body (ConvertPurchaseRequestInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConvertPurchaseRequestResult]
    """

    kwargs = _get_kwargs(
        request_id=request_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    request_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ConvertPurchaseRequestInput,
) -> Optional[ConvertPurchaseRequestResult]:
    """[Buyer] Order an approved request: a purchase order from its lines, supplier, cost center, GL
    account and quote, each overridable. Within what was approved it keeps the request's approval.

    Args:
        request_id (str):
        body (ConvertPurchaseRequestInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConvertPurchaseRequestResult
    """

    return sync_detailed(
        request_id=request_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    request_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ConvertPurchaseRequestInput,
) -> Response[ConvertPurchaseRequestResult]:
    """[Buyer] Order an approved request: a purchase order from its lines, supplier, cost center, GL
    account and quote, each overridable. Within what was approved it keeps the request's approval.

    Args:
        request_id (str):
        body (ConvertPurchaseRequestInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConvertPurchaseRequestResult]
    """

    kwargs = _get_kwargs(
        request_id=request_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    request_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ConvertPurchaseRequestInput,
) -> Optional[ConvertPurchaseRequestResult]:
    """[Buyer] Order an approved request: a purchase order from its lines, supplier, cost center, GL
    account and quote, each overridable. Within what was approved it keeps the request's approval.

    Args:
        request_id (str):
        body (ConvertPurchaseRequestInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConvertPurchaseRequestResult
    """

    return (
        await asyncio_detailed(
            request_id=request_id,
            client=client,
            body=body,
        )
    ).parsed
