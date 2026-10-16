from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.remove_invoice_replacement_link_result import (
    RemoveInvoiceReplacementLinkResult,
)
from ...types import Response


def _get_kwargs(
    invoice_id: str,
    original_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": "/invoices/{invoice_id}/replaces/{original_id}".format(
            invoice_id=invoice_id,
            original_id=original_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[RemoveInvoiceReplacementLinkResult]:
    if response.status_code == 200:
        response_200 = RemoveInvoiceReplacementLinkResult.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[RemoveInvoiceReplacementLinkResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    invoice_id: str,
    original_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[RemoveInvoiceReplacementLinkResult]:
    """[Buyer] Undo a replacement link entered wrongly (credit notes spec §20), on both invoices. The
    rejected invoice an invoice corrects on its purchase order stays linked.

    Args:
        invoice_id (str):
        original_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoveInvoiceReplacementLinkResult]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        original_id=original_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    invoice_id: str,
    original_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[RemoveInvoiceReplacementLinkResult]:
    """[Buyer] Undo a replacement link entered wrongly (credit notes spec §20), on both invoices. The
    rejected invoice an invoice corrects on its purchase order stays linked.

    Args:
        invoice_id (str):
        original_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoveInvoiceReplacementLinkResult
    """

    return sync_detailed(
        invoice_id=invoice_id,
        original_id=original_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    invoice_id: str,
    original_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[RemoveInvoiceReplacementLinkResult]:
    """[Buyer] Undo a replacement link entered wrongly (credit notes spec §20), on both invoices. The
    rejected invoice an invoice corrects on its purchase order stays linked.

    Args:
        invoice_id (str):
        original_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoveInvoiceReplacementLinkResult]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        original_id=original_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    invoice_id: str,
    original_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[RemoveInvoiceReplacementLinkResult]:
    """[Buyer] Undo a replacement link entered wrongly (credit notes spec §20), on both invoices. The
    rejected invoice an invoice corrects on its purchase order stays linked.

    Args:
        invoice_id (str):
        original_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoveInvoiceReplacementLinkResult
    """

    return (
        await asyncio_detailed(
            invoice_id=invoice_id,
            original_id=original_id,
            client=client,
        )
    ).parsed
