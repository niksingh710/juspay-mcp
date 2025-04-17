# Juspay Tools

A Python package that provides MCP (Model Control Protocol) tools to interact with Juspay payment APIs. This package enables LLM tools to interact with the Juspay payment gateway for processing online payments, checking order status, creating refunds, and managing customer data.

## Installation

### Prerequisites

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

### Installation Steps

```bash
# Clone the repository
git clone [repo_url]
cd juspay-tools

# Install the package in development mode
uv install -e .
# OR
pip install -e .

# Install for production use
uv install .
# OR
pip install .
```

## Configuration

Before using the package, you need to set up your Juspay API credentials. Create a .env file in your working directory with the following variables:

```
JUSPAY_API_KEY=your_juspay_api_key
JUSPAY_MERCHANT_ID=your_juspay_merchant_id
JUSPAY_SANDBOX_BASE_URL=https://sandbox.juspay.in
JUSPAY_PROD_BASE_URL=https://api.juspay.in
```

## Usage

### Starting the Server

You can run the server in either HTTP mode (for web interfaces) or stdio mode (for command-line integration):

#### HTTP/SSE Mode

```bash
# If installed as package
juspay-tools --mode http --host 0.0.0.0 --port 8000

# If running from source
python -m juspay_tools --mode http --host 0.0.0.0 --port 8000
# OR
python main.py --mode http --host 0.0.0.0 --port 8000
```

This will start the MCP server on `http://0.0.0.0:8000/sse`.

#### stdio Mode (for CLI Integration)

```bash
# If installed as package
juspay-tools --mode stdio

# If running from source
python -m juspay_tools --mode stdio
# OR
python main.py --mode stdio
```

### Available Tools

| Tool Name | Description | Required Parameters |
|-----------|-------------|---------------------|
| **session_api_juspay** | Creates a payment session with Juspay | order_id, amount, customer_id, customer_email, customer_phone, payment_page_client_id, action, return_url |
| **order_status_api_juspay** | Retrieves the status of an order | order_id |
| **create_refund_juspay** | Initiates a refund for an order | order_id, unique_request_id, amount |
| **get_customer_juspay** | Retrieves customer information | customer_id |

### Connecting to the MCP Server

For HTTP mode, connect to the MCP server using any compatible MCP client. The server exposes an SSE endpoint at:

```
http://[host]:[port]/sse
```

For stdio mode, the tool communicates through standard input/output streams, which is useful for integration with other CLI tools or language models.