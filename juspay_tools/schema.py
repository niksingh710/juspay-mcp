# Schema for the Session API
juspay_session_schema = {
    "type": "object",
    "required": [
        "order_id", "amount", "customer_id", "customer_email",
        "customer_phone", "payment_page_client_id", "action", "return_url"
    ],
    "properties": {
        "order_id": {"type": "string", "description": "Unique Identifier for the order (Max 21 Alphanumeric)."},
        "amount": {"type": "string", "description": "Amount customer has to pay (e.g., '1.00')."},
        "customer_id": {"type": "string", "description": "Unique merchant identifier for the customer."},
        "customer_email": {"type": "string", "description": "Customer's email address."},
        "customer_phone": {"type": "string", "description": "Customer's mobile number."},
        "payment_page_client_id": {"type": "string", "description": "Unique merchant identifier provided by Juspay."},
        "action": {"type": "string", "enum": ["paymentPage", "paymentManagement"], "description": "Action to be performed, e.g., 'paymentPage'."},
        "return_url": {"type": "string", "description": "URL for redirection post payment."},
        "description": {"type": "string", "description": "Order description for user.", "isRequired": "False"},
        "first_name": {"type": "string", "description": "Customer's first name.", "isRequired": "False"},
        "last_name": {"type": "string", "description": "Customer's last name.", "isRequired": "False"},
        "mobile_country_code": {"type": "string", "description": "Mobile country code without '+'", "isRequired": "False"},
        "udf1": {"type": "string", "description": "User defined field 1.", "isRequired": "False"},
    },
}

juspay_order_status_schema = {
   "type": "object",
   "required": ["order_id"],
   "properties": {
       "order_id": {
           "type": "string",
           "description": "Unique identifier for the order to check its status."
       },
   }
}

juspay_refund_schema = {
    "type": "object",
    "required": ["order_id", "unique_request_id", "amount"],
    "properties": {
        "order_id": {
            "type": "string",
            "description": "Unique identifier of the order to refund."
        },
        "unique_request_id": {
            "type": "string",
            "description": "Unique refund request identifier (e.g., 'xyz123')."
        },
        "amount": {
            "type": "string",
            "description": "Refund amount as a string (e.g., '100.00')."
        }
    },
}


juspay_get_customer_schema = {
    "type": "object",
    "required": ["customer_id"],
    "properties": {
        "customer_id": {
            "type": "string",
            "description": "Unique identifier of the customer."
        }
    }
}