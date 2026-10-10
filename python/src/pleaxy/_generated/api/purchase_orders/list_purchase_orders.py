from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.purchase_order import PurchaseOrder
from ...models.purchase_order_supplier_view import PurchaseOrderSupplierView
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    from_: Union[Unset, str] = UNSET,
    to: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["from"] = from_

    params["to"] = to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/purchase-orders",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List[Union["PurchaseOrder", "PurchaseOrderSupplierView"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:

            def _parse_response_200_item(
                data: object,
            ) -> Union["PurchaseOrder", "PurchaseOrderSupplierView"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_list_purchase_orders_item_type_0 = (
                        PurchaseOrder.from_dict(data)
                    )

                    return componentsschemas_list_purchase_orders_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_list_purchase_orders_item_type_1 = (
                    PurchaseOrderSupplierView.from_dict(data)
                )

                return componentsschemas_list_purchase_orders_item_type_1

            response_200_item = _parse_response_200_item(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List[Union["PurchaseOrder", "PurchaseOrderSupplierView"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    from_: Union[Unset, str] = UNSET,
    to: Union[Unset, str] = UNSET,
) -> Response[List[Union["PurchaseOrder", "PurchaseOrderSupplierView"]]]:
    """[Both] List purchase orders - optionally scoped to a createdAt range via ?from=&to=. A Supplier
    caller gets a reduced view (see GetPurchaseOrder).

    Args:
        from_ (Union[Unset, str]):
        to (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List[Union['PurchaseOrder', 'PurchaseOrderSupplierView']]]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    from_: Union[Unset, str] = UNSET,
    to: Union[Unset, str] = UNSET,
) -> Optional[List[Union["PurchaseOrder", "PurchaseOrderSupplierView"]]]:
    """[Both] List purchase orders - optionally scoped to a createdAt range via ?from=&to=. A Supplier
    caller gets a reduced view (see GetPurchaseOrder).

    Args:
        from_ (Union[Unset, str]):
        to (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List[Union['PurchaseOrder', 'PurchaseOrderSupplierView']]
    """

    return sync_detailed(
        client=client,
        from_=from_,
        to=to,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    from_: Union[Unset, str] = UNSET,
    to: Union[Unset, str] = UNSET,
) -> Response[List[Union["PurchaseOrder", "PurchaseOrderSupplierView"]]]:
    """[Both] List purchase orders - optionally scoped to a createdAt range via ?from=&to=. A Supplier
    caller gets a reduced view (see GetPurchaseOrder).

    Args:
        from_ (Union[Unset, str]):
        to (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List[Union['PurchaseOrder', 'PurchaseOrderSupplierView']]]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    from_: Union[Unset, str] = UNSET,
    to: Union[Unset, str] = UNSET,
) -> Optional[List[Union["PurchaseOrder", "PurchaseOrderSupplierView"]]]:
    """[Both] List purchase orders - optionally scoped to a createdAt range via ?from=&to=. A Supplier
    caller gets a reduced view (see GetPurchaseOrder).

    Args:
        from_ (Union[Unset, str]):
        to (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List[Union['PurchaseOrder', 'PurchaseOrderSupplierView']]
    """

    return (
        await asyncio_detailed(
            client=client,
            from_=from_,
            to=to,
        )
    ).parsed
