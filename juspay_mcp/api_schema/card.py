from typing import List, Optional
from pydantic import Field
from juspay_mcp.api_schema.routing import WithRoutingId

class JuspayAddCardPayload(WithRoutingId):
    merchant_id: str = Field(..., description="Merchant identifier.")
    customer_id: str = Field(..., description="Customer identifier.")
    customer_email: str = Field(..., description="Customer's email address.")
    card_number: str = Field(..., description="Complete card number.")
    card_exp_year: str = Field(..., description="Card expiry year (e.g., '2025').")
    card_exp_month: str = Field(..., description="Card expiry month (e.g., '07').")
    name_on_card: str = Field(..., description="Name as printed on the card.")
    nickname: Optional[str] = Field(None, description="Friendly name for the card.")


class JuspayListCardsPayload(WithRoutingId):
    customer_id: str = Field(..., description="Customer identifier whose cards to retrieve.")
    options_check_cvv_less_support: Optional[bool] = Field(False, description="Check if cards support CVV-less transactions.")


class JuspayDeleteCardPayload(WithRoutingId):
    card_token: str = Field(..., description="Unique token of the card to be deleted.")


class JuspayUpdateCardPayload(WithRoutingId):
    card_token: str = Field(..., description="Unique token of the card to be updated.")
    nickname: Optional[str] = Field(None, description="New friendly name for the card.")
    customer_id: Optional[str] = Field(None, description="Customer identifier associated with the card.")


class JuspayCardInfoPayload(WithRoutingId):
    bin: str = Field(..., description="First 6-9 digits of the card number (BIN).")


class JuspayBinListPayload(WithRoutingId):
    auth_type: Optional[str] = Field("OTP", description="Authentication type (e.g., 'OTP').")
