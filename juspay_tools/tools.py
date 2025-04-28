import json
import mcp.types as types
import inspect
from mcp.server.lowlevel import Server
from mcp.server.sse import SseServerTransport

from juspay_tools import schema, response_schema
from juspay_tools.api import *

app = Server("juspay")

AVAILABLE_TOOLS = [
    {
        "name": "session_api_juspay",
        "description": f"""
            Creates a new Juspay session for a given order and returns with below json schema:
                {json.dumps(response_schema.session_response_schema, indent=2)}        
        """,
        "schema": schema.juspay_session_schema,
        "handler": session.session_api_juspay
    },
    {
        "name": "order_status_api_juspay",
        "description": f"""
            Retrieves the status of a specific Juspay order using its `order_id` and returns with below json schema:
                {json.dumps(response_schema.order_status_response_schema, indent=2)}
        """,
        "schema": schema.juspay_order_status_schema,
        "handler": order.order_status_api_juspay
    },
    {
        "name": "create_refund_juspay",
        "description": f"""
            Initiates a refund for a specific Juspay order using its `order_id` and returns with below json schema:
                {json.dumps(response_schema.refund_creation_response_schema, indent=2)}
        """,
        "schema": schema.juspay_refund_schema,
        "handler": order.create_refund_juspay
    },
    {
        "name": "get_customer_juspay",
        "description": f""" 
            Retrieves customer details using the Juspay customer ID and returns with below json schema:
                {json.dumps(response_schema.get_customer_response_schema, indent=2)}
        """,
        "schema": schema.juspay_get_customer_schema,
        "handler": customer.get_customer_juspay
    },
    {
        "name": "create_customer_juspay",
        "description": f"""
            Creates a new customer in Juspay with the provided details and returns with below json schema:
                {json.dumps(response_schema.create_customer_response_schema, indent=2)}
        """,
        "schema": schema.juspay_create_customer_schema,
        "handler": customer.create_customer_juspay
    },
    {
        "name": "update_customer_juspay",
        "description": f"""
            Updates an existing customer in Juspay with the provided details and returns with below json schema:
                {json.dumps(response_schema.update_customer_response_schema, indent=2)}
        """,
        "schema": schema.juspay_update_customer_schema,
        "handler": customer.update_customer_juspay
    },
    {
        "name": "order_fulfillment_sync_juspay",
        "description": f"""
            Updates the fulfillment status of a Juspay order and returns with below json schema:
                {json.dumps(response_schema.order_fulfillment_response_schema, indent=2)}
        """,
        "schema": schema.juspay_order_fulfillment_schema,
        "handler": order.order_fulfillment_sync
    },
    {
        "name": "create_txn_refund_juspay",
        "description": f"""
            Initiates a refund based on transaction ID (instead of order ID) and returns with below json schema:
                {json.dumps(response_schema.txn_refund_response_schema, indent=2)}
        """,
        "schema": schema.juspay_txn_refund_schema,
        "handler": order.create_txn_refund_juspay
    },
    {
        "name": "create_txn_juspay",
        "description": f"""
            Creates an order and processes payment in a single API call and returns with below json schema:
                {json.dumps(response_schema.create_txn_response_schema, indent=2)}
        """,
        "schema": schema.juspay_create_txn_schema,
        "handler": order.create_txn_juspay
    },
    {
        "name": "create_moto_txn_juspay",
        "description": f"""
            Creates an order with MOTO (Mail Order/Telephone Order) authentication and returns with below json schema:
                {json.dumps(response_schema.create_moto_txn_response_schema, indent=2)}
        """,
        "schema": schema.juspay_create_moto_txn_schema,
        "handler": order.create_moto_txn_juspay
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
