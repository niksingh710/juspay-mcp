import json
import mcp.types as types
from mcp.server.lowlevel import Server
from mcp.server.sse import SseServerTransport

import schema
from api import session, order_status, refund, service_config_time
from api import production_alerts, merchant_dashboard, code_versions
from api import gateway_downtime, order_metadata, customer, audit_logs
from api import merchant_dashboard, code_versions
from api import gateway_downtime, order_metadata, customer, audit_logs
from api import merchant_dashboard, code_versions
from api import gateway_downtime, order_metadata, customer, audit_logs
from api import merchant_dashboard, code_versions

app = Server("sse")

@app.list_tools()
async def list_my_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="session_api_juspay",
            description="Calls the Juspay Session API with the provided payload.",
            inputSchema=schema.juspay_session_schema,
        ),
        types.Tool(
            name="order_status_api_juspay",
            description="Calls the Juspay Order Status API with the provided payload.",
            inputSchema=schema.juspay_order_status_schema,
        ),
        types.Tool(
            name="create_refund_juspay",
            description="Calls the Juspay Refund API for the specified order.",
            inputSchema=schema.juspay_refund_schema,
        ),
        types.Tool(
            name="get_customer_juspay",
            description="Calls the Juspay Get Customer API using the provided customer_id.",
            inputSchema=schema.juspay_get_customer_schema,
        ),
    ]

@app.call_tool()
async def handle_tool_calls(name: str, arguments: dict) -> list[types.TextContent]:
    print(f"Calling tool: {name} with args: {arguments}")

    try:
        if name == "session_api_juspay":
            # Validation for session API tool
            required_keys = [
                "order_id", "amount", "customer_id", "customer_email", 
                "customer_phone", "payment_page_client_id", "action", "return_url"
            ]
            if not all(key in arguments for key in required_keys):
                raise ValueError(f"Missing one or more required arguments for session_api_juspay: {required_keys}")
            response_data = await session.session_api_juspay(arguments)
            return [types.TextContent(type="text", text=json.dumps(response_data))]

        elif name == "order_status_api_juspay":
            # Validation for Order Status API tool
            required_keys = ["order_id"]
            if not all(key in arguments for key in required_keys):
                raise ValueError(f"Missing one or more required arguments for order_status_api_juspay: {required_keys}")
            response_data = await order_status.order_status_api_juspay(arguments)
            return [types.TextContent(type="text", text=json.dumps(response_data))]

        elif name == "create_refund_juspay":
            required_keys = ["order_id", "unique_request_id", "amount"]
            if not all(key in arguments for key in required_keys):
                raise ValueError(f"Missing one or more required arguments for create_refund_juspay: {required_keys}")
            response_data = await refund.create_refund_juspay(arguments)
            return [types.TextContent(type="text", text=json.dumps(response_data))]

        elif name == "get_customer_juspay":
            required_keys = ["customer_id"]
            if not all(key in arguments for key in required_keys):
                raise ValueError(f"Missing required argument for get_customer_juspay: {required_keys}")
            response_data = await customer.get_customer_juspay(arguments)
            return [types.TextContent(type="text", text=json.dumps(response_data))]
        
        else:
            print(f"Error: Unknown tool '{name}'")
            raise ValueError(f"Unknown tool: {name}")

    except Exception as e:
        print(f"Error executing tool {name}: {e}")
        error_message = f"Tool execution failed: {str(e)}"
        return [types.TextContent(type="text", text=f"ERROR: {error_message}")]

