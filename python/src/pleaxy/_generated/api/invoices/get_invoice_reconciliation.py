from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_invoice_reconciliation_result import GetInvoiceReconciliationResult
from ...types import Response


def _get_kwargs(
    invoice_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/invoices/{invoice_id}/reconciliation".format(
            invoice_id=invoice_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetInvoiceReconciliationResult]:
    if response.status_code == 200:
        response_200 = GetInvoiceReconciliationResult.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetInvoiceReconciliationResult]:
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
) -> Response[GetInvoiceReconciliationResult]:
    """[Buyer] An invoice's match result as the UCP vendor capability ai.pleaxy.procurement.reconciliation
    returns it (https://pleaxy.ai/docs/mcp#ucp): the order, contract and usage records it was checked
    against, each check group's result, every failure by check name with Pleaxy's code and figures, and
    the first failure in a fixed order. Read-only: it changes nothing. Codes and figures only, no plain-
    language text. Pleaxy stores failures, not passes, so a group says no_failures_recorded where its
    check runs only when its data is there.

    Args:
        invoice_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetInvoiceReconciliationResult]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    invoice_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetInvoiceReconciliationResult]:
    """[Buyer] An invoice's match result as the UCP vendor capability ai.pleaxy.procurement.reconciliation
    returns it (https://pleaxy.ai/docs/mcp#ucp): the order, contract and usage records it was checked
    against, each check group's result, every failure by check name with Pleaxy's code and figures, and
    the first failure in a fixed order. Read-only: it changes nothing. Codes and figures only, no plain-
    language text. Pleaxy stores failures, not passes, so a group says no_failures_recorded where its
    check runs only when its data is there.

    Args:
        invoice_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetInvoiceReconciliationResult
    """

    return sync_detailed(
        invoice_id=invoice_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    invoice_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetInvoiceReconciliationResult]:
    """[Buyer] An invoice's match result as the UCP vendor capability ai.pleaxy.procurement.reconciliation
    returns it (https://pleaxy.ai/docs/mcp#ucp): the order, contract and usage records it was checked
    against, each check group's result, every failure by check name with Pleaxy's code and figures, and
    the first failure in a fixed order. Read-only: it changes nothing. Codes and figures only, no plain-
    language text. Pleaxy stores failures, not passes, so a group says no_failures_recorded where its
    check runs only when its data is there.

    Args:
        invoice_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetInvoiceReconciliationResult]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    invoice_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetInvoiceReconciliationResult]:
    """[Buyer] An invoice's match result as the UCP vendor capability ai.pleaxy.procurement.reconciliation
    returns it (https://pleaxy.ai/docs/mcp#ucp): the order, contract and usage records it was checked
    against, each check group's result, every failure by check name with Pleaxy's code and figures, and
    the first failure in a fixed order. Read-only: it changes nothing. Codes and figures only, no plain-
    language text. Pleaxy stores failures, not passes, so a group says no_failures_recorded where its
    check runs only when its data is there.

    Args:
        invoice_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetInvoiceReconciliationResult
    """

    return (
        await asyncio_detailed(
            invoice_id=invoice_id,
            client=client,
        )
    ).parsed
