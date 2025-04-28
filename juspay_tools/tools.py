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
    },
    {
        "name": "add_card_juspay",
        "description": f"""
            Adds a new card to the Juspay system for a customer and returns with below json schema:
                {json.dumps(response_schema.add_card_response_schema, indent=2)}
        """,
        "schema": schema.juspay_add_card_schema,
        "handler": card.add_card_juspay
    },
    {
        "name": "list_cards_juspay",
        "description": f"""
            Retrieves all stored cards for a specific customer and returns with below json schema:
                {json.dumps(response_schema.list_cards_response_schema, indent=2)}
        """,
        "schema": schema.juspay_list_cards_schema,
        "handler": card.list_cards_juspay
    },
    {
        "name": "delete_card_juspay",
        "description": f"""
            Deletes a saved card from the Juspay system and returns with below json schema:
                {json.dumps(response_schema.delete_card_response_schema, indent=2)}
        """,
        "schema": schema.juspay_delete_card_schema,
        "handler": card.delete_card_juspay
    },
    {
        "name": "update_card_juspay",
        "description": f"""
            Updates details for a saved card and returns with below json schema:
                {json.dumps(response_schema.update_card_response_schema, indent=2)}
        """,
        "schema": schema.juspay_update_card_schema,
        "handler": card.update_card_juspay
    },
    {
        "name": "get_card_info_juspay",
        "description": f"""
            Retrieves information about a specific card BIN (Bank Identification Number) and returns with below json schema:
                {json.dumps(response_schema.card_info_response_schema, indent=2)}
        """,
        "schema": schema.juspay_card_info_schema,
        "handler": card.get_card_info_juspay
    },
    {
        "name": "get_bin_list_juspay",
        "description": f"""
            Retrieves a list of eligible BINs for a specific authentication type and returns with below json schema:
                {json.dumps(response_schema.bin_list_response_schema, indent=2)}
        """,
        "schema": schema.juspay_bin_list_schema,
        "handler": card.get_bin_list_juspay
    },
    {
        "name": "get_saved_payment_methods",
        "description": f"""
            Retrieves a customer's saved payment methods and returns with below json schema:
                {json.dumps(response_schema.saved_payment_methods_response_schema, indent=2)}
        """,
        "schema": schema.juspay_saved_payment_methods_schema,
        "handler": upi.get_saved_payment_methods
    },
    {
        "name": "upi_collect",
        "description": f"""
            Creates a UPI Collect transaction for requesting payment from a customer's UPI ID and returns with below json schema:
                {json.dumps(response_schema.upi_collect_response_schema, indent=2)}
        """,
        "schema": schema.juspay_upi_collect_schema,
        "handler": upi.upi_collect
    },
    {
        "name": "verify_vpa",
        "description": f"""
            Verifies if a UPI Virtual Payment Address (VPA) is valid and returns with below json schema:
                {json.dumps(response_schema.verify_vpa_response_schema, indent=2)}
        """,
        "schema": schema.juspay_verify_vpa_schema,
        "handler": upi.verify_vpa
    },
    {
        "name": "upi_intent",
        "description": f"""
            Creates a UPI Intent transaction for payment using UPI apps and returns with below json schema:
                {json.dumps(response_schema.upi_intent_response_schema, indent=2)}
        """,
        "schema": schema.juspay_upi_intent_schema,
        "handler": upi.upi_intent
    },
    {
        "name": "list_offers_juspay",
        "description": f"""
            Lists available offers for a given order with optional coupon code and returns with below json schema:
                {json.dumps(response_schema.list_offers_response_schema, indent=2)}
        """,
        "schema": schema.juspay_list_offers_schema,
        "handler": offer.list_offers_juspay
    },
    {
        "name": "get_offer_order_status_juspay",
        "description": f"""
            Retrieves the status of an order with offer details and returns with below json schema:
                {json.dumps(response_schema.offer_order_status_response_schema, indent=2)}
        """,
        "schema": schema.juspay_offer_order_status_schema,
        "handler": offer.get_offer_order_status_juspay
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
