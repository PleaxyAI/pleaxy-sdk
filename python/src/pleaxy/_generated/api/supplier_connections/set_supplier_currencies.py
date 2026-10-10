from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.set_connection_currencies_input import SetConnectionCurrenciesInput
from ...models.set_supplier_currencies_result_type_0 import (
    SetSupplierCurrenciesResultType0,
)
from ...models.set_supplier_currencies_result_type_1 import (
    SetSupplierCurrenciesResultType1,
)
from ...types import Response


def _get_kwargs(
    connection_id: str,
    *,
    body: SetConnectionCurrenciesInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/supplier-connections/{connection_id}/currencies".format(
            connection_id=connection_id,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union["SetSupplierCurrenciesResultType0", "SetSupplierCurrenciesResultType1"]
]:
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> Union[
            "SetSupplierCurrenciesResultType0", "SetSupplierCurrenciesResultType1"
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_set_supplier_currencies_result_type_0 = (
                    SetSupplierCurrenciesResultType0.from_dict(data)
                )

                return componentsschemas_set_supplier_currencies_result_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_set_supplier_currencies_result_type_1 = (
                SetSupplierCurrenciesResultType1.from_dict(data)
            )

            return componentsschemas_set_supplier_currencies_result_type_1

        response_200 = _parse_response_200(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union["SetSupplierCurrenciesResultType0", "SetSupplierCurrenciesResultType1"]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    connection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SetConnectionCurrenciesInput,
) -> Response[
    Union["SetSupplierCurrenciesResultType0", "SetSupplierCurrenciesResultType1"]
]:
    r"""[Buyer] Set \"Bills in\" (billingCurrency, a supplier with no Pleaxy account only) and \"Pay in\"
    (paymentCurrency) for this supplier: the defaults for its new orders and invoices. Absent leaves a
    field, null removes it. Existing documents keep their currencies. 400
    BILLING_CURRENCY_SUPPLIER_OWNED for a supplier with an account; 400 PAYMENT_CURRENCY_NOT_ACCEPTED
    when it doesn't accept that currency. The supplier never sees either.

    Args:
        connection_id (str):
        body (SetConnectionCurrenciesInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['SetSupplierCurrenciesResultType0', 'SetSupplierCurrenciesResultType1']]
    """

    kwargs = _get_kwargs(
        connection_id=connection_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    connection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SetConnectionCurrenciesInput,
) -> Optional[
    Union["SetSupplierCurrenciesResultType0", "SetSupplierCurrenciesResultType1"]
]:
    r"""[Buyer] Set \"Bills in\" (billingCurrency, a supplier with no Pleaxy account only) and \"Pay in\"
    (paymentCurrency) for this supplier: the defaults for its new orders and invoices. Absent leaves a
    field, null removes it. Existing documents keep their currencies. 400
    BILLING_CURRENCY_SUPPLIER_OWNED for a supplier with an account; 400 PAYMENT_CURRENCY_NOT_ACCEPTED
    when it doesn't accept that currency. The supplier never sees either.

    Args:
        connection_id (str):
        body (SetConnectionCurrenciesInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['SetSupplierCurrenciesResultType0', 'SetSupplierCurrenciesResultType1']
    """

    return sync_detailed(
        connection_id=connection_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    connection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SetConnectionCurrenciesInput,
) -> Response[
    Union["SetSupplierCurrenciesResultType0", "SetSupplierCurrenciesResultType1"]
]:
    r"""[Buyer] Set \"Bills in\" (billingCurrency, a supplier with no Pleaxy account only) and \"Pay in\"
    (paymentCurrency) for this supplier: the defaults for its new orders and invoices. Absent leaves a
    field, null removes it. Existing documents keep their currencies. 400
    BILLING_CURRENCY_SUPPLIER_OWNED for a supplier with an account; 400 PAYMENT_CURRENCY_NOT_ACCEPTED
    when it doesn't accept that currency. The supplier never sees either.

    Args:
        connection_id (str):
        body (SetConnectionCurrenciesInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['SetSupplierCurrenciesResultType0', 'SetSupplierCurrenciesResultType1']]
    """

    kwargs = _get_kwargs(
        connection_id=connection_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    connection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SetConnectionCurrenciesInput,
) -> Optional[
    Union["SetSupplierCurrenciesResultType0", "SetSupplierCurrenciesResultType1"]
]:
    r"""[Buyer] Set \"Bills in\" (billingCurrency, a supplier with no Pleaxy account only) and \"Pay in\"
    (paymentCurrency) for this supplier: the defaults for its new orders and invoices. Absent leaves a
    field, null removes it. Existing documents keep their currencies. 400
    BILLING_CURRENCY_SUPPLIER_OWNED for a supplier with an account; 400 PAYMENT_CURRENCY_NOT_ACCEPTED
    when it doesn't accept that currency. The supplier never sees either.

    Args:
        connection_id (str):
        body (SetConnectionCurrenciesInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['SetSupplierCurrenciesResultType0', 'SetSupplierCurrenciesResultType1']
    """

    return (
        await asyncio_detailed(
            connection_id=connection_id,
            client=client,
            body=body,
        )
    ).parsed
