from pydantic import Field
from typing import Optional
from juspay_mcp.api_schema.routing import WithRoutingId

class JuspayGetCustomerPayload(WithRoutingId):
    customer_id: str = Field(..., description="Unique identifier of the customer.")

class JuspayCreateCustomerPayload(WithRoutingId):
    object_reference_id: str = Field(..., description="Unique reference ID for the customer (typically email address).")
    mobile_number: str = Field(..., description="Customer's mobile number without country code.")
    email_address: str = Field(..., description="Customer's email address.")
    
    first_name: Optional[str] = Field(None, description="Customer's first name.")
    last_name: Optional[str] = Field(None, description="Customer's last name.")
    mobile_country_code: Optional[str] = Field(None, description="Mobile country code without '+' (e.g., '91').")
    get_client_auth_token: Optional[bool] = Field(False, description="Set to true to get client authentication token in response.")
    routing_id: Optional[str] = Field(
        None,
        description="Optional custom routing ID for the API request. "
                    "We recommend passing the customer_id as the x-routing-id. "
                    "If the customer is checking out as a guest, you can pass an alternative ID "
                    "that helps track the payment session lifecycle (e.g., Order ID or Cart ID)."
    )


class JuspayUpdateCustomerPayload(WithRoutingId):
    customer_id: str = Field(..., description="Juspay customer ID to update (starts with 'cst_').")
    
    mobile_number: Optional[str] = Field(None, description="Updated mobile number.")
    email_address: Optional[str] = Field(None, description="Updated email address.")
    first_name: Optional[str] = Field(None, description="Updated first name.")
    last_name: Optional[str] = Field(None, description="Updated last name.")
    mobile_country_code: Optional[str] = Field(None, description="Updated mobile country code without '+' (e.g., '91').")
    routing_id: Optional[str] = Field(
        None,
        description="Optional custom routing ID for the API request. "
                    "We recommend passing the customer_id as the x-routing-id. "
                    "If the customer is checking out as a guest, you can pass an alternative ID "
                    "that helps track the payment session lifecycle (e.g., Order ID or Cart ID)."
    )

