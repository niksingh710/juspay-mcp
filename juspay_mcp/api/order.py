import httpx
from juspay_mcp.config import ENDPOINTS 
from juspay_mcp.api.utils import call, post

async def order_status_api_juspay(payload: dict) -> dict:
    """
    Retrieves the status of a specific Juspay order using the order_id.

    This function sends an HTTP GET request to the Juspay Order Status endpoint.
    The 'order_id' from the payload is appended to the URL. If 'customer_id'
    is present in the payload, it's used for the routing_id header.

    Args:
        payload (dict): Must include:
            - order_id (str): Unique identifier of the order to check.
        May include:
            - customer_id (str, optional): If provided, used for the x-routing-id header.

    Returns:
        dict: Parsed JSON response from the Juspay Order Status API, containing details
              about the order, such as its status.

    Raises:
        ValueError: If 'order_id' is missing in the payload.
        Exception: If the API call fails (e.g., HTTP error, network issue).
    """
    order_id = payload.get("order_id")
    if not order_id:
        raise ValueError("The payload must include 'order_id'.")

    customer_id = payload.get("customer_id")

    api_url = ENDPOINTS["order_status"].format(order_id=order_id)
    await call(api_url, customer_id)

async def create_order_juspay(payload: dict) -> dict:
    """
    Creates a new order in Juspay payment system.

    This function sends an HTTP POST request to the Juspay Orders endpoint.
    It includes order details like order_id, amount, currency, customer info, etc.
    If 'customer_id' is present in the payload, it's used for the routing_id header.

    Args:
        payload (dict): Must include required fields like:
            - order_id (str): Unique identifier for the order (max 21 alphanumeric chars).
            - amount (str): The order amount (e.g., '100.00').
            - currency (str): Currency code (e.g., 'INR').
            - customer_id (str): Merchant's identifier for the customer.
            - customer_email (str): Customer's email address.
            - customer_phone (str): Customer's phone number.
            - return_url (str): URL to redirect after payment.
        May include many optional fields like description, billing address, shipping address.
        
    Returns:
        dict: Parsed JSON response from the Juspay Create Order API, containing order details.

    Raises:
        ValueError: If any required field is missing.
        Exception: If the API call fails (e.g., HTTP error, network issue).
    """
    required_fields = [
        "order_id", "amount", "currency", "customer_id", 
        "customer_email", "customer_phone", "return_url"
    ]
    
    for field in required_fields:
        if not payload.get(field):
            raise ValueError(f"The payload must include '{field}'.")
            
    # Process any boolean options
    if payload.get("get_client_auth_token"):
        payload["options.get_client_auth_token"] = "true"
        
    # Process any metadata fields
    for key, value in list(payload.items()):
        if key.startswith("metadata."):
            payload[key] = str(value)
            
    # Get routing ID if provided, otherwise use customer_id
    routing_id = payload.get("routing_id", payload.get("customer_id"))
    
    api_url = ENDPOINTS["create_order"]
    await post(api_url, payload, routing_id)

async def update_order_juspay(payload: dict) -> dict:
    """
    Updates an existing order in Juspay.
    
    This function sends an HTTP POST request to the Juspay Update Order endpoint.
    The order_id is used in the URL path, and other fields are sent as form data.
    
    Args:
        payload (dict): Must include:
            - order_id (str): Juspay order ID to update.
        May include:
            - amount (str): Updated order amount.
            - currency (str): Updated currency code.
            - And other updateable fields.
            
    Returns:
        dict: Parsed JSON response containing the updated order details.
        
    Raises:
        ValueError: If order_id is missing.
        Exception: If the API call fails.
    """
    order_id = payload.get("order_id")
    if not order_id:
        raise ValueError("The payload must include 'order_id'.")
    
    # Remove order_id from payload as it's in the URL
    update_data = {k: v for k, v in payload.items() if k != "order_id"}
    
    if not update_data:
        raise ValueError("At least one field must be provided for update.")
    
    # Get routing ID if provided
    routing_id = payload.get("routing_id", payload.get("customer_id"))
    
    api_url = ENDPOINTS["update_order"].format(order_id=order_id)
    await post(api_url, update_data, routing_id)

async def order_fulfillment_sync(payload: dict) -> dict:
    """
    Updates the fulfillment status of an order.
    
    This function sends an HTTP POST request to the Juspay Order Fulfillment endpoint
    to synchronize the order's delivery/fulfillment status with Juspay.
    
    Args:
        payload (dict): Must include:
            - order_id (str): Unique identifier of the order to update.
            - fulfillment_status (str): Status of fulfillment (SUCCESS, FAILURE, PENDING).
            - fulfillment_command (str): Command for fulfillment (NO_ACTION, RELEASE_HOLD, HOLD).
            - fulfillment_time (str): Time of fulfillment in ISO format.
            - fulfillment_id (str): Unique identifier for this fulfillment action.
        May include:
            - fulfillment_data (str): Optional metadata for the fulfillment.
            - routing_id (str): Optional routing ID.
            
    Returns:
        dict: Parsed JSON response containing the fulfillment update status.
        
    Raises:
        ValueError: If required fields are missing.
        Exception: If the API call fails.
    """
    order_id = payload.pop("order_id")
    if not order_id:
        raise ValueError("The payload must include 'order_id'.")
    
    required_fields = ["fulfillment_status", "fulfillment_command", "fulfillment_time", "fulfillment_id"]
    for field in required_fields:
        if not payload.get(field):
            raise ValueError(f"The payload must include '{field}'.")
    
    routing_id = payload.get("routing_id")
    if "routing_id" in payload:
        payload.pop("routing_id")
    
    api_url = ENDPOINTS["order_fulfillment"].format(order_id=order_id)
    await post(api_url, payload, routing_id)

