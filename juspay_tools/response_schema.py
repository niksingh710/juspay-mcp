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

create_customer_response_schema = get_customer_response_schema
update_customer_response_schema = get_customer_response_schema

create_order_response_schema = {
    "type": "object",
    "properties": {
        "status_id": {"type": "integer", "description": "Numeric status identifier (e.g., 10 for NEW)."},
        "status": {"type": "string", "description": "Order status (e.g., 'NEW')."},
        "payment_links": {
            "type": "object",
            "properties": {
                "web": {"type": "string", "description": "URL for web payment."},
                "mobile": {"type": "string", "description": "URL for mobile payment."},
                "iframe": {"type": "string", "description": "URL for iframe payment."}
            }
        },
        "order_id": {"type": "string", "description": "Merchant's order identifier."},
        "merchant_id": {"type": "string", "description": "Merchant identifier."},
        "juspay": {
            "type": "object",
            "properties": {
                "client_auth_token_expiry": {"type": "string", "description": "Expiry time of client auth token."},
                "client_auth_token": {"type": "string", "description": "Client authentication token."}
            }
        },
        "id": {"type": "string", "description": "Juspay's unique identifier for the order."},
        "date_created": {"type": "string", "description": "Order creation timestamp."},
        "customer_phone": {"type": "string", "description": "Customer's phone number."},
        "customer_id": {"type": "string", "description": "Customer identifier."},
        "customer_email": {"type": "string", "description": "Customer's email address."},
        "currency": {"type": "string", "description": "Order currency code (e.g., 'INR')."},
        "amount": {"type": "number", "description": "Order amount."},
        "amount_refunded": {"type": "number", "description": "Refunded amount."},
        "refunded": {"type": "boolean", "description": "Whether the order has been refunded."}
    }
}

update_order_response_schema = {
    "type": "object",
    "properties": {
        "customer_email": {"type": "string", "description": "Customer's email address."},
        "customer_phone": {"type": "string", "description": "Customer's phone number."},
        "customer_id": {"type": "string", "description": "Customer identifier."},
        "status_id": {"type": "integer", "description": "Numeric status identifier."},
        "status": {"type": "string", "description": "Order status (e.g., 'NEW')."},
        "id": {"type": "string", "description": "Juspay's unique identifier for the order."},
        "merchant_id": {"type": "string", "description": "Merchant identifier."},
        "amount": {"type": "number", "description": "Updated order amount."},
        "currency": {"type": "string", "description": "Order currency code."},
        "order_id": {"type": "string", "description": "Merchant's order identifier."},
        "date_created": {"type": "string", "description": "Order creation timestamp."},
        "return_url": {"type": "string", "description": "URL to redirect after payment."},
        "payment_links": {
            "type": "object",
            "properties": {
                "iframe": {"type": "string", "description": "URL for iframe payment."},
                "web": {"type": "string", "description": "URL for web payment."},
                "mobile": {"type": "string", "description": "URL for mobile payment."}
            }
        },
        "refunded": {"type": "boolean", "description": "Whether the order has been refunded."},
        "amount_refunded": {"type": "number", "description": "Refunded amount."},
        "effective_amount": {"type": "number", "description": "Effective amount after discounts."}
    }
}

order_fulfillment_response_schema = {
    "type": "object",
    "properties": {
        "status": {"type": "string", "description": "Status of the fulfillment operation (e.g., 'SUCCESS')."},
        "merchant_id": {"type": "string", "description": "Merchant identifier."},
        "order_id": {"type": "string", "description": "Order identifier for which fulfillment was updated."},
        "commands": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "status": {"type": "string", "description": "Status of the command execution."},
                    "metadata": {"type": "string", "description": "Any metadata provided with the fulfillment."},
                    "date_created": {"type": "string", "description": "When the command was executed."},
                    "command": {"type": "string", "description": "The executed command (e.g., 'NO_ACTION')."}
                }
            }
        }
    }
}

txn_refund_response_schema = {
    "type": "object",
    "properties": {
        "unique_request_id": {"type": "string", "description": "Unique identifier for this refund request."},
        "txn_id": {"type": "string", "description": "Transaction ID that was refunded."},
        "status": {"type": "string", "description": "Status of the refund (e.g., 'PENDING')."},
        "sent_to_gateway": {"type": "boolean", "description": "Whether the refund was sent to the payment gateway."},
        "response_code": {"type": "string", "description": "Response code from the payment gateway, if any."},
        "refund_type": {"type": "string", "description": "Type of refund (e.g., 'STANDARD')."},
        "refund_source": {"type": "string", "description": "Source of the refund (e.g., 'RAZORPAY')."},
        "order_id": {"type": "string", "description": "ID of the order that was refunded."},
        "initiated_by": {"type": "string", "description": "Who initiated the refund (e.g., 'API')."},
        "created": {"type": "string", "description": "Timestamp when the refund was created."},
        "amount": {"type": "number", "description": "Amount that was refunded."}
    }
}

create_txn_response_schema = {
    "type": "object",
    "properties": {
        "order_id": {"type": "string", "description": "Order identifier."},
        "status": {"type": "string", "description": "Status of the transaction (e.g., 'PENDING_VBV', 'AUTHORIZED')."},
        "payment": {
            "type": "object",
            "properties": {
                "authentication": {
                    "type": "object",
                    "properties": {
                        "url": {"type": "string", "description": "URL for any required authentication steps."},
                        "method": {"type": "string", "description": "HTTP method to use for authentication."}
                    }
                }
            }
        },
        "txn_uuid": {"type": "string", "description": "Unique transaction identifier."},
        "offer_details": {
            "type": "object",
            "properties": {
                "offers": {"type": "array", "description": "List of applicable offers."}
            }
        },
        "txn_id": {"type": "string", "description": "Transaction identifier."},
        "merchant_return_url": {"type": "string", "description": "URL where the customer will be redirected after payment."}
    }
}

create_moto_txn_response_schema = create_txn_response_schema