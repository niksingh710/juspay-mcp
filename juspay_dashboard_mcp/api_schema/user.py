from typing import Optional
from pydantic import BaseModel, Field

from juspay_dashboard_mcp.api_schema.headers import WithHeaders

class JuspayGetUserPayload(WithHeaders):
    userId: str = Field(
        ..., 
        description="Unique identifier for the user to retrieve."
    )

class JuspayGetUserDetailsPayload(WithHeaders):
    userId: str = Field(
        ..., 
        description="Unique identifier for the user to retrieve detailed information for."
    )

class JuspayListUsersV2Payload(WithHeaders):
    offset: Optional[int] = Field(
        0, 
        description="Pagination offset for the user list (default: 0)."
    )