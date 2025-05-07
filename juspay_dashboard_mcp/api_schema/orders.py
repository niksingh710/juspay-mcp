# Copyright 2025 Juspay
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at https://www.apache.org/licenses/LICENSE-2.0.txt

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