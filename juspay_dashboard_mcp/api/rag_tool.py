from juspay_dashboard_mcp.api.utils import post, get_juspay_host_from_api
import os
import base64


async def query_rag_tool(payload: dict, meta_info: dict = None) -> dict:
    """
    Queries the RAG Tool API with the given payload and returns the response.

    The API endpoint is:
        https://genius.juspay.in/api/v3/rag/query

    Headers include:
        - Authorization: Basic (Base64-encoded credentials)
        - Content-Type: application/json

    Args:
        payload (dict): The request payload containing the query and similarity_top_k.
        meta_info (dict, optional): Additional metadata for the request.

    Returns:
        dict: The parsed JSON response from the RAG Tool API.

    Raises:
        Exception: If the API call fails or if no authentication token is available.
    """
    token = os.environ.get("JUSPAY_WEB_LOGIN_TOKEN") or (
        meta_info.get("x-web-logintoken") if meta_info else None
    )

    if not token:
        raise Exception("Authentication token is required.")

    encoded_token = base64.b64encode(token.encode()).decode()
    auth_header = f"Basic {encoded_token}"

    api_url = f"https://genius.juspay.in/api/v3/rag/query"
    
    return await post(api_url, payload, {"Authorization": auth_header}, meta_info)
