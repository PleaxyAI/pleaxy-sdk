from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.invoice_supplier_view import InvoiceSupplierView
from ...types import UNSET, Response, Unset


def _get_kwargs(
    invoice_id: str,
    *,
    buyer: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["buyer"] = buyer

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/invoices/{invoice_id}/remind".format(
            invoice_id=invoice_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[InvoiceSupplierView]:
    if response.status_code == 201:
        response_201 = InvoiceSupplierView.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[InvoiceSupplierView]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    invoice_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    buyer: Union[Unset, str] = UNSET,
) -> Response[InvoiceSupplierView]:
    """[Supplier] Send a reminder for an invoice waiting on approval, or a payment reminder for an
    approved, unpaid one. At most one a day per invoice. When two buyers issued the same invoice id, add
    ?buyer=<buyer Workspace ID> (409 INVOICE_ID_AMBIGUOUS otherwise).

    Args:
        invoice_id (str):
        buyer (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvoiceSupplierView]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        buyer=buyer,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    invoice_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    buyer: Union[Unset, str] = UNSET,
) -> Optional[InvoiceSupplierView]:
    """[Supplier] Send a reminder for an invoice waiting on approval, or a payment reminder for an
    approved, unpaid one. At most one a day per invoice. When two buyers issued the same invoice id, add
    ?buyer=<buyer Workspace ID> (409 INVOICE_ID_AMBIGUOUS otherwise).

    Args:
        invoice_id (str):
        buyer (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvoiceSupplierView
    """

    return sync_detailed(
        invoice_id=invoice_id,
        client=client,
        buyer=buyer,
    ).parsed


async def asyncio_detailed(
    invoice_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    buyer: Union[Unset, str] = UNSET,
) -> Response[InvoiceSupplierView]:
    """[Supplier] Send a reminder for an invoice waiting on approval, or a payment reminder for an
    approved, unpaid one. At most one a day per invoice. When two buyers issued the same invoice id, add
    ?buyer=<buyer Workspace ID> (409 INVOICE_ID_AMBIGUOUS otherwise).

    Args:
        invoice_id (str):
        buyer (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvoiceSupplierView]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        buyer=buyer,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    invoice_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    buyer: Union[Unset, str] = UNSET,
) -> Optional[InvoiceSupplierView]:
    """[Supplier] Send a reminder for an invoice waiting on approval, or a payment reminder for an
    approved, unpaid one. At most one a day per invoice. When two buyers issued the same invoice id, add
    ?buyer=<buyer Workspace ID> (409 INVOICE_ID_AMBIGUOUS otherwise).

    Args:
        invoice_id (str):
        buyer (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvoiceSupplierView
    """

    return (
        await asyncio_detailed(
            invoice_id=invoice_id,
            client=client,
            buyer=buyer,
        )
    ).parsed
