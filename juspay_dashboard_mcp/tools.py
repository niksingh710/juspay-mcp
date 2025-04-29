import json
import mcp.types as types
import inspect
from mcp.server.lowlevel import Server
from mcp.server.sse import SseServerTransport

from juspay_dashboard_mcp import response_schema
from juspay_dashboard_mcp.api import *
import juspay_dashboard_mcp.api_schema as api_schema
import juspay_dashboard_mcp.utils as util

app = Server("juspay-dashboard")

AVAILABLE_TOOLS = [
    util.make_api_config(
        name="juspay_list_configured_gateway",
        description="This API gets all the configured gateways for the given merchan",
        model=api_schema.gateway.JuspayListConfiguredGatewaysPayload,
        handler=gateway.list_configured_gateways_juspay,
        response_schema=None,
    ),
    util.make_api_config(
        name="juspay_get_gateway_scheme",
        description="This API provides detailed configuration information for a gateway, including required/optional fields and supported payment methods.",
        model=api_schema.gateway.JuspayGetGatewaySchemePayload,
        handler=gateway.get_gateway_scheme_juspay,
        response_schema=None,
    ),
    util.make_api_config(
        name="juspay_get_gateway_details",
        description="This API returns detailed information about a specific gateway configured by the merchant. Requires mga_id and merchantId.",
        model=api_schema.gateway.JuspayGetGatewayDetailsPayload,
        handler=gateway.get_gateway_details_juspay,
        response_schema=None,
    ),
    util.make_api_config(
        name="juspay_list_gateway_scheme",
        description="This API returns a list of all available payment gateways that can be configured on PGCC.",
        model=api_schema.gateway.JuspayListGatewaySchemePayload,
        handler=gateway.list_gateway_scheme_juspay,
        response_schema=None,
    ),
    util.make_api_config(
        name="juspay_gateway_downtime",
        description="This API retrieves downtime information for a gateway using order_id and merchant_id. Optionally accepts txn_uuid.",
        model=api_schema.gateway.JuspayGatewayDowntimePayload,
        handler=gateway.get_gateway_downtime,
        response_schema=None,
    ),
    util.make_api_config(
        name="juspay_get_merchant_gateways_pm_details",
        description="This API fetches all gateways and their supported payment methods for the merchant.",
        model=api_schema.gateway.JuspayGetMerchantGatewaysPmDetailsPayload,
        handler=gateway.get_merchant_gateways_pm_details_juspay,
        response_schema=None,
    ),
    util.make_api_config(
        name="juspay_fetch_feature_details",
        description="This API provides comprehensive information for a specific feature ID, including overview, description, FAQs, usage by other merchants, supported PGs/PMTs/platforms, and related features.",
        model=api_schema.feature.JuspayFetchFeatureDetailsPayload,
        handler=feature.fetch_feature_details_juspay,
        response_schema=None,
    ),
    util.make_api_config(
        name="juspay_fetch_feature_list",
        description="Lists all marketplace features with high-level details such as feature summary, supported PMTs and compatible products.",
        model=api_schema.feature.JuspayFetchFeatureListPayload,
        handler=feature.fetch_feature_list_juspay,
        response_schema=None,
    ),
    util.make_api_config(
        name="juspay_alert_details",
        description="Provides detailed information for a specific alert ID, including source, monitored metrics, and applied filters.",
        model=api_schema.alert.JuspayAlertDetailsPayload,
        handler=alert.alert_details_juspay,
        response_schema=None,
    ),
    util.make_api_config(
        name="juspay_list_alerts",
        description="Retrieves all alerts configured by the merchant, including their status, recipients, thresholds, and monitoring intervals.",
        model=api_schema.alert.JuspayListAlertsPayload,
        handler=alert.list_alerts_juspay,
        response_schema=None,
    ),
    util.make_api_config(
        name="juspay_list_orders_v4",
        description="Retrieves a list of orders created within a specified time range. Supports optional filters for payment status and order type.",
        model=api_schema.orders.JuspayListOrdersV4Payload,
        handler=orders.list_orders_v4_juspay,
        response_schema=None,
    ),
    util.make_api_config(
        name="juspay_get_order_details",
        description="Returns complete details for a given order ID.",
        model=api_schema.orders.JuspayGetOrderDetailsPayload,
        handler=orders.get_order_details_juspay,
        response_schema=None,
    ),
    util.make_api_config(
        name="juspay_list_payout_orders",
        description="Retrieves a list of payout orders created within a specified time range (mandatory). Supports additional filters from the Q API (payout domain) such as order_status and fulfillment_method.",
        model=api_schema.orders.JuspayListPayoutOrdersPayload,
        handler=orders.list_payout_orders_juspay,
        response_schema=None,
    ),
    util.make_api_config(
        name="juspay_payout_order_details",
        description="Returns complete details for a given payout order ID.",
        model=api_schema.orders.JuspayPayoutOrderDetailsPayload,
        handler=orders.payout_order_details_juspay,
        response_schema=None,
    ),
    util.make_api_config(
        name="juspay_list_payment_links_v1",
        description="Retrieves a list of payment links created within a specified time range (mandatory). Supports filters from the transactions (txns) domain such as payment_status and order_type.",
        model=api_schema.payments.JuspayListPaymentLinksV1Payload,
        handler=payments.list_payment_links_v1_juspay,
        response_schema=None,
    ),
    util.make_api_config(
        name="juspay_list_surcharge_rules",
        description="No input required. Returns a list of all configured surcharge rules, including their current status and rule definitions.",
        model=api_schema.surcharge.JuspayListSurchargeRulesPayload,
        handler=surcharge.list_surcharge_rules_juspay,
        response_schema=None,
    ),
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

        model_cls = tool_entry.get("model")
        if (model_cls):
            try:
                payload = model_cls(**arguments)  
                payload_dict = payload.dict(exclude_none=True) 
            except Exception as e:
                raise ValueError(f"Validation error: {str(e)}")
        else:
            payload_dict = arguments 
        
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
