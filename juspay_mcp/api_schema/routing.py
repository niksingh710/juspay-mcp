from pydantic import BaseModel, Field
from typing import Optional

class WithRoutingId(BaseModel):
    routing_id: Optional[str] = Field(
        None,
        description=(
            "Optional custom routing ID for the API request. "
            "We recommend passing the customer_id as the x-routing-id. "
            "If the customer is checking out as a guest, you can pass an alternative ID "
            "that helps track the payment session lifecycle (e.g., Order ID or Cart ID)."
        )
    )
