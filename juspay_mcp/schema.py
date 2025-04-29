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

juspay_create_customer_schema = {
    "type": "object",
    "required": ["object_reference_id", "mobile_number", "email_address"],
    "properties": {
        "object_reference_id": {
            "type": "string",
            "description": "Unique reference ID for the customer (typically email address)."
        },
        "mobile_number": {
            "type": "string",
            "description": "Customer's mobile number without country code."
        },
        "email_address": {
            "type": "string",
            "description": "Customer's email address."
        },
        "first_name": {
            "type": "string",
            "description": "Customer's first name."
        },
        "last_name": {
            "type": "string",
            "description": "Customer's last name."
        },
        "mobile_country_code": {
            "type": "string",
            "description": "Mobile country code without '+' (e.g., '91')."
        },
        "get_client_auth_token": {
            "type": "boolean",
            "description": "Set to true to get client authentication token in response.",
            "default": False
        },
        "routing_id": {
            "type": "string",
            "description": "Optional custom routing ID for the API request. We recommend passing the customer_id as the x-routing-id. If the customer is checking out as a guest, you can pass an alternative ID that helps track the payment session lifecycle. For example, this could be an Order ID or Cart ID."
        }
    }
}

juspay_update_customer_schema = {
    "type": "object",
    "required": ["customer_id"],
    "properties": {
        "customer_id": {
            "type": "string",
            "description": "Juspay customer ID to update (starts with 'cst_')."
        },
        "mobile_number": {
            "type": "string",
            "description": "Updated mobile number."
        },
        "email_address": {
            "type": "string",
            "description": "Updated email address."
        },
        "first_name": {
            "type": "string",
            "description": "Updated first name."
        },
        "last_name": {
            "type": "string",
            "description": "Updated last name."
        },
        "mobile_country_code": {
            "type": "string",
            "description": "Updated mobile country code without '+' (e.g., '91')."
        },
        "routing_id": {
            "type": "string",
            "description": "Optional custom routing ID for the API request. We recommend passing the customer_id as the x-routing-id. If the customer is checking out as a guest, you can pass an alternative ID that helps track the payment session lifecycle. For example, this could be an Order ID or Cart ID."
        }
    }
}

juspay_create_order_schema = {
    "type": "object",
    "required": [
        "order_id", "amount", "currency", "customer_id", 
        "customer_email", "customer_phone", "return_url"
    ],
    "properties": {
        "order_id": {
            "type": "string",
            "description": "Unique identifier for the order (max 21 alphanumeric chars)."
        },
        "amount": {
            "type": "string", 
            "description": "The order amount (e.g., '100.00')."
        },
        "currency": {
            "type": "string",
            "description": "Currency code (e.g., 'INR')."
        },
        "customer_id": {
            "type": "string",
            "description": "Merchant's identifier for the customer."
        },
        "customer_email": {
            "type": "string",
            "description": "Customer's email address."
        },
        "customer_phone": {
            "type": "string",
            "description": "Customer's phone number."
        },
        "return_url": {
            "type": "string",
            "description": "URL to redirect after payment."
        },
        "description": {
            "type": "string",
            "description": "Description of the order."
        },
        "product_id": {
            "type": "string",
            "description": "Product identifier."
        },
        "get_client_auth_token": {
            "type": "boolean",
            "description": "Whether to get client auth token in response.",
            "default": False 
        },
        "billing_address_first_name": {"type": "string", "description": "Billing first name"},
        "billing_address_last_name": {"type": "string", "description": "Billing last name"},
        "billing_address_line1": {"type": "string", "description": "Billing address line 1"},
        "billing_address_line2": {"type": "string", "description": "Billing address line 2"},
        "billing_address_line3": {"type": "string", "description": "Billing address line 3"},
        "billing_address_city": {"type": "string", "description": "Billing city"},
        "billing_address_state": {"type": "string", "description": "Billing state"},
        "billing_address_country": {"type": "string", "description": "Billing country"},
        "billing_address_postal_code": {"type": "string", "description": "Billing postal code"},
        "billing_address_phone": {"type": "string", "description": "Billing phone"},
        "billing_address_country_code_iso": {"type": "string", "description": "Billing country ISO code"},
        
        "shipping_address_first_name": {"type": "string", "description": "Shipping first name"},
        "shipping_address_last_name": {"type": "string", "description": "Shipping last name"},
        "shipping_address_line1": {"type": "string", "description": "Shipping address line 1"},
        "shipping_address_line2": {"type": "string", "description": "Shipping address line 2"},
        "shipping_address_line3": {"type": "string", "description": "Shipping address line 3"},
        "shipping_address_city": {"type": "string", "description": "Shipping city"},
        "shipping_address_state": {"type": "string", "description": "Shipping state"},
        "shipping_address_country": {"type": "string", "description": "Shipping country"},
        "shipping_address_postal_code": {"type": "string", "description": "Shipping postal code"},
        "shipping_address_phone": {"type": "string", "description": "Shipping phone"},
        "shipping_address_country_code_iso": {"type": "string", "description": "Shipping country ISO code"},
        
        "routing_id": {
            "type": "string", 
            "description": "Optional custom routing ID for the API request. We recommend passing the customer_id as the x-routing-id. If the customer is checking out as a guest, you can pass an alternative ID that helps track the payment session lifecycle. For example, this could be an Order ID or Cart ID."
        },
    },
    "additionalProperties": True
}

