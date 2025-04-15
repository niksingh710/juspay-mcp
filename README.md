# Juspay Tools

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
uv install
# OR
pip install -e .
```

## Current Usage

### Starting the Server

```bash
python main.py --host 0.0.0.0 --port 8000 # or python3
```

This will start the MCP server on `http://0.0.0.0:8000/sse`.

### Available Tools

| Tool Name | Description | Required Parameters |
|-----------|-------------|---------------------|
| **Session API** | Calls the Juspay Session API with the provided payload. | order_id, amount, customer_id, customer_email, customer_phone, payment_page_client_id, action, return_url |
| **Order Status API** | Calls the Juspay Order Status API with the provided payload. | order_id |
| **Refund API** | Calls the Juspay Refund API for the specified order. | order_id, unique_request_id, amount |
| **Customer API** | Calls the Juspay Get Customer API using the provided customer_id. | customer_id |