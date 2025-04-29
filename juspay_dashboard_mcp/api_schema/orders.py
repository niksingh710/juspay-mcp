from typing import Optional
from pydantic import BaseModel, Field
from juspay_dashboard_mcp.api_schema.headers import WithHeaders


class JuspayListOrdersV4Payload(WithHeaders):
    dateFrom: str = Field(
        ...,
        description="Start date/time in ISO 8601 format (e.g., 'YYYY-MM-DDTHH:MM:SSZ')."
    )
    dateTo: str = Field(
        ...,
        description="End date/time in ISO 8601 format (e.g., 'YYYY-MM-DDTHH:MM:SSZ')."
    )
    offset: Optional[int] = Field(
        0,
        description="Offset for pagination (optional, default is 0)."
    )
    paymentStatus: Optional[str] = Field(
        None,
        description="Optional filter for payment status (e.g., 'CHARGED', 'PENDING')."
    )
    orderType: Optional[str] = Field(
        None,
        description="Optional filter for order type."
    )
    domain: Optional[str] = Field(
        "ordersELS",
        description="Domain for query (optional, default is 'ordersELS')."
    )

class JuspayGetOrderDetailsPayload(WithHeaders):
    order_id: str = Field(
        ...,
        description="Order ID for which details are to be fetched."
    )

class JuspayListPayoutOrdersPayload(WithHeaders):
    createdAt_lte: str = Field(
        ...,
        alias="createdAt.lte",
        description="Upper bound for order creation time (ISO 8601)."
    )
    createdAt_gte: str = Field(
        ...,
        alias="createdAt.gte",
        description="Lower bound for order creation time (ISO 8601)."
    )
    limit: Optional[int] = Field(
        None,
        description="Maximum number of orders to return."
    )
    offset: Optional[int] = Field(
        None,
        description="Offset for pagination."
    )
    order_status: Optional[str] = Field(
        None,
        description="Filter by order status."
    )
    fulfillment_method: Optional[str] = Field(
        None,
        description="Filter by fulfillment method."
    )

class JuspayPayoutOrderDetailsPayload(WithHeaders):
    orderId: str = Field(
        ...,
        description="Payout order ID for which details are to be fetched."
    )