juspay_update_order_schema = {
    "type": "object",
    "required": ["order_id"],
    "properties": {
        "order_id": {
            "type": "string",
            "description": "Juspay order ID to update."
        },
        "amount": {
            "type": "string",
            "description": "Updated order amount (e.g., '90.00')."
        },
        "currency": {
            "type": "string",
            "description": "Updated currency code."
        },
        "routing_id": {
            "type": "string",
            "description": "Optional custom routing ID for the API request. We recommend passing the customer_id as the x-routing-id. If the customer is checking out as a guest, you can pass an alternative ID that helps track the payment session lifecycle. For example, this could be an Order ID or Cart ID."
        }
    },
    "additionalProperties": True
}

juspay_order_fulfillment_schema = {
    "type": "object",
    "required": ["order_id", "fulfillment_status", "fulfillment_command", "fulfillment_time", "fulfillment_id"],
    "properties": {
        "order_id": {
            "type": "string",
            "description": "Unique identifier of the order to update fulfillment status."
        },
        "fulfillment_status": {
            "type": "string",
            "enum": ["SUCCESS", "FAILURE", "PENDING"],
            "description": "Status of the fulfillment (SUCCESS, FAILURE, PENDING)."
        },
        "fulfillment_command": {
            "type": "string",
            "enum": ["NO_ACTION", "RELEASE_HOLD", "HOLD"],
            "description": "Command for the fulfillment action."
        },
        "fulfillment_time": {
            "type": "string",
            "format": "date-time",
            "description": "Time of fulfillment in ISO format (e.g., '2024-07-08T16:30:33')."
        },
        "fulfillment_id": {
            "type": "string",
            "description": "Unique identifier for this fulfillment action."
        },
        "fulfillment_data": {
            "type": "string",
            "description": "Optional metadata for the fulfillment."
        },
        "routing_id": {
            "type": "string",
            "description": "Optional custom routing ID for the API request. We recommend passing the customer_id as the x-routing-id. If the customer is checking out as a guest, you can pass an alternative ID that helps track the payment session lifecycle. For example, this could be an Order ID or Cart ID."
        }
    }
}

juspay_txn_refund_schema = {
    "type": "object",
    "required": ["txn_id", "unique_request_id", "amount"],
    "properties": {
        "txn_id": {
            "type": "string",
            "description": "Transaction ID to be refunded (e.g., 'merchant_id-order_id-1')."
        },
        "unique_request_id": {
            "type": "string",
            "description": "Unique identifier for this refund request."
        },
        "amount": {
            "type": "string",
            "description": "Refund amount as a string (e.g., '100.00')."
        },
        "routing_id": {
            "type": "string",
            "description": "Optional custom routing ID for the API request. We recommend passing the customer_id as the x-routing-id. If the customer is checking out as a guest, you can pass an alternative ID that helps track the payment session lifecycle. For example, this could be an Order ID or Cart ID."
        }
    }
}

