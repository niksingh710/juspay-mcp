import json
import mcp.types as types
import inspect
from mcp.server.lowlevel import Server
from mcp.server.sse import SseServerTransport

from juspay_tools import schema
from juspay_tools.api import *

app = Server("juspay")

AVAILABLE_TOOLS = [
    {
        "name": "session_api_juspay",
        "description": (
            "Creates a Juspay payment session to initiate a transaction. "
            "Requires order details (`order_id`, `amount`), customer info (`customer_id`, `customer_email`, etc.), and `return_url`. "
            "Returns a JSON object containing details needed to launch the payment page or SDK. "
            "Key fields in the response typically include: `status` (session status, e.g., 'NEW'), `order_id`, `id` (Juspay session ID), "
            "`payment_links` (object with URLs like 'web', 'iframe', 'mobile'), and potentially `sdk_payload` for mobile SDK integration."
        ),
        "schema": schema.juspay_session_schema,
        "handler": session.session_api_juspay
    },
    {
        "name": "order_status_api_juspay",
        "description": (
            "Retrieves the current status and details of a Juspay order using its `order_id`. "
            "Returns a detailed JSON object representing the order state. "
            "Key fields include: `order_id` (merchant's ID), `id` (Juspay's internal order ID, e.g., 'ordeh_...'), "
            "`status` (e.g., 'CHARGED', 'PENDING_VBV', 'REFUNDED'), `amount`, `currency`, `customer_id`, `customer_email`, `customer_phone`, "
            "`date_created`, `payment_method_type`, `payment_method`, `card` (object with card details like 'last_four_digits', 'card_brand' if applicable), "
            "`refunded` (boolean), `amount_refunded`, and an array `refunds` containing details of any refunds processed (each object has `id`, `amount`, `unique_request_id`, `status`, `created`). "
            "Also includes detailed `txn_detail` and `payment_gateway_response` objects."
        ),
        "schema": schema.juspay_order_status_schema,
        "handler": order_status.order_status_api_juspay
    },
    {
        "name": "create_refund_juspay",
        "description": (
            "Initiates a refund for a specific Juspay order. "
            "Requires the `order_id`, a `unique_request_id` (for idempotency), and the refund `amount`. "
            "Returns a JSON object confirming the refund initiation attempt. "
            "Key fields typically include: `order_id`, `refund_id` (unique ID for this refund transaction, e.g., 'rfnd_...'), "
            "`unique_request_id` (echoed back from the request), `status` (initial status, e.g., 'PENDING', 'INITIATED', 'ACCEPTED'), "
            "`amount_refunded`, `currency`, and `created` timestamp. Note: The sample response provided in the prompt shows the *order status* after a refund, not the direct response of the refund creation POST itself."
        ),
        "schema": schema.juspay_refund_schema,
        "handler": refund.create_refund_juspay
    },
    {
        "name": "get_customer_juspay",
        "description": (
            "Retrieves details for a specific customer registered with Juspay using their `customer_id`. "
            "Returns a JSON object containing customer information. "
            "Key fields include: `id` (Juspay customer ID, e.g., 'cst_...'), `object` ('customer'), "
            "`object_reference_id` (merchant's reference ID used during creation, often email or unique ID), "
            "`mobile_number`, `email_address`, `first_name`, `last_name`, `mobile_country_code`, `date_created`, `last_updated`."
        ),
        "schema": schema.juspay_get_customer_schema,
        "handler": customer.get_customer_juspay
    }
]

@app.list_tools()
async def list_my_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name=tool["name"],
            description=tool["description"],
            inputSchema=tool["schema"],
        )
        for tool in AVAILABLE_TOOLS
    ]

@app.call_tool()
async def handle_tool_calls(name: str, arguments: dict) -> list[types.TextContent]:
    print(f"Calling tool: {name} with args: {arguments}")

    try:
        tool_entry = next((t for t in AVAILABLE_TOOLS if t["name"] == name), None)
        if not tool_entry:
            raise ValueError(f"Unknown tool: {name}")

        schema = tool_entry["schema"]
        required = schema.get("required", [])
        missing = [key for key in required if key not in arguments]
        if missing:
            raise ValueError(f"Missing required fields for {name}: {missing}")

        handler = tool_entry["handler"]
        if not handler:
            raise ValueError(f"No handler defined for tool: {name}")
        
        meta_info = arguments.pop("juspay_meta_info", None)

        sig = inspect.signature(handler)
        param_count = len(sig.parameters)

        if param_count == 0:
            response = await handler()

        elif param_count == 1:
            if arguments or not meta_info:
                response = await handler(arguments)
            else:
                response = await handler(meta_info)

        elif param_count == 2:
            response = await handler(arguments, meta_info)

        else:
            raise ValueError(f"Unsupported number of parameters in tool handler: {param_count}")
        return [types.TextContent(type="text", text=json.dumps(response))]

    except Exception as e:
        print(f"Error executing tool {name}: {e}")
        return [types.TextContent(type="text", text=f"ERROR: Tool execution failed: {str(e)}")]
