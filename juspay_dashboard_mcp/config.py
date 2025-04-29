import os
import base64
import dotenv

dotenv.load_dotenv()

JUSPAY_ENV = os.getenv("JUSPAY_ENV", "sandbox").lower() 

if JUSPAY_ENV == "production":
    JUSPAY_BASE_URL = os.getenv("JUSPAY_PROD_BASE_URL", "https://euler-x.internal.svc.k8s.mum.juspay.net")
    print("Using Juspay Production Environment")
else:
    JUSPAY_BASE_URL = os.getenv("JUSPAY_SANDBOX_BASE_URL", "https://portal.juspay.in")
    print("Using Juspay Sandbox Environment")


ENDPOINTS = {
    "list_configured_gateways": ""
}

def verify_env_vars():
    """Verifies that required environment variables are set."""
    pass

def get_base64_auth():
    """Returns the base64 encoded auth string."""
    pass
    
def get_common_headers(payload: dict):
    """
    Returns common headers used by all API calls.
    Uses the provided routing_id, or defaults to JUSPAY_MERCHANT_ID if None.
    """
    verify_env_vars()

    return {
       "Content-Type": "application/json",
        "accept": "*/*",
        "x-request-id": f"mcp-tool-{os.urandom(6).hex()}",
        "x-tenant-id": payload.pop("tenant_id", None),
        "x-web-logintoken": payload.pop("web_login_str"),
        "cookie": payload.pop("cookie", None),
    }