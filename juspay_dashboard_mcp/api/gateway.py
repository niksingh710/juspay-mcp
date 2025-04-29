import os
import httpx
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

async def list_configured_gateways_juspay(payload: dict) -> dict:
    """
    Retrieves a list of all payment gateways (PGs) configured for a merchant,
    including high-level details such as gateway reference ID, creation/modification dates,
    and configured payment methods (PMs). Note: Payment Method Types (PMTs) are not included.

    The API endpoint is:
        https://portal.juspay.in/api/ec/v1/gateway/list

    The call uses JSON data containing:
        - merchantId (e.g., "paypal")

    Headers include:
        - x-tenant-id from meta_info
        - x-web-logintoken from meta_info
        - content-type: application/json

    Args:
        payload (dict): A dictionary with the following required key:
            - merchantId: Merchant identifier.

    Returns:
        dict: The parsed JSON response from the Juspay List Configured Gateways API.

    Raises:
        Exception: If the API call fails.
    """

    logger.info(f"API URL: {api_url}")
    login_token = meta_info.get("x_web_login_token")
    tenant_id = meta_info.get("x_tenant_id")
    logger.info(f"NON PARSED HEADERS: ${login_token} ${tenant_id}")
    #headers = config.get_common_headers(web_login_token=login_token)
    #logger.info(f"PARSED HEADERS: {headers}")

    headers = {
        "x-tenant-id": tenant_id,
        "x-web-logintoken": login_token,
        "content-type": "application/json",
        "accept": "*/*",
    }
    auth_type = payload.get("auth_type", "OTP")
    routing_id = payload.get("routing_id")
    
    api_url = "https://portal.juspay.in/api/ec/v1/gateway/list"
    await call(api_url, routing_id)
