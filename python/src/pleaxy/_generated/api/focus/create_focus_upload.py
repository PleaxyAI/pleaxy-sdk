from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_focus_upload_input import CreateFocusUploadInput
from ...models.create_focus_upload_result import CreateFocusUploadResult
from ...types import Response


def _get_kwargs(
    *,
    body: CreateFocusUploadInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/focus-sources/uploads",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CreateFocusUploadResult]:
    if response.status_code == 201:
        response_201 = CreateFocusUploadResult.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CreateFocusUploadResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateFocusUploadInput,
) -> Response[CreateFocusUploadResult]:
    """[Buyer] Start a FOCUS file upload (.csv or .csv.gz, up to 500 MB): returns a presigned PUT URL valid
    a few minutes and the upload's id. PUT the file with the returned content type, then call
    CompleteFocusUpload. 'edit' on invoices.

    Args:
        body (CreateFocusUploadInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateFocusUploadResult]
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
    body: CreateFocusUploadInput,
) -> Optional[CreateFocusUploadResult]:
    """[Buyer] Start a FOCUS file upload (.csv or .csv.gz, up to 500 MB): returns a presigned PUT URL valid
    a few minutes and the upload's id. PUT the file with the returned content type, then call
    CompleteFocusUpload. 'edit' on invoices.

    Args:
        body (CreateFocusUploadInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateFocusUploadResult
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateFocusUploadInput,
) -> Response[CreateFocusUploadResult]:
    """[Buyer] Start a FOCUS file upload (.csv or .csv.gz, up to 500 MB): returns a presigned PUT URL valid
    a few minutes and the upload's id. PUT the file with the returned content type, then call
    CompleteFocusUpload. 'edit' on invoices.

    Args:
        body (CreateFocusUploadInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateFocusUploadResult]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateFocusUploadInput,
) -> Optional[CreateFocusUploadResult]:
    """[Buyer] Start a FOCUS file upload (.csv or .csv.gz, up to 500 MB): returns a presigned PUT URL valid
    a few minutes and the upload's id. PUT the file with the returned content type, then call
    CompleteFocusUpload. 'edit' on invoices.

    Args:
        body (CreateFocusUploadInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateFocusUploadResult
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