async def create_refund_juspay(payload: dict) -> dict:
    """
    Initiates a refund for a previously successful Juspay order.

    This function sends an HTTP POST request (form URL-encoded) to the Juspay Refund endpoint.
    The 'order_id' is part of the URL. 'unique_request_id' and 'amount' are sent as form data.
    If 'customer_id' is present in the payload, it's used for the routing_id header.

    Args:
        payload (dict): Must include:
            - order_id (str): Unique identifier of the order to be refunded.
            - unique_request_id (str): A unique identifier for this refund attempt.
            - amount (str): The amount to be refunded (e.g., "50.00").
        May include:
            - customer_id (str, optional): If provided, used for the x-routing-id header.

    Returns:
        dict: Parsed JSON response from the Juspay Refund API, indicating the status
              of the refund request.

    Raises:
        ValueError: If 'order_id', 'unique_request_id', or 'amount' are missing.
        Exception: If the API call fails (e.g., HTTP error, network issue).
    """
    order_id = payload.get("order_id")
    unique_request_id = payload.get("unique_request_id")
    amount = payload.get("amount")

    if not order_id:
        raise ValueError("The payload must include 'order_id'.")
    if not unique_request_id:
        raise ValueError("The payload must include 'unique_request_id'.")
    if not amount:
         raise ValueError("The payload must include 'amount'.")

    
    customer_id = payload.get("customer_id")
    
    api_url = ENDPOINTS["refund"].format(order_id=order_id)
    
    form_data = {
        "unique_request_id": unique_request_id,
        "amount": amount,
    }
    await post(api_url, form_data)

async def create_txn_refund_juspay(payload: dict) -> dict:
    """
    Initiates a transaction-based refund using the transaction ID instead of order ID.
    
    This function sends an HTTP POST request to the Juspay Transaction Refund endpoint.
    It requires txn_id rather than order_id for refunds.
    
    Args:
        payload (dict): Must include:
            - txn_id (str): Transaction identifier to be refunded.
            - unique_request_id (str): A unique identifier for this refund attempt.
            - amount (str): The amount to be refunded (e.g., "50.00").
        May include:
            - routing_id (str, optional): If provided, used for the x-routing-id header.
            
    Returns:
        dict: Parsed JSON response from the Juspay Txn Refund API.
        
    Raises:
        ValueError: If required fields are missing.
        Exception: If the API call fails.
    """
    txn_id = payload.get("txn_id")
    unique_request_id = payload.get("unique_request_id")
    amount = payload.get("amount")
    
    if not txn_id:
        raise ValueError("The payload must include 'txn_id'.")
    if not unique_request_id:
        raise ValueError("The payload must include 'unique_request_id'.")
    if not amount:
        raise ValueError("The payload must include 'amount'.")
    
    routing_id = payload.get("routing_id")
    
    refund_data = {
        "txn_id": txn_id,
        "unique_request_id": unique_request_id,
        "amount": amount
    }
    
    api_url = ENDPOINTS["txn_refund"]
    await post(api_url, refund_data, routing_id)

async def create_txn_juspay(payload: dict) -> dict:
    """
    Creates an order and processes payment in a single API call.
    
    This function sends an HTTP POST request to the Juspay Txns endpoint to create
    an order and initiate payment processing simultaneously.
    
    Args:
        payload (dict): A dictionary containing order and payment details.
        Must include:
            - order.order_id (str): Unique identifier for the order.
            - order.amount (str): The order amount.
            - order.currency (str): Currency code.
            - order.customer_id (str): Customer identifier.
            - order.return_url (str): URL to redirect after payment.
            - merchant_id (str): Your merchant ID.
            - payment_method_type (str): Type of payment method (CARD, NB, etc.).
        For CARD payments, must also include:
            - card_number, card_exp_month, card_exp_year, etc.
            
    Returns:
        dict: Parsed JSON response containing transaction details.
        
    Raises:
        ValueError: If required fields are missing.
        Exception: If the API call fails.
    """
    required_fields = ["order.order_id", "order.amount", "order.currency", 
                      "order.customer_id", "payment_method_type", 
                      "order.return_url", "merchant_id"]
    
    for field in required_fields:
        if not payload.get(field):
            raise ValueError(f"The payload must include '{field}'.")
    
    # Set format to json if not specified
    if "format" not in payload:
        payload["format"] = "json"
    
    # Extract routing_id if present, otherwise use order.customer_id
    routing_id = payload.get("routing_id", payload.get("order.customer_id"))
    if "routing_id" in payload:
        payload.pop("routing_id")
    
    api_url = ENDPOINTS["create_txn"]
    return await post(api_url, payload, routing_id)

async def create_moto_txn_juspay(payload: dict) -> dict:
    """
    Creates an order with MOTO (Mail Order/Telephone Order) payment.
    
    Similar to create_txn_juspay but specifically for MOTO transactions which
    bypass the standard 3D Secure authentication.
    
    Args:
        payload (dict): A dictionary containing order and payment details.
        Must include:
            - The same fields as create_txn_juspay
            - auth_type (str): Must be "MOTO"
        May include:
            - tavv (str): Transaction Authentication Verification Value
            
    Returns:
        dict: Parsed JSON response containing transaction details.
        
    Raises:
        ValueError: If required fields are missing or auth_type is not "MOTO".
        Exception: If the API call fails.
    """
    if payload.get("auth_type") != "MOTO":
        raise ValueError("For MOTO transactions, 'auth_type' must be 'MOTO'.")
    
    # Use the standard txn creation function with additional MOTO parameters
    await create_txn_juspay(payload)