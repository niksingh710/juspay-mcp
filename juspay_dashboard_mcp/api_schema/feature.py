from typing import Optional
from pydantic import BaseModel, Field

class JuspayFetchFeatureDetailsPayload(BaseModel):
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