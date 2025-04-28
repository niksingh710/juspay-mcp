session_response_schema = {
    "type": "object",
    "properties": {
        "status": {"type": "string", "description": "Status of the session (e.g., 'NEW', 'AUTHENTICATED')."},
        "order_id": {"type": "string", "description": "The unique order identifier provided in the request."},
        "id": {"type": "string", "description": "Unique Juspay identifier for this session (e.g., 'hyp_sess_...')."},
        "payment_links": {
            "type": "object",
            "description": "Contains URLs for different payment integration methods.",
            "properties": {
                "web": {"type": "string", "description": "URL for standard web redirection payment flow."},
                "iframe": {"type": "string", "description": "URL to embed the payment page in an iframe."},
                "mobile": {"type": "string", "description": "Intent URL for invoking mobile SDK/app payments."}
            }
        },
        "sdk_payload": {
            "type": "object",
            "description": "Payload specifically for integration with Juspay Mobile SDKs.",
             "properties": {
                 "requestId": {"type": "string", "description": "Request identifier for SDK."},
                 "service": {"type": "string", "description": "Service identifier for SDK."},
                 "payload": {"type": "object", "description": "Nested payload containing SDK-specific parameters."}
             }
        }
    },
    "required": ["status", "order_id", "id", "payment_links"]
}

order_status_response_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string", "description": "Unique Juspay identifier for the order (e.g., 'ordeh_...')."},
        "order_id": {"type": "string", "description": "The unique order identifier provided by the merchant."},
        "status": {"type": "string", "description": "Current status of the order (e.g., 'CHARGED', 'PENDING_VBV', 'REFUNDED')."},
        "status_id": {"type": "integer", "description": "Numeric ID corresponding to the order status."},
        "amount": {"type": "number", "format": "double", "description": "The total amount of the order."},
        "currency": {"type": "string", "description": "Currency code (e.g., 'INR')."},
        "customer_id": {"type": "string", "description": "Merchant's identifier for the customer."},
        "customer_email": {"type": "string", "description": "Customer's email address."},
        "customer_phone": {"type": "string", "description": "Customer's phone number."},
        "date_created": {"type": "string", "format": "date-time", "description": "Timestamp when the order was created (UTC)."},
        "amount_refunded": {"type": "number", "format": "double", "description": "Total amount refunded for this order so far."},
        "refunded": {"type": "boolean", "description": "Indicates if the order has been fully refunded."},
        "txn_id": {"type": "string", "description": "Juspay's transaction identifier for the primary payment attempt."},
        "payment_method_type": {"type": "string", "description": "Type of payment method used (e.g., 'CARD', 'NB', 'WALLET')."},
        "payment_method": {"type": "string", "description": "Specific payment method used (e.g., 'VISA', 'HDFC')."},
        "card": {
            "type": "object",
            "description": "Details of the card used for payment (present if payment_method_type is 'CARD').",
            "properties": {
                 "last_four_digits": {"type": "string"},
                 "card_brand": {"type": "string"},
                 "card_type": {"type": "string", "description": "e.g., 'CREDIT', 'DEBIT'"},
                 "card_issuer": {"type": "string", "description": "Issuing bank name."}
            }
        },
        "refunds": {
            "type": "array",
            "description": "List of refund transactions associated with this order.",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string", "description": "Unique Juspay identifier for the refund (e.g., 'rfnd_...')."},
                    "unique_request_id": {"type": "string", "description": "The unique ID provided by the merchant when initiating the refund."},
                    "amount": {"type": "number", "format": "double", "description": "Amount of this specific refund."},
                    "status": {"type": "string", "description": "Status of the refund (e.g., 'COMPLETED', 'PENDING')."},
                    "created": {"type": "string", "format": "date-time", "description": "Timestamp when the refund was created (UTC)."}
                }
            }
        },
        "txn_detail": {"type": "object", "description": "Detailed information about the transaction."},
        "payment_gateway_response": {"type": "object", "description": "Raw response details from the payment gateway."}
    },
    "required": ["id", "order_id", "status", "status_id", "amount", "currency", "date_created"]
}

refund_creation_response_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string", "description": "Unique Juspay identifier for the newly created refund transaction (e.g., 'rfnd_...')."},
        "order_id": {"type": "string", "description": "The identifier of the order being refunded."},
        "unique_request_id": {"type": "string", "description": "The unique identifier provided in the refund request."},
        "amount": {"type": "number", "format": "double", "description": "The amount requested for this refund."},
        "currency": {"type": "string", "description": "Currency code (e.g., 'INR')."},
        "status": {"type": "string", "description": "Initial status of the refund upon creation (e.g., 'PENDING', 'INITIATED')."},
        "created": {"type": "string", "format": "date-time", "description": "Timestamp when the refund request was processed (UTC)."}
    },
    "required": ["id", "order_id", "unique_request_id", "amount", "currency", "status", "created"]
}

get_customer_response_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string", "description": "Unique Juspay identifier for the customer (e.g., 'cst_...')."},
        "object": {"type": "string", "enum": ["customer"], "description": "Object type, always 'customer'."},
        "object_reference_id": {"type": "string", "description": "The unique identifier provided by the merchant when the customer was created."},
        "mobile_number": {"type": "string", "description": "Customer's registered mobile number."},
        "email_address": {"type": "string", "description": "Customer's registered email address."},
        "first_name": {"type": "string", "description": "Customer's first name."},
        "last_name": {"type": "string", "description": "Customer's last name."},
        "mobile_country_code": {"type": "string", "description": "Mobile country code associated with the number."},
        "date_created": {"type": "string", "format": "date-time", "description": "Timestamp when the customer record was created (UTC)."},
        "last_updated": {"type": "string", "format": "date-time", "description": "Timestamp when the customer record was last updated (UTC)."}
    },
    "required": ["id", "object", "object_reference_id", "date_created", "last_updated"]
}