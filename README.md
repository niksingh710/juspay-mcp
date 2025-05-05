# Juspay MCP Tools

[![Python Version](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) <!-- Assuming MIT License -->

A Model Context Protocol (MCP) server to interact with Juspay APIs. This package enables AI agents and other tools to leverage Juspay's capabilities for core payment processing and merchant dashboard interactions.

### Key Features

- **Dual API Coverage:** Provides tools for both Juspay's Core Payment APIs and Dashboard APIs.

- **MCP Integration:** Enables seamless integration with LLMs and AI agents via the Model Context Protocol.

- **Configurable Modes:** Run the server specifically for Core APIs or Dashboard APIs using an environment variable.

## Usage with Claude Desktop

### Juspay Payments MCP

Add the following to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "juspay-mcp": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "-e",
        "JUSPAY_API_KEY",
        "-e",
        "JUSPAY_MERCHANT_ID",
        "-e",
        "JUSPAY_ENV",
        "juspaydotin/juspay-mcp:latest"
      ],
      "env": {
        "JUSPAY_API_KEY": "your_juspay_api_key",
        "JUSPAY_MERCHANT_ID": "your_juspay_merchant_id",
        "JUSPAY_ENV": "sandbox | production"
      }
    }
  }
}
```

Please replace the `your_juspay_api_key` and `your_juspay_merchant_id` with your api key and merchant id.
Default values for `JUSPAY_ENV` is `sandbox` and `JUSPAY_MCP_TYPE` is `EC`

### Juspay Dashboard MCP

```json
{
  "mcpServers": {
    "juspay-dashboard-mcp": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "-e",
        "JUSPAY_WEB_LOGIN_TOKEN",
        "-e",
        "JUSPAY_ENV",
        "juspaydotin/juspay-dashboard-mcp:latest"
      ],
      "env": {
        "JUSPAY_WEB_LOGIN_TOKEN": "your_juspay_web_login_token",
        "JUSPAY_ENV": "sandbox | production"
      }
    }
  }
}
```

Please replace the `your_juspay_web_login_token` with your dashboard login token

## Available Tools

### Juspay Payments Tools

These tools interact with Juspay's standard payment processing APIs.

| Tool Name                       | Description                                                                   |
| :------------------------------ | :---------------------------------------------------------------------------- |
| `session_api_juspay`            | Creates a new Juspay session for a given order.                               |
| `order_status_api_juspay`       | Retrieves the status of a specific Juspay order using its `order_id`.         |
| `create_refund_juspay`          | Initiates a refund for a specific Juspay order using its `order_id`.          |
| `get_customer_juspay`           | Retrieves customer details using the Juspay customer ID.                      |
| `create_customer_juspay`        | Creates a new customer in Juspay with the provided details.                   |
| `update_customer_juspay`        | Updates an existing customer in Juspay with the provided details.             |
| `order_fulfillment_sync_juspay` | Updates the fulfillment status of a Juspay order.                             |
| `create_txn_refund_juspay`      | Initiates a refund based on transaction ID (instead of order ID).             |
| `create_txn_juspay`             | Creates an order and processes payment in a single API call.                  |
| `create_moto_txn_juspay`        | Creates an order with MOTO (Mail Order/Telephone Order) authentication.       |
| `add_card_juspay`               | Adds a new card to the Juspay system for a customer.                          |
| `list_cards_juspay`             | Retrieves all stored cards for a specific customer.                           |
| `delete_card_juspay`            | Deletes a saved card from the Juspay system.                                  |
| `update_card_juspay`            | Updates details for a saved card.                                             |
| `get_card_info_juspay`          | Retrieves information about a specific card BIN (Bank Identification Number). |
| `get_bin_list_juspay`           | Retrieves a list of eligible BINs for a specific authentication type.         |
| `get_saved_payment_methods`     | Retrieves a customer's saved payment methods.                                 |
| `upi_collect`                   | Creates a UPI Collect transaction for requesting payment from a UPI ID.       |
| `verify_vpa`                    | Verifies if a UPI Virtual Payment Address (VPA) is valid.                     |
| `upi_intent`                    | Creates a UPI Intent transaction for payment using UPI apps.                  |
| `list_offers_juspay`            | Lists available offers for a given order with optional coupon code.           |
| `get_offer_order_status_juspay` | Retrieves the status of an order along with offer details.                    |
| `list_wallets`                  | Fetches all wallets linked to the given customer.                             |
| `create_order_juspay`           | Creates a new order in Juspay payment system.                                 |
| `update_order_juspay`           | Updates an existing order in Juspay.                                          |

### Juspay Dashboard Tools

These tools interact with Juspay's merchant dashboard functionalities.

| Tool Name                                 | Description                                                                                        |
| :---------------------------------------- | :------------------------------------------------------------------------------------------------- |
| `juspay_list_configured_gateway`          | Gets all configured gateways for the merchant.                                                     |
| `juspay_get_gateway_scheme`               | Provides detailed configuration info for a gateway (fields, payment methods).                      |
| `juspay_get_gateway_details`              | Returns detailed information about a specific configured gateway (`mga_id` required).              |
| `juspay_list_gateway_scheme`              | Returns a list of all available payment gateways that can be configured.                           |
| `juspay_gateway_downtime`                 | Retrieves downtime information for a gateway (`order_id` required).                                |
| `juspay_get_merchant_gateways_pm_details` | Fetches all gateways and their supported payment methods for the merchant.                         |
| `juspay_report_details`                   | Returns detailed information for a specific report ID.                                             |
| `juspay_list_report`                      | Lists all reports configured by the merchant.                                                      |
| `juspay_get_offer_details`                | Retrieves detailed information for a specific offer (dashboard perspective).                       |
| `juspay_list_offers`                      | Lists all offers configured by the merchant (dashboard perspective).                               |
| `juspay_get_user`                         | Fetches details for a specific user by user ID.                                                    |
| `juspay_get_user_details`                 | Retrieves detailed information for a specific user.                                                |
| `juspay_list_users_v2`                    | Retrieves a list of users associated with a merchant, with optional pagination.                    |
| `juspay_get_conflict_settings`            | Retrieves conflict settings configuration for payment processing.                                  |
| `juspay_get_general_settings`             | Retrieves general configuration settings for the merchant.                                         |
| `juspay_get_mandate_settings`             | Retrieves mandate-related settings for recurring payments.                                         |
| `juspay_get_priority_logic_settings`      | Fetches all configured priority logic rules.                                                       |
| `juspay_get_routing_settings`             | Provides details of success rate-based routing thresholds.                                         |
| `juspay_get_webhook_settings`             | Retrieves webhook configuration settings for the merchant.                                         |
| `juspay_alert_details`                    | Provides detailed information for a specific alert ID.                                             |
| `juspay_list_alerts`                      | Retrieves all alerts configured by the merchant.                                                   |
| `juspay_list_orders_v4`                   | Retrieves orders within a time range (dashboard perspective).                                      |
| `juspay_get_order_details`                | Returns complete details for a given order ID (dashboard perspective).                             |
| `juspay_list_payment_links_v1`            | Retrieves payment links created within a time range.                                               |
| `juspay_list_surcharge_rules`             | Returns a list of all configured surcharge rules.                                                  |
| `q_api`                                   | Generic Query API for various dashboard data domains (refer to `api_schema/q_api.py` for details). |

## Development

### Prerequisites

- Python 3.13+

- pip

## Installation

```bash

