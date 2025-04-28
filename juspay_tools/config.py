import os
import base64
import dotenv

dotenv.load_dotenv()

JUSPAY_API_KEY = os.getenv("JUSPAY_API_KEY")
JUSPAY_MERCHANT_ID = os.getenv("JUSPAY_MERCHANT_ID")
JUSPAY_ENV = os.getenv("JUSPAY_ENV", "sandbox").lower() 

if JUSPAY_ENV == "production":
    JUSPAY_BASE_URL = os.getenv("JUSPAY_PROD_BASE_URL", "https://api.juspay.in")
    print("Using Juspay Production Environment")
else:
    JUSPAY_BASE_URL = os.getenv("JUSPAY_SANDBOX_BASE_URL", "https://sandbox.juspay.in")
    print("Using Juspay Sandbox Environment")


ENDPOINTS = {
    "session": f"{JUSPAY_BASE_URL}/session",
    "order_status": f"{JUSPAY_BASE_URL}/order/status/{{order_id}}",
    "refund": f"{JUSPAY_BASE_URL}/orders/{{order_id}}/refunds", 
    "customer": f"{JUSPAY_BASE_URL}/customers/{{customer_id}}",
}

def verify_env_vars():
    """Verifies that required environment variables are set."""
    if not JUSPAY_API_KEY or not JUSPAY_MERCHANT_ID:
        raise ValueError("JUSPAY_API_KEY and JUSPAY_MERCHANT_ID environment variables must be set.")

def get_base64_auth():
    """Returns the base64 encoded auth string."""
    verify_env_vars() 
    auth_string = f"{JUSPAY_API_KEY}:"
    return base64.b64encode(auth_string.encode()).decode()

def get_common_headers(routing_id: str | None = None):
    """
    Returns common headers used by all API calls.
    Uses the provided routing_id, or defaults to JUSPAY_MERCHANT_ID if None.
    """
    verify_env_vars()
    
    effective_routing_id = routing_id or JUSPAY_MERCHANT_ID
    return {
        "Authorization": f"Basic {get_base64_auth()}",
        "x-merchantid": JUSPAY_MERCHANT_ID,
        "x-routing-id": effective_routing_id,
        "Accept": "application/json",
        "x-request-id": f"mcp-tool-{os.urandom(6).hex()}" 
    }

def get_json_headers(routing_id: str | None = None):
    """Returns headers for JSON content type."""
    headers = get_common_headers(routing_id)
    headers["Content-Type"] = "application/json"
    return headers

def get_form_headers(routing_id: str | None = None):
    """Returns headers for form URL-encoded content type."""
    headers = get_common_headers(routing_id)
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    return headers