juspay_create_txn_schema = {
    "type": "object",
    "required": ["order.order_id", "order.amount", "order.currency", "order.customer_id", 
                "payment_method_type", "order.return_url", "merchant_id"],
    "properties": {
        "order.order_id": {
            "type": "string",
            "description": "Unique identifier for the order (max 21 alphanumeric chars)."
        },
        "order.amount": {
            "type": "string", 
            "description": "The order amount (e.g., '100.00')."
        },
        "order.currency": {
            "type": "string",
            "description": "Currency code (e.g., 'INR')."
        },
        "order.customer_id": {
            "type": "string",
            "description": "Merchant's identifier for the customer."
        },
        "order.customer_email": {
            "type": "string",
            "description": "Customer's email address."
        },
        "order.customer_phone": {
            "type": "string",
            "description": "Customer's phone number."
        },
        "order.return_url": {
            "type": "string",
            "description": "URL to redirect after payment."
        },
        "merchant_id": {
            "type": "string",
            "description": "Your merchant ID provided by Juspay."
        },
        "payment_method_type": {
            "type": "string",
            "enum": ["CARD", "NB", "WALLET", "UPI", "EMI"],
            "description": "Type of payment method."
        },
        "payment_method": {
            "type": "string",
            "description": "Specific payment method (e.g., 'VISA', 'MASTERCARD')."
        },
        "card_number": {
            "type": "string",
            "description": "Card number (for CARD payment method)."
        },
        "card_exp_month": {
            "type": "string",
            "description": "Card expiry month (e.g., '05')."
        },
        "card_exp_year": {
            "type": "string",
            "description": "Card expiry year (e.g., '25')."
        },
        "name_on_card": {
            "type": "string",
            "description": "Name as printed on the card."
        },
        "card_security_code": {
            "type": "string",
            "description": "Card CVV/security code."
        },
        "save_to_locker": {
            "type": "boolean",
            "description": "Whether to save card details for future use."
        },
        "redirect_after_payment": {
            "type": "boolean",
            "description": "Whether to redirect to return URL after payment."
        },
        "format": {
            "type": "string",
            "enum": ["json"],
            "description": "Response format, typically 'json'."
        },
        "routing_id": {
            "type": "string",
            "description": "Optional custom routing ID for the API request. We recommend passing the customer_id as the x-routing-id. If the customer is checking out as a guest, you can pass an alternative ID that helps track the payment session lifecycle. For example, this could be an Order ID or Cart ID."
        }
    },
    "additionalProperties": True
}

juspay_create_moto_txn_schema = {
    "type": "object",
    "required": ["order.order_id", "order.amount", "order.currency", "order.customer_id", 
                "payment_method_type", "order.return_url", "merchant_id", "auth_type"],
    "properties": {
        "order.order_id": {
            "type": "string",
            "description": "Unique identifier for the order."
        },
        "order.amount": {
            "type": "string", 
            "description": "The order amount (e.g., '100.00')."
        },
        "order.currency": {
            "type": "string",
            "description": "Currency code (e.g., 'INR')."
        },
        "order.customer_id": {
            "type": "string",
            "description": "Merchant's identifier for the customer."
        },
        "order.return_url": {
            "type": "string",
            "description": "URL to redirect after payment."
        },
        "merchant_id": {
            "type": "string",
            "description": "Your merchant ID provided by Juspay."
        },
        "payment_method_type": {
            "type": "string",
            "enum": ["CARD"],
            "description": "Type of payment method (only CARD for MOTO)."
        },
        "payment_method": {
            "type": "string",
            "description": "Specific payment method (e.g., 'VISA', 'MASTERCARD')."
        },
        "card_number": {
            "type": "string",
            "description": "Card number (masked or full)."
        },
        "card_exp_month": {
            "type": "string",
            "description": "Card expiry month (e.g., '05')."
        },
        "card_exp_year": {
            "type": "string",
            "description": "Card expiry year (e.g., '26')."
        },
        "redirect_after_payment": {
            "type": "boolean",
            "description": "Whether to redirect to return URL after payment."
        },
        "format": {
            "type": "string",
            "enum": ["json"],
            "description": "Response format, typically 'json'."
        },
        "auth_type": {
            "type": "string",
            "enum": ["MOTO"],
            "description": "Authentication type, must be 'MOTO'."
        },
        "tavv": {
            "type": "string",
            "description": "Transaction Authentication Verification Value for MOTO transactions."
        },
        "routing_id": {
            "type": "string",
            "description": "Optional custom routing ID for the API request. We recommend passing the customer_id as the x-routing-id. If the customer is checking out as a guest, you can pass an alternative ID that helps track the payment session lifecycle. For example, this could be an Order ID or Cart ID."
        }
    },
    "additionalProperties": True
}
