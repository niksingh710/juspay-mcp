import json
import mcp.types as types
from mcp.server.lowlevel import Server
from mcp.server.sse import SseServerTransport

import schema
from api import *

app = Server("sse")

AVAILABLE_TOOLS = [
    {
        "name": "session_api_juspay",
        "description": "Calls the Juspay Session API with the provided payload.",
        "schema": schema.juspay_session_schema,
        "handler": session.session_api_juspay
    },
    {
        "name": "order_status_api_juspay",
        "description": "Calls the Juspay Order Status API with the provided payload.",
        "schema": schema.juspay_order_status_schema,
        "handler": order_status.order_status_api_juspay
    },
    {
        "name": "create_refund_juspay",
        "description": "Calls the Juspay Refund API for the specified order.",
        "schema": schema.juspay_refund_schema,
        "handler": refund.create_refund_juspay
    },
    {
        "name": "get_customer_juspay",
        "description": "Calls the Juspay Get Customer API using the provided customer_id.",
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

        response = await handler(arguments)
        return [types.TextContent(type="text", text=json.dumps(response))]

    except Exception as e:
        print(f"Error executing tool {name}: {e}")
        return [types.TextContent(type="text", text=f"ERROR: Tool execution failed: {str(e)}")]