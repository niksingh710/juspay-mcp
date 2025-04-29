from pydantic import BaseModel, Field
from typing import Optional
from juspay_mcp.api_schema.routing import WithRoutingId

class ListWalletsPayload(WithRoutingId):
    customer_id: str = Field(
        ...,
        description="Unique identifier for the customer whose wallets are to be listed."
    )
