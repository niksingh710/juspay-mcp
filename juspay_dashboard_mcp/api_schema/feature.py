from typing import Optional
from pydantic import BaseModel, Field
from juspay_dashboard_mcp.api_schema.headers import WithHeaders

class JuspayFetchFeatureDetailsPayload(WithHeaders):
    merchant_id: str = Field(
        ...,
        description="Merchant ID for which feature details are to be fetched."
    )
    feature_id: str = Field(
        ...,
        description="Feature ID for which details are to be fetched."
    )
    client_id: Optional[str] = Field(
        None,
        description="Optional client ID."
    )

class JuspayFetchFeatureListPayload(WithHeaders):
    merchant_id: str = Field(
        ...,
        description="Merchant ID for which features are to be fetched."
    )
    client_id: Optional[str] = Field(
        None,
        description="Optional client ID."
    )