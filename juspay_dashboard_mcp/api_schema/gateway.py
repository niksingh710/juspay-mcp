from typing import Optional
from pydantic import BaseModel, Field

from juspay_dashboard_mcp.api_schema.headers import WithHeaders

class JuspayListConfiguredGatewaysPayload(WithHeaders):
    merchantId: str = Field(
        ...,
        description="Merchant identifier for which to list configured payment gateways."
    )

