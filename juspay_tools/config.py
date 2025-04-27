import os
import base64
import dotenv

dotenv.load_dotenv()

JUSPAY_API_KEY = os.getenv("JUSPAY_API_KEY")
JUSPAY_MERCHANT_ID = os.getenv("JUSPAY_MERCHANT_ID")
JUSPAY_SANDBOX_BASE_URL = os.getenv("JUSPAY_SANDBOX_BASE_URL", "https://sandbox.juspay.in")
JUSPAY_PROD_BASE_URL = os.getenv("JUSPAY_PROD_BASE_URL", "https://api.juspay.in")

ENDPOINTS = {
    "session": f"{JUSPAY_SANDBOX_BASE_URL}/session",
    "order_status": f"{JUSPAY_SANDBOX_BASE_URL}/order/status/{{order_id}}",
    "refund": f"{JUSPAY_PROD_BASE_URL}/orders/{{order_id}}/refunds",
    "customer": f"{JUSPAY_PROD_BASE_URL}/customers/{{customer_id}}",
}

def verify_env_vars():
    """Verifies that required environment variables are set."""
    if not JUSPAY_API_KEY or not JUSPAY_MERCHANT_ID:
        raise ValueError("JUSPAY_API_KEY and JUSPAY_MERCHANT_ID environment variables must be set.")

def get_base64_auth():
    """Returns the base64 encoded auth string."""
    auth_string = f"{JUSPAY_API_KEY}:"
    return base64.b64encode(auth_string.encode()).decode()

def get_common_headers(routing_id="customer_1122"):
    """Returns common headers used by all API calls."""
    verify_env_vars()
    return {
        "Authorization": f"Basic {get_base64_auth()}",
        "x-merchantid": JUSPAY_MERCHANT_ID,
        "x-routing-id": routing_id,
        "Accept": "application/json",
    }

def get_json_headers(routing_id="customer_1122"):
    """Returns headers for JSON content type."""
    headers = get_common_headers(routing_id)
    headers["Content-Type"] = "application/json"
    return headers

def get_form_headers(routing_id="customer_1122"):
    """Returns headers for form URL-encoded content type."""
    headers = get_common_headers(routing_id)
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    return headers
