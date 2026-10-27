from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.request_file_upload_input import RequestFileUploadInput
from ...models.request_purchase_request_file_upload_result import (
    RequestPurchaseRequestFileUploadResult,
)
from ...types import Response


def _get_kwargs(
    *,
    body: RequestFileUploadInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/purchase-requests/files/upload-url",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[RequestPurchaseRequestFileUploadResult]:
    if response.status_code == 200:
        response_200 = RequestPurchaseRequestFileUploadResult.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[RequestPurchaseRequestFileUploadResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: RequestFileUploadInput,
) -> Response[RequestPurchaseRequestFileUploadResult]:
    """[Buyer] A presigned URL to upload the answer to a request form's 'file' question (PDF, image, Word,
    Excel, CSV or text, up to 25 MB). PUT the file there, then save the answer with the returned fileId.
    Any workspace member, before or after the request exists.

    Args:
        body (RequestFileUploadInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequestPurchaseRequestFileUploadResult]
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
    body: RequestFileUploadInput,
) -> Optional[RequestPurchaseRequestFileUploadResult]:
    """[Buyer] A presigned URL to upload the answer to a request form's 'file' question (PDF, image, Word,
    Excel, CSV or text, up to 25 MB). PUT the file there, then save the answer with the returned fileId.
    Any workspace member, before or after the request exists.

    Args:
        body (RequestFileUploadInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequestPurchaseRequestFileUploadResult
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: RequestFileUploadInput,
) -> Response[RequestPurchaseRequestFileUploadResult]:
    """[Buyer] A presigned URL to upload the answer to a request form's 'file' question (PDF, image, Word,
    Excel, CSV or text, up to 25 MB). PUT the file there, then save the answer with the returned fileId.
    Any workspace member, before or after the request exists.

    Args:
        body (RequestFileUploadInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequestPurchaseRequestFileUploadResult]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: RequestFileUploadInput,
) -> Optional[RequestPurchaseRequestFileUploadResult]:
    """[Buyer] A presigned URL to upload the answer to a request form's 'file' question (PDF, image, Word,
    Excel, CSV or text, up to 25 MB). PUT the file there, then save the answer with the returned fileId.
    Any workspace member, before or after the request exists.

    Args:
        body (RequestFileUploadInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequestPurchaseRequestFileUploadResult
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
