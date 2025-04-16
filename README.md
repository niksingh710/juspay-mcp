# Juspay Tools

A Python package that provides MCP tools to interact with Juspay payment APIs.

## Installation

### Prerequisites

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) or pip

### Setup

```bash
# Clone the repository
git clone [repo_url]
cd juspay-tools

# Install dependencies
uv install -e .
# OR
pip install -e .
```

## Usage

### Starting the Server for HTTP

You can start the server either using the installed CLI tool:

```bash
python main.py --mode http --host 0.0.0.0 --port 8000
```
This will start the MCP server on `http://0.0.0.0:8000/sse`.

### Starting the Server for STDIO

```bash
python main.py --mode stdio

# or

python -m juspay_tools --mode stdio
```


### Available Tools

| Tool Name | Description | Required Parameters |
|-----------|-------------|---------------------|
| **session_api_juspay** | Calls the Juspay Session API with the provided payload. | order_id, amount, customer_id, customer_email, customer_phone, payment_page_client_id, action, return_url |
| **order_status_api_juspay** | Calls the Juspay Order Status API with the provided payload. | order_id |
| **create_refund_juspay** | Calls the Juspay Refund API for the specified order. | order_id, unique_request_id, amount |
| **get_customer_juspay** | Calls the Juspay Get Customer API using the provided customer_id. | customer_id |

### Connecting to the MCP Server

You can connect to the MCP server using any compatible MCP client. The server exposes an SSE endpoint at:

```
http://[host]:[port]/sse
```

### API Examples

#### Session API

```json
{
  "order_id": "ORDER123456",
  "amount": "100.00",
  "customer_id": "CUST123",
  "customer_email": "customer@example.com",
  "customer_phone": "9876543210",
  "payment_page_client_id": "your-client-id",
  "action": "paymentPage",
  "return_url": "https://yourwebsite.com/return"
}
```

#### Order Status API

```json
{
  "order_id": "ORDER123456"
}
```

#### Refund API

```json
{
  "order_id": "ORDER123456",
  "unique_request_id": "REFUND123",
  "amount": "100.00"
}
```

#### Get Customer API

```json
{
  "customer_id": "CUST123"
}
```

## Development

To add new tools, update the `AVAILABLE_TOOLS` list in tools.py and add the corresponding handler in the api directory.
