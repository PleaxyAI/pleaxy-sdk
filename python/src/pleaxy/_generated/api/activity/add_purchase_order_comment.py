from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_comment_input import CreateCommentInput
from ...models.document_comment_view import DocumentCommentView
from ...types import UNSET, Response, Unset


def _get_kwargs(
    po_id: str,
    *,
    body: CreateCommentInput,
    buyer: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["buyer"] = buyer

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/purchase-orders/{po_id}/comments".format(
            po_id=po_id,
        ),
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DocumentCommentView]:
    if response.status_code == 201:
        response_201 = DocumentCommentView.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DocumentCommentView]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    po_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateCommentInput,
    buyer: Union[Unset, str] = UNSET,
) -> Response[DocumentCommentView]:
    """[Both] Comment on a purchase order - as AddInvoiceComment. Human session only.

    Args:
        po_id (str):
        buyer (Union[Unset, str]):
        body (CreateCommentInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DocumentCommentView]
    """

    kwargs = _get_kwargs(
        po_id=po_id,
        body=body,
        buyer=buyer,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    po_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateCommentInput,
    buyer: Union[Unset, str] = UNSET,
) -> Optional[DocumentCommentView]:
    """[Both] Comment on a purchase order - as AddInvoiceComment. Human session only.

    Args:
        po_id (str):
        buyer (Union[Unset, str]):
        body (CreateCommentInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DocumentCommentView
    """

    return sync_detailed(
        po_id=po_id,
        client=client,
        body=body,
        buyer=buyer,
    ).parsed


async def asyncio_detailed(
    po_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateCommentInput,
    buyer: Union[Unset, str] = UNSET,
) -> Response[DocumentCommentView]:
    """[Both] Comment on a purchase order - as AddInvoiceComment. Human session only.

    Args:
        po_id (str):
        buyer (Union[Unset, str]):
        body (CreateCommentInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DocumentCommentView]
    """

    kwargs = _get_kwargs(
        po_id=po_id,
        body=body,
        buyer=buyer,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    po_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateCommentInput,
    buyer: Union[Unset, str] = UNSET,
) -> Optional[DocumentCommentView]:
    """[Both] Comment on a purchase order - as AddInvoiceComment. Human session only.

    Args:
        po_id (str):
        buyer (Union[Unset, str]):
        body (CreateCommentInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DocumentCommentView
    """

    return (
        await asyncio_detailed(
            po_id=po_id,
            client=client,
            body=body,
            buyer=buyer,
        )
    ).parsed
