from typing import Optional
from pydantic import BaseModel, Field

from juspay_dashboard_mcp.api_schema.headers import WithHeaders

class JuspayConflictSettingsPayload(WithHeaders):
    """Schema for conflict settings API."""
    pass  # No specific fields required beyond the common headers

class JuspayGeneralSettingsPayload(WithHeaders):
    """Schema for general settings API."""
    pass  # No specific fields required beyond the common headers

class JuspayMandateSettingsPayload(WithHeaders):
    merchantId: Optional[str] = Field(
        None, 
        description="Optional merchant ID to retrieve mandate settings for."
    )

class JuspayPriorityLogicSettingsPayload(WithHeaders):
    """Schema for priority logic settings API."""
    pass  # No specific fields required beyond the common headers

class JuspayRoutingSettingsPayload(WithHeaders):
    """Schema for routing settings API."""
    pass  # No specific fields required beyond the common headers

class JuspayWebhookSettingsPayload(WithHeaders):
    """Schema for webhook settings API."""
    pass  # No specific fields required beyond the common headers