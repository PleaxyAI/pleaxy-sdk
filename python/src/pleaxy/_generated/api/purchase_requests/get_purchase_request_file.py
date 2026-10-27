from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_purchase_request_file_result import GetPurchaseRequestFileResult
from ...types import Response


def _get_kwargs(
    request_id: str,
    file_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/purchase-requests/{request_id}/files/{file_id}".format(
            request_id=request_id,
            file_id=file_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetPurchaseRequestFileResult]:
    if response.status_code == 200:
        response_200 = GetPurchaseRequestFileResult.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetPurchaseRequestFileResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    request_id: str,
    file_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetPurchaseRequestFileResult]:
    """[Buyer] A short-lived link to a file answering one of the request's questions, for whoever may see
    the request

    Args:
        request_id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPurchaseRequestFileResult]
    """

    kwargs = _get_kwargs(
        request_id=request_id,
        file_id=file_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    request_id: str,
    file_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetPurchaseRequestFileResult]:
    """[Buyer] A short-lived link to a file answering one of the request's questions, for whoever may see
    the request

    Args:
        request_id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPurchaseRequestFileResult
    """

    return sync_detailed(
        request_id=request_id,
        file_id=file_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    request_id: str,
    file_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetPurchaseRequestFileResult]:
    """[Buyer] A short-lived link to a file answering one of the request's questions, for whoever may see
    the request

    Args:
        request_id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPurchaseRequestFileResult]
    """

    kwargs = _get_kwargs(
        request_id=request_id,
        file_id=file_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    request_id: str,
    file_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetPurchaseRequestFileResult]:
    """[Buyer] A short-lived link to a file answering one of the request's questions, for whoever may see
    the request

    Args:
        request_id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPurchaseRequestFileResult
    """

    return (
        await asyncio_detailed(
            request_id=request_id,
            file_id=file_id,
            client=client,
        )
    ).parsed
