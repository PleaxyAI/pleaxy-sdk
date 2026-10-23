from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sync_event_page import SyncEventPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    after: Union[Unset, str] = UNSET,
    limit: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["after"] = after

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/sync/events",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SyncEventPage]:
    if response.status_code == 200:
        response_200 = SyncEventPage.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SyncEventPage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    after: Union[Unset, str] = UNSET,
    limit: Union[Unset, str] = UNSET,
) -> Response[SyncEventPage]:
    """[Both] What changed, oldest first, to keep another system in step: { events: [{ id, at, type,
    documentType, documentId, buyerWorkspaceId? }], nextCursor, hasMore }. A supplier gets
    purchase_order.issued|changed|canceled|rejected,
    invoice.received|approved|rejected|paid|payment_withdrawn|remittance_sent|credit_applied and
    credit_note.accepted|rejected; a buyer gets invoice.received, invoice.payment_failed,
    credit_note.received and purchase_order.updated / invoice.updated whenever one of its documents is
    decided or moves on. An event names the document only: read it with GetPurchaseOrder,
    GetPurchaseOrderDocument, GetInvoiceStatus or GetInvoiceRemittance (pass buyerWorkspaceId as
    ?buyer=). Pass nextCursor back as ?after= on the next call; call again at once while hasMore is
    true. ?limit= 1-500 (default 100). Events are kept 30 days and delivered at least once; the newest 5
    seconds wait for the next call. A buyer sees only the document types its procurement role can view.

    Args:
        after (Union[Unset, str]):
        limit (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SyncEventPage]
    """

    kwargs = _get_kwargs(
        after=after,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    after: Union[Unset, str] = UNSET,
    limit: Union[Unset, str] = UNSET,
) -> Optional[SyncEventPage]:
    """[Both] What changed, oldest first, to keep another system in step: { events: [{ id, at, type,
    documentType, documentId, buyerWorkspaceId? }], nextCursor, hasMore }. A supplier gets
    purchase_order.issued|changed|canceled|rejected,
    invoice.received|approved|rejected|paid|payment_withdrawn|remittance_sent|credit_applied and
    credit_note.accepted|rejected; a buyer gets invoice.received, invoice.payment_failed,
    credit_note.received and purchase_order.updated / invoice.updated whenever one of its documents is
    decided or moves on. An event names the document only: read it with GetPurchaseOrder,
    GetPurchaseOrderDocument, GetInvoiceStatus or GetInvoiceRemittance (pass buyerWorkspaceId as
    ?buyer=). Pass nextCursor back as ?after= on the next call; call again at once while hasMore is
    true. ?limit= 1-500 (default 100). Events are kept 30 days and delivered at least once; the newest 5
    seconds wait for the next call. A buyer sees only the document types its procurement role can view.

    Args:
        after (Union[Unset, str]):
        limit (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SyncEventPage
    """

    return sync_detailed(
        client=client,
        after=after,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    after: Union[Unset, str] = UNSET,
    limit: Union[Unset, str] = UNSET,
) -> Response[SyncEventPage]:
    """[Both] What changed, oldest first, to keep another system in step: { events: [{ id, at, type,
    documentType, documentId, buyerWorkspaceId? }], nextCursor, hasMore }. A supplier gets
    purchase_order.issued|changed|canceled|rejected,
    invoice.received|approved|rejected|paid|payment_withdrawn|remittance_sent|credit_applied and
    credit_note.accepted|rejected; a buyer gets invoice.received, invoice.payment_failed,
    credit_note.received and purchase_order.updated / invoice.updated whenever one of its documents is
    decided or moves on. An event names the document only: read it with GetPurchaseOrder,
    GetPurchaseOrderDocument, GetInvoiceStatus or GetInvoiceRemittance (pass buyerWorkspaceId as
    ?buyer=). Pass nextCursor back as ?after= on the next call; call again at once while hasMore is
    true. ?limit= 1-500 (default 100). Events are kept 30 days and delivered at least once; the newest 5
    seconds wait for the next call. A buyer sees only the document types its procurement role can view.

    Args:
        after (Union[Unset, str]):
        limit (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SyncEventPage]
    """

    kwargs = _get_kwargs(
        after=after,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    after: Union[Unset, str] = UNSET,
    limit: Union[Unset, str] = UNSET,
) -> Optional[SyncEventPage]:
    """[Both] What changed, oldest first, to keep another system in step: { events: [{ id, at, type,
    documentType, documentId, buyerWorkspaceId? }], nextCursor, hasMore }. A supplier gets
    purchase_order.issued|changed|canceled|rejected,
    invoice.received|approved|rejected|paid|payment_withdrawn|remittance_sent|credit_applied and
    credit_note.accepted|rejected; a buyer gets invoice.received, invoice.payment_failed,
    credit_note.received and purchase_order.updated / invoice.updated whenever one of its documents is
    decided or moves on. An event names the document only: read it with GetPurchaseOrder,
    GetPurchaseOrderDocument, GetInvoiceStatus or GetInvoiceRemittance (pass buyerWorkspaceId as
    ?buyer=). Pass nextCursor back as ?after= on the next call; call again at once while hasMore is
    true. ?limit= 1-500 (default 100). Events are kept 30 days and delivered at least once; the newest 5
    seconds wait for the next call. A buyer sees only the document types its procurement role can view.

    Args:
        after (Union[Unset, str]):
        limit (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SyncEventPage
    """

    return (
        await asyncio_detailed(
            client=client,
            after=after,
            limit=limit,
        )
    ).parsed