# 1. Clone the repository

git  clone https://github.com/juspay/juspay-mcp.git
cd  juspay-mcp

# 2. Install dependencies

pip  install  -e  .  # For development (editable install)
```

## Configuration

Configuration is managed via environment variables. Create a `.env` file in the project root or set these variables in your environment:

```dotenv

# --- Required Juspay Credentials for Payments ---

JUSPAY_API_KEY="your_juspay_api_key"

JUSPAY_MERCHANT_ID="your_juspay_merchant_id"

# --- Required Juspay Credentials for Dashboard ---

JUSPAY_WEB_LOGIN_TOKEN = "your_juspay_web_login_token"

# --- Required Server Mode ---

# Determines which set of tools the server will expose.

# Options: "CORE" (default), "DASHBOARD"

JUSPAY_MCP_TYPE="CORE"



# --- Optional: Juspay Environment ---

# Set to "production" to use live API endpoints.

# Options: "sandbox" (default), "production"

JUSPAY_ENV="sandbox"
```

**Important:** The server runs _either_ Core _or_ Dashboard tools per instance, controlled by `JUSPAY_MCP_TYPE`. To access both sets simultaneously, run two separate server instances with different `JUSPAY_MCP_TYPE` values and ports.

## Usage

### Starting the Server

```bash
python main.py
```

### For STDIO mode

```bash
python stdio.py
```

## License

This project is licensed under the terms of the MIT open source license. Please refer to [LICENSE](./LICENSE) for the full terms.
