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
}

def verify_env_vars():
    """Verifies that required environment variables are set."""
    pass

def get_base64_auth():
    """Returns the base64 encoded auth string."""
    pass

def get_common_headers():
    """
    Returns common headers used by all API calls.
    """
    verify_env_vars()
    return {
        "Authorization": f"Basic {get_base64_auth()}",
        "Accept": "application/json",
        "x-request-id": f"mcp-tool-{os.urandom(6).hex()}" 
    }

def get_json_headers():
    """Returns headers for JSON content type."""
    headers = get_common_headers()
    headers["Content-Type"] = "application/json"
    return headers

def get_form_headers():
    """Returns headers for form URL-encoded content type."""
    headers = get_common_headers()
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    return headers
